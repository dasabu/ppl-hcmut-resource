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


    # Visit a parse tree produced by BKOOLParser#vardecls.
    def visitVardecls(self, ctx:BKOOLParser.VardeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vardecl.
    def visitVardecl(self, ctx:BKOOLParser.VardeclContext):
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


    # Visit a parse tree produced by BKOOLParser#subexpr.
    def visitSubexpr(self, ctx:BKOOLParser.SubexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#atom.
    def visitAtom(self, ctx:BKOOLParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arrayLit.
    def visitArrayLit(self, ctx:BKOOLParser.ArrayLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#indexedArray.
    def visitIndexedArray(self, ctx:BKOOLParser.IndexedArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exprlist.
    def visitExprlist(self, ctx:BKOOLParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exprprime.
    def visitExprprime(self, ctx:BKOOLParser.ExprprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#associativeArray.
    def visitAssociativeArray(self, ctx:BKOOLParser.AssociativeArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#pairlist.
    def visitPairlist(self, ctx:BKOOLParser.PairlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#pairprime.
    def visitPairprime(self, ctx:BKOOLParser.PairprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#pair.
    def visitPair(self, ctx:BKOOLParser.PairContext):
        return self.visitChildren(ctx)



del BKOOLParser