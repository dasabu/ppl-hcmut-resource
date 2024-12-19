from os import linesep
from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *

class ASTGeneration(BKOOLVisitor):

    def visitProgram(self,ctx:BKOOLParser.ProgramContext):
        #program: (class_decl)+ EOF;
        return Program([self.visit(x) for x in ctx.classDecl()])


    def visitType_name(self, ctx: BKOOLParser.Type_nameContext):
        #Type: BOOLEAN | INT | FLOAT | STRING | arrType | objType;
        if ctx.BOOLEAN():
            return BoolType()
        elif ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.arrType():
            return self.visit(ctx.arrType())
        elif ctx.objType():
            return self.visit(ctx.objType())

    def visitArrType(self, ctx: BKOOLParser.ArrTypeContext):
        return ArrayType(self.visit(ctx.size()), self.visit(ctx.element_type()))

    def visitSize(self, ctx: BKOOLParser.SizeContext):
        return int(ctx.INTLIT().getText())
    # Visit a parse tree produced by BKOOLParser#element_type.
    def visitElement_type(self, ctx: BKOOLParser.Element_typeContext):
        if ctx.BOOLEAN():
            return BoolType()
        if ctx.STRING():
            return StringType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.INT():
            return IntType()
        if ctx.objType():
            return self.visit(ctx.objType())
    def visitClassDecl(self, ctx: BKOOLParser.ClassDeclContext):
        # classDecl: CLASS className (EXTENDS ID)? LP classMem* RP;
        return ClassDecl(self.visit(ctx.className()),
                         [self.visit(x) for x in ctx.classMem()],
                         Id(ctx.ID().getText()) if ctx.EXTENDS() else None)

    def visitClassName(self, ctx: BKOOLParser.ClassNameContext):
        return Id(ctx.ID().getText())

    def visitClassMem(self, ctx:BKOOLParser.ClassMemContext):
        #classMem: attributeDecl | methodDecl | constructor | mainMethod | voidMethod;
        if ctx.attributeDecl():
            return self.visit(ctx.attributeDecl())
        elif ctx.methodDecl():
            return self.visit(ctx.methodDecl())
        elif ctx.mainMethod():
            return self.visit(ctx.mainMethod())
        elif ctx.voidMethod():
            return self.visit(ctx.voidMethod())
        elif ctx.constructor():
            return self.visit(ctx.constructor())

    def visitAttributeDecl(self, ctx: BKOOLParser.AttributeDeclContext):
        # attributeDecl: mutableAttribute | immutableAttribute | objAttribute;
        if ctx.mutableAttribute():
            return self.visit(ctx.mutableAttribute())
        elif ctx.immutableAttribute():
            return self.visit(ctx.immutableAttribute())
        elif ctx.objAttribute():
            return self.visit(ctx.objAttribute())

    def visitMutableAttribute(self, ctx: BKOOLParser.MutableAttributeContext):
        # mutableAttribute: STATIC? type ID muInit (COMMA ID muInit)* SEMI;
        kind = Static() if ctx.STATIC() else Instance()
        result = ""
        result += str(AttributeDecl(kind, VarDecl(Id(ctx.ID(0).getText()),
                                                  self.visit(ctx.type_name()),
                                                  self.visit(ctx.muInit(0)))))
        if ctx.COMMA():
            size = len(ctx.COMMA())
            for i in range(1, size + 1):
                result += ',' + str(AttributeDecl(kind, VarDecl(Id(ctx.ID(i).getText()),
                                                                self.visit(ctx.type_name()),
                                                                self.visit(ctx.muInit(i)))))
        return result

    def visitMuInit(self, ctx: BKOOLParser.MuInitContext):
        # muInit: (EQUAL_SIGN expr)?;
        return self.visit(ctx.expr())if ctx.expr() else None

    def visitImmutableAttribute(self, ctx: BKOOLParser.ImmutableAttributeContext):
        # immutableAttribute: (FINAL | STATIC FINAL | FINAL STATIC) type ID immuInit (COMMA ID immuInit)* SEMI;
        kind = Static() if ctx.STATIC() else Instance()
        result = ""
        result += str(AttributeDecl(kind, ConstDecl(Id(ctx.ID(0).getText()), self.visit(ctx.type_name()),
                                                    self.visit(ctx.immuInit(0)))))
        if ctx.COMMA():
            size = len(ctx.COMMA())
            for i in range(1, size + 1):
                result += ',' + str(AttributeDecl(kind, ConstDecl(Id(ctx.ID(i).getText()), self.visit(ctx.type_name()),
                                                                  self.visit(ctx.immuInit(i)))))
        return result

    def visitImmuInit(self, ctx: BKOOLParser.ImmuInitContext):
        # immuInit: EQUAL_SIGN exp;
        return self.visit(ctx.expr())

    def visitObjAttribute(self, ctx: BKOOLParser.ObjAttributeContext):
        # objAttribute: STATIC? objType ID objInit (COMMA ID objInit)* SEMI;
        kind = Static() if ctx.STATIC() else Instance()
        result = ""
        result += str(AttributeDecl(kind, VarDecl(Id(ctx.ID(0).getText()), self.visit(ctx.objType),
                                                  self.visit(ctx.objInit(0)))))
        if ctx.COMMA():
            size = len(ctx.COMMA())
            for i in range(1, size + 1):
                result += ',' + str(AttributeDecl(kind, VarDecl(Id(ctx.ID(i).getText()),
                                                                self.visit(ctx.objType),
                                                                self.visit(ctx.objInit(i)))))
        return result

    def visitObjType(self, ctx: BKOOLParser.ObjTypeContext):
        # objType: ID;
        return ClassType(Id(ctx.ID().getText()))

    def visitObjInit(self, ctx: BKOOLParser.ObjInitContext):
        # objInit: (EQUAL_SIGN exp10)?;
        return NewExpr(Id(ctx.ID().getText()),
                       self.visit(ctx.expList) if ctx.expList() else [])

    def visitMethodDecl(self, ctx: BKOOLParser.MethodDeclContext):
        # methodDecl: STATIC? type ID LB paramList? RB stmtBlock;
        kind = Static() if ctx.STATIC() else Instance()
        result = ""
        result += str(MethodDecl(kind,
                                 Id(ctx.ID().getText()),
                                 ctx.paramList().accept(self) if ctx.paramList() else [],
                                 self.visit(ctx.type_name()),
                                 ctx.stmtBlock().accept(self)))
        return result

    def visitParamList(self, ctx: BKOOLParser.ParamListContext):
        # paramList: paramInit (SEMI paramInit)*;
        result = []
        if ctx.SEMI():
            size = len(ctx.SEMI())
            for i in range(0, size + 1):
                result += ctx.paramInit(i).accept(self)
        else:
            result += ctx.paramInit(0).accept(self)
        return result

    def visitParamInit(self, ctx: BKOOLParser.ParamInitContext):
        # paramInit: type ID (COMMA ID)*;
        paramInit = []
        type = self.visit(ctx.type_name())
        if ctx.COMMA():
            size = len(ctx.COMMA())
            for i in range(0, size + 1):
                paramInit.append(VarDecl(Id(ctx.ID(i).getText()), type))
        else:
            paramInit.append(VarDecl(Id(ctx.ID(0).getText()), type))
        return paramInit

    def visitMainMethod(self, ctx: BKOOLParser.MainMethodContext):
        # mainMethod: STATIC? VOID 'main' LB RB stmtBlock_wo_return;
        result = ""
        result += str(MethodDecl(Static(),
                                 Id('main'),
                                 [],
                                 VoidType(),
                                 self.visit(ctx.stmtBlock_wo_return())))
        return result

    def visitVoidMethod(self, ctx: BKOOLParser.VoidMethodContext):
        # voidMethod: STATIC? VOID ID LB paramList? RB stmtBlock_wo_return;
        kind = Static() if ctx.STATIC() else Instance()
        result = ""
        result += str(MethodDecl(kind,
                                 Id(ctx.ID().getText()),
                                 ctx.paramList().accept(self) if ctx.paramList() else [],
                                 VoidType(),
                                 self.visit(ctx.stmtBlock_wo_return())))
        return result

    def visitConstructor(self, ctx: BKOOLParser.ConstructorContext):
        # constructor: className LB paramList? RB stmtBlock_constructor;
        result = ""
        result += str(MethodDecl(Instance(),
                                 Id('"<init>"'),
                                 ctx.paramList().accept(self) if ctx.paramList() else [],
                                 None,
                                 ctx.stmtBlock_constructor().accept(self)))
        return result

    def visitStmt(self, ctx: BKOOLParser.StmtContext):
        if ctx.asmStmt():
            return self.visit(ctx.asmStmt())
        elif ctx.ifStmt():
            return self.visit(ctx.ifStmt())
        elif ctx.forStmt():
            return self.visit(ctx.forStmt())
        elif ctx.breakStmt():
            return self.visit(ctx.breakStmt())
        elif ctx.continueStmt():
            return self.visit(ctx.continueStmt())
        elif ctx.returnStmt():
            return ctx.returnStmt().accept(self)
        elif ctx.method_invo_stmt():
            return self.visit(ctx.method_invo_stmt())
        elif ctx.stmtBlock():
            return ctx.stmtBlock().accept(self)

    def visitStmt_wo_return(self, ctx: BKOOLParser.Stmt_wo_returnContext):
        ##print("Load")
        if ctx.asmStmt():
            return self.visit(ctx.asmStmt())
        elif ctx.ifStmt():
            return self.visit(ctx.ifStmt())
        elif ctx.forStmt():
            return self.visit(ctx.forStmt())
        elif ctx.breakStmt():
            return self.visit(ctx.breakStmt())
        elif ctx.continueStmt():
            return self.visit(ctx.continueStmt())
        elif ctx.method_invo_stmt():
            return self.visit(ctx.method_invo_stmt())
        elif ctx.stmtBlock_wo_return():
            return self.visit(ctx.stmtBlock_wo_return())

    def visitExpr(self, ctx: BKOOLParser.ExprContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        else:
            return self.visit(ctx.exp2(0))

    # Visit a parse tree produced by BKOOLParser#exp2.
    def visitExp2(self, ctx: BKOOLParser.Exp2Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(self.visit(ctx.relational()), self.visit(ctx.exp3(0)), self.visit(ctx.exp3(1)))
        else:
            return self.visit(ctx.exp3(0))

    # Visit a parse tree produced by BKOOLParser#relational.
    def visitRelational(self, ctx: BKOOLParser.RelationalContext):
        return ctx.getChild(0).getText()

    # Visit a parse tree produced by BKOOLParser#exp3.
    def visitExp3(self, ctx: BKOOLParser.Exp3Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))
        else:
            return self.visit(ctx.exp4())

    # Visit a parse tree produced by BKOOLParser#exp4.
    def visitExp4(self, ctx: BKOOLParser.Exp4Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        else:
            return self.visit(ctx.exp5())

    # Visit a parse tree produced by BKOOLParser#exp5.
    def visitExp5(self, ctx: BKOOLParser.Exp5Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp5()), self.visit(ctx.exp6()))
        else:
            return self.visit(ctx.exp6())

    # Visit a parse tree produced by BKOOLParser#exp6.
    def visitExp6(self, ctx: BKOOLParser.Exp6Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.exp6()))
        else:
            return self.visit(ctx.exp7())

    # Visit a parse tree produced by BKOOLParser#exp7.
    def visitExp7(self, ctx: BKOOLParser.Exp7Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.exp7()))
        else:
            return self.visit(ctx.exp8())

    def visitExp8(self, ctx: BKOOLParser.Exp8Context):
        # exp8: exp8 LSB exp8 RSB | exp9;
        if ctx.getChildCount() == 4:
            return ArrayCell(self.visit(ctx.exp8()), self.visit(ctx.expr()))
        else:
            return self.visit(ctx.exp9())

    def visitExp9(self, ctx: BKOOLParser.Exp9Context):
        #print("visit exp9")
        if ctx.getChildCount() == 3:
            if ctx.tail_part().getChildCount() == 1:
                return FieldAccess(self.visit(ctx.exp9()), self.visit(ctx.tail_part()))
            else:
                temp = self.visit(ctx.tail_part())
                return CallExpr(self.visit(ctx.exp9()), temp[0], temp[1])
        else:
            return self.visit(ctx.exp10())

        # Visit a parse tree produced by BKOOLParser#tail_part.
    def visitTail_part(self, ctx: BKOOLParser.Tail_partContext):
        #print("visit tail")
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        else:
            return (Id(ctx.ID().getText()), self.visit(ctx.expList()) if ctx.expList() else [])

    def visitExp10(self, ctx: BKOOLParser.Exp10Context):
        #print("10")
        if ctx.THIS():
            return SelfLiteral()
        else:
            return self.visit(ctx.exp11())

    def visitExp11(self, ctx: BKOOLParser.Exp11Context):
        if ctx.exp11_access():
            return self.visit(ctx.exp11_access())
        elif ctx.exp11_call():
            return self.visit(ctx.exp11_call())
        else:
            return self.visit(ctx.exp12())

    def visitExp11_access(self, ctx: BKOOLParser.Exp11_accessContext):
        return FieldAccess(Id(ctx.ID(0).getText()),
                           Id(ctx.ID(1).getText()))

    def visitExp11_call(self, ctx: BKOOLParser.Exp11_callContext):
        return CallExpr(Id(ctx.ID(0).getText()),
                 Id(ctx.ID(1).getText()),
                 self.visit(ctx.expList()) if ctx.expList() else [])

    def visitExp12(self, ctx: BKOOLParser.Exp12Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp13())
        else:
            return NewExpr(Id(ctx.ID().getText()), self.visit(ctx.expList()) if ctx.expList() else [])

    def visitExp13(self, ctx: BKOOLParser.Exp13Context):
        #print("13")
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.getChildCount() == 3:
            return self.visit(ctx.expr())
        else:
            return self.visit(ctx.literal())


    def visitExpList(self, ctx: BKOOLParser.ExpListContext):
        # expList: (exp (COMMA exp)*);
        result = []
        result.append(ctx.expr(0).accept(self))
        if ctx.COMMA():
            size = len(ctx.COMMA())
            for i in range(1, size + 1):
                result.append(ctx.expr(i).accept(self))
        return result


    def visitVarDecl(self, ctx: BKOOLParser.VarDeclContext):
        # varDecl: mutableVar | immutableVar | objVar;
        if ctx.mutableVar():
            return ctx.mutableVar().accept(self)
        elif ctx.immutableVar():
            return ctx.immutableVar().accept(self)
        elif ctx.objVar():
            return ctx.objVar().accept(self)

    def visitMutableVar(self, ctx: BKOOLParser.MutableVarContext):
        # mutableVar: type ID muInit (COMMA ID muInit)* SEMI;
        result = ""
        result += str(VarDecl(Id(ctx.ID(0).getText()),
                              self.visit(ctx.type_name()),
                              self.visit(ctx.muInit(0))))
        if ctx.COMMA():
            size = len(ctx.COMMA())
            for i in range(1, size + 1):
                result += ',' + str(VarDecl(Id(ctx.ID(i).getText()),
                                            self.visit(ctx.type_name()),
                                            self.visit(ctx.muInit(i))))
        return result

    def visitImmutableVar(self, ctx: BKOOLParser.ImmutableVarContext):
        # immutableVar: FINAL? type ID immuInit (COMMA ID immuInit)* SEMI;
        result = ""
        result += str(ConstDecl(Id(ctx.ID(0).getText()),
                                self.visit(ctx.type_name()),
                                self.visit(ctx.immuInit(0))))
        if ctx.COMMA():
            size = len(ctx.COMMA())
            for i in range(1, size + 1):
                result += ',' + str(ConstDecl(Id(ctx.ID(i).getText()),
                                              self.visit(ctx.type_name()),
                                              self.visit(ctx.immuInit(i))))
        return result

    def visitObjVar(self, ctx: BKOOLParser.ObjVarContext):
        # objVar: objType ID objInit (COMMA ID objInit)* SEMI;
        result = ""
        result += str(VarDecl(Id(ctx.ID(0).getText()),
                              self.visit(ctx.objType()),
                              ctx.objInit(0).accept(self)))
        if ctx.COMMA():
            size = len(ctx.COMMA())
            for i in range(1, size + 1):
                result += ',' + str(VarDecl(Id(ctx.ID(i).getText()),
                                            self.visit(ctx.objType()),
                                            self.visit(ctx.objInit(i))))
        return result

    def visitVarDecl_constructor(self, ctx: BKOOLParser.VarDecl_constructorContext):
        # varDecl: mutableVar_constructor | immutableVar | objVar;
        if ctx.mutableVar_constructor():
            return self.visit(ctx.mutableVar_constructor())
        elif ctx.immutableVar():
            return self.visit(ctx.immutableVar())
        elif ctx.objVar():
            return self.visit(ctx.objVar())

    def visitMutableVar_constructor(self, ctx: BKOOLParser.MutableVar_constructorContext):
        # mutableVar_constructor: type ID constructorInit (COMMA ID constructorInit)* SEMI;
        result = ""
        result += str(VarDecl(Id(ctx.ID(0).getText()),
                              self.visit(ctx.type_name()),
                              self.visit(ctx.constructorInit(0))))
        if ctx.COMMA():
            size = len(ctx.COMMA())
            for i in range(1, size + 1):
                result += ',' + str(VarDecl(Id(ctx.ID(i).getText()),
                                            self.visit(ctx.type_name()),
                                            self.visit(ctx.constructorInit(i))))
        return result

    def visitConstructorInit(self, ctx: BKOOLParser.ConstructorInitContext):
        return self.visit(ctx.expr()) if ctx.expr() else NullLiteral()

    def visitStmtBlock(self, ctx: BKOOLParser.StmtBlockContext):
        # stmtBlock: LP (varDecl | stmt)* RP;
        return Block([self.visit(x) for x in ctx.varDecl()],
                     [self.visit(y) for y in ctx.stmt()])

    def visitStmtBlock_wo_return(self, ctx: BKOOLParser.StmtBlock_wo_returnContext):
        # stmtBlock_wo_return: LP (varDecl | stmt_wo_return)* RP;
        return Block([self.visit(x) for x in ctx.varDecl()],
                     [self.visit(y) for y in ctx.stmt_wo_return()])

    def visitStmtBlock_constructor(self, ctx: BKOOLParser.StmtBlock_constructorContext):
        # stmtBlock_constructor: LP (varDecl_constructor | stmt_wo_return)* RP;
        return Block([self.visit(x) for x in ctx.varDecl_constructor()],
                     [self.visit(y) for y in ctx.stmt_wo_return()])

    def visitAsmStmt(self, ctx: BKOOLParser.AsmStmtContext):
        # asmStmt: lhs ASSIGN exp SEMI;
        return Assign(self.visit(ctx.lhs()), self.visit(ctx.expr()))

    def visitLhs(self, ctx: BKOOLParser.LhsContext):
        # lhs: ID | (ID|THIS) DOT (ID|ID LSB exp RSB) | ID LSB exp RSB;
        if ctx.getChildCount() == 1:
            return Id(ctx.ID(0).getText())
        elif ctx.getChildCount() == 4:
            return ArrayCell(Id(ctx.ID(0).getText()), self.visit(ctx.expr()))
        else:
            if ctx.getChildCount() == 3:
                return FieldAccess(Id(ctx.getChild(0).getText()) if ctx.ID() else SelfLiteral(),
                                   Id(ctx.getChild(2).getText()))
            else:
                return FieldAccess(Id(ctx.getChild(0).getText()) if ctx.ID() else SelfLiteral(),
                                   ArrayCell(Id(ctx.getChild(2).getText()), self.visit(ctx.expr())))

    def visitIfStmt(self, ctx: BKOOLParser.IfStmtContext):
        # ifStmt: IF exp THEN stmt (ELSE stmt)?;
        return If(self.visit(ctx.expr()),
                  self.visit(ctx.stmt(0)),
                  self.visit(ctx.stmt(1)) if ctx.ELSE() else None)

    def visitForStmt(self, ctx: BKOOLParser.ForStmtContext):
        # forStmt: FOR ID ASSIGN exp (TO|DOWNTO) exp DO stmt;
        return For(Id(ctx.ID().getText()),
                   self.visit(ctx.expr(0)),
                   self.visit(ctx.expr(1)),
                   bool(True) if ctx.TO() else bool(False),
                   self.visit(ctx.stmt()))

    def visitBreakStmt(self, ctx: BKOOLParser.BreakStmtContext):
        # breakStmt: BREAK SEMI;
        return Break()

    def visitContinueStmt(self, ctx: BKOOLParser.ContinueStmtContext):
        # continueStmt: CONTINUE SEMI;
        return Continue()

    def visitReturnStmt(self, ctx: BKOOLParser.ReturnStmtContext):
        # returnStmt: RETURN exp SEMI;
        return Return(self.visit(ctx.expr()))

    def visitMethod_invo_stmt(self, ctx: BKOOLParser.Method_invo_stmtContext):
        # method_invo: (ID|THIS) DOT exp expListWithBrackets? SEMI;
        #print("visit invo")
        expr = str(self.visit(ctx.expr()))
        if ctx.getChildCount() > 4:
            return CallStmt(expr,
                            Id(ctx.ID().getText()),
                            self.visit(ctx.expList()) if ctx.expList() else [])
        else:
            return FieldAccess(expr, Id(ctx.ID().getText()))

    def visitLiteral(self, ctx: BKOOLParser.LiteralContext):
        # literal: FLOATLIT | INTLIT | bool_lit | STRING_LIT | arr_lit;
        if ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.bool_lit():
            return BooleanLiteral(ctx.bool_lit().accept(self))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.indexarr_lit():
            return self.visit(ctx.indexarr_lit())

    def visitIndexarr_lit(self, ctx: BKOOLParser.Indexarr_litContext):
        return ArrayLiteral(self.visit(ctx.arr_exp()))

    def visitArr_exp(self, ctx: BKOOLParser.Arr_expContext):
        return [self.visit(ctx.literal())] + self.visit(ctx.arr_exp()) if ctx.arr_exp() else [self.visit(ctx.literal())]

    def visitBool_lit(self, ctx: BKOOLParser.Bool_litContext):
        # bool_lit: TRUE | FALSE;
        return bool(True) if ctx.TRUE() else bool(False)

    def visitArrlit(self, ctx: BKOOLParser.ArrTypeContext):
        # arr_lit: LP arr_value (COMMA arr_value)* RP;
        result = []
        result.append(ctx.arr_value(0).accept(self))
        if ctx.COMMA():
            size = len(ctx.COMMA())
            for i in range(1, size + 1):
                result.append(ctx.arr_value(i).accept(self))
        return ArrayLiteral(result)
