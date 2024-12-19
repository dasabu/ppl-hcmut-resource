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


    # Visit a parse tree produced by BKOOLParser#classExtends.
    def visitClassExtends(self, ctx:BKOOLParser.ClassExtendsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classBody.
    def visitClassBody(self, ctx:BKOOLParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classMemberList.
    def visitClassMemberList(self, ctx:BKOOLParser.ClassMemberListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classMember.
    def visitClassMember(self, ctx:BKOOLParser.ClassMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#methodDecl.
    def visitMethodDecl(self, ctx:BKOOLParser.MethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#constructor.
    def visitConstructor(self, ctx:BKOOLParser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#normalMethod.
    def visitNormalMethod(self, ctx:BKOOLParser.NormalMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#typ.
    def visitTyp(self, ctx:BKOOLParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramDecl.
    def visitParamDecl(self, ctx:BKOOLParser.ParamDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramList.
    def visitParamList(self, ctx:BKOOLParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramPrime.
    def visitParamPrime(self, ctx:BKOOLParser.ParamPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param.
    def visitParam(self, ctx:BKOOLParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#idlist.
    def visitIdlist(self, ctx:BKOOLParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attrDecl.
    def visitAttrDecl(self, ctx:BKOOLParser.AttrDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#immutDecl.
    def visitImmutDecl(self, ctx:BKOOLParser.ImmutDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mutDecl.
    def visitMutDecl(self, ctx:BKOOLParser.MutDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mutKeyword.
    def visitMutKeyword(self, ctx:BKOOLParser.MutKeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mutMemberList.
    def visitMutMemberList(self, ctx:BKOOLParser.MutMemberListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mutMember.
    def visitMutMember(self, ctx:BKOOLParser.MutMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mutInit.
    def visitMutInit(self, ctx:BKOOLParser.MutInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#immutKeywords.
    def visitImmutKeywords(self, ctx:BKOOLParser.ImmutKeywordsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#immutInitList.
    def visitImmutInitList(self, ctx:BKOOLParser.ImmutInitListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#immutInit.
    def visitImmutInit(self, ctx:BKOOLParser.ImmutInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arrayLit.
    def visitArrayLit(self, ctx:BKOOLParser.ArrayLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arrMemberList.
    def visitArrMemberList(self, ctx:BKOOLParser.ArrMemberListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arrMember.
    def visitArrMember(self, ctx:BKOOLParser.ArrMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#booleanLit.
    def visitBooleanLit(self, ctx:BKOOLParser.BooleanLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr1.
    def visitExpr1(self, ctx:BKOOLParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr2.
    def visitExpr2(self, ctx:BKOOLParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr3.
    def visitExpr3(self, ctx:BKOOLParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr4.
    def visitExpr4(self, ctx:BKOOLParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr5.
    def visitExpr5(self, ctx:BKOOLParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr6.
    def visitExpr6(self, ctx:BKOOLParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr7.
    def visitExpr7(self, ctx:BKOOLParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr8.
    def visitExpr8(self, ctx:BKOOLParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr9.
    def visitExpr9(self, ctx:BKOOLParser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr10.
    def visitExpr10(self, ctx:BKOOLParser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr11.
    def visitExpr11(self, ctx:BKOOLParser.Expr11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arglist.
    def visitArglist(self, ctx:BKOOLParser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#argprime.
    def visitArgprime(self, ctx:BKOOLParser.ArgprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#primiLit.
    def visitPrimiLit(self, ctx:BKOOLParser.PrimiLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#subexpr.
    def visitSubexpr(self, ctx:BKOOLParser.SubexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmtlist.
    def visitStmtlist(self, ctx:BKOOLParser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt.
    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#blockstmt.
    def visitBlockstmt(self, ctx:BKOOLParser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vardecllist.
    def visitVardecllist(self, ctx:BKOOLParser.VardecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vardecl.
    def visitVardecl(self, ctx:BKOOLParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#immutVardecl.
    def visitImmutVardecl(self, ctx:BKOOLParser.ImmutVardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mutVardecl.
    def visitMutVardecl(self, ctx:BKOOLParser.MutVardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#immutVarBody.
    def visitImmutVarBody(self, ctx:BKOOLParser.ImmutVarBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#immutVarMem.
    def visitImmutVarMem(self, ctx:BKOOLParser.ImmutVarMemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mutVarBody.
    def visitMutVarBody(self, ctx:BKOOLParser.MutVarBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mutVarMemList.
    def visitMutVarMemList(self, ctx:BKOOLParser.MutVarMemListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mutVarMem.
    def visitMutVarMem(self, ctx:BKOOLParser.MutVarMemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#asmstmt.
    def visitAsmstmt(self, ctx:BKOOLParser.AsmstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#asmlhs.
    def visitAsmlhs(self, ctx:BKOOLParser.AsmlhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#ifstmt.
    def visitIfstmt(self, ctx:BKOOLParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#forstmt.
    def visitForstmt(self, ctx:BKOOLParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#breakstmt.
    def visitBreakstmt(self, ctx:BKOOLParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#contstmt.
    def visitContstmt(self, ctx:BKOOLParser.ContstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#retstmt.
    def visitRetstmt(self, ctx:BKOOLParser.RetstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#methodivkstmt.
    def visitMethodivkstmt(self, ctx:BKOOLParser.MethodivkstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#primiTyp.
    def visitPrimiTyp(self, ctx:BKOOLParser.PrimiTypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classTyp.
    def visitClassTyp(self, ctx:BKOOLParser.ClassTypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arrayTyp.
    def visitArrayTyp(self, ctx:BKOOLParser.ArrayTypContext):
        return self.visitChildren(ctx)



del BKOOLParser