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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u0235\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3\2\3")
        buf.write("\2\3\3\6\3\u0089\n\3\r\3\16\3\u008a\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\5\5\u0097\n\5\3\6\3\6\3\6\3\6\5")
        buf.write("\6\u009d\n\6\3\7\3\7\5\7\u00a1\n\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\5\b\u00aa\n\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\5\t\u00b5\n\t\3\n\3\n\3\n\3\n\5\n\u00bb\n\n\3\13")
        buf.write("\3\13\3\13\3\13\5\13\u00c1\n\13\3\f\5\f\u00c4\n\f\3\f")
        buf.write("\3\f\3\f\3\f\5\f\u00ca\n\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\16\5\16\u00d6\n\16\3\16\3\16\3\16\3\16\5\16")
        buf.write("\u00dc\n\16\3\16\3\16\3\16\3\17\3\17\3\17\5\17\u00e4\n")
        buf.write("\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\5\20")
        buf.write("\u00ef\n\20\3\21\3\21\3\21\3\21\3\21\5\21\u00f6\n\21\3")
        buf.write("\22\3\22\3\22\3\23\3\23\3\23\3\23\5\23\u00ff\n\23\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\5\25\u0107\n\25\3\26\6\26\u010a")
        buf.write("\n\26\r\26\16\26\u010b\3\27\3\27\5\27\u0110\n\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0119\n\30\3\30\3")
        buf.write("\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\5\31\u0127\n\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3")
        buf.write("\33\5\33\u0131\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\5\34\u013e\n\34\3\35\3\35\3\35\3")
        buf.write("\35\3\35\5\35\u0145\n\35\3\35\5\35\u0148\n\35\3\36\3\36")
        buf.write("\3\36\5\36\u014d\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\5\37\u0157\n\37\3 \3 \3 \3!\3!\3!\3\"\3\"\5\"")
        buf.write("\u0161\n\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3&\3&\3&\3&\3&\5&\u0176\n&\3\'\3\'\3\'\3\'\3\'\5\'\u017d")
        buf.write("\n\'\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)\7)\u018a\n)\f)\16")
        buf.write(")\u018d\13)\3*\3*\3*\3*\3*\3*\3*\3*\3*\7*\u0198\n*\f*")
        buf.write("\16*\u019b\13*\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+")
        buf.write("\3+\3+\7+\u01ac\n+\f+\16+\u01af\13+\3,\3,\3,\5,\u01b4")
        buf.write("\n,\3-\3-\3-\5-\u01b9\n-\3.\3.\3.\3.\3.\7.\u01c0\n.\f")
        buf.write(".\16.\u01c3\13.\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3")
        buf.write("\60\7\60\u01cf\n\60\f\60\16\60\u01d2\13\60\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\61\5\61\u01da\n\61\3\62\3\62\5\62\u01de")
        buf.write("\n\62\3\63\3\63\3\63\5\63\u01e3\n\63\3\64\3\64\3\64\3")
        buf.write("\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\5\66\u01f7\n\66\3\67\3\67\5\67\u01fb")
        buf.write("\n\67\38\38\38\38\38\58\u0202\n8\39\39\39\39\39\39\59")
        buf.write("\u020a\n9\3:\3:\3;\3;\3;\5;\u0211\n;\3;\3;\3<\3<\3<\3")
        buf.write("<\3<\5<\u021a\n<\3=\3=\3>\3>\3?\3?\3?\3?\3?\3?\5?\u0226")
        buf.write("\n?\3@\3@\3A\3A\3A\3A\3A\5A\u022f\nA\3B\3B\3B\3B\3B\2")
        buf.write("\7PRTZ^C\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(")
        buf.write("*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080")
        buf.write("\u0082\2\7\3\2\34\35\4\2\'\')-\3\2\36\37\6\2\6\6\16\17")
        buf.write("\21\21\27\27\3\2\25\26\2\u0245\2\u0084\3\2\2\2\4\u0088")
        buf.write("\3\2\2\2\6\u008c\3\2\2\2\b\u0096\3\2\2\2\n\u009c\3\2\2")
        buf.write("\2\f\u00a0\3\2\2\2\16\u00a9\3\2\2\2\20\u00b4\3\2\2\2\22")
        buf.write("\u00ba\3\2\2\2\24\u00c0\3\2\2\2\26\u00c3\3\2\2\2\30\u00ce")
        buf.write("\3\2\2\2\32\u00d5\3\2\2\2\34\u00e0\3\2\2\2\36\u00ee\3")
        buf.write("\2\2\2 \u00f5\3\2\2\2\"\u00f7\3\2\2\2$\u00fe\3\2\2\2&")
        buf.write("\u0100\3\2\2\2(\u0106\3\2\2\2*\u0109\3\2\2\2,\u010f\3")
        buf.write("\2\2\2.\u0118\3\2\2\2\60\u0126\3\2\2\2\62\u0128\3\2\2")
        buf.write("\2\64\u0130\3\2\2\2\66\u013d\3\2\2\28\u013f\3\2\2\2:\u0149")
        buf.write("\3\2\2\2<\u014e\3\2\2\2>\u0158\3\2\2\2@\u015b\3\2\2\2")
        buf.write("B\u015e\3\2\2\2D\u0164\3\2\2\2F\u0167\3\2\2\2H\u0169\3")
        buf.write("\2\2\2J\u0175\3\2\2\2L\u017c\3\2\2\2N\u017e\3\2\2\2P\u0180")
        buf.write("\3\2\2\2R\u018e\3\2\2\2T\u019c\3\2\2\2V\u01b3\3\2\2\2")
        buf.write("X\u01b8\3\2\2\2Z\u01ba\3\2\2\2\\\u01c4\3\2\2\2^\u01c8")
        buf.write("\3\2\2\2`\u01d9\3\2\2\2b\u01dd\3\2\2\2d\u01e2\3\2\2\2")
        buf.write("f\u01e4\3\2\2\2h\u01e8\3\2\2\2j\u01f6\3\2\2\2l\u01fa\3")
        buf.write("\2\2\2n\u0201\3\2\2\2p\u0209\3\2\2\2r\u020b\3\2\2\2t\u020d")
        buf.write("\3\2\2\2v\u0219\3\2\2\2x\u021b\3\2\2\2z\u021d\3\2\2\2")
        buf.write("|\u0225\3\2\2\2~\u0227\3\2\2\2\u0080\u022e\3\2\2\2\u0082")
        buf.write("\u0230\3\2\2\2\u0084\u0085\5\4\3\2\u0085\u0086\7\2\2\3")
        buf.write("\u0086\3\3\2\2\2\u0087\u0089\5\6\4\2\u0088\u0087\3\2\2")
        buf.write("\2\u0089\u008a\3\2\2\2\u008a\u0088\3\2\2\2\u008a\u008b")
        buf.write("\3\2\2\2\u008b\5\3\2\2\2\u008c\u008d\7\b\2\2\u008d\u008e")
        buf.write("\7>\2\2\u008e\u008f\5\b\5\2\u008f\u0090\79\2\2\u0090\u0091")
        buf.write("\5\n\6\2\u0091\u0092\7:\2\2\u0092\7\3\2\2\2\u0093\u0094")
        buf.write("\7\r\2\2\u0094\u0097\7>\2\2\u0095\u0097\3\2\2\2\u0096")
        buf.write("\u0093\3\2\2\2\u0096\u0095\3\2\2\2\u0097\t\3\2\2\2\u0098")
        buf.write("\u0099\5\f\7\2\u0099\u009a\5\n\6\2\u009a\u009d\3\2\2\2")
        buf.write("\u009b\u009d\3\2\2\2\u009c\u0098\3\2\2\2\u009c\u009b\3")
        buf.write("\2\2\2\u009d\13\3\2\2\2\u009e\u00a1\5\16\b\2\u009f\u00a1")
        buf.write("\5\24\13\2\u00a0\u009e\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1")
        buf.write("\r\3\2\2\2\u00a2\u00a3\7\32\2\2\u00a3\u00aa\7\33\2\2\u00a4")
        buf.write("\u00a5\7\33\2\2\u00a5\u00aa\7\32\2\2\u00a6\u00aa\7\33")
        buf.write("\2\2\u00a7\u00aa\7\32\2\2\u00a8\u00aa\3\2\2\2\u00a9\u00a2")
        buf.write("\3\2\2\2\u00a9\u00a4\3\2\2\2\u00a9\u00a6\3\2\2\2\u00a9")
        buf.write("\u00a7\3\2\2\2\u00a9\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2")
        buf.write("\u00ab\u00ac\5\36\20\2\u00ac\u00ad\5\20\t\2\u00ad\u00ae")
        buf.write("\7\67\2\2\u00ae\17\3\2\2\2\u00af\u00b0\5\22\n\2\u00b0")
        buf.write("\u00b1\7\66\2\2\u00b1\u00b2\5\20\t\2\u00b2\u00b5\3\2\2")
        buf.write("\2\u00b3\u00b5\5\22\n\2\u00b4\u00af\3\2\2\2\u00b4\u00b3")
        buf.write("\3\2\2\2\u00b5\21\3\2\2\2\u00b6\u00bb\7>\2\2\u00b7\u00b8")
        buf.write("\7>\2\2\u00b8\u00b9\7(\2\2\u00b9\u00bb\5J&\2\u00ba\u00b6")
        buf.write("\3\2\2\2\u00ba\u00b7\3\2\2\2\u00bb\23\3\2\2\2\u00bc\u00c1")
        buf.write("\5\26\f\2\u00bd\u00c1\5\34\17\2\u00be\u00c1\5\30\r\2\u00bf")
        buf.write("\u00c1\5\32\16\2\u00c0\u00bc\3\2\2\2\u00c0\u00bd\3\2\2")
        buf.write("\2\u00c0\u00be\3\2\2\2\u00c0\u00bf\3\2\2\2\u00c1\25\3")
        buf.write("\2\2\2\u00c2\u00c4\7\33\2\2\u00c3\u00c2\3\2\2\2\u00c3")
        buf.write("\u00c4\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c6\5\36\20")
        buf.write("\2\u00c6\u00c7\7>\2\2\u00c7\u00c9\7\61\2\2\u00c8\u00ca")
        buf.write("\5 \21\2\u00c9\u00c8\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca")
        buf.write("\u00cb\3\2\2\2\u00cb\u00cc\7\62\2\2\u00cc\u00cd\5&\24")
        buf.write("\2\u00cd\27\3\2\2\2\u00ce\u00cf\7\27\2\2\u00cf\u00d0\7")
        buf.write("\3\2\2\u00d0\u00d1\7\61\2\2\u00d1\u00d2\7\62\2\2\u00d2")
        buf.write("\u00d3\5&\24\2\u00d3\31\3\2\2\2\u00d4\u00d6\7\33\2\2\u00d5")
        buf.write("\u00d4\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d7\3\2\2\2")
        buf.write("\u00d7\u00d8\7\27\2\2\u00d8\u00d9\7>\2\2\u00d9\u00db\7")
        buf.write("\61\2\2\u00da\u00dc\5 \21\2\u00db\u00da\3\2\2\2\u00db")
        buf.write("\u00dc\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00de\7\62\2")
        buf.write("\2\u00de\u00df\5&\24\2\u00df\33\3\2\2\2\u00e0\u00e1\7")
        buf.write(">\2\2\u00e1\u00e3\7\61\2\2\u00e2\u00e4\5 \21\2\u00e3\u00e2")
        buf.write("\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5")
        buf.write("\u00e6\7\62\2\2\u00e6\u00e7\5&\24\2\u00e7\35\3\2\2\2\u00e8")
        buf.write("\u00ef\7\16\2\2\u00e9\u00ef\7\17\2\2\u00ea\u00ef\7\6\2")
        buf.write("\2\u00eb\u00ef\7\21\2\2\u00ec\u00ef\5t;\2\u00ed\u00ef")
        buf.write("\5z>\2\u00ee\u00e8\3\2\2\2\u00ee\u00e9\3\2\2\2\u00ee\u00ea")
        buf.write("\3\2\2\2\u00ee\u00eb\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ee")
        buf.write("\u00ed\3\2\2\2\u00ef\37\3\2\2\2\u00f0\u00f1\5\"\22\2\u00f1")
        buf.write("\u00f2\7\67\2\2\u00f2\u00f3\5 \21\2\u00f3\u00f6\3\2\2")
        buf.write("\2\u00f4\u00f6\5\"\22\2\u00f5\u00f0\3\2\2\2\u00f5\u00f4")
        buf.write("\3\2\2\2\u00f6!\3\2\2\2\u00f7\u00f8\5\36\20\2\u00f8\u00f9")
        buf.write("\5$\23\2\u00f9#\3\2\2\2\u00fa\u00fb\7>\2\2\u00fb\u00fc")
        buf.write("\7\66\2\2\u00fc\u00ff\5$\23\2\u00fd\u00ff\7>\2\2\u00fe")
        buf.write("\u00fa\3\2\2\2\u00fe\u00fd\3\2\2\2\u00ff%\3\2\2\2\u0100")
        buf.write("\u0101\79\2\2\u0101\u0102\5(\25\2\u0102\u0103\7:\2\2\u0103")
        buf.write("\'\3\2\2\2\u0104\u0107\5*\26\2\u0105\u0107\3\2\2\2\u0106")
        buf.write("\u0104\3\2\2\2\u0106\u0105\3\2\2\2\u0107)\3\2\2\2\u0108")
        buf.write("\u010a\5,\27\2\u0109\u0108\3\2\2\2\u010a\u010b\3\2\2\2")
        buf.write("\u010b\u0109\3\2\2\2\u010b\u010c\3\2\2\2\u010c+\3\2\2")
        buf.write("\2\u010d\u0110\5.\30\2\u010e\u0110\5\60\31\2\u010f\u010d")
        buf.write("\3\2\2\2\u010f\u010e\3\2\2\2\u0110-\3\2\2\2\u0111\u0112")
        buf.write("\7\32\2\2\u0112\u0119\7\33\2\2\u0113\u0114\7\33\2\2\u0114")
        buf.write("\u0119\7\32\2\2\u0115\u0119\7\33\2\2\u0116\u0119\7\32")
        buf.write("\2\2\u0117\u0119\3\2\2\2\u0118\u0111\3\2\2\2\u0118\u0113")
        buf.write("\3\2\2\2\u0118\u0115\3\2\2\2\u0118\u0116\3\2\2\2\u0118")
        buf.write("\u0117\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u011b\5\36\20")
        buf.write("\2\u011b\u011c\5\20\t\2\u011c\u011d\7\67\2\2\u011d/\3")
        buf.write("\2\2\2\u011e\u0127\5\62\32\2\u011f\u0127\58\35\2\u0120")
        buf.write("\u0127\5<\37\2\u0121\u0127\5> \2\u0122\u0127\5@!\2\u0123")
        buf.write("\u0127\5B\"\2\u0124\u0127\5D#\2\u0125\u0127\5&\24\2\u0126")
        buf.write("\u011e\3\2\2\2\u0126\u011f\3\2\2\2\u0126\u0120\3\2\2\2")
        buf.write("\u0126\u0121\3\2\2\2\u0126\u0122\3\2\2\2\u0126\u0123\3")
        buf.write("\2\2\2\u0126\u0124\3\2\2\2\u0126\u0125\3\2\2\2\u0127\61")
        buf.write("\3\2\2\2\u0128\u0129\5\64\33\2\u0129\u012a\7\60\2\2\u012a")
        buf.write("\u012b\5J&\2\u012b\u012c\7\67\2\2\u012c\63\3\2\2\2\u012d")
        buf.write("\u0131\5\66\34\2\u012e\u012f\7>\2\2\u012f\u0131\5\\/\2")
        buf.write("\u0130\u012d\3\2\2\2\u0130\u012e\3\2\2\2\u0131\65\3\2")
        buf.write("\2\2\u0132\u013e\7>\2\2\u0133\u013e\5f\64\2\u0134\u0135")
        buf.write("\5^\60\2\u0135\u0136\7\65\2\2\u0136\u0137\7>\2\2\u0137")
        buf.write("\u013e\3\2\2\2\u0138\u0139\7>\2\2\u0139\u013a\7\65\2\2")
        buf.write("\u013a\u013b\5^\60\2\u013b\u013c\5\\/\2\u013c\u013e\3")
        buf.write("\2\2\2\u013d\u0132\3\2\2\2\u013d\u0133\3\2\2\2\u013d\u0134")
        buf.write("\3\2\2\2\u013d\u0138\3\2\2\2\u013e\67\3\2\2\2\u013f\u0140")
        buf.write("\7\13\2\2\u0140\u0141\5J&\2\u0141\u0144\7\22\2\2\u0142")
        buf.write("\u0145\5,\27\2\u0143\u0145\5&\24\2\u0144\u0142\3\2\2\2")
        buf.write("\u0144\u0143\3\2\2\2\u0145\u0147\3\2\2\2\u0146\u0148\5")
        buf.write(":\36\2\u0147\u0146\3\2\2\2\u0147\u0148\3\2\2\2\u01489")
        buf.write("\3\2\2\2\u0149\u014c\7\f\2\2\u014a\u014d\5,\27\2\u014b")
        buf.write("\u014d\5&\24\2\u014c\u014a\3\2\2\2\u014c\u014b\3\2\2\2")
        buf.write("\u014d;\3\2\2\2\u014e\u014f\7\23\2\2\u014f\u0150\5\66")
        buf.write("\34\2\u0150\u0151\7\60\2\2\u0151\u0152\5J&\2\u0152\u0153")
        buf.write("\t\2\2\2\u0153\u0156\5J&\2\u0154\u0157\5,\27\2\u0155\u0157")
        buf.write("\5&\24\2\u0156\u0154\3\2\2\2\u0156\u0155\3\2\2\2\u0157")
        buf.write("=\3\2\2\2\u0158\u0159\7\7\2\2\u0159\u015a\7\67\2\2\u015a")
        buf.write("?\3\2\2\2\u015b\u015c\7\t\2\2\u015c\u015d\7\67\2\2\u015d")
        buf.write("A\3\2\2\2\u015e\u0160\7\24\2\2\u015f\u0161\5J&\2\u0160")
        buf.write("\u015f\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u0162\3\2\2\2")
        buf.write("\u0162\u0163\7\67\2\2\u0163C\3\2\2\2\u0164\u0165\5F$\2")
        buf.write("\u0165\u0166\7\67\2\2\u0166E\3\2\2\2\u0167\u0168\5H%\2")
        buf.write("\u0168G\3\2\2\2\u0169\u016a\5^\60\2\u016a\u016b\7\65\2")
        buf.write("\2\u016b\u016c\7>\2\2\u016c\u016d\7\61\2\2\u016d\u016e")
        buf.write("\5l\67\2\u016e\u016f\7\62\2\2\u016fI\3\2\2\2\u0170\u0171")
        buf.write("\5L\'\2\u0171\u0172\7.\2\2\u0172\u0173\5L\'\2\u0173\u0176")
        buf.write("\3\2\2\2\u0174\u0176\5L\'\2\u0175\u0170\3\2\2\2\u0175")
        buf.write("\u0174\3\2\2\2\u0176K\3\2\2\2\u0177\u0178\5P)\2\u0178")
        buf.write("\u0179\5N(\2\u0179\u017a\5P)\2\u017a\u017d\3\2\2\2\u017b")
        buf.write("\u017d\5P)\2\u017c\u0177\3\2\2\2\u017c\u017b\3\2\2\2\u017d")
        buf.write("M\3\2\2\2\u017e\u017f\t\3\2\2\u017fO\3\2\2\2\u0180\u0181")
        buf.write("\b)\1\2\u0181\u0182\5R*\2\u0182\u018b\3\2\2\2\u0183\u0184")
        buf.write("\f\5\2\2\u0184\u0185\7%\2\2\u0185\u018a\5R*\2\u0186\u0187")
        buf.write("\f\4\2\2\u0187\u0188\7&\2\2\u0188\u018a\5R*\2\u0189\u0183")
        buf.write("\3\2\2\2\u0189\u0186\3\2\2\2\u018a\u018d\3\2\2\2\u018b")
        buf.write("\u0189\3\2\2\2\u018b\u018c\3\2\2\2\u018cQ\3\2\2\2\u018d")
        buf.write("\u018b\3\2\2\2\u018e\u018f\b*\1\2\u018f\u0190\5T+\2\u0190")
        buf.write("\u0199\3\2\2\2\u0191\u0192\f\5\2\2\u0192\u0193\7\36\2")
        buf.write("\2\u0193\u0198\5T+\2\u0194\u0195\f\4\2\2\u0195\u0196\7")
        buf.write("\37\2\2\u0196\u0198\5T+\2\u0197\u0191\3\2\2\2\u0197\u0194")
        buf.write("\3\2\2\2\u0198\u019b\3\2\2\2\u0199\u0197\3\2\2\2\u0199")
        buf.write("\u019a\3\2\2\2\u019aS\3\2\2\2\u019b\u0199\3\2\2\2\u019c")
        buf.write("\u019d\b+\1\2\u019d\u019e\5V,\2\u019e\u01ad\3\2\2\2\u019f")
        buf.write("\u01a0\f\7\2\2\u01a0\u01a1\7 \2\2\u01a1\u01ac\5V,\2\u01a2")
        buf.write("\u01a3\f\6\2\2\u01a3\u01a4\7!\2\2\u01a4\u01ac\5V,\2\u01a5")
        buf.write("\u01a6\f\5\2\2\u01a6\u01a7\7#\2\2\u01a7\u01ac\5V,\2\u01a8")
        buf.write("\u01a9\f\4\2\2\u01a9\u01aa\7\"\2\2\u01aa\u01ac\5V,\2\u01ab")
        buf.write("\u019f\3\2\2\2\u01ab\u01a2\3\2\2\2\u01ab\u01a5\3\2\2\2")
        buf.write("\u01ab\u01a8\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad\u01ab\3")
        buf.write("\2\2\2\u01ad\u01ae\3\2\2\2\u01aeU\3\2\2\2\u01af\u01ad")
        buf.write("\3\2\2\2\u01b0\u01b1\7$\2\2\u01b1\u01b4\5V,\2\u01b2\u01b4")
        buf.write("\5X-\2\u01b3\u01b0\3\2\2\2\u01b3\u01b2\3\2\2\2\u01b4W")
        buf.write("\3\2\2\2\u01b5\u01b6\t\4\2\2\u01b6\u01b9\5X-\2\u01b7\u01b9")
        buf.write("\5Z.\2\u01b8\u01b5\3\2\2\2\u01b8\u01b7\3\2\2\2\u01b9Y")
        buf.write("\3\2\2\2\u01ba\u01bb\b.\1\2\u01bb\u01bc\5^\60\2\u01bc")
        buf.write("\u01c1\3\2\2\2\u01bd\u01be\f\4\2\2\u01be\u01c0\5\\/\2")
        buf.write("\u01bf\u01bd\3\2\2\2\u01c0\u01c3\3\2\2\2\u01c1\u01bf\3")
        buf.write("\2\2\2\u01c1\u01c2\3\2\2\2\u01c2[\3\2\2\2\u01c3\u01c1")
        buf.write("\3\2\2\2\u01c4\u01c5\7\63\2\2\u01c5\u01c6\5J&\2\u01c6")
        buf.write("\u01c7\7\64\2\2\u01c7]\3\2\2\2\u01c8\u01c9\b\60\1\2\u01c9")
        buf.write("\u01ca\5b\62\2\u01ca\u01d0\3\2\2\2\u01cb\u01cc\f\4\2\2")
        buf.write("\u01cc\u01cd\7\65\2\2\u01cd\u01cf\5`\61\2\u01ce\u01cb")
        buf.write("\3\2\2\2\u01cf\u01d2\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0")
        buf.write("\u01d1\3\2\2\2\u01d1_\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d3")
        buf.write("\u01da\7>\2\2\u01d4\u01d5\7>\2\2\u01d5\u01d6\7\61\2\2")
        buf.write("\u01d6\u01d7\5l\67\2\u01d7\u01d8\7\62\2\2\u01d8\u01da")
        buf.write("\3\2\2\2\u01d9\u01d3\3\2\2\2\u01d9\u01d4\3\2\2\2\u01da")
        buf.write("a\3\2\2\2\u01db\u01de\7\31\2\2\u01dc\u01de\5d\63\2\u01dd")
        buf.write("\u01db\3\2\2\2\u01dd\u01dc\3\2\2\2\u01dec\3\2\2\2\u01df")
        buf.write("\u01e3\5f\64\2\u01e0\u01e3\5h\65\2\u01e1\u01e3\5j\66\2")
        buf.write("\u01e2\u01df\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2\u01e1\3")
        buf.write("\2\2\2\u01e3e\3\2\2\2\u01e4\u01e5\7>\2\2\u01e5\u01e6\7")
        buf.write("\65\2\2\u01e6\u01e7\7>\2\2\u01e7g\3\2\2\2\u01e8\u01e9")
        buf.write("\7>\2\2\u01e9\u01ea\7\65\2\2\u01ea\u01eb\7>\2\2\u01eb")
        buf.write("\u01ec\7\61\2\2\u01ec\u01ed\5l\67\2\u01ed\u01ee\7\62\2")
        buf.write("\2\u01eei\3\2\2\2\u01ef\u01f0\7\20\2\2\u01f0\u01f1\7>")
        buf.write("\2\2\u01f1\u01f2\7\61\2\2\u01f2\u01f3\5l\67\2\u01f3\u01f4")
        buf.write("\7\62\2\2\u01f4\u01f7\3\2\2\2\u01f5\u01f7\5p9\2\u01f6")
        buf.write("\u01ef\3\2\2\2\u01f6\u01f5\3\2\2\2\u01f7k\3\2\2\2\u01f8")
        buf.write("\u01fb\5n8\2\u01f9\u01fb\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fa")
        buf.write("\u01f9\3\2\2\2\u01fbm\3\2\2\2\u01fc\u01fd\5J&\2\u01fd")
        buf.write("\u01fe\7\66\2\2\u01fe\u01ff\5n8\2\u01ff\u0202\3\2\2\2")
        buf.write("\u0200\u0202\5J&\2\u0201\u01fc\3\2\2\2\u0201\u0200\3\2")
        buf.write("\2\2\u0202o\3\2\2\2\u0203\u020a\5|?\2\u0204\u020a\7>\2")
        buf.write("\2\u0205\u0206\7\61\2\2\u0206\u0207\5J&\2\u0207\u0208")
        buf.write("\7\62\2\2\u0208\u020a\3\2\2\2\u0209\u0203\3\2\2\2\u0209")
        buf.write("\u0204\3\2\2\2\u0209\u0205\3\2\2\2\u020aq\3\2\2\2\u020b")
        buf.write("\u020c\t\5\2\2\u020cs\3\2\2\2\u020d\u020e\5v<\2\u020e")
        buf.write("\u0210\7\63\2\2\u020f\u0211\5x=\2\u0210\u020f\3\2\2\2")
        buf.write("\u0210\u0211\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u0213\7")
        buf.write("\64\2\2\u0213u\3\2\2\2\u0214\u021a\7\16\2\2\u0215\u021a")
        buf.write("\7\17\2\2\u0216\u021a\7\6\2\2\u0217\u021a\7\21\2\2\u0218")
        buf.write("\u021a\5z>\2\u0219\u0214\3\2\2\2\u0219\u0215\3\2\2\2\u0219")
        buf.write("\u0216\3\2\2\2\u0219\u0217\3\2\2\2\u0219\u0218\3\2\2\2")
        buf.write("\u021aw\3\2\2\2\u021b\u021c\7;\2\2\u021cy\3\2\2\2\u021d")
        buf.write("\u021e\7>\2\2\u021e{\3\2\2\2\u021f\u0226\7;\2\2\u0220")
        buf.write("\u0226\7<\2\2\u0221\u0226\5~@\2\u0222\u0226\7=\2\2\u0223")
        buf.write("\u0226\5\u0082B\2\u0224\u0226\7\30\2\2\u0225\u021f\3\2")
        buf.write("\2\2\u0225\u0220\3\2\2\2\u0225\u0221\3\2\2\2\u0225\u0222")
        buf.write("\3\2\2\2\u0225\u0223\3\2\2\2\u0225\u0224\3\2\2\2\u0226")
        buf.write("}\3\2\2\2\u0227\u0228\t\6\2\2\u0228\177\3\2\2\2\u0229")
        buf.write("\u022f\5|?\2\u022a\u022b\5|?\2\u022b\u022c\7\66\2\2\u022c")
        buf.write("\u022d\5\u0080A\2\u022d\u022f\3\2\2\2\u022e\u0229\3\2")
        buf.write("\2\2\u022e\u022a\3\2\2\2\u022f\u0081\3\2\2\2\u0230\u0231")
        buf.write("\79\2\2\u0231\u0232\5\u0080A\2\u0232\u0233\7:\2\2\u0233")
        buf.write("\u0083\3\2\2\2\65\u008a\u0096\u009c\u00a0\u00a9\u00b4")
        buf.write("\u00ba\u00c0\u00c3\u00c9\u00d5\u00db\u00e3\u00ee\u00f5")
        buf.write("\u00fe\u0106\u010b\u010f\u0118\u0126\u0130\u013d\u0144")
        buf.write("\u0147\u014c\u0156\u0160\u0175\u017c\u0189\u018b\u0197")
        buf.write("\u0199\u01ab\u01ad\u01b3\u01b8\u01c1\u01d0\u01d9\u01dd")
        buf.write("\u01e2\u01f6\u01fa\u0201\u0209\u0210\u0219\u0225\u022e")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "<INVALID>", "<INVALID>", "'boolean'", 
                     "'break'", "'class'", "'continue'", "'do'", "'if'", 
                     "'else'", "'extends'", "'int'", "'float'", "'new'", 
                     "'string'", "'then'", "'for'", "'return'", "'true'", 
                     "'false'", "'void'", "'nil'", "'this'", "'final'", 
                     "'static'", "'to'", "'downto'", "'+'", "'-'", "'*'", 
                     "'/'", "'\\'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
                     "'='", "'!='", "'<'", "'<='", "'>'", "'>='", "'^'", 
                     "'::'", "':='", "'('", "')'", "'['", "']'", "'.'", 
                     "','", "';'", "':'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "WS", "COMMENT", "BOOLEAN", 
                      "BREAK", "CLASS", "CONTINUE", "DO", "IF", "ELSE", 
                      "EXTENDS", "INT", "FLOAT", "NEW", "STRING", "THEN", 
                      "FOR", "RETURN", "TRUE", "FALSE", "VOID", "NIL", "THIS", 
                      "FINAL", "STATIC", "TO", "DOWNTO", "ADD", "SUB", "MUL", 
                      "DIV", "IDIV", "MOD", "NOT", "AND", "OR", "EQQ", "EQ", 
                      "NOTEQ", "LT", "LTEQ", "GT", "GTEQ", "CONCAT", "SCOPE", 
                      "ASSIGN", "LR", "RR", "LS", "RS", "DOT", "COMMA", 
                      "SEMI", "COLON", "LB", "RB", "INTLIT", "FLOATLIT", 
                      "STRING_LIT", "ID", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_TOKEN" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_class_decl = 2
    RULE_superclass = 3
    RULE_memberlist = 4
    RULE_member = 5
    RULE_variable_decl = 6
    RULE_attribute_list = 7
    RULE_attribute = 8
    RULE_method_decl = 9
    RULE_normalMethod = 10
    RULE_mainMethod = 11
    RULE_voidMethod = 12
    RULE_constructor = 13
    RULE_type_name = 14
    RULE_paramlist = 15
    RULE_param = 16
    RULE_idlist = 17
    RULE_block_stmt = 18
    RULE_block_body = 19
    RULE_blocks = 20
    RULE_stmt = 21
    RULE_var_decl = 22
    RULE_other_stmt = 23
    RULE_assignment_stmt = 24
    RULE_lhs = 25
    RULE_scalar_variable = 26
    RULE_if_stmt = 27
    RULE_else_stmt = 28
    RULE_for_stmt = 29
    RULE_break_stmt = 30
    RULE_continue_stmt = 31
    RULE_return_stmt = 32
    RULE_method_invo_stmt = 33
    RULE_method_invo = 34
    RULE_exp9_method = 35
    RULE_expr = 36
    RULE_exp2 = 37
    RULE_relational = 38
    RULE_exp3 = 39
    RULE_exp4 = 40
    RULE_exp5 = 41
    RULE_exp6 = 42
    RULE_exp7 = 43
    RULE_exp8 = 44
    RULE_indexop = 45
    RULE_exp9 = 46
    RULE_tail_part = 47
    RULE_exp13 = 48
    RULE_exp10 = 49
    RULE_exp10_access = 50
    RULE_exp10_call = 51
    RULE_exp11 = 52
    RULE_exp_list = 53
    RULE_exps = 54
    RULE_exp12 = 55
    RULE_primitive_type = 56
    RULE_array_type = 57
    RULE_element_type = 58
    RULE_size = 59
    RULE_class_type = 60
    RULE_literal = 61
    RULE_boolean_lit = 62
    RULE_arr_exp = 63
    RULE_indexarr_lit = 64

    ruleNames =  [ "program", "decl", "class_decl", "superclass", "memberlist", 
                   "member", "variable_decl", "attribute_list", "attribute", 
                   "method_decl", "normalMethod", "mainMethod", "voidMethod", 
                   "constructor", "type_name", "paramlist", "param", "idlist", 
                   "block_stmt", "block_body", "blocks", "stmt", "var_decl", 
                   "other_stmt", "assignment_stmt", "lhs", "scalar_variable", 
                   "if_stmt", "else_stmt", "for_stmt", "break_stmt", "continue_stmt", 
                   "return_stmt", "method_invo_stmt", "method_invo", "exp9_method", 
                   "expr", "exp2", "relational", "exp3", "exp4", "exp5", 
                   "exp6", "exp7", "exp8", "indexop", "exp9", "tail_part", 
                   "exp13", "exp10", "exp10_access", "exp10_call", "exp11", 
                   "exp_list", "exps", "exp12", "primitive_type", "array_type", 
                   "element_type", "size", "class_type", "literal", "boolean_lit", 
                   "arr_exp", "indexarr_lit" ]

    EOF = Token.EOF
    T__0=1
    WS=2
    COMMENT=3
    BOOLEAN=4
    BREAK=5
    CLASS=6
    CONTINUE=7
    DO=8
    IF=9
    ELSE=10
    EXTENDS=11
    INT=12
    FLOAT=13
    NEW=14
    STRING=15
    THEN=16
    FOR=17
    RETURN=18
    TRUE=19
    FALSE=20
    VOID=21
    NIL=22
    THIS=23
    FINAL=24
    STATIC=25
    TO=26
    DOWNTO=27
    ADD=28
    SUB=29
    MUL=30
    DIV=31
    IDIV=32
    MOD=33
    NOT=34
    AND=35
    OR=36
    EQQ=37
    EQ=38
    NOTEQ=39
    LT=40
    LTEQ=41
    GT=42
    GTEQ=43
    CONCAT=44
    SCOPE=45
    ASSIGN=46
    LR=47
    RR=48
    LS=49
    RS=50
    DOT=51
    COMMA=52
    SEMI=53
    COLON=54
    LB=55
    RB=56
    INTLIT=57
    FLOATLIT=58
    STRING_LIT=59
    ID=60
    UNCLOSE_STRING=61
    ILLEGAL_ESCAPE=62
    ERROR_TOKEN=63

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

        def decl(self):
            return self.getTypedRuleContext(BKOOLParser.DeclContext,0)


        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.decl()
            self.state = 131
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Class_declContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Class_declContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = BKOOLParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 133
                self.class_decl()
                self.state = 136 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.CLASS):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(BKOOLParser.CLASS, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def superclass(self):
            return self.getTypedRuleContext(BKOOLParser.SuperclassContext,0)


        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def memberlist(self):
            return self.getTypedRuleContext(BKOOLParser.MemberlistContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_class_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_decl" ):
                return visitor.visitClass_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_decl(self):

        localctx = BKOOLParser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(BKOOLParser.CLASS)
            self.state = 139
            self.match(BKOOLParser.ID)
            self.state = 140
            self.superclass()
            self.state = 141
            self.match(BKOOLParser.LB)
            self.state = 142
            self.memberlist()
            self.state = 143
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuperclassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXTENDS(self):
            return self.getToken(BKOOLParser.EXTENDS, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_superclass

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuperclass" ):
                return visitor.visitSuperclass(self)
            else:
                return visitor.visitChildren(self)




    def superclass(self):

        localctx = BKOOLParser.SuperclassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_superclass)
        try:
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.EXTENDS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.match(BKOOLParser.EXTENDS)
                self.state = 146
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.LB]:
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


    class MemberlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(BKOOLParser.MemberContext,0)


        def memberlist(self):
            return self.getTypedRuleContext(BKOOLParser.MemberlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_memberlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberlist" ):
                return visitor.visitMemberlist(self)
            else:
                return visitor.visitChildren(self)




    def memberlist(self):

        localctx = BKOOLParser.MemberlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_memberlist)
        try:
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.INT, BKOOLParser.FLOAT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.FINAL, BKOOLParser.STATIC, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.member()
                self.state = 151
                self.memberlist()
                pass
            elif token in [BKOOLParser.RB]:
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


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Variable_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Method_declContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember" ):
                return visitor.visitMember(self)
            else:
                return visitor.visitChildren(self)




    def member(self):

        localctx = BKOOLParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_member)
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.variable_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.method_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_name(self):
            return self.getTypedRuleContext(BKOOLParser.Type_nameContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(BKOOLParser.Attribute_listContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_variable_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_decl" ):
                return visitor.visitVariable_decl(self)
            else:
                return visitor.visitChildren(self)




    def variable_decl(self):

        localctx = BKOOLParser.Variable_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variable_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 160
                self.match(BKOOLParser.FINAL)
                self.state = 161
                self.match(BKOOLParser.STATIC)
                pass

            elif la_ == 2:
                self.state = 162
                self.match(BKOOLParser.STATIC)
                self.state = 163
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 3:
                self.state = 164
                self.match(BKOOLParser.STATIC)
                pass

            elif la_ == 4:
                self.state = 165
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 5:
                pass


            self.state = 169
            self.type_name()
            self.state = 170
            self.attribute_list()
            self.state = 171
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def attribute_list(self):
            return self.getTypedRuleContext(BKOOLParser.Attribute_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attribute_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_list" ):
                return visitor.visitAttribute_list(self)
            else:
                return visitor.visitChildren(self)




    def attribute_list(self):

        localctx = BKOOLParser.Attribute_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attribute_list)
        try:
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.attribute()
                self.state = 174
                self.match(BKOOLParser.COMMA)
                self.state = 175
                self.attribute_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.attribute()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def EQ(self):
            return self.getToken(BKOOLParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = BKOOLParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attribute)
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.match(BKOOLParser.ID)
                self.state = 182
                self.match(BKOOLParser.EQ)
                self.state = 183
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normalMethod(self):
            return self.getTypedRuleContext(BKOOLParser.NormalMethodContext,0)


        def constructor(self):
            return self.getTypedRuleContext(BKOOLParser.ConstructorContext,0)


        def mainMethod(self):
            return self.getTypedRuleContext(BKOOLParser.MainMethodContext,0)


        def voidMethod(self):
            return self.getTypedRuleContext(BKOOLParser.VoidMethodContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = BKOOLParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_method_decl)
        try:
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.normalMethod()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.constructor()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 188
                self.mainMethod()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 189
                self.voidMethod()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NormalMethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_name(self):
            return self.getTypedRuleContext(BKOOLParser.Type_nameContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LR(self):
            return self.getToken(BKOOLParser.LR, 0)

        def RR(self):
            return self.getToken(BKOOLParser.RR, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def paramlist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_normalMethod

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormalMethod" ):
                return visitor.visitNormalMethod(self)
            else:
                return visitor.visitChildren(self)




    def normalMethod(self):

        localctx = BKOOLParser.NormalMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_normalMethod)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 192
                self.match(BKOOLParser.STATIC)


            self.state = 195
            self.type_name()
            self.state = 196
            self.match(BKOOLParser.ID)
            self.state = 197
            self.match(BKOOLParser.LR)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0):
                self.state = 198
                self.paramlist()


            self.state = 201
            self.match(BKOOLParser.RR)
            self.state = 202
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainMethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def LR(self):
            return self.getToken(BKOOLParser.LR, 0)

        def RR(self):
            return self.getToken(BKOOLParser.RR, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_mainMethod

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMainMethod" ):
                return visitor.visitMainMethod(self)
            else:
                return visitor.visitChildren(self)




    def mainMethod(self):

        localctx = BKOOLParser.MainMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_mainMethod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(BKOOLParser.VOID)
            self.state = 205
            self.match(BKOOLParser.T__0)
            self.state = 206
            self.match(BKOOLParser.LR)
            self.state = 207
            self.match(BKOOLParser.RR)
            self.state = 208
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VoidMethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LR(self):
            return self.getToken(BKOOLParser.LR, 0)

        def RR(self):
            return self.getToken(BKOOLParser.RR, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def paramlist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_voidMethod

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVoidMethod" ):
                return visitor.visitVoidMethod(self)
            else:
                return visitor.visitChildren(self)




    def voidMethod(self):

        localctx = BKOOLParser.VoidMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_voidMethod)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 210
                self.match(BKOOLParser.STATIC)


            self.state = 213
            self.match(BKOOLParser.VOID)
            self.state = 214
            self.match(BKOOLParser.ID)
            self.state = 215
            self.match(BKOOLParser.LR)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0):
                self.state = 216
                self.paramlist()


            self.state = 219
            self.match(BKOOLParser.RR)
            self.state = 220
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LR(self):
            return self.getToken(BKOOLParser.LR, 0)

        def RR(self):
            return self.getToken(BKOOLParser.RR, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def paramlist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_constructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = BKOOLParser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(BKOOLParser.ID)
            self.state = 223
            self.match(BKOOLParser.LR)
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0):
                self.state = 224
                self.paramlist()


            self.state = 227
            self.match(BKOOLParser.RR)
            self.state = 228
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def array_type(self):
            return self.getTypedRuleContext(BKOOLParser.Array_typeContext,0)


        def class_type(self):
            return self.getTypedRuleContext(BKOOLParser.Class_typeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_type_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_name" ):
                return visitor.visitType_name(self)
            else:
                return visitor.visitChildren(self)




    def type_name(self):

        localctx = BKOOLParser.Type_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_type_name)
        try:
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.match(BKOOLParser.INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.match(BKOOLParser.FLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 232
                self.match(BKOOLParser.BOOLEAN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 233
                self.match(BKOOLParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 234
                self.array_type()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 235
                self.class_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def paramlist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = BKOOLParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_paramlist)
        try:
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.param()
                self.state = 239
                self.match(BKOOLParser.SEMI)
                self.state = 240
                self.paramlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_name(self):
            return self.getTypedRuleContext(BKOOLParser.Type_nameContext,0)


        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = BKOOLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.type_name()
            self.state = 246
            self.idlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = BKOOLParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_idlist)
        try:
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(BKOOLParser.ID)
                self.state = 249
                self.match(BKOOLParser.COMMA)
                self.state = 250
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def block_body(self):
            return self.getTypedRuleContext(BKOOLParser.Block_bodyContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = BKOOLParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(BKOOLParser.LB)
            self.state = 255
            self.block_body()
            self.state = 256
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blocks(self):
            return self.getTypedRuleContext(BKOOLParser.BlocksContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_block_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_body" ):
                return visitor.visitBlock_body(self)
            else:
                return visitor.visitChildren(self)




    def block_body(self):

        localctx = BKOOLParser.Block_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_block_body)
        try:
            self.state = 260
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.BREAK, BKOOLParser.CONTINUE, BKOOLParser.IF, BKOOLParser.INT, BKOOLParser.FLOAT, BKOOLParser.NEW, BKOOLParser.STRING, BKOOLParser.FOR, BKOOLParser.RETURN, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.FINAL, BKOOLParser.STATIC, BKOOLParser.LR, BKOOLParser.LB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.blocks()
                pass
            elif token in [BKOOLParser.RB]:
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


    class BlocksContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmtContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_blocks

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlocks" ):
                return visitor.visitBlocks(self)
            else:
                return visitor.visitChildren(self)




    def blocks(self):

        localctx = BKOOLParser.BlocksContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_blocks)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 262
                self.stmt()
                self.state = 265 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.LR) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.ID))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Var_declContext,0)


        def other_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Other_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_stmt)
        try:
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.other_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_name(self):
            return self.getTypedRuleContext(BKOOLParser.Type_nameContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(BKOOLParser.Attribute_listContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = BKOOLParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 271
                self.match(BKOOLParser.FINAL)
                self.state = 272
                self.match(BKOOLParser.STATIC)
                pass

            elif la_ == 2:
                self.state = 273
                self.match(BKOOLParser.STATIC)
                self.state = 274
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 3:
                self.state = 275
                self.match(BKOOLParser.STATIC)
                pass

            elif la_ == 4:
                self.state = 276
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 5:
                pass


            self.state = 280
            self.type_name()
            self.state = 281
            self.attribute_list()
            self.state = 282
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Other_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Assignment_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Return_stmtContext,0)


        def method_invo_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Method_invo_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_other_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOther_stmt" ):
                return visitor.visitOther_stmt(self)
            else:
                return visitor.visitChildren(self)




    def other_stmt(self):

        localctx = BKOOLParser.Other_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_other_stmt)
        try:
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.assignment_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 286
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 287
                self.break_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 288
                self.continue_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 289
                self.return_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 290
                self.method_invo_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 291
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(BKOOLParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_assignment_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_stmt" ):
                return visitor.visitAssignment_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assignment_stmt(self):

        localctx = BKOOLParser.Assignment_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_assignment_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.lhs()
            self.state = 295
            self.match(BKOOLParser.ASSIGN)
            self.state = 296
            self.expr()
            self.state = 297
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_variable(self):
            return self.getTypedRuleContext(BKOOLParser.Scalar_variableContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def indexop(self):
            return self.getTypedRuleContext(BKOOLParser.IndexopContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_lhs)
        try:
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.scalar_variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.match(BKOOLParser.ID)
                self.state = 301
                self.indexop()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_variableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def exp10_access(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10_accessContext,0)


        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def indexop(self):
            return self.getTypedRuleContext(BKOOLParser.IndexopContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_scalar_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_variable" ):
                return visitor.visitScalar_variable(self)
            else:
                return visitor.visitChildren(self)




    def scalar_variable(self):

        localctx = BKOOLParser.Scalar_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_scalar_variable)
        try:
            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                self.exp10_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 306
                self.exp9(0)
                self.state = 307
                self.match(BKOOLParser.DOT)
                self.state = 308
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 310
                self.match(BKOOLParser.ID)
                self.state = 311
                self.match(BKOOLParser.DOT)
                self.state = 312
                self.exp9(0)
                self.state = 313
                self.indexop()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def else_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Else_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = BKOOLParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(BKOOLParser.IF)
            self.state = 318
            self.expr()
            self.state = 319
            self.match(BKOOLParser.THEN)
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 320
                self.stmt()
                pass

            elif la_ == 2:
                self.state = 321
                self.block_stmt()
                pass


            self.state = 325
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 324
                self.else_stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_else_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = BKOOLParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_else_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(BKOOLParser.ELSE)
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 328
                self.stmt()
                pass

            elif la_ == 2:
                self.state = 329
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def scalar_variable(self):
            return self.getTypedRuleContext(BKOOLParser.Scalar_variableContext,0)


        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = BKOOLParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(BKOOLParser.FOR)
            self.state = 333
            self.scalar_variable()
            self.state = 334
            self.match(BKOOLParser.ASSIGN)
            self.state = 335
            self.expr()
            self.state = 336
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 337
            self.expr()
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 338
                self.stmt()
                pass

            elif la_ == 2:
                self.state = 339
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = BKOOLParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(BKOOLParser.BREAK)
            self.state = 343
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKOOLParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = BKOOLParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(BKOOLParser.CONTINUE)
            self.state = 346
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = BKOOLParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(BKOOLParser.RETURN)
            self.state = 350
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LR) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 349
                self.expr()


            self.state = 352
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invo_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_invo(self):
            return self.getTypedRuleContext(BKOOLParser.Method_invoContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_method_invo_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invo_stmt" ):
                return visitor.visitMethod_invo_stmt(self)
            else:
                return visitor.visitChildren(self)




    def method_invo_stmt(self):

        localctx = BKOOLParser.Method_invo_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_method_invo_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.method_invo()
            self.state = 355
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9_method(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9_methodContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_method_invo

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invo" ):
                return visitor.visitMethod_invo(self)
            else:
                return visitor.visitChildren(self)




    def method_invo(self):

        localctx = BKOOLParser.Method_invoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_method_invo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.exp9_method()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp9_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LR(self):
            return self.getToken(BKOOLParser.LR, 0)

        def exp_list(self):
            return self.getTypedRuleContext(BKOOLParser.Exp_listContext,0)


        def RR(self):
            return self.getToken(BKOOLParser.RR, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp9_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9_method" ):
                return visitor.visitExp9_method(self)
            else:
                return visitor.visitChildren(self)




    def exp9_method(self):

        localctx = BKOOLParser.Exp9_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_exp9_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.exp9(0)
            self.state = 360
            self.match(BKOOLParser.DOT)
            self.state = 361
            self.match(BKOOLParser.ID)
            self.state = 362
            self.match(BKOOLParser.LR)
            self.state = 363
            self.exp_list()
            self.state = 364
            self.match(BKOOLParser.RR)
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

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Exp2Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Exp2Context,i)


        def CONCAT(self):
            return self.getToken(BKOOLParser.CONCAT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expr)
        try:
            self.state = 371
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.exp2()
                self.state = 367
                self.match(BKOOLParser.CONCAT)
                self.state = 368
                self.exp2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.exp2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Exp3Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Exp3Context,i)


        def relational(self):
            return self.getTypedRuleContext(BKOOLParser.RelationalContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)




    def exp2(self):

        localctx = BKOOLParser.Exp2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_exp2)
        try:
            self.state = 378
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.exp3(0)
                self.state = 374
                self.relational()
                self.state = 375
                self.exp3(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.exp3(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQQ(self):
            return self.getToken(BKOOLParser.EQQ, 0)

        def NOTEQ(self):
            return self.getToken(BKOOLParser.NOTEQ, 0)

        def LT(self):
            return self.getToken(BKOOLParser.LT, 0)

        def GT(self):
            return self.getToken(BKOOLParser.GT, 0)

        def LTEQ(self):
            return self.getToken(BKOOLParser.LTEQ, 0)

        def GTEQ(self):
            return self.getToken(BKOOLParser.GTEQ, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_relational

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational" ):
                return visitor.visitRelational(self)
            else:
                return visitor.visitChildren(self)




    def relational(self):

        localctx = BKOOLParser.RelationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.EQQ) | (1 << BKOOLParser.NOTEQ) | (1 << BKOOLParser.LT) | (1 << BKOOLParser.LTEQ) | (1 << BKOOLParser.GT) | (1 << BKOOLParser.GTEQ))) != 0)):
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


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKOOLParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKOOLParser.Exp3Context,0)


        def AND(self):
            return self.getToken(BKOOLParser.AND, 0)

        def OR(self):
            return self.getToken(BKOOLParser.OR, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 393
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 391
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 385
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 386
                        self.match(BKOOLParser.AND)
                        self.state = 387
                        self.exp4(0)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 388
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 389
                        self.match(BKOOLParser.OR)
                        self.state = 390
                        self.exp4(0)
                        pass

             
                self.state = 395
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(BKOOLParser.Exp4Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_exp4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 407
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 405
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 399
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 400
                        self.match(BKOOLParser.ADD)
                        self.state = 401
                        self.exp5(0)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 402
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 403
                        self.match(BKOOLParser.SUB)
                        self.state = 404
                        self.exp5(0)
                        pass

             
                self.state = 409
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(BKOOLParser.Exp6Context,0)


        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def DIV(self):
            return self.getToken(BKOOLParser.DIV, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def IDIV(self):
            return self.getToken(BKOOLParser.IDIV, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)



    def exp5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_exp5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.exp6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 427
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 425
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                        self.state = 413
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 414
                        self.match(BKOOLParser.MUL)
                        self.state = 415
                        self.exp6()
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                        self.state = 416
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 417
                        self.match(BKOOLParser.DIV)
                        self.state = 418
                        self.exp6()
                        pass

                    elif la_ == 3:
                        localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                        self.state = 419
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 420
                        self.match(BKOOLParser.MOD)
                        self.state = 421
                        self.exp6()
                        pass

                    elif la_ == 4:
                        localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                        self.state = 422
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 423
                        self.match(BKOOLParser.IDIV)
                        self.state = 424
                        self.exp6()
                        pass

             
                self.state = 429
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

        def exp6(self):
            return self.getTypedRuleContext(BKOOLParser.Exp6Context,0)


        def exp7(self):
            return self.getTypedRuleContext(BKOOLParser.Exp7Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = BKOOLParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_exp6)
        try:
            self.state = 433
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self.match(BKOOLParser.NOT)
                self.state = 431
                self.exp6()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.LR, BKOOLParser.LB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 432
                self.exp7()
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


    class Exp7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(BKOOLParser.Exp7Context,0)


        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def exp8(self):
            return self.getTypedRuleContext(BKOOLParser.Exp8Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = BKOOLParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_exp7)
        self._la = 0 # Token type
        try:
            self.state = 438
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADD, BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 436
                self.exp7()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.LR, BKOOLParser.LB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.exp8(0)
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


    class Exp8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def exp8(self):
            return self.getTypedRuleContext(BKOOLParser.Exp8Context,0)


        def indexop(self):
            return self.getTypedRuleContext(BKOOLParser.IndexopContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)



    def exp8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.exp9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 447
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                    self.state = 443
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 444
                    self.indexop() 
                self.state = 449
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class IndexopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(BKOOLParser.LS, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RS(self):
            return self.getToken(BKOOLParser.RS, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_indexop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexop" ):
                return visitor.visitIndexop(self)
            else:
                return visitor.visitChildren(self)




    def indexop(self):

        localctx = BKOOLParser.IndexopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_indexop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.match(BKOOLParser.LS)
            self.state = 451
            self.expr()
            self.state = 452
            self.match(BKOOLParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp13(self):
            return self.getTypedRuleContext(BKOOLParser.Exp13Context,0)


        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def tail_part(self):
            return self.getTypedRuleContext(BKOOLParser.Tail_partContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)



    def exp9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_exp9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self.exp13()
            self._ctx.stop = self._input.LT(-1)
            self.state = 462
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                    self.state = 457
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 458
                    self.match(BKOOLParser.DOT)
                    self.state = 459
                    self.tail_part() 
                self.state = 464
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Tail_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LR(self):
            return self.getToken(BKOOLParser.LR, 0)

        def exp_list(self):
            return self.getTypedRuleContext(BKOOLParser.Exp_listContext,0)


        def RR(self):
            return self.getToken(BKOOLParser.RR, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_tail_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTail_part" ):
                return visitor.visitTail_part(self)
            else:
                return visitor.visitChildren(self)




    def tail_part(self):

        localctx = BKOOLParser.Tail_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_tail_part)
        try:
            self.state = 471
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 465
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 466
                self.match(BKOOLParser.ID)
                self.state = 467
                self.match(BKOOLParser.LR)
                self.state = 468
                self.exp_list()
                self.state = 469
                self.match(BKOOLParser.RR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp13Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp13

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp13" ):
                return visitor.visitExp13(self)
            else:
                return visitor.visitChildren(self)




    def exp13(self):

        localctx = BKOOLParser.Exp13Context(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_exp13)
        try:
            self.state = 475
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 473
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.LR, BKOOLParser.LB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 474
                self.exp10()
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


    class Exp10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp10_access(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10_accessContext,0)


        def exp10_call(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10_callContext,0)


        def exp11(self):
            return self.getTypedRuleContext(BKOOLParser.Exp11Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp10" ):
                return visitor.visitExp10(self)
            else:
                return visitor.visitChildren(self)




    def exp10(self):

        localctx = BKOOLParser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_exp10)
        try:
            self.state = 480
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
                self.exp10_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 478
                self.exp10_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 479
                self.exp11()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp10_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp10_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp10_access" ):
                return visitor.visitExp10_access(self)
            else:
                return visitor.visitChildren(self)




    def exp10_access(self):

        localctx = BKOOLParser.Exp10_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_exp10_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.match(BKOOLParser.ID)
            self.state = 483
            self.match(BKOOLParser.DOT)
            self.state = 484
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp10_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def LR(self):
            return self.getToken(BKOOLParser.LR, 0)

        def exp_list(self):
            return self.getTypedRuleContext(BKOOLParser.Exp_listContext,0)


        def RR(self):
            return self.getToken(BKOOLParser.RR, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp10_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp10_call" ):
                return visitor.visitExp10_call(self)
            else:
                return visitor.visitChildren(self)




    def exp10_call(self):

        localctx = BKOOLParser.Exp10_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_exp10_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.match(BKOOLParser.ID)
            self.state = 487
            self.match(BKOOLParser.DOT)
            self.state = 488
            self.match(BKOOLParser.ID)
            self.state = 489
            self.match(BKOOLParser.LR)
            self.state = 490
            self.exp_list()
            self.state = 491
            self.match(BKOOLParser.RR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(BKOOLParser.NEW, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LR(self):
            return self.getToken(BKOOLParser.LR, 0)

        def exp_list(self):
            return self.getTypedRuleContext(BKOOLParser.Exp_listContext,0)


        def RR(self):
            return self.getToken(BKOOLParser.RR, 0)

        def exp12(self):
            return self.getTypedRuleContext(BKOOLParser.Exp12Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp11" ):
                return visitor.visitExp11(self)
            else:
                return visitor.visitChildren(self)




    def exp11(self):

        localctx = BKOOLParser.Exp11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_exp11)
        try:
            self.state = 500
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 493
                self.match(BKOOLParser.NEW)
                self.state = 494
                self.match(BKOOLParser.ID)
                self.state = 495
                self.match(BKOOLParser.LR)
                self.state = 496
                self.exp_list()
                self.state = 497
                self.match(BKOOLParser.RR)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.LR, BKOOLParser.LB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 499
                self.exp12()
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


    class Exp_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exps(self):
            return self.getTypedRuleContext(BKOOLParser.ExpsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_list" ):
                return visitor.visitExp_list(self)
            else:
                return visitor.visitChildren(self)




    def exp_list(self):

        localctx = BKOOLParser.Exp_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_exp_list)
        try:
            self.state = 504
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT, BKOOLParser.LR, BKOOLParser.LB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 502
                self.exps()
                pass
            elif token in [BKOOLParser.RR]:
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


    class ExpsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def exps(self):
            return self.getTypedRuleContext(BKOOLParser.ExpsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exps

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExps" ):
                return visitor.visitExps(self)
            else:
                return visitor.visitChildren(self)




    def exps(self):

        localctx = BKOOLParser.ExpsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_exps)
        try:
            self.state = 511
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 506
                self.expr()
                self.state = 507
                self.match(BKOOLParser.COMMA)
                self.state = 508
                self.exps()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 510
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp12Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(BKOOLParser.LiteralContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LR(self):
            return self.getToken(BKOOLParser.LR, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RR(self):
            return self.getToken(BKOOLParser.RR, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp12

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp12" ):
                return visitor.visitExp12(self)
            else:
                return visitor.visitChildren(self)




    def exp12(self):

        localctx = BKOOLParser.Exp12Context(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_exp12)
        try:
            self.state = 519
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.LB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 513
                self.literal()
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 514
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.LR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 515
                self.match(BKOOLParser.LR)
                self.state = 516
                self.expr()
                self.state = 517
                self.match(BKOOLParser.RR)
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


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = BKOOLParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID))) != 0)):
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


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element_type(self):
            return self.getTypedRuleContext(BKOOLParser.Element_typeContext,0)


        def LS(self):
            return self.getToken(BKOOLParser.LS, 0)

        def RS(self):
            return self.getToken(BKOOLParser.RS, 0)

        def size(self):
            return self.getTypedRuleContext(BKOOLParser.SizeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = BKOOLParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_array_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.element_type()
            self.state = 524
            self.match(BKOOLParser.LS)
            self.state = 526
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.INTLIT:
                self.state = 525
                self.size()


            self.state = 528
            self.match(BKOOLParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def class_type(self):
            return self.getTypedRuleContext(BKOOLParser.Class_typeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_element_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_type" ):
                return visitor.visitElement_type(self)
            else:
                return visitor.visitChildren(self)




    def element_type(self):

        localctx = BKOOLParser.Element_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_element_type)
        try:
            self.state = 535
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 530
                self.match(BKOOLParser.INT)
                pass
            elif token in [BKOOLParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 531
                self.match(BKOOLParser.FLOAT)
                pass
            elif token in [BKOOLParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 532
                self.match(BKOOLParser.BOOLEAN)
                pass
            elif token in [BKOOLParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 533
                self.match(BKOOLParser.STRING)
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 534
                self.class_type()
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


    class SizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_size

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSize" ):
                return visitor.visitSize(self)
            else:
                return visitor.visitChildren(self)




    def size(self):

        localctx = BKOOLParser.SizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 537
            self.match(BKOOLParser.INTLIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_class_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_type" ):
                return visitor.visitClass_type(self)
            else:
                return visitor.visitChildren(self)




    def class_type(self):

        localctx = BKOOLParser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 539
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def boolean_lit(self):
            return self.getTypedRuleContext(BKOOLParser.Boolean_litContext,0)


        def STRING_LIT(self):
            return self.getToken(BKOOLParser.STRING_LIT, 0)

        def indexarr_lit(self):
            return self.getTypedRuleContext(BKOOLParser.Indexarr_litContext,0)


        def NIL(self):
            return self.getToken(BKOOLParser.NIL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BKOOLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_literal)
        try:
            self.state = 547
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 541
                self.match(BKOOLParser.INTLIT)
                pass
            elif token in [BKOOLParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 542
                self.match(BKOOLParser.FLOATLIT)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 543
                self.boolean_lit()
                pass
            elif token in [BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 544
                self.match(BKOOLParser.STRING_LIT)
                pass
            elif token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 545
                self.indexarr_lit()
                pass
            elif token in [BKOOLParser.NIL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 546
                self.match(BKOOLParser.NIL)
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


    class Boolean_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(BKOOLParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKOOLParser.FALSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_boolean_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_lit" ):
                return visitor.visitBoolean_lit(self)
            else:
                return visitor.visitChildren(self)




    def boolean_lit(self):

        localctx = BKOOLParser.Boolean_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_boolean_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TRUE or _la==BKOOLParser.FALSE):
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


    class Arr_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(BKOOLParser.LiteralContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def arr_exp(self):
            return self.getTypedRuleContext(BKOOLParser.Arr_expContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_arr_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_exp" ):
                return visitor.visitArr_exp(self)
            else:
                return visitor.visitChildren(self)




    def arr_exp(self):

        localctx = BKOOLParser.Arr_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_arr_exp)
        try:
            self.state = 556
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 551
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 552
                self.literal()
                self.state = 553
                self.match(BKOOLParser.COMMA)
                self.state = 554
                self.arr_exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Indexarr_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def arr_exp(self):
            return self.getTypedRuleContext(BKOOLParser.Arr_expContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_indexarr_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexarr_lit" ):
                return visitor.visitIndexarr_lit(self)
            else:
                return visitor.visitChildren(self)




    def indexarr_lit(self):

        localctx = BKOOLParser.Indexarr_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_indexarr_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 558
            self.match(BKOOLParser.LB)
            self.state = 559
            self.arr_exp()
            self.state = 560
            self.match(BKOOLParser.RB)
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
        self._predicates[39] = self.exp3_sempred
        self._predicates[40] = self.exp4_sempred
        self._predicates[41] = self.exp5_sempred
        self._predicates[44] = self.exp8_sempred
        self._predicates[46] = self.exp9_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp5_sempred(self, localctx:Exp5Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def exp8_sempred(self, localctx:Exp8Context, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         

    def exp9_sempred(self, localctx:Exp9Context, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         




