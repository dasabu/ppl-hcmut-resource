from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *

class ASTGeneration(BKOOLVisitor):
     # program:            classDeclList EOF;
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return Program(self.visit(ctx.classDeclList()))


    # classDeclList:      classDecl classDeclList | classDecl ;
    def visitClassDeclList(self, ctx:BKOOLParser.ClassDeclListContext):
        if ctx.classDeclList():
            return [self.visit(ctx.classDecl())]+self.visit(ctx.classDeclList())
        return [self.visit(ctx.classDecl())]


    # classDecl: 			CLASS ID (EXTENDS ID)? classBody;
    def visitClassDecl(self, ctx:BKOOLParser.ClassDeclContext):
        classname = Id(ctx.ID(0).getText())
        memList = self.visit(ctx.classBody())
        if ctx.EXTENDS():
            parentname = Id(ctx.ID(1).getText())
            return ClassDecl(classname, memList,parentname)
        return ClassDecl(classname, memList,None)        
            
    # classBody: 			LP classBodyDeclList? RP;
    def visitClassBody(self, ctx:BKOOLParser.ClassBodyContext):
        return self.visit(ctx.classBodyDeclList()) if ctx.classBodyDeclList() else []

    # classBodyDeclList:  classBodyDecl +;
    def visitClassBodyDeclList(self, ctx:BKOOLParser.ClassBodyDeclListContext):
        temp = [self.visit(i) for i in ctx.classBodyDecl()]
        return [item for sublist in temp for item in sublist]



    # classBodyDecl:      attributeDecl |  methodDecl;
    def visitClassBodyDecl(self, ctx:BKOOLParser.ClassBodyDeclContext):
        return self.visit(ctx.attributeDecl()) if ctx.attributeDecl() else self.visit(ctx.methodDecl())


    #methodDecl:         (STATIC? returnType)? ID LB paramList? RB blockStmt;
    def visitMethodDecl(self, ctx:BKOOLParser.MethodDeclContext):
        name = Id(ctx.ID().getText())
        body = self.visit(ctx.blockStmt())
        param = [VarDecl(x[1],x[0],None) for x in self.visit(ctx.paramList())] if ctx.paramList() else []
        if ctx.returnType():
            returnType = self.visit(ctx.returnType())
            if ctx.STATIC():
                return [MethodDecl(Static(),name,param,returnType,body)]
            else:
                return [MethodDecl(Instance(),name,param,returnType,body)]
        else:
            return [MethodDecl(Instance(),Id("<init>"),param,None,body)]

        


    # paramList:          param SM paramList | param ;
    def visitParamList(self, ctx:BKOOLParser.ParamListContext):
        if ctx.paramList():
            return self.visit(ctx.param())+self.visit(ctx.paramList())
        return self.visit(ctx.param())


    # param:              typeType ids;
    def visitParam(self, ctx:BKOOLParser.ParamContext):
        return [[self.visit(ctx.typeType()),x] for x in self.visit(ctx.ids())]


    # ids:                ID COMMA ids | ID ;
    def visitIds(self, ctx:BKOOLParser.IdsContext):
        if ctx.ids():
            return [Id(ctx.ID().getText())]+self.visit(ctx.ids())
        return [Id(ctx.ID().getText())]


    # blockStmt:          LP varDecl* statement* RP;
    def visitBlockStmt(self, ctx:BKOOLParser.BlockStmtContext):
        temp = [self.visit(x) for x in ctx.varDecl()]
        decl = [item for sublist in temp for item in sublist]
        stmt = [self.visit(x) for x in ctx.statement()]
        return Block(decl,stmt)


    # varDecl:            FINAL? typeType variableDeclList SM ;
    def visitVarDecl(self, ctx:BKOOLParser.VarDeclContext):
        if ctx.FINAL():
            constType = self.visit(ctx.typeType())
            return [ConstDecl(x[0],constType,x[1]) for x in self.visit(ctx.variableDeclList())]
        else:
            varType = self.visit(ctx.typeType())
            return [VarDecl(x[0],varType,x[1]) for x in self.visit(ctx.variableDeclList())]


    # attributeDecl:      (STATIC | FINAL | STATIC FINAL | FINAL STATIC)? typeType variableDeclList SM;
    def visitAttributeDecl(self, ctx:BKOOLParser.AttributeDeclContext):
        kieu = self.visit(ctx.typeType())
        constlist =  [ConstDecl(x[0],kieu,x[1]) for x in self.visit(ctx.variableDeclList())]
        varialist =  [VarDecl(x[0],kieu,x[1]) for x in self.visit(ctx.variableDeclList())]
        if ctx.getChildCount() == 5:
            return [AttributeDecl(Static(),x) for x in constlist]
        elif ctx.getChildCount() == 4:
            if ctx.STATIC():
                return [AttributeDecl(Static(),x) for x in varialist]
            elif ctx.FINAL():
                return [AttributeDecl(Instance(),x) for x in constlist]
        else:
            return [AttributeDecl(Instance(),x) for x in varialist]

        


    # variableDeclList:   variableDeclarator COMMA variableDeclList | variableDeclarator ;
    def visitVariableDeclList(self, ctx:BKOOLParser.VariableDeclListContext):
        if ctx.variableDeclList():
            return [self.visit(ctx.variableDeclarator())]+self.visit(ctx.variableDeclList())
        return [self.visit(ctx.variableDeclarator())]


    # variableDeclarator: ID ('=' expression)?;
    def visitVariableDeclarator(self, ctx:BKOOLParser.VariableDeclaratorContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText()),None]
        else:
            return [Id(ctx.ID().getText()), self.visit(ctx.expression())]


    # Visit a parse tree produced by BKOOLParser#statement.
    def visitStatement(self, ctx:BKOOLParser.StatementContext):
        return self.visit(ctx.getChild(0))


    #breakStmt:          BREAK;
    def visitBreakStmt(self, ctx:BKOOLParser.BreakStmtContext):
        return Break()


    # continueStmt:       CONTINUE;
    def visitContinueStmt(self, ctx:BKOOLParser.ContinueStmtContext):
        return Continue()


    # returnStmt:         RETURN expression;
    def visitReturnStmt(self, ctx:BKOOLParser.ReturnStmtContext):
        return Return(self.visit(ctx.expression()))


    # methodInvoStmt:     expression9 DOT ID args;
    def visitMethodInvoStmt(self, ctx:BKOOLParser.MethodInvoStmtContext):
        obj = self.visit(ctx.expression9())
        method = Id(ctx.ID().getText())
        param = self.visit(ctx.args())
        return CallStmt(obj, method, param)


    # assignStmt:         lhsAssign ASS expression;
    def visitAssignStmt(self, ctx:BKOOLParser.AssignStmtContext):
        lhs = self.visit(ctx.lhsAssign())
        exp = self.visit(ctx.expression())
        return Assign(lhs, exp)


    # ifStmt:             IF expression THEN statement (ELSE statement)?;
    def visitIfStmt(self, ctx:BKOOLParser.IfStmtContext):
        expr = self.visit(ctx.expression())
        thenStmt = self.visit(ctx.statement(0))
        elseStmt = self.visit(ctx.statement(1)) if ctx.ELSE() else None
        return If(expr, thenStmt, elseStmt)

    # forStmt:            FOR ID ASS expression (TO | DOWNTO) expression DO statement ;
    def visitForStmt(self, ctx:BKOOLParser.ForStmtContext):
        id = Id(ctx.ID().getText())
        expr1 = self.visit(ctx.expression(0))
        expr2 = self.visit(ctx.expression(1))
        up = True if ctx.TO() else False
        loop = self.visit(ctx.statement())
        return For(id, expr1, expr2, up, loop)


    # lhsAssign:          ID | expression9 DOT ID | expression9 LSB expression RSB;
    def visitLhsAssign(self, ctx:BKOOLParser.LhsAssignContext):
        if ctx.getChildCount()==1:
            return Id(ctx.ID().getText())
        elif ctx.getChildCount()==3:
            obj = self.visit(ctx.expression9())
            fieldname = Id(ctx.ID().getText())
            return FieldAccess(obj, fieldname)
        else:
            arr = self.visit(ctx.expression9())
            idx = self.visit(ctx.expression())
            return ArrayCell(arr, idx)



    # expression:         expression1 (GT | LT | GTE | LTE) expression1 | expression1;
    def visitExpression(self, ctx:BKOOLParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression1(0))
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expression1(0))
        right = self.visit(ctx.expression1(1))
        return BinaryOp(op, left, right)


    # expression1:        expression2 (EQUAL | NEQUAL) expression2 | expression2;
    def visitExpression1(self, ctx:BKOOLParser.Expression1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression2(0))
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expression2(0))
        right = self.visit(ctx.expression2(1))
        return BinaryOp(op, left, right)


    # expression2:        expression2 (AND | OR) expression3 | expression3;
    def visitExpression2(self, ctx:BKOOLParser.Expression2Context):
        if ctx.getChildCount() == 1 :
            return self.visit(ctx.expression3())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expression2())
        right = self.visit(ctx.expression3())
        return BinaryOp(op, left, right)


    # expression3:        expression3 (ADD | SUB) expression4 | expression4;
    def visitExpression3(self, ctx:BKOOLParser.Expression3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression4())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expression3())
        right = self.visit(ctx.expression4())
        return BinaryOp(op, left, right)


    # expression4:        expression4 (MUL | FDIV | IDIV | MOD) expression5 | expression5;
    def visitExpression4(self, ctx:BKOOLParser.Expression4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression5())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expression4())
        right = self.visit(ctx.expression5())
        return BinaryOp(op, left, right)



    # expression5:        expression5 CONCAT expression6 | expression6;
    def visitExpression5(self, ctx:BKOOLParser.Expression5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression6())
        op=ctx.CONCAT().getText()
        left = self.visit(ctx.expression5())
        right = self.visit(ctx.expression6())
        return BinaryOp(op,left,right)


    # expression6:        NOT expression6 | expression7;
    def visitExpression6(self, ctx:BKOOLParser.Expression6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression7())
        op = ctx.NOT().getText()
        body = self.visit(ctx.expression6())
        return UnaryOp(op, body)


    # expression7:        (ADD | SUB) expression7 | expression8;
    def visitExpression7(self, ctx:BKOOLParser.Expression7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression8())
        op = ctx.ADD().getText() if ctx.ADD() else ctx.SUB().getText()
        body = self.visit(ctx.expression7())
        return UnaryOp(op, body)


    #expression8:        expression9 LSB expression RSB | expression9; 
    def visitExpression8(self, ctx:BKOOLParser.Expression8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression9())
        arr = self.visit(ctx.expression9())
        idx = self.visit(ctx.expression())
        return ArrayCell(arr, idx)


    #expression9:        expression9 DOT ID args | expression10 | expression9 DOT ID;
    def visitExpression9(self, ctx:BKOOLParser.Expression9Context):
        if ctx.getChildCount() == 4:
            obj = self.visit(ctx.expression9())
            method = Id(ctx.ID().getText())
            param = self.visit(ctx.args())
            return CallExpr(obj, method, param)
        elif ctx.getChildCount() == 3:
            obj = self.visit(ctx.expression9())
            fieldname = Id(ctx.ID().getText())
            return FieldAccess(obj, fieldname)
        else:
            return self.visit(ctx.expression10())
        



    # expression10:       NEW ID args | expression11;
    def visitExpression10(self, ctx:BKOOLParser.Expression10Context):
        if ctx.NEW():
            classname = Id(ctx.ID().getText())
            param = self.visit(ctx.args())
            return NewExpr(classname, param)
        return self.visit(ctx.expression11())



    # expression11:       elem | arrayLit | THIS | LB expression RB | ID;
    def visitExpression11(self, ctx:BKOOLParser.Expression11Context):
        if ctx.elem():
            return self.visit(ctx.elem())
        elif ctx.arrayLit():
            return self.visit(ctx.arrayLit())
        elif ctx.THIS():
            return SelfLiteral()
        elif ctx.expression():
            return self.visit(ctx.expression())
        elif ctx.ID():
            return Id(ctx.ID().getText())

    # args:               LB expList? RB;
    def visitArgs(self, ctx:BKOOLParser.ArgsContext):
        return self.visit(ctx.expList()) if ctx.expList() else []


    # expList:            expression COMMA expList | expression;
    def visitExpList(self, ctx:BKOOLParser.ExpListContext):
        if ctx.expList():
            return [self.visit(ctx.expression())]+self.visit(ctx.expList())
        return [self.visit(ctx.expression())]


    # typeType:           primitiveType | arrayType | classType ;
    def visitTypeType(self, ctx:BKOOLParser.TypeTypeContext):
        if ctx.primitiveType():
            return self.visit(ctx.primitiveType())
        elif ctx.arrayType():
            return self.visit(ctx.arrayType())
        elif ctx.classType():
            return self.visit(ctx.classType())

    # returnType: 		typeType;
    def visitReturnType(self, ctx:BKOOLParser.ReturnTypeContext):
        return self.visit(ctx.typeType())


    # arrayType:          (primitiveType | ID ) LSB INTLIT RSB;
    def visitArrayType(self, ctx:BKOOLParser.ArrayTypeContext):
        eleType = ClassType(Id(ctx.ID().getText())) if ctx.ID() else self.visit(ctx.primitiveType())
        size = int(ctx.INTLIT().getText())
        return ArrayType(size,eleType)

    # primitiveType:      INT | FLOAT | BOOLEAN | STRING | VOID ;
    def visitPrimitiveType(self, ctx:BKOOLParser.PrimitiveTypeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        elif ctx.VOID():
            return VoidType()


    # classType:			ID;
    def visitClassType(self, ctx:BKOOLParser.ClassTypeContext):
        return ClassType(Id(ctx.ID().getText()))


    #arrayLit:           LP elemArrays RP;
    def visitArrayLit(self, ctx:BKOOLParser.ArrayLitContext):
        return ArrayLiteral(self.visit(ctx.elemArrays()))


    # elemArrays:         elemArray COMMA elemArrays | elemArray ;
    def visitElemArrays(self, ctx:BKOOLParser.ElemArraysContext):
        if ctx.elemArrays():
            return [self.visit(ctx.elemArray())]+self.visit(ctx.elemArrays())
        return [self.visit(ctx.elemArray())]


    # elemArray:          INTLIT | FLOATLIT | booleanlit | STRINGLIT | NIL | THIS;
    def visitElemArray(self, ctx:BKOOLParser.ElemArrayContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.booleanlit():
            return self.visit(ctx.booleanlit())
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())  
        elif ctx.NIL():
            return NullLiteral()
        elif ctx.THIS():
            return SelfLiteral() 


    # elem:           	INTLIT | FLOATLIT | booleanlit | STRINGLIT | NIL;
    def visitElem(self, ctx:BKOOLParser.ElemContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.NIL():
            return NullLiteral()
        elif ctx.booleanlit():
            return self.visit(ctx.booleanlit())  
    
    # booleanlit:         TRUE | FALSE;
    def visitBooleanlit(self, ctx:BKOOLParser.BooleanlitContext):
        return BooleanLiteral(True) if ctx.TRUE() else BooleanLiteral(False)

    
