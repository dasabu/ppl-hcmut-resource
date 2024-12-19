# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#decl.
    def visitDecl(self, ctx:BKOOLParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_decl.
    def visitClass_decl(self, ctx:BKOOLParser.Class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#superclass.
    def visitSuperclass(self, ctx:BKOOLParser.SuperclassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#memberlist.
    def visitMemberlist(self, ctx:BKOOLParser.MemberlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#members.
    def visitMembers(self, ctx:BKOOLParser.MembersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#member.
    def visitMember(self, ctx:BKOOLParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#variable_decl.
    def visitVariable_decl(self, ctx:BKOOLParser.Variable_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attribute_list.
    def visitAttribute_list(self, ctx:BKOOLParser.Attribute_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attribute.
    def visitAttribute(self, ctx:BKOOLParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#type_name.
    def visitType_name(self, ctx:BKOOLParser.Type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_prefix.
    def visitVar_prefix(self, ctx:BKOOLParser.Var_prefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_decl.
    def visitMethod_decl(self, ctx:BKOOLParser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#normal_method.
    def visitNormal_method(self, ctx:BKOOLParser.Normal_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramlist.
    def visitParamlist(self, ctx:BKOOLParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#params.
    def visitParams(self, ctx:BKOOLParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param.
    def visitParam(self, ctx:BKOOLParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#idlist.
    def visitIdlist(self, ctx:BKOOLParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_prefix.
    def visitMethod_prefix(self, ctx:BKOOLParser.Method_prefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#construct_method.
    def visitConstruct_method(self, ctx:BKOOLParser.Construct_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#main_method.
    def visitMain_method(self, ctx:BKOOLParser.Main_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_type_name.
    def visitMethod_type_name(self, ctx:BKOOLParser.Method_type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#block_stmt.
    def visitBlock_stmt(self, ctx:BKOOLParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#block_body.
    def visitBlock_body(self, ctx:BKOOLParser.Block_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_decl_part.
    def visitVar_decl_part(self, ctx:BKOOLParser.Var_decl_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt_part.
    def visitStmt_part(self, ctx:BKOOLParser.Stmt_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_decl_list.
    def visitVar_decl_list(self, ctx:BKOOLParser.Var_decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt_list.
    def visitStmt_list(self, ctx:BKOOLParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt.
    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assignment_stmt.
    def visitAssignment_stmt(self, ctx:BKOOLParser.Assignment_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#left_exp.
    def visitLeft_exp(self, ctx:BKOOLParser.Left_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#scalar_variable.
    def visitScalar_variable(self, ctx:BKOOLParser.Scalar_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#if_stmt.
    def visitIf_stmt(self, ctx:BKOOLParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#if_part.
    def visitIf_part(self, ctx:BKOOLParser.If_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#else_part.
    def visitElse_part(self, ctx:BKOOLParser.Else_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#else_block.
    def visitElse_block(self, ctx:BKOOLParser.Else_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#for_stmt.
    def visitFor_stmt(self, ctx:BKOOLParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#break_stmt.
    def visitBreak_stmt(self, ctx:BKOOLParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#continue_stmt.
    def visitContinue_stmt(self, ctx:BKOOLParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_stmt.
    def visitReturn_stmt(self, ctx:BKOOLParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_invo_stmt.
    def visitMethod_invo_stmt(self, ctx:BKOOLParser.Method_invo_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_invo.
    def visitMethod_invo(self, ctx:BKOOLParser.Method_invoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#relational.
    def visitRelational(self, ctx:BKOOLParser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp2.
    def visitExp2(self, ctx:BKOOLParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp3.
    def visitExp3(self, ctx:BKOOLParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp4.
    def visitExp4(self, ctx:BKOOLParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp5.
    def visitExp5(self, ctx:BKOOLParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp6.
    def visitExp6(self, ctx:BKOOLParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp7.
    def visitExp7(self, ctx:BKOOLParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp8.
    def visitExp8(self, ctx:BKOOLParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp9.
    def visitExp9(self, ctx:BKOOLParser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp10.
    def visitExp10(self, ctx:BKOOLParser.Exp10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#tail_part.
    def visitTail_part(self, ctx:BKOOLParser.Tail_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp13.
    def visitExp13(self, ctx:BKOOLParser.Exp13Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp11.
    def visitExp11(self, ctx:BKOOLParser.Exp11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp_list.
    def visitExp_list(self, ctx:BKOOLParser.Exp_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exps.
    def visitExps(self, ctx:BKOOLParser.ExpsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp12.
    def visitExp12(self, ctx:BKOOLParser.Exp12Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#primitive_type.
    def visitPrimitive_type(self, ctx:BKOOLParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_type.
    def visitArray_type(self, ctx:BKOOLParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#element_type.
    def visitElement_type(self, ctx:BKOOLParser.Element_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#size.
    def visitSize(self, ctx:BKOOLParser.SizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_type.
    def visitClass_type(self, ctx:BKOOLParser.Class_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#literal.
    def visitLiteral(self, ctx:BKOOLParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#indexarr_lit.
    def visitIndexarr_lit(self, ctx:BKOOLParser.Indexarr_litContext):
        return self.visitChildren(ctx)



del BKOOLParser