import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_stuff(self):
        """ Test Valid Lowercase Keywords """
        self.assertTrue(TestLexer.test(
            r"""
"He ask me: \"Where is John?\""
""",
            r"He ask me: \"Where is John?\",<EOF>",
            101
        ))

    def test_2_valid_keywords(self):
        """ Test Valid Keywords """
        self.assertTrue(TestLexer.test(
            """ boolean
int float
void string
if else then
new break continue to downto
for return true
false class extends static
final
nil this
""",

            "boolean,int,float,void,string,if,else,then,new,break,continue,to,downto,for,return,true,false,class,extends,static,final,nil,this,<EOF>",
            102
        ))

