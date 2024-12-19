# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\32")
        buf.write("\u0088\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f")
        buf.write("\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\6\22\\\n\22\r\22\16\22]\3\23")
        buf.write("\6\23a\n\23\r\23\16\23b\3\23\3\23\6\23g\n\23\r\23\16\23")
        buf.write("h\3\24\3\24\7\24m\n\24\f\24\16\24p\13\24\3\24\3\24\3\25")
        buf.write("\3\25\7\25v\n\25\f\25\16\25y\13\25\3\26\6\26|\n\26\r\26")
        buf.write("\16\26}\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3")
        buf.write("n\2\32\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\3\2\6\3\2\62;\5\2C\\aac|\6\2\62;C\\aac|\5\2")
        buf.write("\13\f\17\17\"\"\2\u008d\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\3\63\3")
        buf.write("\2\2\2\5\65\3\2\2\2\7\67\3\2\2\2\t9\3\2\2\2\13;\3\2\2")
        buf.write("\2\r=\3\2\2\2\17?\3\2\2\2\21B\3\2\2\2\23E\3\2\2\2\25G")
        buf.write("\3\2\2\2\27I\3\2\2\2\31K\3\2\2\2\33M\3\2\2\2\35O\3\2\2")
        buf.write("\2\37Q\3\2\2\2!T\3\2\2\2#[\3\2\2\2%`\3\2\2\2\'j\3\2\2")
        buf.write("\2)s\3\2\2\2+{\3\2\2\2-\u0081\3\2\2\2/\u0084\3\2\2\2\61")
        buf.write("\u0086\3\2\2\2\63\64\5)\25\2\64\4\3\2\2\2\65\66\7?\2\2")
        buf.write("\66\6\3\2\2\2\678\7=\2\28\b\3\2\2\29:\7*\2\2:\n\3\2\2")
        buf.write("\2;<\7+\2\2<\f\3\2\2\2=>\7.\2\2>\16\3\2\2\2?@\7?\2\2@")
        buf.write("A\7@\2\2A\20\3\2\2\2BC\7A\2\2CD\7A\2\2D\22\3\2\2\2EF\7")
        buf.write("-\2\2F\24\3\2\2\2GH\7/\2\2H\26\3\2\2\2IJ\7\61\2\2J\30")
        buf.write("\3\2\2\2KL\7,\2\2L\32\3\2\2\2MN\7\'\2\2N\34\3\2\2\2OP")
        buf.write("\7\60\2\2P\36\3\2\2\2QR\7,\2\2RS\7,\2\2S \3\2\2\2TU\7")
        buf.write("c\2\2UV\7t\2\2VW\7t\2\2WX\7c\2\2XY\7{\2\2Y\"\3\2\2\2Z")
        buf.write("\\\t\2\2\2[Z\3\2\2\2\\]\3\2\2\2][\3\2\2\2]^\3\2\2\2^$")
        buf.write("\3\2\2\2_a\t\2\2\2`_\3\2\2\2ab\3\2\2\2b`\3\2\2\2bc\3\2")
        buf.write("\2\2cd\3\2\2\2df\5\35\17\2eg\t\2\2\2fe\3\2\2\2gh\3\2\2")
        buf.write("\2hf\3\2\2\2hi\3\2\2\2i&\3\2\2\2jn\7$\2\2km\13\2\2\2l")
        buf.write("k\3\2\2\2mp\3\2\2\2no\3\2\2\2nl\3\2\2\2oq\3\2\2\2pn\3")
        buf.write("\2\2\2qr\7$\2\2r(\3\2\2\2sw\t\3\2\2tv\t\4\2\2ut\3\2\2")
        buf.write("\2vy\3\2\2\2wu\3\2\2\2wx\3\2\2\2x*\3\2\2\2yw\3\2\2\2z")
        buf.write("|\t\5\2\2{z\3\2\2\2|}\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\177")
        buf.write("\3\2\2\2\177\u0080\b\26\2\2\u0080,\3\2\2\2\u0081\u0082")
        buf.write("\13\2\2\2\u0082\u0083\b\27\3\2\u0083.\3\2\2\2\u0084\u0085")
        buf.write("\13\2\2\2\u0085\60\3\2\2\2\u0086\u0087\13\2\2\2\u0087")
        buf.write("\62\3\2\2\2\t\2]bhnw}\4\b\2\2\3\27\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PAIRNAME = 1
    EQ = 2
    SEMI = 3
    LP = 4
    RP = 5
    COMMA = 6
    ARROW = 7
    DQUES = 8
    ADD = 9
    SUB = 10
    DIV = 11
    MUL = 12
    MOD = 13
    DOT = 14
    DSTAR = 15
    ARRAY = 16
    INTLIT = 17
    FLOATLIT = 18
    STRINGLIT = 19
    VARNAME = 20
    WS = 21
    ERROR_CHAR = 22
    UNCLOSE_STRING = 23
    ILLEGAL_ESCAPE = 24

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "';'", "'('", "')'", "','", "'=>'", "'??'", "'+'", "'-'", 
            "'/'", "'*'", "'%'", "'.'", "'**'", "'array'" ]

    symbolicNames = [ "<INVALID>",
            "PAIRNAME", "EQ", "SEMI", "LP", "RP", "COMMA", "ARROW", "DQUES", 
            "ADD", "SUB", "DIV", "MUL", "MOD", "DOT", "DSTAR", "ARRAY", 
            "INTLIT", "FLOATLIT", "STRINGLIT", "VARNAME", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "PAIRNAME", "EQ", "SEMI", "LP", "RP", "COMMA", "ARROW", 
                  "DQUES", "ADD", "SUB", "DIV", "MUL", "MOD", "DOT", "DSTAR", 
                  "ARRAY", "INTLIT", "FLOATLIT", "STRINGLIT", "VARNAME", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[21] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


