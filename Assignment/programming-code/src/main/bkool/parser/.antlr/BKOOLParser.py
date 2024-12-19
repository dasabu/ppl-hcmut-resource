# Generated from /Users/duyanhle/Desktop/procode/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\32")
        buf.write("\u0098\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\60\n\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\5\5<\n\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\5\6C\n\6\3\7\3\7\3\7\3\7\3\7\3\7\7\7K\n\7")
        buf.write("\f\7\16\7N\13\7\3\b\3\b\3\b\3\b\3\b\3\b\7\bV\n\b\f\b\16")
        buf.write("\bY\13\b\3\t\3\t\3\t\3\t\3\t\5\t`\n\t\3\n\3\n\5\nd\n\n")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\5\fn\n\f\3\r\3\r")
        buf.write("\5\rr\n\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\5\17{\n\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\5\20\u0082\n\20\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\22\3\22\5\22\u008b\n\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\5\23\u0092\n\23\3\24\3\24\3\24\3\24\3\24\2")
        buf.write("\4\f\16\25\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$")
        buf.write("&\2\4\3\2\13\f\3\2\r\17\2\u0093\2(\3\2\2\2\4/\3\2\2\2")
        buf.write("\6\61\3\2\2\2\b;\3\2\2\2\nB\3\2\2\2\fD\3\2\2\2\16O\3\2")
        buf.write("\2\2\20_\3\2\2\2\22c\3\2\2\2\24e\3\2\2\2\26m\3\2\2\2\30")
        buf.write("q\3\2\2\2\32s\3\2\2\2\34z\3\2\2\2\36\u0081\3\2\2\2 \u0083")
        buf.write("\3\2\2\2\"\u008a\3\2\2\2$\u0091\3\2\2\2&\u0093\3\2\2\2")
        buf.write("()\5\4\3\2)*\7\2\2\3*\3\3\2\2\2+,\5\6\4\2,-\5\4\3\2-\60")
        buf.write("\3\2\2\2.\60\5\6\4\2/+\3\2\2\2/.\3\2\2\2\60\5\3\2\2\2")
        buf.write("\61\62\7\26\2\2\62\63\7\4\2\2\63\64\5\b\5\2\64\65\7\5")
        buf.write("\2\2\65\7\3\2\2\2\66\67\5\n\6\2\678\7\n\2\289\5\n\6\2")
        buf.write("9<\3\2\2\2:<\5\n\6\2;\66\3\2\2\2;:\3\2\2\2<\t\3\2\2\2")
        buf.write("=>\5\f\7\2>?\t\2\2\2?@\5\n\6\2@C\3\2\2\2AC\5\f\7\2B=\3")
        buf.write("\2\2\2BA\3\2\2\2C\13\3\2\2\2DE\b\7\1\2EF\5\16\b\2FL\3")
        buf.write("\2\2\2GH\f\4\2\2HI\t\3\2\2IK\5\16\b\2JG\3\2\2\2KN\3\2")
        buf.write("\2\2LJ\3\2\2\2LM\3\2\2\2M\r\3\2\2\2NL\3\2\2\2OP\b\b\1")
        buf.write("\2PQ\5\20\t\2QW\3\2\2\2RS\f\4\2\2ST\7\20\2\2TV\5\20\t")
        buf.write("\2UR\3\2\2\2VY\3\2\2\2WU\3\2\2\2WX\3\2\2\2X\17\3\2\2\2")
        buf.write("YW\3\2\2\2Z[\5\22\n\2[\\\7\21\2\2\\]\5\20\t\2]`\3\2\2")
        buf.write("\2^`\5\22\n\2_Z\3\2\2\2_^\3\2\2\2`\21\3\2\2\2ad\5\26\f")
        buf.write("\2bd\5\24\13\2ca\3\2\2\2cb\3\2\2\2d\23\3\2\2\2ef\7\6\2")
        buf.write("\2fg\5\b\5\2gh\7\7\2\2h\25\3\2\2\2in\7\23\2\2jn\7\24\2")
        buf.write("\2kn\7\25\2\2ln\5\30\r\2mi\3\2\2\2mj\3\2\2\2mk\3\2\2\2")
        buf.write("ml\3\2\2\2n\27\3\2\2\2or\5\32\16\2pr\5 \21\2qo\3\2\2\2")
        buf.write("qp\3\2\2\2r\31\3\2\2\2st\7\22\2\2tu\7\6\2\2uv\5\34\17")
        buf.write("\2vw\7\7\2\2w\33\3\2\2\2x{\5\36\20\2y{\3\2\2\2zx\3\2\2")
        buf.write("\2zy\3\2\2\2{\35\3\2\2\2|}\5\b\5\2}~\7\b\2\2~\177\5\36")
        buf.write("\20\2\177\u0082\3\2\2\2\u0080\u0082\5\b\5\2\u0081|\3\2")
        buf.write("\2\2\u0081\u0080\3\2\2\2\u0082\37\3\2\2\2\u0083\u0084")
        buf.write("\7\22\2\2\u0084\u0085\7\6\2\2\u0085\u0086\5\"\22\2\u0086")
        buf.write("\u0087\7\7\2\2\u0087!\3\2\2\2\u0088\u008b\5$\23\2\u0089")
        buf.write("\u008b\3\2\2\2\u008a\u0088\3\2\2\2\u008a\u0089\3\2\2\2")
        buf.write("\u008b#\3\2\2\2\u008c\u008d\5&\24\2\u008d\u008e\7\b\2")
        buf.write("\2\u008e\u008f\5$\23\2\u008f\u0092\3\2\2\2\u0090\u0092")
        buf.write("\5&\24\2\u0091\u008c\3\2\2\2\u0091\u0090\3\2\2\2\u0092")
        buf.write("%\3\2\2\2\u0093\u0094\7\3\2\2\u0094\u0095\7\t\2\2\u0095")
        buf.write("\u0096\5\b\5\2\u0096\'\3\2\2\2\17/;BLW_cmqz\u0081\u008a")
        buf.write("\u0091")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'='", "';'", "'('", "')'", 
                     "','", "'=>'", "'??'", "'+'", "'-'", "'/'", "'*'", 
                     "'%'", "'.'", "'**'", "'array'" ]

    symbolicNames = [ "<INVALID>", "PAIRNAME", "EQ", "SEMI", "LP", "RP", 
                      "COMMA", "ARROW", "DQUES", "ADD", "SUB", "DIV", "MUL", 
                      "MOD", "DOT", "DSTAR", "ARRAY", "INTLIT", "FLOATLIT", 
                      "STRINGLIT", "VARNAME", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_vardecls = 1
    RULE_vardecl = 2
    RULE_expr = 3
    RULE_expr1 = 4
    RULE_expr2 = 5
    RULE_expr3 = 6
    RULE_expr4 = 7
    RULE_expr5 = 8
    RULE_subexpr = 9
    RULE_atom = 10
    RULE_arrayLit = 11
    RULE_indexedArray = 12
    RULE_exprlist = 13
    RULE_exprprime = 14
    RULE_associativeArray = 15
    RULE_pairlist = 16
    RULE_pairprime = 17
    RULE_pair = 18

    ruleNames =  [ "program", "vardecls", "vardecl", "expr", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "subexpr", "atom", "arrayLit", 
                   "indexedArray", "exprlist", "exprprime", "associativeArray", 
                   "pairlist", "pairprime", "pair" ]

    EOF = Token.EOF
    PAIRNAME=1
    EQ=2
    SEMI=3
    LP=4
    RP=5
    COMMA=6
    ARROW=7
    DQUES=8
    ADD=9
    SUB=10
    DIV=11
    MUL=12
    MOD=13
    DOT=14
    DSTAR=15
    ARRAY=16
    INTLIT=17
    FLOATLIT=18
    STRINGLIT=19
    VARNAME=20
    WS=21
    ERROR_CHAR=22
    UNCLOSE_STRING=23
    ILLEGAL_ESCAPE=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecls(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclsContext,0)


        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_program




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.vardecls()
            self.state = 39
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def vardecls(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_vardecls




    def vardecls(self):

        localctx = BKOOLParser.VardeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_vardecls)
        try:
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.vardecl()
                self.state = 42
                self.vardecls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.vardecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARNAME(self):
            return self.getToken(BKOOLParser.VARNAME, 0)

        def EQ(self):
            return self.getToken(BKOOLParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_vardecl




    def vardecl(self):

        localctx = BKOOLParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(BKOOLParser.VARNAME)
            self.state = 48
            self.match(BKOOLParser.EQ)
            self.state = 49
            self.expr()
            self.state = 50
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Expr1Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expr1Context,i)


        def DQUES(self):
            return self.getToken(BKOOLParser.DQUES, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr)
        try:
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.expr1()
                self.state = 53
                self.match(BKOOLParser.DQUES)
                self.state = 54
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(BKOOLParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(BKOOLParser.Expr1Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr1




    def expr1(self):

        localctx = BKOOLParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.expr2(0)
                self.state = 60
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 61
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(BKOOLParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(BKOOLParser.Expr2Context,0)


        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def DIV(self):
            return self.getToken(BKOOLParser.DIV, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 74
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 69
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 70
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.DIV) | (1 << BKOOLParser.MUL) | (1 << BKOOLParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 71
                    self.expr3(0) 
                self.state = 76
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(BKOOLParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(BKOOLParser.Expr3Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr3



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.expr4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 85
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 80
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 81
                    self.match(BKOOLParser.DOT)
                    self.state = 82
                    self.expr4() 
                self.state = 87
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(BKOOLParser.Expr5Context,0)


        def DSTAR(self):
            return self.getToken(BKOOLParser.DSTAR, 0)

        def expr4(self):
            return self.getTypedRuleContext(BKOOLParser.Expr4Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr4




    def expr4(self):

        localctx = BKOOLParser.Expr4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expr4)
        try:
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.expr5()
                self.state = 89
                self.match(BKOOLParser.DSTAR)
                self.state = 90
                self.expr4()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.expr5()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(BKOOLParser.AtomContext,0)


        def subexpr(self):
            return self.getTypedRuleContext(BKOOLParser.SubexprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr5




    def expr5(self):

        localctx = BKOOLParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expr5)
        try:
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ARRAY, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.atom()
                pass
            elif token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.subexpr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_subexpr




    def subexpr(self):

        localctx = BKOOLParser.SubexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(BKOOLParser.LP)
            self.state = 100
            self.expr()
            self.state = 101
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(BKOOLParser.STRINGLIT, 0)

        def arrayLit(self):
            return self.getTypedRuleContext(BKOOLParser.ArrayLitContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_atom




    def atom(self):

        localctx = BKOOLParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_atom)
        try:
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.match(BKOOLParser.INTLIT)
                pass
            elif token in [BKOOLParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.match(BKOOLParser.FLOATLIT)
                pass
            elif token in [BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 105
                self.match(BKOOLParser.STRINGLIT)
                pass
            elif token in [BKOOLParser.ARRAY]:
                self.enterOuterAlt(localctx, 4)
                self.state = 106
                self.arrayLit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def indexedArray(self):
            return self.getTypedRuleContext(BKOOLParser.IndexedArrayContext,0)


        def associativeArray(self):
            return self.getTypedRuleContext(BKOOLParser.AssociativeArrayContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_arrayLit




    def arrayLit(self):

        localctx = BKOOLParser.ArrayLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arrayLit)
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.indexedArray()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.associativeArray()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexedArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(BKOOLParser.ARRAY, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def exprlist(self):
            return self.getTypedRuleContext(BKOOLParser.ExprlistContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_indexedArray




    def indexedArray(self):

        localctx = BKOOLParser.IndexedArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_indexedArray)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(BKOOLParser.ARRAY)
            self.state = 114
            self.match(BKOOLParser.LP)
            self.state = 115
            self.exprlist()
            self.state = 116
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprprime(self):
            return self.getTypedRuleContext(BKOOLParser.ExprprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exprlist




    def exprlist(self):

        localctx = BKOOLParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_exprlist)
        try:
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LP, BKOOLParser.ARRAY, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.exprprime()
                pass
            elif token in [BKOOLParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def exprprime(self):
            return self.getTypedRuleContext(BKOOLParser.ExprprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exprprime




    def exprprime(self):

        localctx = BKOOLParser.ExprprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_exprprime)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.expr()
                self.state = 123
                self.match(BKOOLParser.COMMA)
                self.state = 124
                self.exprprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssociativeArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(BKOOLParser.ARRAY, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def pairlist(self):
            return self.getTypedRuleContext(BKOOLParser.PairlistContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_associativeArray




    def associativeArray(self):

        localctx = BKOOLParser.AssociativeArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_associativeArray)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(BKOOLParser.ARRAY)
            self.state = 130
            self.match(BKOOLParser.LP)
            self.state = 131
            self.pairlist()
            self.state = 132
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pairprime(self):
            return self.getTypedRuleContext(BKOOLParser.PairprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_pairlist




    def pairlist(self):

        localctx = BKOOLParser.PairlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_pairlist)
        try:
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.PAIRNAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.pairprime()
                pass
            elif token in [BKOOLParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pair(self):
            return self.getTypedRuleContext(BKOOLParser.PairContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def pairprime(self):
            return self.getTypedRuleContext(BKOOLParser.PairprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_pairprime




    def pairprime(self):

        localctx = BKOOLParser.PairprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_pairprime)
        try:
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.pair()
                self.state = 139
                self.match(BKOOLParser.COMMA)
                self.state = 140
                self.pairprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.pair()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAIRNAME(self):
            return self.getToken(BKOOLParser.PAIRNAME, 0)

        def ARROW(self):
            return self.getToken(BKOOLParser.ARROW, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_pair




    def pair(self):

        localctx = BKOOLParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(BKOOLParser.PAIRNAME)
            self.state = 146
            self.match(BKOOLParser.ARROW)
            self.state = 147
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expr2_sempred
        self._predicates[6] = self.expr3_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




