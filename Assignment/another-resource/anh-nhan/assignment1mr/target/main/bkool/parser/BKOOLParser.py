# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("\65\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\5\2\25\n\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\5\5\"\n\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\7\6,\n\6\f\6\16\6/\13\6\3\7\3\7\5\7\63\n")
        buf.write("\7\3\7\2\3\n\b\2\4\6\b\n\f\2\3\3\2\5\6\2\62\2\16\3\2\2")
        buf.write("\2\4\31\3\2\2\2\6\33\3\2\2\2\b\36\3\2\2\2\n%\3\2\2\2\f")
        buf.write("\62\3\2\2\2\16\17\5\4\3\2\17\20\7\3\2\2\20\21\7\t\2\2")
        buf.write("\21\22\7\n\2\2\22\24\7\13\2\2\23\25\5\6\4\2\24\23\3\2")
        buf.write("\2\2\24\25\3\2\2\2\25\26\3\2\2\2\26\27\7\f\2\2\27\30\7")
        buf.write("\2\2\3\30\3\3\2\2\2\31\32\t\2\2\2\32\5\3\2\2\2\33\34\5")
        buf.write("\n\6\2\34\35\7\r\2\2\35\7\3\2\2\2\36\37\7\7\2\2\37!\7")
        buf.write("\t\2\2 \"\5\n\6\2! \3\2\2\2!\"\3\2\2\2\"#\3\2\2\2#$\7")
        buf.write("\n\2\2$\t\3\2\2\2%&\b\6\1\2&\'\5\f\7\2\'-\3\2\2\2()\f")
        buf.write("\4\2\2)*\7\4\2\2*,\5\f\7\2+(\3\2\2\2,/\3\2\2\2-+\3\2\2")
        buf.write("\2-.\3\2\2\2.\13\3\2\2\2/-\3\2\2\2\60\63\5\b\5\2\61\63")
        buf.write("\7\b\2\2\62\60\3\2\2\2\62\61\3\2\2\2\63\r\3\2\2\2\6\24")
        buf.write("!-\62")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'+'", "'int'", "'void'", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "ADD", "INTTYPE", "VOIDTYPE", 
                      "ID", "INTLIT", "LB", "RB", "LP", "RP", "SEMI", "WS", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_mptype = 1
    RULE_body = 2
    RULE_funcall = 3
    RULE_exp = 4
    RULE_exp1 = 5

    ruleNames =  [ "program", "mptype", "body", "funcall", "exp", "exp1" ]

    EOF = Token.EOF
    T__0=1
    ADD=2
    INTTYPE=3
    VOIDTYPE=4
    ID=5
    INTLIT=6
    LB=7
    RB=8
    LP=9
    RP=10
    SEMI=11
    WS=12
    ERROR_CHAR=13
    UNCLOSE_STRING=14
    ILLEGAL_ESCAPE=15

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

        def mptype(self):
            return self.getTypedRuleContext(BKOOLParser.MptypeContext,0)


        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def body(self):
            return self.getTypedRuleContext(BKOOLParser.BodyContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.mptype()
            self.state = 13
            self.match(BKOOLParser.T__0)
            self.state = 14
            self.match(BKOOLParser.LB)
            self.state = 15
            self.match(BKOOLParser.RB)
            self.state = 16
            self.match(BKOOLParser.LP)
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.ID or _la==BKOOLParser.INTLIT:
                self.state = 17
                self.body()


            self.state = 20
            self.match(BKOOLParser.RP)
            self.state = 21
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MptypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(BKOOLParser.INTTYPE, 0)

        def VOIDTYPE(self):
            return self.getToken(BKOOLParser.VOIDTYPE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_mptype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMptype" ):
                return visitor.visitMptype(self)
            else:
                return visitor.visitChildren(self)




    def mptype(self):

        localctx = BKOOLParser.MptypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mptype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.INTTYPE or _la==BKOOLParser.VOIDTYPE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = BKOOLParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.exp(0)
            self.state = 26
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_funcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)




    def funcall(self):

        localctx = BKOOLParser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(BKOOLParser.ID)
            self.state = 29
            self.match(BKOOLParser.LB)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.ID or _la==BKOOLParser.INTLIT:
                self.state = 30
                self.exp(0)


            self.state = 33
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self):
            return self.getTypedRuleContext(BKOOLParser.Exp1Context,0)


        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.exp1()
            self._ctx.stop = self._input.LT(-1)
            self.state = 43
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                    self.state = 38
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 39
                    self.match(BKOOLParser.ADD)
                    self.state = 40
                    self.exp1() 
                self.state = 45
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(BKOOLParser.FuncallContext,0)


        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = BKOOLParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_exp1)
        try:
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.funcall()
                pass
            elif token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.match(BKOOLParser.INTLIT)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.exp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




