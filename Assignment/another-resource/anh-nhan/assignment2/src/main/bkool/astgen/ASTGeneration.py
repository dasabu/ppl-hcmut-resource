from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *


class ASTGeneration(BKOOLVisitor):

    def visitProgram(self, ctx: BKOOLParser.ProgramContext):
        return Program(self.visit(ctx.decl()))

    def visitDecl(self, ctx: BKOOLParser.DeclContext):
        return [self.visit(x) for x in ctx.class_decl()]

    def visitClass_decl(self, ctx: BKOOLParser.Class_declContext):
        classname = ctx.ID().getText()
        memberlist = self.visit(ctx.memberlist())
        superclass = self.visit(ctx.superclass())
        return ClassDecl(Id(classname), memberlist, superclass)

    def visitSuperclass(self, ctx: BKOOLParser.SuperclassContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return None

    def visitMemberlist(self, ctx: BKOOLParser.MemberlistContext):
        if ctx.member():
            return self.visit(ctx.member()) + self.visit(ctx.memberlist())
        else:
            return []

    def visitMember(self, ctx: BKOOLParser.MemberContext):
        if ctx.method_decl():
            return [self.visit(ctx.method_decl())]
        else:
            return self.visit(ctx.variable_decl())

    def visitVariable_decl(self, ctx: BKOOLParser.Variable_declContext):
        typename = self.visit(ctx.type_name())
        attribute_list = self.visit(ctx.attribute_list())
        # attribute (id, type, ())
        lst = []

        if ctx.STATIC():
            if ctx.FINAL():
                for i in range(len(attribute_list)):
                    if type(typename) == ClassType:
                        lst += [str(AttributeDecl(Static(), ConstDecl(attribute_list[i][0], typename, NullLiteral())))]
                    else:
                        lst += [str(AttributeDecl(Static(), ConstDecl(attribute_list[i][0], typename, attribute_list[i][1])))]
            else:
                for i in range(len(attribute_list)):
                    if type(typename) == ClassType:
                        lst += [str(AttributeDecl(Static(), VarDecl(attribute_list[i][0], typename, NullLiteral())))]
                    else:
                        lst += [str(AttributeDecl(Static(), VarDecl(attribute_list[i][0], typename, attribute_list[i][1])))]
        else:
            if ctx.FINAL():
                for i in range(len(attribute_list)):
                    if type(typename) == ClassType:
                        lst += [str(AttributeDecl(Instance(), ConstDecl(attribute_list[i][0], typename, NullLiteral())))]
                    else:
                        lst += [str(AttributeDecl(Instance(), ConstDecl(attribute_list[i][0], typename, attribute_list[i][1])))]
            else:
                for i in range(len(attribute_list)):
                    if type(typename) == ClassType:
                        lst += [str(AttributeDecl(Instance(), VarDecl(attribute_list[i][0], typename, NullLiteral())))]
                    else:
                        lst += [
                            str(AttributeDecl(Instance(), VarDecl(attribute_list[i][0], typename, attribute_list[i][1])))]
        return lst

    def visitAttribute_list(self, ctx: BKOOLParser.Attribute_listContext):
        if ctx.attribute_list():
            return [self.visit(ctx.attribute())] + self.visit(ctx.attribute_list())
        else:
            return [self.visit(ctx.attribute())]

    def visitAttribute(self, ctx: BKOOLParser.AttributeContext):
        if ctx.EQ():
            return (Id(ctx.ID().getText()), self.visit(ctx.expr()))
        else:
            return (Id(ctx.ID().getText()), None)  ## depend on định nghĩa của anh bí

    def visitMethod_decl(self, ctx: BKOOLParser.Method_declContext):
        if ctx.normalMethod():
            return self.visit(ctx.normalMethod())
        elif ctx.mainMethod():
            return self.visit(ctx.mainMethod())
        elif ctx.voidMethod():
            return self.visit(ctx.voidMethod())
        else:
            return self.visit(ctx.constructor())

    def visitNormalMethod(self, ctx: BKOOLParser.NormalMethodContext):
        kind = Static() if ctx.STATIC() else Instance()
        return str(MethodDecl(kind, Id(ctx.ID().getText()),
                          self.visit(ctx.paramlist()) if ctx.paramlist() else [],
                          self.visit(ctx.type_name()),
                          self.visit(ctx.block_stmt())))

    def visitMainMethod(self, ctx: BKOOLParser.MainMethodContext):
        kind = Static()

        return str(MethodDecl(kind, Id("main"), [] ,VoidType(), self.visit(ctx.block_stmt())))

    def visitVoidMethod(self, ctx: BKOOLParser.VoidMethodContext):
        kind = Static() if ctx.STATIC() else Instance()
        return str(MethodDecl(kind, Id(ctx.ID().getText()),
                          self.visit(ctx.paramlist()) if ctx.paramlist() else [],
                          VoidType(),
                          self.visit(ctx.block_stmt())))

    def visitConstructor(self, ctx: BKOOLParser.ConstructorContext):
        return str(MethodDecl(Instance(),Id('"<init>"'),
                          self.visit(ctx.paramlist()) if ctx.paramlist() else [],
                          None,
                          self.visit(ctx.block_stmt())))

    def visitType_name(self, ctx: BKOOLParser.Type_nameContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        elif ctx.array_type():
            return self.visit(ctx.array_type())
        elif ctx.class_type():
            return self.visit(ctx.class_type())

    def visitParam_list(self, ctx: BKOOLParser.ParamlistContext):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.param()) + self.visit(ctx.paramlist())
        else:
            return self.vist(ctx.param())

    def visitParam(self, ctx: BKOOLParser.ParamContext):
        type_name = self.visit(ctx.type_name())
        id_lst = self.visit(ctx.idlist())

        lst = []
        for i in range(len(id_lst)):
            lst += [VarDecl(id_lst[i], type_name, None)]

        return lst

    def visitIdlist(self, ctx: BKOOLParser.IdlistContext):
        if ctx.COMMA():
            return [Id(ctx.ID().getText())] + self.visit(ctx.idlist())
        else:
            return [Id(ctx.ID().getText())]

    def visitBlock_stmt(self, ctx: BKOOLParser.Block_stmtContext):
        return self.visit(ctx.block_body())

    def visitBlock_body(self, ctx: BKOOLParser.Block_bodyContext):
        if ctx.blocks():
            return self.visit(ctx.blocks())
        else:
            return []

    def visitBlocks(self, ctx: BKOOLParser.BlocksContext):
        var_decl = []
        stmt_decl = []

        for x in ctx.stmt():
            temp = self.visit(x)
            if temp[0] == 0:
                var_decl += temp[1]
            else:
                stmt_decl += temp[1]
        return Block(var_decl, stmt_decl)

    def visitStmt(self, ctx: BKOOLParser.StmtContext):
        if ctx.var_decl():
            return [0, self.visit(ctx.var_decl())]
        else:
            return [1, self.visit(ctx.other_stmt())]

    def visitVar_decl(self, ctx: BKOOLParser.Var_declContext):
        typename = self.visit(ctx.type_name())
        attribute_list = self.visit(ctx.attribute_list())
        # attribute (id, type, ())
        lst = []

        if ctx.FINAL():
            for i in range(len(attribute_list)):
                lst += [ConstDecl(attribute_list[i][0], typename, attribute_list[i][1])]
        else:
            for i in range(len(attribute_list)):
                lst += [VarDecl(attribute_list[i][0], typename, attribute_list[i][1])]
        return lst

    # Visit a parse tree produced by BKOOLParser#stmt.
    def visitOther_stmt(self, ctx: BKOOLParser.Other_stmtContext):
        if ctx.assignment_stmt():
            return [self.visit(ctx.assignment_stmt())]
        elif ctx.if_stmt():
            return [self.visit(ctx.if_stmt())]
        elif ctx.for_stmt():
            return [self.visit(ctx.for_stmt())]
        elif ctx.break_stmt():
            return [self.visit(ctx.break_stmt())]
        elif ctx.continue_stmt():
            return [self.visit(ctx.continue_stmt())]
        elif ctx.return_stmt():
            return [self.visit(ctx.return_stmt())]
        elif ctx.method_invo_stmt():
            return [self.visit(ctx.method_invo_stmt())]
        elif ctx.block_stmt():
            return [self.visit(ctx.block_stmt())]

    def visitAssignment_stmt(self, ctx: BKOOLParser.Assignment_stmtContext):
        left = self.visit(ctx.lhs())
        right = self.visit(ctx.expr())
        return Assign(left, right)

    def visitLhs(self, ctx: BKOOLParser.LhsContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.scalar_variable())
        else:
            return ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.indexop()))

    def visitScalar_variable(self, ctx: BKOOLParser.Scalar_variableContext):
        if ctx.getChildCount() == 1:
            if ctx.ID():
                return Id(ctx.ID().getText())
            else:
                return self.visit(ctx.exp10_access())
        elif ctx.getChildCount() == 3:
            return FieldAccess(self.visit(ctx.exp9()), Id(ctx.ID().getText()))
        else:
            return FieldAccess(Id(ctx.ID().getText()), ArrayCell(self.visit(ctx.exp9()), self.visit(ctx.indexop())))

    def visitIf_stmt(self, ctx: BKOOLParser.If_stmtContext):
        if ctx.else_stmt():
            if ctx.block_stmt():
                return If(self.visit(ctx.expr()), self.visit(ctx.block_stmt()), self.visit(ctx.else_stmt()))
            else:
                return If(self.visit(ctx.expr()), self.visit(ctx.stmt())[1][0], self.visit(ctx.else_stmt()))
        else:
            if ctx.block_stmt():
                return If(self.visit(ctx.expr()), self.visit(ctx.block_stmt()), None)
            else:
                return If(self.visit(ctx.expr()), self.visit(ctx.stmt())[1][0], None)

    def visitElse_stmt(self, ctx: BKOOLParser.Else_stmtContext):
        if ctx.block_stmt():
            return self.visit(ctx.block_stmt())
        else:
            return self.visit(ctx.stmt())[1][0]

    def visitFor_stmt(self, ctx: BKOOLParser.For_stmtContext):
        return For(self.visit(ctx.scalar_variable()),
                   self.visit(ctx.expr(0)),
                   self.visit(ctx.expr(1)),
                   bool(True) if ctx.TO() else bool(False),
                   self.visit(ctx.stmt())[1][0] if ctx.stmt() else self.visit(ctx.block_stmt()))

    def visitBreak_stmt(self, ctx: BKOOLParser.Break_stmtContext):
        # breakStmt: BREAK SEMI;
        return Break()

    def visitContinue_stmt(self, ctx: BKOOLParser.Continue_stmtContext):
        # continueStmt: CONTINUE SEMI;
        return Continue()

    def visitReturn_stmt(self, ctx: BKOOLParser.Return_stmtContext):
        # returnStmt: RETURN exp SEMI;
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        else:
            return Return(None)

    def visitMethod_invo_stmt(self, ctx: BKOOLParser.Method_invo_stmtContext):
        return self.visit(ctx.method_invo())

    # Visit a parse tree produced by BKOOLParser#method_invo.
    def visitMethod_invo(self, ctx: BKOOLParser.Method_invoContext):
        if ctx.exp9_method():
            return self.visit(ctx.exp9_method())

    # Visit a parse tree produced by BKOOLParser#exp9_method.
    def visitExp9_method(self, ctx: BKOOLParser.Exp9_methodContext):
        return CallStmt(self.visit(ctx.exp9()), Id(ctx.ID().getText()), self.visit(ctx.exp_list()))

    # Visit a parse tree produced by BKOOLParser#expr.
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


    # Visit a parse tree produced by BKOOLParser#exp8.
    def visitExp8(self, ctx: BKOOLParser.Exp8Context):
        if ctx.indexop():
            return ArrayCell(self.visit(ctx.exp8()), self.visit(ctx.indexop()))
        else:
            return self.visit(ctx.exp9())

    # Visit a parse tree produced by BKOOLParser#indexop.
    def visitIndexop(self, ctx: BKOOLParser.IndexopContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by BKOOLParser#exp9.
    def visitExp9(self, ctx: BKOOLParser.Exp9Context):
        if ctx.getChildCount() == 3:
            if ctx.tail_part().getChildCount() == 1:
                return FieldAccess(self.visit(ctx.exp9()), self.visit(ctx.tail_part()))
            else:
                temp = self.visit(ctx.tail_part())
                return CallExpr(self.visit(ctx.exp9()), temp[0], temp[1])
        else:
            return self.visit(ctx.exp13())

    # Visit a parse tree produced by BKOOLParser#tail_part.
    def visitTail_part(self, ctx: BKOOLParser.Tail_partContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        else:
            return (Id(ctx.ID().getText()), self.visit(ctx.exp_list()))

    # Visit a parse tree produced by BKOOLParser#exp13.
    def visitExp13(self, ctx: BKOOLParser.Exp13Context):
        if ctx.THIS():
            return SelfLiteral()
        else:
            return self.visit(ctx.exp10())

    # Visit a parse tree produced by BKOOLParser#exp10.
    def visitExp10(self, ctx: BKOOLParser.Exp10Context):
        if ctx.exp10_access():
            return self.visit(ctx.exp10_access())
        elif ctx.exp10_call():
            return self.visit(ctx.exp10_call())
        else:
            return self.visit(ctx.exp11())

    # Visit a parse tree produced by BKOOLParser#exp10_access.
    def visitExp10_access(self, ctx: BKOOLParser.Exp10_accessContext):
        return FieldAccess(Id(ctx.ID(0).getText()), Id(ctx.ID(1).getText()))

    # Visit a parse tree produced by BKOOLParser#exp10_call.
    def visitExp10_call(self, ctx: BKOOLParser.Exp10_callContext):
        return CallExpr(Id(ctx.ID(0).getText()), Id(ctx.ID(1).getText()), self.visit(ctx.exp_list()))

    # Visit a parse tree produced by BKOOLParser#exp11.
    def visitExp11(self, ctx: BKOOLParser.Exp11Context):
        if ctx.getChildCount() == 5:
            return NewExpr(Id(ctx.ID().getText()), self.visit(ctx.exp_list()))
        else:
            return self.visit(ctx.exp12())

    # Visit a parse tree produced by BKOOLParser#exp_list.
    def visitExp_list(self, ctx: BKOOLParser.Exp_listContext):
        if ctx.exps():
            return self.visit(ctx.exps())
        else:
            return []

    # Visit a parse tree produced by BKOOLParser#exps.
    def visitExps(self, ctx: BKOOLParser.ExpsContext):
        if ctx.exps():
            return [self.visit(ctx.expr())] + self.visit(ctx.exps())
        else:
            return [self.visit(ctx.expr())]

    # Visit a parse tree produced by BKOOLParser#exp12.
    def visitExp12(self, ctx: BKOOLParser.Exp12Context):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.expr())

    # Visit a parse tree produced by BKOOLParser#primitive_type.
    def visitPrimitive_type(self, ctx: BKOOLParser.Primitive_typeContext):
        if ctx.BOOLEAN():
            return BoolType()
        if ctx.STRING():
            return StringType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.INT():
            return IntType()
        if ctx.VOID():
            return VoidType()

    # Visit a parse tree produced by BKOOLParser#array_type.
    def visitArray_type(self, ctx: BKOOLParser.Array_typeContext):
        return ArrayType(self.visit(ctx.size()), self.visit(ctx.element_type()))

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
        if ctx.class_type():
            return self.visit(ctx.class_type())

    # Visit a parse tree produced by BKOOLParser#size.
    def visitSize(self, ctx: BKOOLParser.SizeContext):
        return int(ctx.INTLIT().getText())

    # Visit a parse tree produced by BKOOLParser#class_type.
    def visitClass_type(self, ctx: BKOOLParser.Class_typeContext):
        return ClassType(Id(ctx.ID().getText()))

    # Visit a parse tree produced by BKOOLParser#literal.
    def visitLiteral(self, ctx: BKOOLParser.LiteralContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.boolean_lit():
            value = self.visit(ctx.boolean_lit())
            return BooleanLiteral(value)
        elif ctx.indexarr_lit():
            return self.visit(ctx.indexarr_lit())
        elif ctx.NIL():
            return NullLiteral()

    def visitBoolean_lit(self, ctx: BKOOLParser.Boolean_litContext):
        if ctx.TRUE():
            return True
        else:
            return False

    def visitIndexarr_lit(self, ctx: BKOOLParser.Indexarr_litContext):
        return ArrayLiteral(self.visit(ctx.arr_exp()))
    def visitArr_exp(self, ctx: BKOOLParser.Arr_expContext):
        return [self.visit(ctx.literal())] + self.visit(ctx.arr_exp()) if ctx.arr_exp() else [self.visit(ctx.literal())]
