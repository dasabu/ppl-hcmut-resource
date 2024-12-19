# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#decl.
    def visitDecl(self, ctx:D96Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_decl.
    def visitClass_decl(self, ctx:D96Parser.Class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#superclass.
    def visitSuperclass(self, ctx:D96Parser.SuperclassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#memberlist.
    def visitMemberlist(self, ctx:D96Parser.MemberlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#members.
    def visitMembers(self, ctx:D96Parser.MembersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member.
    def visitMember(self, ctx:D96Parser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#variable_decl.
    def visitVariable_decl(self, ctx:D96Parser.Variable_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#without_init.
    def visitWithout_init(self, ctx:D96Parser.Without_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_list.
    def visitAttribute_list(self, ctx:D96Parser.Attribute_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute.
    def visitAttribute(self, ctx:D96Parser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#type_name.
    def visitType_name(self, ctx:D96Parser.Type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#with_init.
    def visitWith_init(self, ctx:D96Parser.With_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#pair_list.
    def visitPair_list(self, ctx:D96Parser.Pair_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#pair.
    def visitPair(self, ctx:D96Parser.PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_decl.
    def visitMethod_decl(self, ctx:D96Parser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#normal_method.
    def visitNormal_method(self, ctx:D96Parser.Normal_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_name.
    def visitMethod_name(self, ctx:D96Parser.Method_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#paramlist.
    def visitParamlist(self, ctx:D96Parser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#params.
    def visitParams(self, ctx:D96Parser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#param.
    def visitParam(self, ctx:D96Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idlist.
    def visitIdlist(self, ctx:D96Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#construct_method.
    def visitConstruct_method(self, ctx:D96Parser.Construct_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destruct_method.
    def visitDestruct_method(self, ctx:D96Parser.Destruct_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_stmt.
    def visitBlock_stmt(self, ctx:D96Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_body.
    def visitBlock_body(self, ctx:D96Parser.Block_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#blocks.
    def visitBlocks(self, ctx:D96Parser.BlocksContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx:D96Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#vardecl_stmt.
    def visitVardecl_stmt(self, ctx:D96Parser.Vardecl_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#without_init2.
    def visitWithout_init2(self, ctx:D96Parser.Without_init2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_list2.
    def visitAttribute_list2(self, ctx:D96Parser.Attribute_list2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#with_init2.
    def visitWith_init2(self, ctx:D96Parser.With_init2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#pair_list2.
    def visitPair_list2(self, ctx:D96Parser.Pair_list2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#pair2.
    def visitPair2(self, ctx:D96Parser.Pair2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assignment_stmt.
    def visitAssignment_stmt(self, ctx:D96Parser.Assignment_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#left_exp.
    def visitLeft_exp(self, ctx:D96Parser.Left_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#scalar_variable.
    def visitScalar_variable(self, ctx:D96Parser.Scalar_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_stmt.
    def visitIf_stmt(self, ctx:D96Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_part.
    def visitIf_part(self, ctx:D96Parser.If_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elseif_list.
    def visitElseif_list(self, ctx:D96Parser.Elseif_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elif_stmt.
    def visitElif_stmt(self, ctx:D96Parser.Elif_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#else_part.
    def visitElse_part(self, ctx:D96Parser.Else_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#for_stmt.
    def visitFor_stmt(self, ctx:D96Parser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_stmt.
    def visitBreak_stmt(self, ctx:D96Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:D96Parser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_stmt.
    def visitReturn_stmt(self, ctx:D96Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_invo_stmt.
    def visitMethod_invo_stmt(self, ctx:D96Parser.Method_invo_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_invo.
    def visitMethod_invo(self, ctx:D96Parser.Method_invoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp9_method.
    def visitExp9_method(self, ctx:D96Parser.Exp9_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp10_method.
    def visitExp10_method(self, ctx:D96Parser.Exp10_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp2.
    def visitExp2(self, ctx:D96Parser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#relational.
    def visitRelational(self, ctx:D96Parser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp3.
    def visitExp3(self, ctx:D96Parser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp4.
    def visitExp4(self, ctx:D96Parser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp5.
    def visitExp5(self, ctx:D96Parser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp6.
    def visitExp6(self, ctx:D96Parser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp7.
    def visitExp7(self, ctx:D96Parser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp8.
    def visitExp8(self, ctx:D96Parser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#indexop.
    def visitIndexop(self, ctx:D96Parser.IndexopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp9.
    def visitExp9(self, ctx:D96Parser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#tail_part.
    def visitTail_part(self, ctx:D96Parser.Tail_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp13.
    def visitExp13(self, ctx:D96Parser.Exp13Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp10.
    def visitExp10(self, ctx:D96Parser.Exp10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp10_access.
    def visitExp10_access(self, ctx:D96Parser.Exp10_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp10_call.
    def visitExp10_call(self, ctx:D96Parser.Exp10_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp11.
    def visitExp11(self, ctx:D96Parser.Exp11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_list.
    def visitExp_list(self, ctx:D96Parser.Exp_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exps.
    def visitExps(self, ctx:D96Parser.ExpsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp12.
    def visitExp12(self, ctx:D96Parser.Exp12Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#primitive_type.
    def visitPrimitive_type(self, ctx:D96Parser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_type.
    def visitArray_type(self, ctx:D96Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#element_type.
    def visitElement_type(self, ctx:D96Parser.Element_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#size.
    def visitSize(self, ctx:D96Parser.SizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_type.
    def visitClass_type(self, ctx:D96Parser.Class_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal.
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#boolean_lit.
    def visitBoolean_lit(self, ctx:D96Parser.Boolean_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#indexarr_lit.
    def visitIndexarr_lit(self, ctx:D96Parser.Indexarr_litContext):
        return self.visitChildren(ctx)



del D96Parser