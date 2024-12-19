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


    # Visit a parse tree produced by BKOOLParser#classDeclList.
    def visitClassDeclList(self, ctx:BKOOLParser.ClassDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classDecl.
    def visitClassDecl(self, ctx:BKOOLParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classBody.
    def visitClassBody(self, ctx:BKOOLParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classBodyDeclList.
    def visitClassBodyDeclList(self, ctx:BKOOLParser.ClassBodyDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classBodyDecl.
    def visitClassBodyDecl(self, ctx:BKOOLParser.ClassBodyDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#methodDecl.
    def visitMethodDecl(self, ctx:BKOOLParser.MethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramList.
    def visitParamList(self, ctx:BKOOLParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param.
    def visitParam(self, ctx:BKOOLParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#ids.
    def visitIds(self, ctx:BKOOLParser.IdsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#blockStmt.
    def visitBlockStmt(self, ctx:BKOOLParser.BlockStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#varDecl.
    def visitVarDecl(self, ctx:BKOOLParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attributeDecl.
    def visitAttributeDecl(self, ctx:BKOOLParser.AttributeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#variableDeclList.
    def visitVariableDeclList(self, ctx:BKOOLParser.VariableDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#variableDeclarator.
    def visitVariableDeclarator(self, ctx:BKOOLParser.VariableDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#statement.
    def visitStatement(self, ctx:BKOOLParser.StatementContext):
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


    # Visit a parse tree produced by BKOOLParser#methodInvoStmt.
    def visitMethodInvoStmt(self, ctx:BKOOLParser.MethodInvoStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assignStmt.
    def visitAssignStmt(self, ctx:BKOOLParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#ifStmt.
    def visitIfStmt(self, ctx:BKOOLParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#forStmt.
    def visitForStmt(self, ctx:BKOOLParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhsAssign.
    def visitLhsAssign(self, ctx:BKOOLParser.LhsAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expression.
    def visitExpression(self, ctx:BKOOLParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expression1.
    def visitExpression1(self, ctx:BKOOLParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expression2.
    def visitExpression2(self, ctx:BKOOLParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expression3.
    def visitExpression3(self, ctx:BKOOLParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expression4.
    def visitExpression4(self, ctx:BKOOLParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expression5.
    def visitExpression5(self, ctx:BKOOLParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expression6.
    def visitExpression6(self, ctx:BKOOLParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expression7.
    def visitExpression7(self, ctx:BKOOLParser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expression8.
    def visitExpression8(self, ctx:BKOOLParser.Expression8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expression9.
    def visitExpression9(self, ctx:BKOOLParser.Expression9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expression10.
    def visitExpression10(self, ctx:BKOOLParser.Expression10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expression11.
    def visitExpression11(self, ctx:BKOOLParser.Expression11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#args.
    def visitArgs(self, ctx:BKOOLParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expList.
    def visitExpList(self, ctx:BKOOLParser.ExpListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#typeType.
    def visitTypeType(self, ctx:BKOOLParser.TypeTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#returnType.
    def visitReturnType(self, ctx:BKOOLParser.ReturnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arrayType.
    def visitArrayType(self, ctx:BKOOLParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#primitiveType.
    def visitPrimitiveType(self, ctx:BKOOLParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classType.
    def visitClassType(self, ctx:BKOOLParser.ClassTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arrayLit.
    def visitArrayLit(self, ctx:BKOOLParser.ArrayLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#elemArrays.
    def visitElemArrays(self, ctx:BKOOLParser.ElemArraysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#elemArray.
    def visitElemArray(self, ctx:BKOOLParser.ElemArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#elem.
    def visitElem(self, ctx:BKOOLParser.ElemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#booleanlit.
    def visitBooleanlit(self, ctx:BKOOLParser.BooleanlitContext):
        return self.visitChildren(ctx)



del BKOOLParser