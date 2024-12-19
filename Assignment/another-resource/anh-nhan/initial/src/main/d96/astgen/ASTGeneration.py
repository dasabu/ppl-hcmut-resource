# ID: 1912190
# Nguyễn Mai Thy

from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *


class ASTGeneration(D96Visitor):
        # Visit a parse tree produced by D96Parser#program.  # dùng hàm program()
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return Program(self.visit(ctx.decl()))


    # Visit a parse tree produced by D96Parser#decl.         # trả về list[ClassDecl]
    def visitDecl(self, ctx:D96Parser.DeclContext):
        if ctx.decl():
            return [self.visit(ctx.class_decl())] + self.visit(ctx.decl())
        else:
            return [self.visit(ctx.class_decl())]


    # Visit a parse tree produced by D96Parser#class_decl.   # trả về ClassDecl()
    def visitClass_decl(self, ctx:D96Parser.Class_declContext):
        classname = ctx.ID().getText()
        memberlist = self.visit(ctx.memberlist())
        superclass = self.visit(ctx.superclass())            

        if classname == "Program":
            for element in memberlist:
                if type(element) == MethodDecl:
                    if element.name.name == "main" and element.param == []:
                        element.kind = Static()

        return ClassDecl(Id(classname), memberlist, superclass)


    # Visit a parse tree produced by D96Parser#superclass.   # Thuộc tính thứ 3 Id của ClassDecl, Id hoặc None
    def visitSuperclass(self, ctx:D96Parser.SuperclassContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return None

    # Visit a parse tree produced by D96Parser#memberlist.   # list[MemDecl] có thể rỗng
    def visitMemberlist(self, ctx:D96Parser.MemberlistContext):
        if ctx.members():
            return self.visit(ctx.members())
        else:
            return []

    # Visit a parse tree produced by D96Parser#members.      # trả về list[MemDecl]
    def visitMembers(self, ctx:D96Parser.MembersContext):
        if ctx.members():
            return self.visit(ctx.member()) + self.visit(ctx.members())
        else:
            return self.visit(ctx.member())


    # Visit a parse tree produced by D96Parser#member.
    def visitMember(self, ctx:D96Parser.MemberContext):
        if ctx.variable_decl():
            return self.visit(ctx.variable_decl()) # trả về kiểu AttributeDecl (đã là list sẵn nên không cần list)
        else:
            return [self.visit(ctx.method_decl())]   # trả về MethodDecl


    # Visit a parse tree produced by D96Parser#variable_decl.  # Var a, b : int = 1, 2; => AttributeDecl(static/instance, const/var)
    def visitVariable_decl(self, ctx:D96Parser.Variable_declContext):
        if ctx.with_init():
            return self.visit(ctx.with_init())   # có phần gán giá trị
        else:
            return self.visit(ctx.without_init()) # không có phần gán giá trị


    # Visit a parse tree produced by D96Parser#without_init.
    def visitWithout_init(self, ctx:D96Parser.Without_initContext):
        attribute_list = self.visit(ctx.attribute_list())
        type_name = self.visit(ctx.type_name())

        lst = []
        if ctx.VAR():
            for i in range(len(attribute_list)):
                lst += [AttributeDecl(attribute_list[i][1], VarDecl(attribute_list[i][0], type_name, NullLiteral() if type(type_name) == ClassType else None))]
        elif ctx.VAL():
            for j in range(len(attribute_list)):
                lst += [AttributeDecl(attribute_list[j][1],ConstDecl(attribute_list[j][0], type_name, None))]            
        return lst


    # Visit a parse tree produced by D96Parser#attribute_list.
    def visitAttribute_list(self, ctx:D96Parser.Attribute_listContext):
        if ctx.attribute_list():
            return [self.visit(ctx.attribute())] + self.visit(ctx.attribute_list())
        else:
            return [self.visit(ctx.attribute())]


    # Visit a parse tree produced by D96Parser#attribute.
    def visitAttribute(self, ctx:D96Parser.AttributeContext):
        if ctx.DOLLAR_ID():
            return (Id(ctx.getChild(0).getText()), Static())
        else:
            return (Id(ctx.getChild(0).getText()), Instance())


    # Visit a parse tree produced by D96Parser#type_name.       #trả về type của attribute
    def visitType_name(self, ctx:D96Parser.Type_nameContext):
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

    # Visit a parse tree produced by D96Parser#with_init.
    def visitWith_init(self, ctx:D96Parser.With_initContext):
        ret = self.visit(ctx.pair_list())
        if ctx.VAR():
            return ret[0]
        elif ctx.VAL():
            return ret[1]

    # Visit a parse tree produced by D96Parser#pair_list.
    def visitPair_list(self, ctx:D96Parser.Pair_listContext):
        temp = [self.visit(ctx.attribute())] + self.visit(ctx.pair()) + [self.visit(ctx.expr())]

        type_name = temp[int(len(temp)/2)]
        id_lst = temp[:(int(len(temp)/2))]
        exp_lst = temp[(int(len(temp)/2)+1):]
        lst_var = []
        lst_val = []
        for i in range(len(id_lst)):
            lst_var += [AttributeDecl(id_lst[i][1], VarDecl(id_lst[i][0], type_name, exp_lst[i]))]
            lst_val += [AttributeDecl(id_lst[i][1], ConstDecl(id_lst[i][0], type_name, exp_lst[i]))]
        return (lst_var, lst_val)

    # Visit a parse tree produced by D96Parser#pair.
    def visitPair(self, ctx:D96Parser.PairContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.type_name())]
        else:
            return [self.visit(ctx.attribute())] + self.visit(ctx.pair()) + [self.visit(ctx.expr())]


    # Visit a parse tree produced by D96Parser#method_decl.
    def visitMethod_decl(self, ctx:D96Parser.Method_declContext):
        if ctx.normal_method():
            return self.visit(ctx.normal_method())
        elif ctx.destruct_method():
            return self.visit(ctx.destruct_method())
        elif ctx.construct_method():
            return self.visit(ctx.construct_method())


    # Visit a parse tree produced by D96Parser#normal_method.
    def visitNormal_method(self, ctx:D96Parser.Normal_methodContext):
        temp = self.visit(ctx.method_name())
        return MethodDecl(temp[0], temp[1], self.visit(ctx.paramlist()), self.visit(ctx.block_stmt()))


    # Visit a parse tree produced by D96Parser#method_name.
    def visitMethod_name(self, ctx:D96Parser.Method_nameContext):
        if ctx.ID():
            return (Instance(), Id(ctx.ID().getText()))
        elif ctx.DOLLAR_ID():
            return (Static(), Id(ctx.DOLLAR_ID().getText()))


    # Visit a parse tree produced by D96Parser#paramlist.    # một list các parameter có thể rỗng
    def visitParamlist(self, ctx:D96Parser.ParamlistContext):
        if ctx.params():
            return self.visit(ctx.params())
        else:
            return []


    # Visit a parse tree produced by D96Parser#params.
    def visitParams(self, ctx:D96Parser.ParamsContext):
        if ctx.params():
            return self.visit(ctx.param()) + self.visit(ctx.params())
        else:
            return self.visit(ctx.param())


    # Visit a parse tree produced by D96Parser#param.
    def visitParam(self, ctx:D96Parser.ParamContext):
        type_name = self.visit(ctx.type_name())
        id_lst = self.visit(ctx.idlist())
        
        lst = []
        for i in range(len(id_lst)):
            lst += [VarDecl(id_lst[i], type_name, None)]

        return lst

    # Visit a parse tree produced by D96Parser#idlist.
    def visitIdlist(self, ctx:D96Parser.IdlistContext):
        if ctx.idlist():
            return [Id(ctx.ID().getText())] + self.visit(ctx.idlist())
        else:
            return [Id(ctx.ID().getText())]


    # Visit a parse tree produced by D96Parser#construct_method.
    def visitConstruct_method(self, ctx:D96Parser.Construct_methodContext):
        return MethodDecl(Instance(), Id("Constructor"), self.visit(ctx.paramlist()), self.visit(ctx.block_stmt()))


    # Visit a parse tree produced by D96Parser#destruct_method.
    def visitDestruct_method(self, ctx:D96Parser.Destruct_methodContext):
        return MethodDecl(Instance(), Id("Destructor"), [], self.visit(ctx.block_stmt()))


    # Visit a parse tree produced by D96Parser#block_stmt.
    def visitBlock_stmt(self, ctx:D96Parser.Block_stmtContext):
        return Block(self.visit(ctx.block_body()))


    # Visit a parse tree produced by D96Parser#block_body.       #list các stmt có thể rỗng
    def visitBlock_body(self, ctx:D96Parser.Block_bodyContext):
        if ctx.blocks():
            return self.visit(ctx.blocks())
        else:
            return []


    # Visit a parse tree produced by D96Parser#blocks.
    def visitBlocks(self, ctx:D96Parser.BlocksContext):
        if ctx.blocks():
            return self.visit(ctx.stmt()) + self.visit(ctx.blocks())
        else:
            return self.visit(ctx.stmt())


    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx:D96Parser.StmtContext):
        if ctx.vardecl_stmt():
            return self.visit(ctx.vardecl_stmt())
        elif ctx.assignment_stmt():
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


    # Visit a parse tree produced by D96Parser#vardecl_stmt.
    def visitVardecl_stmt(self, ctx:D96Parser.Vardecl_stmtContext):
        if ctx.with_init2():
            return self.visit(ctx.with_init2())
        else:
            return self.visit(ctx.without_init2())


    # Visit a parse tree produced by D96Parser#without_init2.
    def visitWithout_init2(self, ctx:D96Parser.Without_init2Context):
        attribute_list = self.visit(ctx.attribute_list2())
        type_name = self.visit(ctx.type_name())
        lst = []
        if ctx.VAR():
            for i in range(len(attribute_list)):
                lst += [VarDecl(attribute_list[i], type_name, NullLiteral() if type(type_name) == ClassType else None)]
        elif ctx.VAL():
            for j in range(len(attribute_list)):
                lst += [ConstDecl(attribute_list[j], type_name, None)]
        
        return lst


    # Visit a parse tree produced by D96Parser#attribute_list2.
    def visitAttribute_list2(self, ctx:D96Parser.Attribute_list2Context):
        if ctx.attribute_list2():
            return [Id(ctx.ID().getText())] + self.visit(ctx.attribute_list2())
        else:
            return [Id(ctx.ID().getText())]

    # Visit a parse tree produced by D96Parser#with_init2.
    def visitWith_init2(self, ctx:D96Parser.With_init2Context):
        ret = self.visit(ctx.pair_list2())
        if ctx.VAR():
            return ret[0]
        elif ctx.VAL():
            return ret[1]

    # Visit a parse tree produced by D96Parser#pair_list2.
    def visitPair_list2(self, ctx:D96Parser.Pair_list2Context):
        temp = [Id(ctx.ID().getText())] + self.visit(ctx.pair2()) + [self.visit(ctx.expr())]
        
        type_name = temp[int(len(temp)/2)]
        id_lst = temp[:(int(len(temp)/2))]
        exp_lst = temp[(int(len(temp)/2)+1):]
        lst_var = []
        lst_val = []

        for i in range(len(id_lst)):
            lst_var += [VarDecl(id_lst[i], type_name, exp_lst[i])]
            lst_val += [ConstDecl(id_lst[i], type_name, exp_lst[i])]

        return (lst_var, lst_val)

    # Visit a parse tree produced by D96Parser#pair2.
    def visitPair2(self, ctx:D96Parser.Pair2Context):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.type_name())]
        else:
            return [Id(ctx.ID().getText())] + self.visit(ctx.pair2()) + [self.visit(ctx.expr())]


    # Visit a parse tree produced by D96Parser#assignment_stmt.
    def visitAssignment_stmt(self, ctx:D96Parser.Assignment_stmtContext):
        left = self.visit(ctx.left_exp())
        right = self.visit(ctx.expr())
        return Assign(left, right)


    # Visit a parse tree produced by D96Parser#left_exp.
    def visitLeft_exp(self, ctx:D96Parser.Left_expContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.scalar_variable())
        else:
            return ArrayCell(self.visit(ctx.exp9()),self.visit(ctx.indexop()))


    # Visit a parse tree produced by D96Parser#scalar_variable.
    def visitScalar_variable(self, ctx:D96Parser.Scalar_variableContext):
        if ctx.getChildCount() == 1:
            if ctx.ID():
                return Id(ctx.ID().getText())
            elif ctx.DOLLAR_ID():
                return Id(ctx.DOLLAR_ID().getText())
            elif ctx.exp10_access():
                return self.visit(ctx.exp10_access())
        else: 
            return FieldAccess(self.visit(ctx.exp9()), Id(ctx.ID().getText()))


    # Visit a parse tree produced by D96Parser#if_stmt.
    def visitIf_stmt(self, ctx:D96Parser.If_stmtContext):
        if_part = self.visit(ctx.if_part())
        return If(if_part[0], if_part[1], self.visit(ctx.elseif_list()))


    # Visit a parse tree produced by D96Parser#if_part.
    def visitIf_part(self, ctx:D96Parser.If_partContext):
        return (self.visit(ctx.expr()), self.visit(ctx.block_stmt()))


    # Visit a parse tree produced by D96Parser#elseif_list.
    def visitElseif_list(self, ctx:D96Parser.Elseif_listContext):
        if ctx.getChildCount() == 2:
            elif_stmt = self.visit(ctx.elif_stmt())
            return If(elif_stmt[0], elif_stmt[1], self.visit(ctx.elseif_list()))
        else: 
            return self.visit(ctx.else_part())


    # Visit a parse tree produced by D96Parser#elif_stmt.
    def visitElif_stmt(self, ctx:D96Parser.Elif_stmtContext):
        return (self.visit(ctx.expr()), self.visit(ctx.block_stmt()))


    # Visit a parse tree produced by D96Parser#else_part.
    def visitElse_part(self, ctx:D96Parser.Else_partContext):
        if ctx.block_stmt():
            return self.visit(ctx.block_stmt())
        else:
            return None


    # Visit a parse tree produced by D96Parser#for_stmt.
    def visitFor_stmt(self, ctx:D96Parser.For_stmtContext):
        if ctx.BY():
            return For(Id(ctx.ID().getText()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), self.visit(ctx.block_stmt()), self.visit(ctx.expr(2)))
        else:
            return For(Id(ctx.ID().getText()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), self.visit(ctx.block_stmt()), IntLiteral(1))


    # Visit a parse tree produced by D96Parser#break_stmt.
    def visitBreak_stmt(self, ctx:D96Parser.Break_stmtContext):
        return Break()


    # Visit a parse tree produced by D96Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:D96Parser.Continue_stmtContext):
        return Continue()


    # Visit a parse tree produced by D96Parser#return_stmt.
    def visitReturn_stmt(self, ctx:D96Parser.Return_stmtContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        else:
            return Return(None)


    # Visit a parse tree produced by D96Parser#method_invo_stmt.
    def visitMethod_invo_stmt(self, ctx:D96Parser.Method_invo_stmtContext):
        return self.visit(ctx.method_invo())


    # Visit a parse tree produced by D96Parser#method_invo.
    def visitMethod_invo(self, ctx:D96Parser.Method_invoContext):
        if ctx.exp9_method():
            return self.visit(ctx.exp9_method())
        else:
            return self.visit(ctx.exp10_method())


    # Visit a parse tree produced by D96Parser#exp9_method.
    def visitExp9_method(self, ctx:D96Parser.Exp9_methodContext):
        return CallStmt(self.visit(ctx.exp9()), Id(ctx.ID().getText()), self.visit(ctx.exp_list()))


    # Visit a parse tree produced by D96Parser#exp10_method.
    def visitExp10_method(self, ctx:D96Parser.Exp10_methodContext):
        return CallStmt(Id(ctx.ID().getText()), Id(ctx.DOLLAR_ID().getText()), self.visit(ctx.exp_list()))


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp2(0)),self.visit(ctx.exp2(1)))
        else:
            return self.visit(ctx.exp2(0))


    # Visit a parse tree produced by D96Parser#exp2.
    def visitExp2(self, ctx:D96Parser.Exp2Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(self.visit(ctx.relational()), self.visit(ctx.exp3(0)),self.visit(ctx.exp3(1)))
        else:
            return self.visit(ctx.exp3(0))


    # Visit a parse tree produced by D96Parser#relational.
    def visitRelational(self, ctx:D96Parser.RelationalContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by D96Parser#exp3.
    def visitExp3(self, ctx:D96Parser.Exp3Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp3()),self.visit(ctx.exp4()))
        else:
            return self.visit(ctx.exp4())


    # Visit a parse tree produced by D96Parser#exp4.
    def visitExp4(self, ctx:D96Parser.Exp4Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp4()),self.visit(ctx.exp5()))
        else:
            return self.visit(ctx.exp5())


    # Visit a parse tree produced by D96Parser#exp5.
    def visitExp5(self, ctx:D96Parser.Exp5Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp5()),self.visit(ctx.exp6()))
        else:
            return self.visit(ctx.exp6())


    # Visit a parse tree produced by D96Parser#exp6.
    def visitExp6(self, ctx:D96Parser.Exp6Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.exp6()))
        else:
            return self.visit(ctx.exp7())


    # Visit a parse tree produced by D96Parser#exp7.
    def visitExp7(self, ctx:D96Parser.Exp7Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.exp7()))
        else:
            return self.visit(ctx.exp8())


    # Visit a parse tree produced by D96Parser#exp8.
    def visitExp8(self, ctx:D96Parser.Exp8Context):
        if ctx.indexop(): 
            return ArrayCell(self.visit(ctx.exp9()),self.visit(ctx.indexop()))
        else:
            return self.visit(ctx.exp9())

    # Visit a parse tree produced by D96Parser#indexop.
    def visitIndexop(self, ctx:D96Parser.IndexopContext):
        if ctx.indexop():
            return [self.visit(ctx.expr())] + self.visit(ctx.indexop())
        elif ctx.expr():
            return [self.visit(ctx.expr())]


    # Visit a parse tree produced by D96Parser#exp9.
    def visitExp9(self, ctx:D96Parser.Exp9Context):
        if ctx.getChildCount() == 3:
            if ctx.tail_part().getChildCount() == 1:
                return FieldAccess(self.visit(ctx.exp9()), self.visit(ctx.tail_part()))
            else:
                temp = self.visit(ctx.tail_part())
                return CallExpr(self.visit(ctx.exp9()), temp[0], temp[1])
        else:
            return self.visit(ctx.exp13())

    # Visit a parse tree produced by D96Parser#tail_part.
    def visitTail_part(self, ctx:D96Parser.Tail_partContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        else:
            return (Id(ctx.ID().getText()), self.visit(ctx.exp_list()))
      

    # Visit a parse tree produced by D96Parser#exp13.
    def visitExp13(self, ctx:D96Parser.Exp13Context):
        if ctx.SELF():
            return SelfLiteral()
        else:
            return self.visit(ctx.exp10())


    # Visit a parse tree produced by D96Parser#exp10.
    def visitExp10(self, ctx:D96Parser.Exp10Context):
        if ctx.exp10_access():
            return self.visit(ctx.exp10_access())
        elif ctx.exp10_call():
            return self.visit(ctx.exp10_call())
        else:
            return self.visit(ctx.exp11())


    # Visit a parse tree produced by D96Parser#exp10_access.
    def visitExp10_access(self, ctx:D96Parser.Exp10_accessContext):
        return FieldAccess(Id(ctx.ID().getText()), Id(ctx.DOLLAR_ID().getText()))


    # Visit a parse tree produced by D96Parser#exp10_call.
    def visitExp10_call(self, ctx:D96Parser.Exp10_callContext):
        return CallExpr(Id(ctx.ID().getText()), Id(ctx.DOLLAR_ID().getText()), self.visit(ctx.exp_list()))


    # Visit a parse tree produced by D96Parser#exp11.
    def visitExp11(self, ctx:D96Parser.Exp11Context):
        if ctx.getChildCount() == 5:
            return NewExpr(Id(ctx.ID().getText()), self.visit(ctx.exp_list()))
        else:
            return self.visit(ctx.exp12())


    # Visit a parse tree produced by D96Parser#exp_list.
    def visitExp_list(self, ctx:D96Parser.Exp_listContext):
        if ctx.exps():
            return self.visit(ctx.exps())
        else:
            return []


    # Visit a parse tree produced by D96Parser#exps.
    def visitExps(self, ctx:D96Parser.ExpsContext):
        if ctx.exps():
            return [self.visit(ctx.expr())] + self.visit(ctx.exps())
        else:
            return [self.visit(ctx.expr())]


    # Visit a parse tree produced by D96Parser#exp12.
    def visitExp12(self, ctx:D96Parser.Exp12Context):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.expr())


    # Visit a parse tree produced by D96Parser#primitive_type.
    def visitPrimitive_type(self, ctx:D96Parser.Primitive_typeContext):
        if ctx.BOOLEAN():
            return BoolType()
        if ctx.STRING():
            return StringType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.INT():
            return IntType()


    # Visit a parse tree produced by D96Parser#array_type.
    def visitArray_type(self, ctx:D96Parser.Array_typeContext):
        return ArrayType(self.visit(ctx.size()), self.visit(ctx.element_type()))


    # Visit a parse tree produced by D96Parser#element_type.
    def visitElement_type(self, ctx:D96Parser.Element_typeContext):
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        else:
            return self.visit(ctx.array_type())


    # Visit a parse tree produced by D96Parser#size.
    def visitSize(self, ctx:D96Parser.SizeContext):
        return dealwith_intlit(ctx.INTLIT().getText())
    

    # Visit a parse tree produced by D96Parser#class_type.
    def visitClass_type(self, ctx:D96Parser.Class_typeContext):
        return ClassType(Id(ctx.ID().getText()))


    # Visit a parse tree produced by D96Parser#literal.
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        if ctx.INTLIT():
            return IntLiteral(dealwith_intlit(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.boolean_lit():
            value = self.visit(ctx.boolean_lit())
            return BooleanLiteral(value)
        elif ctx.ZEROLIT():
            return IntLiteral(dealwith_intlit(ctx.ZEROLIT().getText()))
        elif ctx.indexarr_lit():
            return self.visit(ctx.indexarr_lit())
        elif ctx.NULL():
            return NullLiteral()
    
    # Visit a parse tree produced by D96Parser#boolean_lit.
    def visitBoolean_lit(self, ctx:D96Parser.Boolean_litContext):
        if ctx.TRUE():
            return True
        else:
            return False


    # Visit a parse tree produced by D96Parser#indexarr_lit.
    def visitIndexarr_lit(self, ctx:D96Parser.Indexarr_litContext):
        return ArrayLiteral(self.visit(ctx.exp_list()))

##------------------------------------------------------
def dealwith_intlit(intlit):
    temp1 = intlit[:2]
    temp2 = intlit[0]

    if (temp1 == "0x" or temp1 == "0X"):
        return int(intlit, 16)
    elif (temp1 == "0b" or temp1 == "0B"):
        return int(intlit, 2)
    elif temp2 =="0":
        return int(intlit, 8)
    else:
        return int(intlit)