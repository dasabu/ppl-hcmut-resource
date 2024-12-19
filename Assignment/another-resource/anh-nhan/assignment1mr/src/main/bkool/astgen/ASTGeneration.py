from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *

class ASTGeneration(BKOOLVisitor):
    def visitProgram(self,ctx:BKOOLParser.ProgramContext):
        return Program([FuncDecl(Id("main"),
                        [],
                        self.visit(ctx.mptype()),
                        Block([],[self.visit(ctx.body())] if ctx.body() else []))])

    def visitMptype(self,ctx:BKOOLParser.MptypeContext):
        if ctx.INTTYPE():
            return IntType()
        else:
            return VoidType()

    def visitBody(self,ctx:BKOOLParser.BodyContext):
        return self.visit(ctx.exp())

    def visitFuncall(self,ctx:BKOOLParser.FuncallContext):
        return CallExpr(Id(ctx.ID().getText()),[self.visit(ctx.exp())] if ctx.exp() else [])

    def visitExp(self,ctx:BKOOLParser.ExpContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp1())

        left = self.visit(ctx.exp())
        right = self.visit(ctx.exp1())

        return addOp(left, right)

    def visitExp1(self, ctx: BKOOLParser.Exp1Context):
        if (ctx.funcall()):
            return self.visit(ctx.funcall())
        else:
            return IntLiteral(int(ctx.INTLIT().getText()))

