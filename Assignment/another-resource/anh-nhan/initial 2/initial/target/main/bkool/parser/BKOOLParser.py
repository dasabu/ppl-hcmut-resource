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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\u0226\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\5\3\u0088\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\5\5\u0094\n\5\3\6\3\6\3\6\3\6\5\6\u009a\n\6\3\7")
        buf.write("\3\7\5\7\u009e\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00a7")
        buf.write("\n\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\5\t\u00b2\n\t")
        buf.write("\3\n\3\n\3\n\3\n\5\n\u00b8\n\n\3\13\3\13\3\13\3\13\5\13")
        buf.write("\u00be\n\13\3\f\5\f\u00c1\n\f\3\f\3\f\3\f\3\f\5\f\u00c7")
        buf.write("\n\f\3\f\3\f\3\f\3\r\5\r\u00cd\n\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\16\5\16\u00d6\n\16\3\16\3\16\3\16\3\16\5\16\u00dc")
        buf.write("\n\16\3\16\3\16\3\16\3\17\3\17\3\17\5\17\u00e4\n\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00ef")
        buf.write("\n\20\3\21\3\21\3\21\3\21\3\21\5\21\u00f6\n\21\3\22\3")
        buf.write("\22\3\22\3\22\3\23\3\23\3\23\3\23\5\23\u0100\n\23\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\5\25\u0108\n\25\3\26\3\26\3")
        buf.write("\26\3\26\5\26\u010e\n\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\5\27\u0119\n\27\3\30\3\30\3\30\3\30\3")
        buf.write("\30\3\31\3\31\3\31\3\31\5\31\u0124\n\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\5\32\u012c\n\32\3\33\3\33\3\33\3\33\3")
        buf.write("\33\5\33\u0133\n\33\3\33\5\33\u0136\n\33\3\34\3\34\3\34")
        buf.write("\5\34\u013b\n\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3")
        buf.write("\35\5\35\u0145\n\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3")
        buf.write(" \5 \u014f\n \3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3$\3$\3$\3$\3$\5$\u0164\n$\3%\3%\3%\3%\3%\5%\u016b")
        buf.write("\n%\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u0178")
        buf.write("\n\'\f\'\16\'\u017b\13\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\7")
        buf.write("(\u0186\n(\f(\16(\u0189\13(\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\3)\7)\u019a\n)\f)\16)\u019d\13)\3*\3")
        buf.write("*\3*\5*\u01a2\n*\3+\3+\3+\5+\u01a7\n+\3,\3,\3,\3,\5,\u01ad")
        buf.write("\n,\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u01b8\n-\3.\3.\3.\3")
        buf.write(".\3.\3.\7.\u01c0\n.\f.\16.\u01c3\13.\3/\3/\3/\3/\3/\3")
        buf.write("/\5/\u01cb\n/\3\60\3\60\5\60\u01cf\n\60\3\61\3\61\3\61")
        buf.write("\5\61\u01d4\n\61\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3")
        buf.write("\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\5\64\u01e8\n\64\3\65\3\65\5\65\u01ec\n\65\3\66\3\66\3")
        buf.write("\66\3\66\3\66\5\66\u01f3\n\66\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\5\67\u01fb\n\67\38\38\39\39\39\59\u0202\n9\39\3")
        buf.write("9\3:\3:\3:\3:\3:\5:\u020b\n:\3;\3;\3<\3<\3=\3=\3=\3=\3")
        buf.write("=\3=\5=\u0217\n=\3>\3>\3?\3?\3?\3?\3?\5?\u0220\n?\3@\3")
        buf.write("@\3@\3@\3@\2\6LNPZA\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjln")
        buf.write("prtvxz|~\2\7\3\2\34\35\4\2\'\')-\3\2\36\37\6\2\6\6\16")
        buf.write("\17\21\21\27\27\3\2\25\26\2\u0235\2\u0080\3\2\2\2\4\u0087")
        buf.write("\3\2\2\2\6\u0089\3\2\2\2\b\u0093\3\2\2\2\n\u0099\3\2\2")
        buf.write("\2\f\u009d\3\2\2\2\16\u00a6\3\2\2\2\20\u00b1\3\2\2\2\22")
        buf.write("\u00b7\3\2\2\2\24\u00bd\3\2\2\2\26\u00c0\3\2\2\2\30\u00cc")
        buf.write("\3\2\2\2\32\u00d5\3\2\2\2\34\u00e0\3\2\2\2\36\u00ee\3")
        buf.write("\2\2\2 \u00f5\3\2\2\2\"\u00f7\3\2\2\2$\u00ff\3\2\2\2&")
        buf.write("\u0101\3\2\2\2(\u0107\3\2\2\2*\u010d\3\2\2\2,\u0118\3")
        buf.write("\2\2\2.\u011a\3\2\2\2\60\u0123\3\2\2\2\62\u012b\3\2\2")
        buf.write("\2\64\u012d\3\2\2\2\66\u0137\3\2\2\28\u013c\3\2\2\2:\u0146")
        buf.write("\3\2\2\2<\u0149\3\2\2\2>\u014c\3\2\2\2@\u0152\3\2\2\2")
        buf.write("B\u0155\3\2\2\2D\u0157\3\2\2\2F\u0163\3\2\2\2H\u016a\3")
        buf.write("\2\2\2J\u016c\3\2\2\2L\u016e\3\2\2\2N\u017c\3\2\2\2P\u018a")
        buf.write("\3\2\2\2R\u01a1\3\2\2\2T\u01a6\3\2\2\2V\u01ac\3\2\2\2")
        buf.write("X\u01b7\3\2\2\2Z\u01b9\3\2\2\2\\\u01ca\3\2\2\2^\u01ce")
        buf.write("\3\2\2\2`\u01d3\3\2\2\2b\u01d5\3\2\2\2d\u01d9\3\2\2\2")
        buf.write("f\u01e7\3\2\2\2h\u01eb\3\2\2\2j\u01f2\3\2\2\2l\u01fa\3")
        buf.write("\2\2\2n\u01fc\3\2\2\2p\u01fe\3\2\2\2r\u020a\3\2\2\2t\u020c")
        buf.write("\3\2\2\2v\u020e\3\2\2\2x\u0216\3\2\2\2z\u0218\3\2\2\2")
        buf.write("|\u021f\3\2\2\2~\u0221\3\2\2\2\u0080\u0081\5\4\3\2\u0081")
        buf.write("\u0082\7\2\2\3\u0082\3\3\2\2\2\u0083\u0084\5\6\4\2\u0084")
        buf.write("\u0085\5\4\3\2\u0085\u0088\3\2\2\2\u0086\u0088\5\6\4\2")
        buf.write("\u0087\u0083\3\2\2\2\u0087\u0086\3\2\2\2\u0088\5\3\2\2")
        buf.write("\2\u0089\u008a\7\b\2\2\u008a\u008b\7>\2\2\u008b\u008c")
        buf.write("\5\b\5\2\u008c\u008d\79\2\2\u008d\u008e\5\n\6\2\u008e")
        buf.write("\u008f\7:\2\2\u008f\7\3\2\2\2\u0090\u0091\7\r\2\2\u0091")
        buf.write("\u0094\7>\2\2\u0092\u0094\3\2\2\2\u0093\u0090\3\2\2\2")
        buf.write("\u0093\u0092\3\2\2\2\u0094\t\3\2\2\2\u0095\u0096\5\f\7")
        buf.write("\2\u0096\u0097\5\n\6\2\u0097\u009a\3\2\2\2\u0098\u009a")
        buf.write("\3\2\2\2\u0099\u0095\3\2\2\2\u0099\u0098\3\2\2\2\u009a")
        buf.write("\13\3\2\2\2\u009b\u009e\5\16\b\2\u009c\u009e\5\24\13\2")
        buf.write("\u009d\u009b\3\2\2\2\u009d\u009c\3\2\2\2\u009e\r\3\2\2")
        buf.write("\2\u009f\u00a0\7\32\2\2\u00a0\u00a7\7\33\2\2\u00a1\u00a2")
        buf.write("\7\33\2\2\u00a2\u00a7\7\32\2\2\u00a3\u00a7\7\33\2\2\u00a4")
        buf.write("\u00a7\7\32\2\2\u00a5\u00a7\3\2\2\2\u00a6\u009f\3\2\2")
        buf.write("\2\u00a6\u00a1\3\2\2\2\u00a6\u00a3\3\2\2\2\u00a6\u00a4")
        buf.write("\3\2\2\2\u00a6\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8")
        buf.write("\u00a9\5\36\20\2\u00a9\u00aa\5\20\t\2\u00aa\u00ab\7\67")
        buf.write("\2\2\u00ab\17\3\2\2\2\u00ac\u00ad\5\22\n\2\u00ad\u00ae")
        buf.write("\7\66\2\2\u00ae\u00af\5\20\t\2\u00af\u00b2\3\2\2\2\u00b0")
        buf.write("\u00b2\5\22\n\2\u00b1\u00ac\3\2\2\2\u00b1\u00b0\3\2\2")
        buf.write("\2\u00b2\21\3\2\2\2\u00b3\u00b8\7>\2\2\u00b4\u00b5\7>")
        buf.write("\2\2\u00b5\u00b6\7(\2\2\u00b6\u00b8\5F$\2\u00b7\u00b3")
        buf.write("\3\2\2\2\u00b7\u00b4\3\2\2\2\u00b8\23\3\2\2\2\u00b9\u00be")
        buf.write("\5\26\f\2\u00ba\u00be\5\34\17\2\u00bb\u00be\5\30\r\2\u00bc")
        buf.write("\u00be\5\32\16\2\u00bd\u00b9\3\2\2\2\u00bd\u00ba\3\2\2")
        buf.write("\2\u00bd\u00bb\3\2\2\2\u00bd\u00bc\3\2\2\2\u00be\25\3")
        buf.write("\2\2\2\u00bf\u00c1\7\33\2\2\u00c0\u00bf\3\2\2\2\u00c0")
        buf.write("\u00c1\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c3\5\36\20")
        buf.write("\2\u00c3\u00c4\7>\2\2\u00c4\u00c6\79\2\2\u00c5\u00c7\5")
        buf.write(" \21\2\u00c6\u00c5\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8")
        buf.write("\3\2\2\2\u00c8\u00c9\7:\2\2\u00c9\u00ca\5&\24\2\u00ca")
        buf.write("\27\3\2\2\2\u00cb\u00cd\7\33\2\2\u00cc\u00cb\3\2\2\2\u00cc")
        buf.write("\u00cd\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cf\7\27\2")
        buf.write("\2\u00cf\u00d0\7\3\2\2\u00d0\u00d1\79\2\2\u00d1\u00d2")
        buf.write("\7:\2\2\u00d2\u00d3\5&\24\2\u00d3\31\3\2\2\2\u00d4\u00d6")
        buf.write("\7\33\2\2\u00d5\u00d4\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6")
        buf.write("\u00d7\3\2\2\2\u00d7\u00d8\7\27\2\2\u00d8\u00d9\7>\2\2")
        buf.write("\u00d9\u00db\79\2\2\u00da\u00dc\5 \21\2\u00db\u00da\3")
        buf.write("\2\2\2\u00db\u00dc\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00de")
        buf.write("\7:\2\2\u00de\u00df\5&\24\2\u00df\33\3\2\2\2\u00e0\u00e1")
        buf.write("\7>\2\2\u00e1\u00e3\79\2\2\u00e2\u00e4\5 \21\2\u00e3\u00e2")
        buf.write("\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5")
        buf.write("\u00e6\7:\2\2\u00e6\u00e7\5&\24\2\u00e7\35\3\2\2\2\u00e8")
        buf.write("\u00ef\7\16\2\2\u00e9\u00ef\7\17\2\2\u00ea\u00ef\7\6\2")
        buf.write("\2\u00eb\u00ef\7\21\2\2\u00ec\u00ef\5p9\2\u00ed\u00ef")
        buf.write("\5v<\2\u00ee\u00e8\3\2\2\2\u00ee\u00e9\3\2\2\2\u00ee\u00ea")
        buf.write("\3\2\2\2\u00ee\u00eb\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ee")
        buf.write("\u00ed\3\2\2\2\u00ef\37\3\2\2\2\u00f0\u00f1\5\"\22\2\u00f1")
        buf.write("\u00f2\7\66\2\2\u00f2\u00f3\5 \21\2\u00f3\u00f6\3\2\2")
        buf.write("\2\u00f4\u00f6\5\"\22\2\u00f5\u00f0\3\2\2\2\u00f5\u00f4")
        buf.write("\3\2\2\2\u00f6!\3\2\2\2\u00f7\u00f8\5$\23\2\u00f8\u00f9")
        buf.write("\78\2\2\u00f9\u00fa\5\36\20\2\u00fa#\3\2\2\2\u00fb\u00fc")
        buf.write("\7>\2\2\u00fc\u00fd\7\66\2\2\u00fd\u0100\5$\23\2\u00fe")
        buf.write("\u0100\7>\2\2\u00ff\u00fb\3\2\2\2\u00ff\u00fe\3\2\2\2")
        buf.write("\u0100%\3\2\2\2\u0101\u0102\79\2\2\u0102\u0103\5(\25\2")
        buf.write("\u0103\u0104\7:\2\2\u0104\'\3\2\2\2\u0105\u0108\5*\26")
        buf.write("\2\u0106\u0108\3\2\2\2\u0107\u0105\3\2\2\2\u0107\u0106")
        buf.write("\3\2\2\2\u0108)\3\2\2\2\u0109\u010a\5,\27\2\u010a\u010b")
        buf.write("\5*\26\2\u010b\u010e\3\2\2\2\u010c\u010e\5,\27\2\u010d")
        buf.write("\u0109\3\2\2\2\u010d\u010c\3\2\2\2\u010e+\3\2\2\2\u010f")
        buf.write("\u0119\5\16\b\2\u0110\u0119\5.\30\2\u0111\u0119\5\64\33")
        buf.write("\2\u0112\u0119\58\35\2\u0113\u0119\5:\36\2\u0114\u0119")
        buf.write("\5<\37\2\u0115\u0119\5> \2\u0116\u0119\5@!\2\u0117\u0119")
        buf.write("\5&\24\2\u0118\u010f\3\2\2\2\u0118\u0110\3\2\2\2\u0118")
        buf.write("\u0111\3\2\2\2\u0118\u0112\3\2\2\2\u0118\u0113\3\2\2\2")
        buf.write("\u0118\u0114\3\2\2\2\u0118\u0115\3\2\2\2\u0118\u0116\3")
        buf.write("\2\2\2\u0118\u0117\3\2\2\2\u0119-\3\2\2\2\u011a\u011b")
        buf.write("\5\60\31\2\u011b\u011c\7\60\2\2\u011c\u011d\5F$\2\u011d")
        buf.write("\u011e\7\67\2\2\u011e/\3\2\2\2\u011f\u0120\5Z.\2\u0120")
        buf.write("\u0121\5X-\2\u0121\u0124\3\2\2\2\u0122\u0124\5\62\32\2")
        buf.write("\u0123\u011f\3\2\2\2\u0123\u0122\3\2\2\2\u0124\61\3\2")
        buf.write("\2\2\u0125\u012c\7>\2\2\u0126\u0127\5Z.\2\u0127\u0128")
        buf.write("\7\65\2\2\u0128\u0129\7>\2\2\u0129\u012c\3\2\2\2\u012a")
        buf.write("\u012c\5b\62\2\u012b\u0125\3\2\2\2\u012b\u0126\3\2\2\2")
        buf.write("\u012b\u012a\3\2\2\2\u012c\63\3\2\2\2\u012d\u012e\7\13")
        buf.write("\2\2\u012e\u012f\5F$\2\u012f\u0132\7\22\2\2\u0130\u0133")
        buf.write("\5,\27\2\u0131\u0133\5&\24\2\u0132\u0130\3\2\2\2\u0132")
        buf.write("\u0131\3\2\2\2\u0133\u0135\3\2\2\2\u0134\u0136\5\66\34")
        buf.write("\2\u0135\u0134\3\2\2\2\u0135\u0136\3\2\2\2\u0136\65\3")
        buf.write("\2\2\2\u0137\u013a\7\f\2\2\u0138\u013b\5,\27\2\u0139\u013b")
        buf.write("\5&\24\2\u013a\u0138\3\2\2\2\u013a\u0139\3\2\2\2\u013b")
        buf.write("\67\3\2\2\2\u013c\u013d\7\23\2\2\u013d\u013e\5\62\32\2")
        buf.write("\u013e\u013f\7\60\2\2\u013f\u0140\5F$\2\u0140\u0141\t")
        buf.write("\2\2\2\u0141\u0144\5F$\2\u0142\u0145\5,\27\2\u0143\u0145")
        buf.write("\5&\24\2\u0144\u0142\3\2\2\2\u0144\u0143\3\2\2\2\u0145")
        buf.write("9\3\2\2\2\u0146\u0147\7\7\2\2\u0147\u0148\7\67\2\2\u0148")
        buf.write(";\3\2\2\2\u0149\u014a\7\t\2\2\u014a\u014b\7\67\2\2\u014b")
        buf.write("=\3\2\2\2\u014c\u014e\7\24\2\2\u014d\u014f\5F$\2\u014e")
        buf.write("\u014d\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0150\3\2\2\2")
        buf.write("\u0150\u0151\7\67\2\2\u0151?\3\2\2\2\u0152\u0153\5B\"")
        buf.write("\2\u0153\u0154\7\67\2\2\u0154A\3\2\2\2\u0155\u0156\5D")
        buf.write("#\2\u0156C\3\2\2\2\u0157\u0158\5Z.\2\u0158\u0159\7\65")
        buf.write("\2\2\u0159\u015a\7>\2\2\u015a\u015b\7\61\2\2\u015b\u015c")
        buf.write("\5h\65\2\u015c\u015d\7\62\2\2\u015dE\3\2\2\2\u015e\u015f")
        buf.write("\5H%\2\u015f\u0160\7.\2\2\u0160\u0161\5H%\2\u0161\u0164")
        buf.write("\3\2\2\2\u0162\u0164\5H%\2\u0163\u015e\3\2\2\2\u0163\u0162")
        buf.write("\3\2\2\2\u0164G\3\2\2\2\u0165\u0166\5L\'\2\u0166\u0167")
        buf.write("\5J&\2\u0167\u0168\5L\'\2\u0168\u016b\3\2\2\2\u0169\u016b")
        buf.write("\5L\'\2\u016a\u0165\3\2\2\2\u016a\u0169\3\2\2\2\u016b")
        buf.write("I\3\2\2\2\u016c\u016d\t\3\2\2\u016dK\3\2\2\2\u016e\u016f")
        buf.write("\b\'\1\2\u016f\u0170\5N(\2\u0170\u0179\3\2\2\2\u0171\u0172")
        buf.write("\f\5\2\2\u0172\u0173\7%\2\2\u0173\u0178\5N(\2\u0174\u0175")
        buf.write("\f\4\2\2\u0175\u0176\7&\2\2\u0176\u0178\5N(\2\u0177\u0171")
        buf.write("\3\2\2\2\u0177\u0174\3\2\2\2\u0178\u017b\3\2\2\2\u0179")
        buf.write("\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017aM\3\2\2\2\u017b")
        buf.write("\u0179\3\2\2\2\u017c\u017d\b(\1\2\u017d\u017e\5P)\2\u017e")
        buf.write("\u0187\3\2\2\2\u017f\u0180\f\5\2\2\u0180\u0181\7\36\2")
        buf.write("\2\u0181\u0186\5P)\2\u0182\u0183\f\4\2\2\u0183\u0184\7")
        buf.write("\37\2\2\u0184\u0186\5P)\2\u0185\u017f\3\2\2\2\u0185\u0182")
        buf.write("\3\2\2\2\u0186\u0189\3\2\2\2\u0187\u0185\3\2\2\2\u0187")
        buf.write("\u0188\3\2\2\2\u0188O\3\2\2\2\u0189\u0187\3\2\2\2\u018a")
        buf.write("\u018b\b)\1\2\u018b\u018c\5R*\2\u018c\u019b\3\2\2\2\u018d")
        buf.write("\u018e\f\7\2\2\u018e\u018f\7 \2\2\u018f\u019a\5R*\2\u0190")
        buf.write("\u0191\f\6\2\2\u0191\u0192\7!\2\2\u0192\u019a\5R*\2\u0193")
        buf.write("\u0194\f\5\2\2\u0194\u0195\7#\2\2\u0195\u019a\5R*\2\u0196")
        buf.write("\u0197\f\4\2\2\u0197\u0198\7\"\2\2\u0198\u019a\5R*\2\u0199")
        buf.write("\u018d\3\2\2\2\u0199\u0190\3\2\2\2\u0199\u0193\3\2\2\2")
        buf.write("\u0199\u0196\3\2\2\2\u019a\u019d\3\2\2\2\u019b\u0199\3")
        buf.write("\2\2\2\u019b\u019c\3\2\2\2\u019cQ\3\2\2\2\u019d\u019b")
        buf.write("\3\2\2\2\u019e\u019f\7$\2\2\u019f\u01a2\5R*\2\u01a0\u01a2")
        buf.write("\5T+\2\u01a1\u019e\3\2\2\2\u01a1\u01a0\3\2\2\2\u01a2S")
        buf.write("\3\2\2\2\u01a3\u01a4\t\4\2\2\u01a4\u01a7\5T+\2\u01a5\u01a7")
        buf.write("\5V,\2\u01a6\u01a3\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7U")
        buf.write("\3\2\2\2\u01a8\u01a9\5Z.\2\u01a9\u01aa\5X-\2\u01aa\u01ad")
        buf.write("\3\2\2\2\u01ab\u01ad\5Z.\2\u01ac\u01a8\3\2\2\2\u01ac\u01ab")
        buf.write("\3\2\2\2\u01adW\3\2\2\2\u01ae\u01af\7\63\2\2\u01af\u01b0")
        buf.write("\5F$\2\u01b0\u01b1\7\64\2\2\u01b1\u01b2\5X-\2\u01b2\u01b8")
        buf.write("\3\2\2\2\u01b3\u01b4\7\63\2\2\u01b4\u01b5\5F$\2\u01b5")
        buf.write("\u01b6\7\64\2\2\u01b6\u01b8\3\2\2\2\u01b7\u01ae\3\2\2")
        buf.write("\2\u01b7\u01b3\3\2\2\2\u01b8Y\3\2\2\2\u01b9\u01ba\b.\1")
        buf.write("\2\u01ba\u01bb\5^\60\2\u01bb\u01c1\3\2\2\2\u01bc\u01bd")
        buf.write("\f\4\2\2\u01bd\u01be\7\65\2\2\u01be\u01c0\5\\/\2\u01bf")
        buf.write("\u01bc\3\2\2\2\u01c0\u01c3\3\2\2\2\u01c1\u01bf\3\2\2\2")
        buf.write("\u01c1\u01c2\3\2\2\2\u01c2[\3\2\2\2\u01c3\u01c1\3\2\2")
        buf.write("\2\u01c4\u01cb\7>\2\2\u01c5\u01c6\7>\2\2\u01c6\u01c7\7")
        buf.write("\61\2\2\u01c7\u01c8\5h\65\2\u01c8\u01c9\7\62\2\2\u01c9")
        buf.write("\u01cb\3\2\2\2\u01ca\u01c4\3\2\2\2\u01ca\u01c5\3\2\2\2")
        buf.write("\u01cb]\3\2\2\2\u01cc\u01cf\7\31\2\2\u01cd\u01cf\5`\61")
        buf.write("\2\u01ce\u01cc\3\2\2\2\u01ce\u01cd\3\2\2\2\u01cf_\3\2")
        buf.write("\2\2\u01d0\u01d4\5b\62\2\u01d1\u01d4\5d\63\2\u01d2\u01d4")
        buf.write("\5f\64\2\u01d3\u01d0\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d3")
        buf.write("\u01d2\3\2\2\2\u01d4a\3\2\2\2\u01d5\u01d6\7>\2\2\u01d6")
        buf.write("\u01d7\7\65\2\2\u01d7\u01d8\7>\2\2\u01d8c\3\2\2\2\u01d9")
        buf.write("\u01da\7>\2\2\u01da\u01db\7\65\2\2\u01db\u01dc\7>\2\2")
        buf.write("\u01dc\u01dd\7\61\2\2\u01dd\u01de\5h\65\2\u01de\u01df")
        buf.write("\7\62\2\2\u01dfe\3\2\2\2\u01e0\u01e1\7\20\2\2\u01e1\u01e2")
        buf.write("\7>\2\2\u01e2\u01e3\7\61\2\2\u01e3\u01e4\5h\65\2\u01e4")
        buf.write("\u01e5\7\62\2\2\u01e5\u01e8\3\2\2\2\u01e6\u01e8\5l\67")
        buf.write("\2\u01e7\u01e0\3\2\2\2\u01e7\u01e6\3\2\2\2\u01e8g\3\2")
        buf.write("\2\2\u01e9\u01ec\5j\66\2\u01ea\u01ec\3\2\2\2\u01eb\u01e9")
        buf.write("\3\2\2\2\u01eb\u01ea\3\2\2\2\u01eci\3\2\2\2\u01ed\u01ee")
        buf.write("\5F$\2\u01ee\u01ef\7\66\2\2\u01ef\u01f0\5j\66\2\u01f0")
        buf.write("\u01f3\3\2\2\2\u01f1\u01f3\5F$\2\u01f2\u01ed\3\2\2\2\u01f2")
        buf.write("\u01f1\3\2\2\2\u01f3k\3\2\2\2\u01f4\u01fb\5x=\2\u01f5")
        buf.write("\u01fb\7>\2\2\u01f6\u01f7\7\61\2\2\u01f7\u01f8\5F$\2\u01f8")
        buf.write("\u01f9\7\62\2\2\u01f9\u01fb\3\2\2\2\u01fa\u01f4\3\2\2")
        buf.write("\2\u01fa\u01f5\3\2\2\2\u01fa\u01f6\3\2\2\2\u01fbm\3\2")
        buf.write("\2\2\u01fc\u01fd\t\5\2\2\u01fdo\3\2\2\2\u01fe\u01ff\5")
        buf.write("r:\2\u01ff\u0201\7\63\2\2\u0200\u0202\5t;\2\u0201\u0200")
        buf.write("\3\2\2\2\u0201\u0202\3\2\2\2\u0202\u0203\3\2\2\2\u0203")
        buf.write("\u0204\7\64\2\2\u0204q\3\2\2\2\u0205\u020b\7\16\2\2\u0206")
        buf.write("\u020b\7\17\2\2\u0207\u020b\7\6\2\2\u0208\u020b\7\21\2")
        buf.write("\2\u0209\u020b\5v<\2\u020a\u0205\3\2\2\2\u020a\u0206\3")
        buf.write("\2\2\2\u020a\u0207\3\2\2\2\u020a\u0208\3\2\2\2\u020a\u0209")
        buf.write("\3\2\2\2\u020bs\3\2\2\2\u020c\u020d\7;\2\2\u020du\3\2")
        buf.write("\2\2\u020e\u020f\7>\2\2\u020fw\3\2\2\2\u0210\u0217\7;")
        buf.write("\2\2\u0211\u0217\7<\2\2\u0212\u0217\5z>\2\u0213\u0217")
        buf.write("\7=\2\2\u0214\u0217\5~@\2\u0215\u0217\7\30\2\2\u0216\u0210")
        buf.write("\3\2\2\2\u0216\u0211\3\2\2\2\u0216\u0212\3\2\2\2\u0216")
        buf.write("\u0213\3\2\2\2\u0216\u0214\3\2\2\2\u0216\u0215\3\2\2\2")
        buf.write("\u0217y\3\2\2\2\u0218\u0219\t\6\2\2\u0219{\3\2\2\2\u021a")
        buf.write("\u0220\5x=\2\u021b\u021c\5x=\2\u021c\u021d\7\66\2\2\u021d")
        buf.write("\u021e\5|?\2\u021e\u0220\3\2\2\2\u021f\u021a\3\2\2\2\u021f")
        buf.write("\u021b\3\2\2\2\u0220}\3\2\2\2\u0221\u0222\79\2\2\u0222")
        buf.write("\u0223\5|?\2\u0223\u0224\7:\2\2\u0224\177\3\2\2\2\65\u0087")
        buf.write("\u0093\u0099\u009d\u00a6\u00b1\u00b7\u00bd\u00c0\u00c6")
        buf.write("\u00cc\u00d5\u00db\u00e3\u00ee\u00f5\u00ff\u0107\u010d")
        buf.write("\u0118\u0123\u012b\u0132\u0135\u013a\u0144\u014e\u0163")
        buf.write("\u016a\u0177\u0179\u0185\u0187\u0199\u019b\u01a1\u01a6")
        buf.write("\u01ac\u01b7\u01c1\u01ca\u01ce\u01d3\u01e7\u01eb\u01f2")
        buf.write("\u01fa\u0201\u020a\u0216\u021f")
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
                     "','", "';'", "':'", "'{'", "'}'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'_'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "WS", "COMMENT", "BOOLEAN", 
                      "BREAK", "CLASS", "CONTINUE", "DO", "IF", "ELSE", 
                      "EXTENDS", "INT", "FLOAT", "NEW", "STRING", "THEN", 
                      "FOR", "RETURN", "TRUE", "FALSE", "VOID", "NIL", "THIS", 
                      "FINAL", "STATIC", "TO", "DOWNTO", "ADD", "SUB", "MUL", 
                      "DIV", "IDIV", "MOD", "NOT", "AND", "OR", "EQQ", "EQ", 
                      "NOTEQ", "LT", "LTEQ", "GT", "GTEQ", "CONCAT", "SCOPE", 
                      "ASSIGN", "LR", "RR", "LS", "RS", "DOT", "COMMA", 
                      "SEMI", "COLON", "LB", "RB", "INTLIT", "FLOATLIT", 
                      "STRING_LIT", "ID", "LETTER", "DIGIT", "UNDERSCORE", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

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
    RULE_assignment_stmt = 22
    RULE_lhs = 23
    RULE_scalar_variable = 24
    RULE_if_stmt = 25
    RULE_else_stmt = 26
    RULE_for_stmt = 27
    RULE_break_stmt = 28
    RULE_continue_stmt = 29
    RULE_return_stmt = 30
    RULE_method_invo_stmt = 31
    RULE_method_invo = 32
    RULE_exp9_method = 33
    RULE_expr = 34
    RULE_exp2 = 35
    RULE_relational = 36
    RULE_exp3 = 37
    RULE_exp4 = 38
    RULE_exp5 = 39
    RULE_exp6 = 40
    RULE_exp7 = 41
    RULE_exp8 = 42
    RULE_indexop = 43
    RULE_exp9 = 44
    RULE_tail_part = 45
    RULE_exp13 = 46
    RULE_exp10 = 47
    RULE_exp10_access = 48
    RULE_exp10_call = 49
    RULE_exp11 = 50
    RULE_exp_list = 51
    RULE_exps = 52
    RULE_exp12 = 53
    RULE_primitive_type = 54
    RULE_array_type = 55
    RULE_element_type = 56
    RULE_size = 57
    RULE_class_type = 58
    RULE_literal = 59
    RULE_boolean_lit = 60
    RULE_arr_exp = 61
    RULE_indexarr_lit = 62

    ruleNames =  [ "program", "decl", "class_decl", "superclass", "memberlist", 
                   "member", "variable_decl", "attribute_list", "attribute", 
                   "method_decl", "normalMethod", "mainMethod", "voidMethod", 
                   "constructor", "type_name", "paramlist", "param", "idlist", 
                   "block_stmt", "block_body", "blocks", "stmt", "assignment_stmt", 
                   "lhs", "scalar_variable", "if_stmt", "else_stmt", "for_stmt", 
                   "break_stmt", "continue_stmt", "return_stmt", "method_invo_stmt", 
                   "method_invo", "exp9_method", "expr", "exp2", "relational", 
                   "exp3", "exp4", "exp5", "exp6", "exp7", "exp8", "indexop", 
                   "exp9", "tail_part", "exp13", "exp10", "exp10_access", 
                   "exp10_call", "exp11", "exp_list", "exps", "exp12", "primitive_type", 
                   "array_type", "element_type", "size", "class_type", "literal", 
                   "boolean_lit", "arr_exp", "indexarr_lit" ]

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
    LETTER=61
    DIGIT=62
    UNDERSCORE=63
    UNCLOSE_STRING=64
    ILLEGAL_ESCAPE=65
    ERROR_TOKEN=66

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
            self.state = 126
            self.decl()
            self.state = 127
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

        def class_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Class_declContext,0)


        def decl(self):
            return self.getTypedRuleContext(BKOOLParser.DeclContext,0)


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
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.class_decl()
                self.state = 130
                self.decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.class_decl()
                pass


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
            self.state = 135
            self.match(BKOOLParser.CLASS)
            self.state = 136
            self.match(BKOOLParser.ID)
            self.state = 137
            self.superclass()
            self.state = 138
            self.match(BKOOLParser.LB)
            self.state = 139
            self.memberlist()
            self.state = 140
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
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.EXTENDS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.match(BKOOLParser.EXTENDS)
                self.state = 143
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
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.INT, BKOOLParser.FLOAT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.FINAL, BKOOLParser.STATIC, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.member()
                self.state = 148
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
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.variable_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
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
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 157
                self.match(BKOOLParser.FINAL)
                self.state = 158
                self.match(BKOOLParser.STATIC)
                pass

            elif la_ == 2:
                self.state = 159
                self.match(BKOOLParser.STATIC)
                self.state = 160
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 3:
                self.state = 161
                self.match(BKOOLParser.STATIC)
                pass

            elif la_ == 4:
                self.state = 162
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 5:
                pass


            self.state = 166
            self.type_name()
            self.state = 167
            self.attribute_list()
            self.state = 168
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
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.attribute()
                self.state = 171
                self.match(BKOOLParser.COMMA)
                self.state = 172
                self.attribute_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
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
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.match(BKOOLParser.ID)
                self.state = 179
                self.match(BKOOLParser.EQ)
                self.state = 180
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
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.normalMethod()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.constructor()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
                self.mainMethod()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 186
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

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

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
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 189
                self.match(BKOOLParser.STATIC)


            self.state = 192
            self.type_name()
            self.state = 193
            self.match(BKOOLParser.ID)
            self.state = 194
            self.match(BKOOLParser.LB)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.ID:
                self.state = 195
                self.paramlist()


            self.state = 198
            self.match(BKOOLParser.RB)
            self.state = 199
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

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 201
                self.match(BKOOLParser.STATIC)


            self.state = 204
            self.match(BKOOLParser.VOID)
            self.state = 205
            self.match(BKOOLParser.T__0)
            self.state = 206
            self.match(BKOOLParser.LB)
            self.state = 207
            self.match(BKOOLParser.RB)
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

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

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
            self.match(BKOOLParser.LB)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.ID:
                self.state = 216
                self.paramlist()


            self.state = 219
            self.match(BKOOLParser.RB)
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

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

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
            self.match(BKOOLParser.LB)
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.ID:
                self.state = 224
                self.paramlist()


            self.state = 227
            self.match(BKOOLParser.RB)
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
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
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


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

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
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.param()
                self.state = 239
                self.match(BKOOLParser.COMMA)
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

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def COLON(self):
            return self.getToken(BKOOLParser.COLON, 0)

        def type_name(self):
            return self.getTypedRuleContext(BKOOLParser.Type_nameContext,0)


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
            self.idlist()
            self.state = 246
            self.match(BKOOLParser.COLON)
            self.state = 247
            self.type_name()
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
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.match(BKOOLParser.ID)
                self.state = 250
                self.match(BKOOLParser.COMMA)
                self.state = 251
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
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
            self.state = 255
            self.match(BKOOLParser.LB)
            self.state = 256
            self.block_body()
            self.state = 257
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
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.BREAK, BKOOLParser.CONTINUE, BKOOLParser.IF, BKOOLParser.INT, BKOOLParser.FLOAT, BKOOLParser.NEW, BKOOLParser.STRING, BKOOLParser.FOR, BKOOLParser.RETURN, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.FINAL, BKOOLParser.STATIC, BKOOLParser.LR, BKOOLParser.LB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
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

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def blocks(self):
            return self.getTypedRuleContext(BKOOLParser.BlocksContext,0)


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
        try:
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.stmt()
                self.state = 264
                self.blocks()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                self.stmt()
                pass


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

        def variable_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Variable_declContext,0)


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
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.variable_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.assignment_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 271
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 272
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 273
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 274
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 275
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 276
                self.method_invo_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 277
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
        self.enterRule(localctx, 44, self.RULE_assignment_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.lhs()
            self.state = 281
            self.match(BKOOLParser.ASSIGN)
            self.state = 282
            self.expr()
            self.state = 283
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

        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def indexop(self):
            return self.getTypedRuleContext(BKOOLParser.IndexopContext,0)


        def scalar_variable(self):
            return self.getTypedRuleContext(BKOOLParser.Scalar_variableContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_lhs)
        try:
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.exp9(0)
                self.state = 286
                self.indexop()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
                self.scalar_variable()
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

        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def exp10_access(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10_accessContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_scalar_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_variable" ):
                return visitor.visitScalar_variable(self)
            else:
                return visitor.visitChildren(self)




    def scalar_variable(self):

        localctx = BKOOLParser.Scalar_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_scalar_variable)
        try:
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 292
                self.exp9(0)
                self.state = 293
                self.match(BKOOLParser.DOT)
                self.state = 294
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 296
                self.exp10_access()
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
        self.enterRule(localctx, 50, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(BKOOLParser.IF)
            self.state = 300
            self.expr()
            self.state = 301
            self.match(BKOOLParser.THEN)
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 302
                self.stmt()
                pass

            elif la_ == 2:
                self.state = 303
                self.block_stmt()
                pass


            self.state = 307
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 306
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
        self.enterRule(localctx, 52, self.RULE_else_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(BKOOLParser.ELSE)
            self.state = 312
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 310
                self.stmt()
                pass

            elif la_ == 2:
                self.state = 311
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
        self.enterRule(localctx, 54, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(BKOOLParser.FOR)
            self.state = 315
            self.scalar_variable()
            self.state = 316
            self.match(BKOOLParser.ASSIGN)
            self.state = 317
            self.expr()
            self.state = 318
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 319
            self.expr()
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 320
                self.stmt()
                pass

            elif la_ == 2:
                self.state = 321
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
        self.enterRule(localctx, 56, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(BKOOLParser.BREAK)
            self.state = 325
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
        self.enterRule(localctx, 58, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(BKOOLParser.CONTINUE)
            self.state = 328
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
        self.enterRule(localctx, 60, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(BKOOLParser.RETURN)
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LR) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 331
                self.expr()


            self.state = 334
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
        self.enterRule(localctx, 62, self.RULE_method_invo_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.method_invo()
            self.state = 337
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
        self.enterRule(localctx, 64, self.RULE_method_invo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
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
        self.enterRule(localctx, 66, self.RULE_exp9_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.exp9(0)
            self.state = 342
            self.match(BKOOLParser.DOT)
            self.state = 343
            self.match(BKOOLParser.ID)
            self.state = 344
            self.match(BKOOLParser.LR)
            self.state = 345
            self.exp_list()
            self.state = 346
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
        self.enterRule(localctx, 68, self.RULE_expr)
        try:
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.exp2()
                self.state = 349
                self.match(BKOOLParser.CONCAT)
                self.state = 350
                self.exp2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
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
        self.enterRule(localctx, 70, self.RULE_exp2)
        try:
            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.exp3(0)
                self.state = 356
                self.relational()
                self.state = 357
                self.exp3(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
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
        self.enterRule(localctx, 72, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
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
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 375
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 373
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 367
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 368
                        self.match(BKOOLParser.AND)
                        self.state = 369
                        self.exp4(0)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 370
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 371
                        self.match(BKOOLParser.OR)
                        self.state = 372
                        self.exp4(0)
                        pass

             
                self.state = 377
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_exp4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 389
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 387
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 381
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 382
                        self.match(BKOOLParser.ADD)
                        self.state = 383
                        self.exp5(0)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 384
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 385
                        self.match(BKOOLParser.SUB)
                        self.state = 386
                        self.exp5(0)
                        pass

             
                self.state = 391
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_exp5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.exp6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 409
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 407
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                        self.state = 395
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 396
                        self.match(BKOOLParser.MUL)
                        self.state = 397
                        self.exp6()
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                        self.state = 398
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 399
                        self.match(BKOOLParser.DIV)
                        self.state = 400
                        self.exp6()
                        pass

                    elif la_ == 3:
                        localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                        self.state = 401
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 402
                        self.match(BKOOLParser.MOD)
                        self.state = 403
                        self.exp6()
                        pass

                    elif la_ == 4:
                        localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                        self.state = 404
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 405
                        self.match(BKOOLParser.IDIV)
                        self.state = 406
                        self.exp6()
                        pass

             
                self.state = 411
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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
        self.enterRule(localctx, 80, self.RULE_exp6)
        try:
            self.state = 415
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.match(BKOOLParser.NOT)
                self.state = 413
                self.exp6()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.LR, BKOOLParser.LB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 414
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
        self.enterRule(localctx, 82, self.RULE_exp7)
        self._la = 0 # Token type
        try:
            self.state = 420
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADD, BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 417
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 418
                self.exp7()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.LR, BKOOLParser.LB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 419
                self.exp8()
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


        def indexop(self):
            return self.getTypedRuleContext(BKOOLParser.IndexopContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = BKOOLParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_exp8)
        try:
            self.state = 426
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.exp9(0)
                self.state = 423
                self.indexop()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 425
                self.exp9(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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

        def indexop(self):
            return self.getTypedRuleContext(BKOOLParser.IndexopContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_indexop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexop" ):
                return visitor.visitIndexop(self)
            else:
                return visitor.visitChildren(self)




    def indexop(self):

        localctx = BKOOLParser.IndexopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_indexop)
        try:
            self.state = 437
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                self.match(BKOOLParser.LS)
                self.state = 429
                self.expr()
                self.state = 430
                self.match(BKOOLParser.RS)
                self.state = 431
                self.indexop()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 433
                self.match(BKOOLParser.LS)
                self.state = 434
                self.expr()
                self.state = 435
                self.match(BKOOLParser.RS)
                pass


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
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_exp9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.exp13()
            self._ctx.stop = self._input.LT(-1)
            self.state = 447
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                    self.state = 442
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 443
                    self.match(BKOOLParser.DOT)
                    self.state = 444
                    self.tail_part() 
                self.state = 449
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
        self.enterRule(localctx, 90, self.RULE_tail_part)
        try:
            self.state = 456
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 450
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 451
                self.match(BKOOLParser.ID)
                self.state = 452
                self.match(BKOOLParser.LR)
                self.state = 453
                self.exp_list()
                self.state = 454
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
        self.enterRule(localctx, 92, self.RULE_exp13)
        try:
            self.state = 460
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 458
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.LR, BKOOLParser.LB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 459
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
        self.enterRule(localctx, 94, self.RULE_exp10)
        try:
            self.state = 465
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.exp10_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
                self.exp10_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 464
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
        self.enterRule(localctx, 96, self.RULE_exp10_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            self.match(BKOOLParser.ID)
            self.state = 468
            self.match(BKOOLParser.DOT)
            self.state = 469
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
        self.enterRule(localctx, 98, self.RULE_exp10_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(BKOOLParser.ID)
            self.state = 472
            self.match(BKOOLParser.DOT)
            self.state = 473
            self.match(BKOOLParser.ID)
            self.state = 474
            self.match(BKOOLParser.LR)
            self.state = 475
            self.exp_list()
            self.state = 476
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
        self.enterRule(localctx, 100, self.RULE_exp11)
        try:
            self.state = 485
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 478
                self.match(BKOOLParser.NEW)
                self.state = 479
                self.match(BKOOLParser.ID)
                self.state = 480
                self.match(BKOOLParser.LR)
                self.state = 481
                self.exp_list()
                self.state = 482
                self.match(BKOOLParser.RR)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.LR, BKOOLParser.LB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 484
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
        self.enterRule(localctx, 102, self.RULE_exp_list)
        try:
            self.state = 489
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT, BKOOLParser.LR, BKOOLParser.LB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 487
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
        self.enterRule(localctx, 104, self.RULE_exps)
        try:
            self.state = 496
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 491
                self.expr()
                self.state = 492
                self.match(BKOOLParser.COMMA)
                self.state = 493
                self.exps()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 495
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
        self.enterRule(localctx, 106, self.RULE_exp12)
        try:
            self.state = 504
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.LB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 498
                self.literal()
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 499
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.LR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 500
                self.match(BKOOLParser.LR)
                self.state = 501
                self.expr()
                self.state = 502
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
        self.enterRule(localctx, 108, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
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
        self.enterRule(localctx, 110, self.RULE_array_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self.element_type()
            self.state = 509
            self.match(BKOOLParser.LS)
            self.state = 511
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.INTLIT:
                self.state = 510
                self.size()


            self.state = 513
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
        self.enterRule(localctx, 112, self.RULE_element_type)
        try:
            self.state = 520
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 515
                self.match(BKOOLParser.INT)
                pass
            elif token in [BKOOLParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 516
                self.match(BKOOLParser.FLOAT)
                pass
            elif token in [BKOOLParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 517
                self.match(BKOOLParser.BOOLEAN)
                pass
            elif token in [BKOOLParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 518
                self.match(BKOOLParser.STRING)
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 519
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
        self.enterRule(localctx, 114, self.RULE_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
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
        self.enterRule(localctx, 116, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
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
        self.enterRule(localctx, 118, self.RULE_literal)
        try:
            self.state = 532
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 526
                self.match(BKOOLParser.INTLIT)
                pass
            elif token in [BKOOLParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 527
                self.match(BKOOLParser.FLOATLIT)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 528
                self.boolean_lit()
                pass
            elif token in [BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 529
                self.match(BKOOLParser.STRING_LIT)
                pass
            elif token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 530
                self.indexarr_lit()
                pass
            elif token in [BKOOLParser.NIL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 531
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
        self.enterRule(localctx, 120, self.RULE_boolean_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
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
        self.enterRule(localctx, 122, self.RULE_arr_exp)
        try:
            self.state = 541
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 536
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 537
                self.literal()
                self.state = 538
                self.match(BKOOLParser.COMMA)
                self.state = 539
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
        self.enterRule(localctx, 124, self.RULE_indexarr_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 543
            self.match(BKOOLParser.LB)
            self.state = 544
            self.arr_exp()
            self.state = 545
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
        self._predicates[37] = self.exp3_sempred
        self._predicates[38] = self.exp4_sempred
        self._predicates[39] = self.exp5_sempred
        self._predicates[44] = self.exp9_sempred
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
         

    def exp9_sempred(self, localctx:Exp9Context, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         




