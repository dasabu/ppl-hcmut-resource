from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *

class ASTGeneration(BKOOLVisitor):
    # ~ 2.1: Class Declaration 
    # program: classDecllist EOF;
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return Program(self.visit(ctx.classDeclList())) # List[ClassDecl]
    
    # classDeclList: classDecl classDeclList | classDecl;
    def visitClassDeclList(self, ctx:BKOOLParser.ClassDeclListContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.classDecl())
        else:
            return self.visit(ctx.classDecl()) + self.visit(ctx.classDeclList())
        
    # classDecl: CLASS ID classExtends classBody;
    def visitClassDecl(self, ctx:BKOOLParser.ClassDeclContext):
        classname = Id(ctx.ID().getText()) # Id
        memlist = self.visit(ctx.classBody()) # List[MemDecl]
        parentname = self.visit(ctx.classExtends()) # Id (None if no parent)
        return [ClassDecl(classname, memlist, parentname)]
    
    # classExtends:	EXTENDS ID | ;
    def visitClassExtends(self, ctx:BKOOLParser.ClassExtendsContext):
        if ctx.EXTENDS():
            return Id(ctx.ID().getText())
        else: 
            return None
    
    # classBody: LP classMemberList RP;
    def visitClassBody(self, ctx:BKOOLParser.ClassBodyContext):
        return self.visit(ctx.classMemberList())
    
    # classMemberList: classMember classMemberList | ;
    def visitClassMemberList(self, ctx:BKOOLParser.ClassMemberListContext):
        if ctx.getChildCount() == 0:
            return []
        else: 
            return self.visit(ctx.classMember()) + self.visit(ctx.classMemberList())
    
    # classMember: attrDecl | methodDecl;
    def visitClassMember(self, ctx:BKOOLParser.ClassMemberContext):
        if ctx.attrDecl():
            return self.visit(ctx.attrDecl())
        else:
            return self.visit(ctx.methodDecl())
    
    # ~ 2.3: Method Declaration 
    # methodDecl: constructor | normalMethod; 
    def visitMethodDecl(self, ctx:BKOOLParser.MethodDeclContext):
        if ctx.constructor():
            return self.visit(ctx.constructor())
        else:
            return self.visit(ctx.normalMethod())
    
    # constructor: ID paramDecl blockstmt;
    def visitConstructor(self, ctx:BKOOLParser.ConstructorContext):
        kind = Instance() # SIKind: Static() or Instance()
        name = Id("<init>") # Id
        param = self.visit(ctx.paramDecl()) # List[VarDecl]
        returnType = None # Type
        body = self.visit(ctx.blockstmt()) # Block
        return [MethodDecl(kind, name, param, returnType, body)]
    
    # normalMethod: (STATIC | ) typ ID paramDecl blockstmt;
    def visitNormalMethod(self, ctx:BKOOLParser.NormalMethodContext):
        kind = Static() if ctx.STATIC() else Instance()
        name = Id(ctx.ID().getText())
        param = self.visit(ctx.paramDecl())
        # returnType = VoidType() if ctx.ID().getText() == 'main' else self.visit(ctx.typ())
        returnType = self.visit(ctx.typ())
        body = self.visit(ctx.blockstmt())
        return [MethodDecl(kind, name, param, returnType, body)]
    
    # ! Problem: there are 2 special method: 
    # ! Constructor:    kind = Instance() 
    # !                 name = Id("<init>") 
    # !                 returnType = None 
    # ! ------------------------------------------
    # ! Main method:    kind = Static()
    # !                 name = Id("main") 
    # !                 returnType = VoidType() 

    # typ: primiTyp | classTyp | arrayTyp | VOID;
    def visitTyp(self, ctx:BKOOLParser.TypContext):
        if ctx.VOID():
            return VoidType()
        elif ctx.primiTyp():
            return self.visit(ctx.primiTyp())
        elif ctx.classTyp():
            return self.visit(ctx.classTyp())
        elif ctx.arrayTyp():
            return self.visit(ctx.arrayTyp())
    
    # paramDecl: LB paramList RB;
    def visitParamDecl(self, ctx:BKOOLParser.ParamDeclContext):
        return self.visit(ctx.paramList())
    
    # paramList: paramPrime | ;
    def visitParamList(self, ctx:BKOOLParser.ParamListContext):
        if ctx.paramPrime():
            return self.visit(ctx.paramPrime())
        else: 
            return []
    
    # paramPrime: param SEMI paramPrime | param;
    def visitParamPrime(self, ctx:BKOOLParser.ParamPrimeContext):
        # int x, y; float z -> [VarDecl(Id(x), IntType), VarDecl(Id(y), IntType)] + [VarDecl(Id(z), FloatType)]
        if ctx.getChildCount() == 1:
            return self.visit(ctx.param())
        else:
            return self.visit(ctx.param()) + self.visit(ctx.paramPrime())
    
    # param: typ idlist (List[VarDecl])
    def visitParam(self, ctx:BKOOLParser.ParamContext):
        # int x, y -> [VarDecl(Id(x), IntType), VarDecl(Id(y), IntType)]
        typ = self.visit(ctx.typ()) # IntType
        idlist = self.visit(ctx.idlist()) # [Id(x), Id(y), Id(z)]
        return [VarDecl(x, typ, None) for x in idlist]
    
    # idlist: ID COMMA idlist | ID;
    def visitIdlist(self, ctx:BKOOLParser.IdlistContext):
        # x, y, z -> [Id(x), Id(y), Id(z)]
        # x -> [Id(x)]
        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText())]
        else:
            idlist = self.visit(ctx.idlist())
            return [Id(ctx.ID().getText())] + idlist

    # ~ 2.2: Attribute Declaration 
    # class AttributeDecl(MemDecl):
    #       kind: SIKind (Static() of Instance())
    #       decl: StoreDecl 
    #             VarDecl for mutable 
    #             ConstDecl for immutable
    
    # attrDecl: immutDecl | mutDecl;
    def visitAttrDecl(self, ctx:BKOOLParser.AttrDeclContext):
        if ctx.immutDecl():
            return self.visit(ctx.immutDecl())
        else:
            return self.visit(ctx.mutDecl())
        
    # immutDecl: immutKeywords typ attrList SEMI;
    def visitImmutDecl(self, ctx:BKOOLParser.ImmutDeclContext):
        kind = self.visit(ctx.immutKeywords()) # SIkind
        # int x = 10 -> [ConstDecl(Id(x), IntType, IntLiteral(10))]
        # int x, y = 10 -> [ConstDecl(Id(x), IntType, IntLiteral(10)), ConstDecl(Id(y), IntType, IntLiteral(10))]
        typ = self.visit(ctx.typ())
        constdecl_list = [ConstDecl(x[0], typ, x[1]) for x in self.visit(ctx.attrList())]
        return [AttributeDecl(kind, x) for x in constdecl_list]

    # mutDecl: mutKeyword typ attrList SEMI;
    def visitMutDecl(self, ctx:BKOOLParser.MutDeclContext):
        kind = self.visit(ctx.mutKeyword())
        
        typ = self.visit(ctx.typ())
        vardecl_list = [VarDecl(x[0], typ, x[1]) for x in self.visit(ctx.attrList())]
        return [AttributeDecl(kind, x) for x in vardecl_list]

    # mutKeyword: STATIC | ;
    def visitMutKeyword(self, ctx:BKOOLParser.MutKeywordContext):
        if ctx.STATIC(): return Static()
        else: return Instance()
    
    # immutKeywords: FINAL | STATIC FINAL | FINAL STATIC;
    def visitImmutKeywords(self, ctx:BKOOLParser.ImmutKeywordsContext):
        if ctx.STATIC(): return Static()
        else: return Instance()
    
    # attrList: attrMember (COMMA attrMember)*;
    def visitAttrList(self, ctx:BKOOLParser.AttrListContext):
        res = [self.visit(x) for x in ctx.attrMember()]
        return [item for sub in res for item in sub]

    # attrMember: idlist attrInit;
    def visitAttrMember(self, ctx:BKOOLParser.AttrMemberContext):
        # x,y = 10
        # [VarDecl(Id("x"), IntType(), IntLiteral(10)),
        #  VarDecl(Id("y"), IntType(), IntLiteral(10))]
        idlist = self.visit(ctx.idlist())
        expr = self.visit(ctx.attrInit())
        return [[x, expr] for x in idlist]
        
    # attrInit: EQUAL_SIGN expr | ;
    def visitAttrInit(self, ctx:BKOOLParser.AttrInitContext):
        if ctx.expr(): return self.visit(ctx.expr())
        else: return None 
    
    # ~ 6: Statement 
    # stmtlist: stmt stmtlist | ;
    def visitStmtlist(self, ctx:BKOOLParser.StmtlistContext):
        if ctx.stmt():
            return [self.visit(ctx.stmt())] + self.visit(ctx.stmtlist())
        else:
            return []
        
    # stmt:	vardecllist
	#     |	blockstmt
	#     |	asmstmt
	#     |	ifstmt
	#     |	forstmt
	#     |	breakstmt
	#     |	contstmt
	#     |	retstmt
	#     |	methodivkstmt;
    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        return self.visit(ctx.getChild(0))      
    
    # ! blockstmt
    # blockstmt: LP stmtlist RP
    def visitBlockstmt(self, ctx:BKOOLParser.BlockstmtContext):
        # {
        #   int x;
        #   y := x;
        #   final int y = 10;
        #   for i := 
        # }
        
        # -> Block( [
        #               VarDecl(Id("x"), IntType()),
        #               ConstDecl(Id("y"), IntType(), IntLiteral(10))
        #           ],
        #           [
        #               Assign((Id("y"), Id("x")))
        #           ]
        #         )
        stmt_visit_list = []
        
        stack = [self.visit(ctx.stmtlist())]
            
        while stack:
            current = stack.pop()
            if isinstance(current, list): 
                stack.extend(reversed(current))
            else: stmt_visit_list.append(current)
        
        decls = []
        stmts = []
        for x in stmt_visit_list:
            if isinstance(x, StoreDecl): decls.append(x)
            elif isinstance(x, Stmt): stmts.append(x)
        return Block(decls, stmts)

    # & vardecl in blockstmt 
    # vardecllist: vardecl vardecllist | vardecl;
    def visitVardecllist(self, ctx:BKOOLParser.VardecllistContext):
        if ctx.vardecllist():
            return self.visit(ctx.vardecl()) + self.visit(ctx.vardecllist())
        else:
            return self.visit(ctx.vardecl())
    
    # vardecl: immutVardecl | mutVardecl;
    def visitVardecl(self, ctx:BKOOLParser.VardeclContext):
        if ctx.immutVardecl():
            return self.visit(ctx.immutVardecl())
        else:
            return self.visit(ctx.mutVardecl())
    
    # immutVardecl: FINAL typ attrList SEMI;
    def visitImmutVardecl(self, ctx:BKOOLParser.ImmutVardeclContext):
        # final int x = 1;
        # -> [ConstDecl(Id(x), IntType, IntLit(1))]
        typ = self.visit(ctx.typ())
        immut_init_list = self.visit(ctx.attrList())
        # x,y = 1, a = 1.2
        # [ [Id(x), IntLit(1)], [Id(y), IntLit(1)], [Id(a), FloatLit(1.2)] ]
        
        return [ConstDecl(x[0], typ, x[1]) for x in immut_init_list]
      
    # mutVardecl: typ attrList SEMI;
    def visitMutVardecl(self, ctx:BKOOLParser.MutVardeclContext):
        typ = self.visit(ctx.typ())
        mut_decl_list = self.visit(ctx.attrList())
        
        return [VarDecl(x[0], typ, x[1]) for x in mut_decl_list]
    
    # & 6.2: Assignment Statement 
    # asmstmt: asmlhs ASSIGN_OP expr SEMI;
    def visitAsmstmt(self, ctx:BKOOLParser.AsmstmtContext):
        lhs = self.visit(ctx.asmlhs()) # Expr
        exp = self.visit(ctx.expr()) # Expr
        return Assign(lhs, exp)

    # asmlhs: ID | expr9 DOT ID | expr8;
    def visitAsmlhs(self, ctx:BKOOLParser.AsmlhsContext):
        if ctx.DOT():
            obj = self.visit(ctx.expr9())
            fieldname = Id(ctx.ID().getText())
            return FieldAccess(obj, fieldname)
        elif ctx.expr8():
            return self.visit(ctx.expr8())
        else:
            return Id(ctx.ID().getText())
    
    # & 6.3: If Statement 
    # ifstmt: IF expr THEN stmt | IF expr THEN stmt ELSE stmt;
    def visitIfstmt(self, ctx:BKOOLParser.IfstmtContext):
        # if y > max then max := y else continue;
        expr = self.visit(ctx.expr()) # Expr (BinaryOp(">", Id("y"), Id("max")))
        thenStmt = self.visit(ctx.stmt(0)) # Stmt (Assign(Id("max"), Id("y")))
        elseStmt = self.visit(ctx.stmt(1)) if ctx.ELSE() else None # Stmt (Continue)
        return If(expr, thenStmt, elseStmt)
    
    # & 6.4: For Statement 
    # forstmt: FOR ID ASSIGN_OP expr (TO | DOWNTO) expr DO stmt;
    def visitForstmt(self, ctx:BKOOLParser.ForstmtContext):
        # for i := 1 to n do 
        id = Id(ctx.ID().getText()) # Id(i)
        expr1 = self.visit(ctx.expr(0)) # Expr (IntLiteral(10))
        expr2 = self.visit(ctx.expr(1)) # Expr (Id("n"))
        up = True if ctx.TO() else False # Bool (True)
        loop = self.visit(ctx.stmt()) # Stmt (Block([...], [...]))
        return For(id, expr1, expr2, up, loop)
    
    # & 6.5: Break Statement 
    # breakstmt: BREAK SEMI;
    def visitBreakstmt(self, ctx:BKOOLParser.BreakstmtContext):
        return Break()
    
    # & 6.6: Continue Statement 
    # contstmt: CONTINUE SEMI;
    def visitContstmt(self, ctx:BKOOLParser.ContstmtContext):
        return Continue()

    # & 6.7: Return Statement 
    # retstmt: RETURN expr SEMI;
    def visitRetstmt(self, ctx:BKOOLParser.RetstmtContext):
        expr = self.visit(ctx.expr()) # Expr
        return Return(expr)
    
    # & 6.8: Method Invocation Statement 
    # methodivkstmt: expr9 DOT ID LB arglist RB SEMI;
    def visitMethodivkstmt(self, ctx:BKOOLParser.MethodivkstmtContext):
        obj = self.visit(ctx.expr9()) # Expr
        method = Id(ctx.ID().getText()) # Id
        param = self.visit(ctx.arglist()) # List[Expr]
        return CallStmt(obj, method, param)
            
    # ~ 5: Expression 
    # expr: expr1 (GT_OP | LT_OP | GTE_OP | LTE_OP) expr1 | expr1
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.expr1(0)) # Expr
            op = ctx.getChild(1).getText() # str ['>', '<', '>=', '=<']
            right = self.visit(ctx.expr1(1)) # Expr
            return BinaryOp(op, left, right)
        else: 
            return self.visit(ctx.expr1(0))
            
    # expr1: expr2 (EQUAL_OP | NEQUAL_OP) expr2 | expr2;
    def visitExpr1(self, ctx:BKOOLParser.Expr1Context):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.expr2(0)) # Expr
            op = ctx.getChild(1).getText() # str
            right = self.visit(ctx.expr2(1)) # Expr
            return BinaryOp(op, left, right)
        else: 
            return self.visit(ctx.expr2(0))
    
    # expr2: expr2 (AND_OP | OR_OP) expr3 | expr3;
    def visitExpr2(self, ctx:BKOOLParser.Expr2Context):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.expr2()) # Expr
            op = ctx.getChild(1).getText() # str
            right = self.visit(ctx.expr3()) # Expr
            return BinaryOp(op, left, right)
        else: 
            return self.visit(ctx.expr3())
    
    # expr3: expr3 (ADD_OP | SUB_OP) expr4 | expr4;
    def visitExpr3(self, ctx:BKOOLParser.Expr3Context):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.expr3()) # Expr
            op = ctx.getChild(1).getText() # str
            right = self.visit(ctx.expr4()) # Expr
            return BinaryOp(op, left, right) 
        else: 
            return self.visit(ctx.expr4())
    
    # expr4: expr4 (MUL_OP | INTDIV_OP | FLODIV_OP | MOD_OP) expr5 | expr5;
    def visitExpr4(self, ctx:BKOOLParser.Expr4Context):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.expr4()) # Expr
            op = ctx.getChild(1).getText() # str
            right = self.visit(ctx.expr5()) # Expr
            return BinaryOp(op, left, right)
        else: 
            return self.visit(ctx.expr5())
    
    # expr5: expr5 (CONCAT_OP) expr6 | expr6;
    def visitExpr5(self, ctx:BKOOLParser.Expr5Context):
        if ctx.CONCAT_OP():
            left = self.visit(ctx.expr5()) # Expr
            op = ctx.getChild(1).getText() # str
            right = self.visit(ctx.expr6()) # Expr
            return BinaryOp(op, left, right)
        else: 
            return self.visit(ctx.expr6())
    
    # expr6: (NOT_OP) expr6 | expr7;
    def visitExpr6(self, ctx:BKOOLParser.Expr6Context):
        if ctx.NOT_OP():
            op = ctx.getChild(0).getText() # str
            body = self.visit(ctx.expr6()) # Expr
            return UnaryOp(op, body)
        else: 
            return self.visit(ctx.expr7())
    
    # expr7: (ADD_OP | SUB_OP) expr7 | expr8; 
    def visitExpr7(self, ctx:BKOOLParser.Expr7Context):
        if ctx.getChildCount() == 2:
            op = ctx.getChild(0).getText() # str
            body = self.visit(ctx.expr7()) # Expr
            return UnaryOp(op, body)
        else: 
            return self.visit(ctx.expr8())
        
    # expr8: expr9 LSB expr RSB | expr9;
    def visitExpr8(self, ctx:BKOOLParser.Expr8Context):
        if ctx.getChildCount() == 4:
            arr = self.visit(ctx.expr9()) # Expr
            idx = self.visit(ctx.expr()) # Expr
            return ArrayCell(arr, idx)
        else: 
            return self.visit(ctx.expr9())
    
    # expr9: expr9 DOT ID 					
	#      | expr9 DOT ID LB arglist RB
	#      | expr10;
    def visitExpr9(self, ctx: BKOOLParser.Expr9Context):
        if ctx.getChildCount() == 3:
            obj = self.visit(ctx.expr9()) # Expr
            fieldname = Id(ctx.ID().getText()) # Id
            return FieldAccess(obj, fieldname)
        elif ctx.arglist():
            obj = self.visit(ctx.expr9()) # Expr
            method = Id(ctx.ID().getText()) # Id 
            param = self.visit(ctx.arglist()) # List[Expr]
            return CallExpr(obj, method, param)
        else: 
            return self.visit(ctx.expr10())
    
    # expr10: NEW ID LB arglist RB | expr11;
    def visitExpr10(self, ctx: BKOOLParser.Expr10Context):
        if ctx.NEW():
            classname = Id(ctx.ID().getText()) # Id
            param = self.visit(ctx.arglist()) # List[Expr]
            return NewExpr(classname, param)
        else:
            return self.visit(ctx.expr11())
    
    # expr11: THIS | ID | NIL | primiLit | arrayLit | subexpr;
    def visitExpr11(self, ctx: BKOOLParser.Expr11Context):
        if ctx.THIS(): 
            return SelfLiteral()
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.NIL():
            return NullLiteral()
        elif ctx.primiLit():
            return self.visit(ctx.primiLit())
        elif ctx.arrayLit():
            return self.visit(ctx.arrayLit())
        elif ctx.subexpr():
            return self.visit(ctx.subexpr())
            
    # arglist: argprime | ;
    def visitArglist(self, ctx: BKOOLParser.ArglistContext):
        if ctx.argprime():
            return self.visit(ctx.argprime())
        else: 
            return []
    
    # argprime: expr COMMA argprime | expr;
    def visitArgprime(self, ctx: BKOOLParser.ArgprimeContext):
        if ctx.COMMA():
            return [self.visit(ctx.expr())] + self.visit(ctx.argprime())
        else:
            return [self.visit(ctx.expr())]
    
    # primiLit: INTLIT | FLOATLIT | STRINGLIT | booleanLit;
    def visitPrimiLit(self, ctx: BKOOLParser.PrimiLitContext):
        if ctx.INTLIT(): 
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.booleanLit():
            return self.visit(ctx.booleanLit())
    
    # subexpr: LB expr RB;
    def visitSubexpr(self, ctx: BKOOLParser.SubexprContext):
        return self.visit(ctx.expr())
    
    # ~ 3.7.4: Boolean Literal 
    # booleanLit: TRUE | FALSE; 
    def visitBooleanLit(self, ctx:BKOOLParser.BooleanLitContext):
        if ctx.TRUE(): return BooleanLiteral(True)
        else: return BooleanLiteral(False)
    
    # ~ 3.7.5: Array Literal 
    # arrayLit:	LP arrMemberList RP;
    def visitArrayLit(self, ctx:BKOOLParser.ArrayLitContext):
        return ArrayLiteral(self.visit(ctx.arrMemberList()))
    
    # arrMemberList: arrMember COMMA arrMemberList | arrMember;
    def visitArrMemberList(self, ctx:BKOOLParser.ArrMemberListContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.arrMember())] + self.visit(ctx.arrMemberList())
        else:
            return [self.visit(ctx.arrMember())]   
    
    # arrMember: INTLIT | FLOATLIT | STRINGLIT | booleanLit;
    def visitArrMember(self, ctx:BKOOLParser.ArrMemberContext):
        if ctx.INTLIT(): 
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.booleanLit():
            return self.visit(ctx.booleanLit())
    
    # ~ 4: TYPE 
    # primiTyp:	INT | FLOAT | STRING | BOOLEAN;
    def visitPrimiTyp(self, ctx:BKOOLParser.PrimiTypContext):
        if ctx.INT():       return IntType()
        elif ctx.FLOAT():   return FloatType()
        elif ctx.STRING():  return StringType()
        elif ctx.BOOLEAN(): return BoolType()
        
    # classTyp: ID
    def visitClassTyp(self, ctx:BKOOLParser.ClassTypContext):
        return ClassType(Id(ctx.ID().getText()))
    
    # arrayTyp: (primiTyp | classTyp) LSB INTLIT RSB;
    def visitArrayTyp(self, ctx:BKOOLParser.ArrayTypContext):
        if ctx.primiTyp(): arrType = self.visit(ctx.primiTyp())
        elif ctx.classTyp(): arrType = self.visit(ctx.classTyp())   
        arrSize = int(ctx.INTLIT().getText())
        return ArrayType(arrSize, arrType)    