import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """
            class a {
                final static int r;
            }
            """
        expect = """Program([ClassDecl(Id(A),[AttributeDecl(Static,ConstDecl(Id(y),IntType,None)),MethodDecl(Id(d),Static,[param(Id(o),StringType)],IntType,Block([VarDecl(Id(a),IntType),VarDecl(Id(c),IntType),VarDecl(Id(d),IntType)],[AssignStmt(Id(y),BinaryOp(*,Id(a),Id(d))),Return(IntLiteral(4))]))])])"""
        self.assertTrue(TestAST.test(input,expect,200))

   