import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Simple program: int main() {} """
        input = """void main() {putInt(100);}"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input, expect, 500))

    def test_int_ast(self):
        input = Program([
            FuncDecl(Id("main"), [], VoidType(), Block([], [
                CallExpr(Id("putInt"), [IntLiteral(5)])]))])
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 501))
    def test_case_1(self):
        input = """int main(){
                 2 + 3;
                }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 1))

    def test_case_2(self):
        input = """int main(){
             2 + 3 + abc();
            }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 2))

    def test_case_3(self):
        input = """int main(){
                         2 + 3 + 5 + 7 + func();
                        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 3))