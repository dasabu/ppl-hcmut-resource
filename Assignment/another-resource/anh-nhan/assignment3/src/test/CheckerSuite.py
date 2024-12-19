import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_undeclared_function(self):
        """Simple program: int main() {} """
        input = Program([ClassDecl(Id("loc"),[AttributeDecl(Instance(),VarDecl(Id("x"),IntType())),MethodDecl(Id("main"),Static(),[],VoidType(),Block([VarDecl(Id("x"),IntType(),IntLiteral(1))],[If(BinaryOp("==",Id("x"),FloatLiteral(1)),Assign(Id("x"),FloatLiteral(10.0)))]))])])
        expect = "Illegal Array Literal: [IntLiteraleral(2),FloatLit(1.2),NullLiteral()]"
        self.assertTrue(TestChecker.test(input,expect,400))

    # def test_diff_numofparam_stmt(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn();
    #     }"""
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),List())"
    #     self.assertTrue(TestChecker.test(input,expect,401))
    #
    # def test_diff_numofparam_expr(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(getInt(4));
    #     }"""
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),List(IntLiteraleraleral(4)))"
    #     self.assertTrue(TestChecker.test(input,expect,402))
    #
    # def test_undeclared_function_use_ast(self):
    #     """Simple program: int main() {} """
    #     input = Program([MethodDecl(Id("main"),[],IntType(),Block([],[
    #         CallExpr(Id("foo"),[])]))])
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,403))
    #
    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             MethodDecl(Id("main"),[],IntType(),Block([],[
    #                 CallExpr(Id("putIntLn"),[
    #                     CallExpr(Id("getInt"),[IntLiteraleraleral(4)])
    #                     ])]))])
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),List(IntLiteraleraleral(4)))"
    #     self.assertTrue(TestChecker.test(input,expect,404))
    #
    # def test_diff_numofparam_stmt_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             MethodDecl(Id("main"),[],IntType(),Block([],[
    #                 CallExpr(Id("putIntLn"),[])]))])
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),List())"
    #     self.assertTrue(TestChecker.test(input,expect,405))
    #