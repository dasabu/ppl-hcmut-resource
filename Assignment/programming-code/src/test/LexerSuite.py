import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_simple_string(self):
        input = "3dc";
        expect = "3dc,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,100))

    # def test_complex_string(self):
    #     """test complex string"""
    #     self.assertTrue(TestLexer.test("'isn''t'","'isn''t',<EOF>",102))
    