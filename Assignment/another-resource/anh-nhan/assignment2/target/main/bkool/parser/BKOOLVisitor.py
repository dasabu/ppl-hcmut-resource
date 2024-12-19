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


    # Visit a parse tree produced by BKOOLParser#method_decl.
    def visitMethod_decl(self, ctx:BKOOLParser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#normalMethod.
    def visitNormalMethod(self, ctx:BKOOLParser.NormalMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mainMethod.
    def visitMainMethod(self, ctx:BKOOLParser.MainMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#voidMethod.
    def visitVoidMethod(self, ctx:BKOOLParser.VoidMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#constructor.
    def visitConstructor(self, ctx:BKOOLParser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#type_name.
    def visitType_name(self, ctx:BKOOLParser.Type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramlist.
    def visitParamlist(self, ctx:BKOOLParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param.
    def visitParam(self, ctx:BKOOLParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#idlist.
    def visitIdlist(self, ctx:BKOOLParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#block_stmt.
    def visitBlock_stmt(self, ctx:BKOOLParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#block_body.
    def visitBlock_body(self, ctx:BKOOLParser.Block_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#blocks.
    def visitBlocks(self, ctx:BKOOLParser.BlocksContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt.
    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_decl.
    def visitVar_decl(self, ctx:BKOOLParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#other_stmt.
    def visitOther_stmt(self, ctx:BKOOLParser.Other_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assignment_stmt.
    def visitAssignment_stmt(self, ctx:BKOOLParser.Assignment_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhs.
    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#scalar_variable.
    def visitScalar_variable(self, ctx:BKOOLParser.Scalar_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#if_stmt.
    def visitIf_stmt(self, ctx:BKOOLParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#else_stmt.
    def visitElse_stmt(self, ctx:BKOOLParser.Else_stmtContext):
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


    # Visit a parse tree produced by BKOOLParser#exp9_method.
    def visitExp9_method(self, ctx:BKOOLParser.Exp9_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp2.
    def visitExp2(self, ctx:BKOOLParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#relational.
    def visitRelational(self, ctx:BKOOLParser.RelationalContext):
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


    # Visit a parse tree produced by BKOOLParser#indexop.
    def visitIndexop(self, ctx:BKOOLParser.IndexopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp9.
    def visitExp9(self, ctx:BKOOLParser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#tail_part.
    def visitTail_part(self, ctx:BKOOLParser.Tail_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp13.
    def visitExp13(self, ctx:BKOOLParser.Exp13Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp10.
    def visitExp10(self, ctx:BKOOLParser.Exp10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp10_access.
    def visitExp10_access(self, ctx:BKOOLParser.Exp10_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp10_call.
    def visitExp10_call(self, ctx:BKOOLParser.Exp10_callContext):
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


    # Visit a parse tree produced by BKOOLParser#boolean_lit.
    def visitBoolean_lit(self, ctx:BKOOLParser.Boolean_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arr_exp.
    def visitArr_exp(self, ctx:BKOOLParser.Arr_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#indexarr_lit.
    def visitIndexarr_lit(self, ctx:BKOOLParser.Indexarr_litContext):
        return self.visitChildren(ctx)



del BKOOLParser