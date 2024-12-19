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


    # Visit a parse tree produced by BKOOLParser#type_name.
    def visitType_name(self, ctx:BKOOLParser.Type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classDecl.
    def visitClassDecl(self, ctx:BKOOLParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#className.
    def visitClassName(self, ctx:BKOOLParser.ClassNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classMem.
    def visitClassMem(self, ctx:BKOOLParser.ClassMemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attributeDecl.
    def visitAttributeDecl(self, ctx:BKOOLParser.AttributeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mutableAttribute.
    def visitMutableAttribute(self, ctx:BKOOLParser.MutableAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#muInit.
    def visitMuInit(self, ctx:BKOOLParser.MuInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#immutableAttribute.
    def visitImmutableAttribute(self, ctx:BKOOLParser.ImmutableAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#immuInit.
    def visitImmuInit(self, ctx:BKOOLParser.ImmuInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#objAttribute.
    def visitObjAttribute(self, ctx:BKOOLParser.ObjAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#objInit.
    def visitObjInit(self, ctx:BKOOLParser.ObjInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#methodDecl.
    def visitMethodDecl(self, ctx:BKOOLParser.MethodDeclContext):
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


    # Visit a parse tree produced by BKOOLParser#paramList.
    def visitParamList(self, ctx:BKOOLParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramInit.
    def visitParamInit(self, ctx:BKOOLParser.ParamInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt.
    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt_wo_return.
    def visitStmt_wo_return(self, ctx:BKOOLParser.Stmt_wo_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmtBlock.
    def visitStmtBlock(self, ctx:BKOOLParser.StmtBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmtBlock_wo_return.
    def visitStmtBlock_wo_return(self, ctx:BKOOLParser.StmtBlock_wo_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmtBlock_constructor.
    def visitStmtBlock_constructor(self, ctx:BKOOLParser.StmtBlock_constructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#asmStmt.
    def visitAsmStmt(self, ctx:BKOOLParser.AsmStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhs.
    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#ifStmt.
    def visitIfStmt(self, ctx:BKOOLParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#forStmt.
    def visitForStmt(self, ctx:BKOOLParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#breakStmt.
    def visitBreakStmt(self, ctx:BKOOLParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#continueStmt.
    def visitContinueStmt(self, ctx:BKOOLParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#returnStmt.
    def visitReturnStmt(self, ctx:BKOOLParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_invo_stmt.
    def visitMethod_invo_stmt(self, ctx:BKOOLParser.Method_invo_stmtContext):
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


    # Visit a parse tree produced by BKOOLParser#exp9.
    def visitExp9(self, ctx:BKOOLParser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#tail_part.
    def visitTail_part(self, ctx:BKOOLParser.Tail_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp10.
    def visitExp10(self, ctx:BKOOLParser.Exp10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp11.
    def visitExp11(self, ctx:BKOOLParser.Exp11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp11_access.
    def visitExp11_access(self, ctx:BKOOLParser.Exp11_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp11_call.
    def visitExp11_call(self, ctx:BKOOLParser.Exp11_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp12.
    def visitExp12(self, ctx:BKOOLParser.Exp12Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp13.
    def visitExp13(self, ctx:BKOOLParser.Exp13Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expList.
    def visitExpList(self, ctx:BKOOLParser.ExpListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#varDecl.
    def visitVarDecl(self, ctx:BKOOLParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mutableVar.
    def visitMutableVar(self, ctx:BKOOLParser.MutableVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#immutableVar.
    def visitImmutableVar(self, ctx:BKOOLParser.ImmutableVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#objVar.
    def visitObjVar(self, ctx:BKOOLParser.ObjVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#varDecl_constructor.
    def visitVarDecl_constructor(self, ctx:BKOOLParser.VarDecl_constructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mutableVar_constructor.
    def visitMutableVar_constructor(self, ctx:BKOOLParser.MutableVar_constructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#constructorInit.
    def visitConstructorInit(self, ctx:BKOOLParser.ConstructorInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#primitive_type.
    def visitPrimitive_type(self, ctx:BKOOLParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arrType.
    def visitArrType(self, ctx:BKOOLParser.ArrTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#element_type.
    def visitElement_type(self, ctx:BKOOLParser.Element_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#size.
    def visitSize(self, ctx:BKOOLParser.SizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#objType.
    def visitObjType(self, ctx:BKOOLParser.ObjTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#literal.
    def visitLiteral(self, ctx:BKOOLParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#bool_lit.
    def visitBool_lit(self, ctx:BKOOLParser.Bool_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arr_exp.
    def visitArr_exp(self, ctx:BKOOLParser.Arr_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#indexarr_lit.
    def visitIndexarr_lit(self, ctx:BKOOLParser.Indexarr_litContext):
        return self.visitChildren(ctx)



del BKOOLParser