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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3?")
        buf.write("\u01f9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0084")
        buf.write("\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\5\5\u0090")
        buf.write("\n\5\3\6\3\6\3\6\3\6\5\6\u0096\n\6\3\7\3\7\5\7\u009a\n")
        buf.write("\7\3\b\5\b\u009d\n\b\3\b\5\b\u00a0\n\b\3\b\3\b\3\b\5\b")
        buf.write("\u00a5\n\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\13\3\13\5")
        buf.write("\13\u00b1\n\13\3\13\3\13\3\13\3\13\3\13\5\13\u00b8\n\13")
        buf.write("\5\13\u00ba\n\13\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\5\17\u00c9\n\17\3\20\3\20\3\20\3")
        buf.write("\20\3\20\5\20\u00d0\n\20\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\5\22\u00da\n\22\3\23\3\23\3\23\3\23\3\24\3")
        buf.write("\24\5\24\u00e2\n\24\3\25\3\25\3\25\3\25\5\25\u00e8\n\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u00f3")
        buf.write("\n\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\5\30")
        buf.write("\u00fe\n\30\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u0106\n")
        buf.write("\31\3\32\3\32\3\32\3\32\3\32\5\32\u010d\n\32\3\32\5\32")
        buf.write("\u0110\n\32\3\33\3\33\3\33\5\33\u0115\n\33\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\5\34\u011f\n\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\37\3\37\5\37\u0129\n\37\3\37\3")
        buf.write("\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3")
        buf.write("#\3#\3#\5#\u013e\n#\3$\3$\3$\3$\3$\5$\u0145\n$\3%\3%\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\3&\7&\u0152\n&\f&\16&\u0155\13")
        buf.write("&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u0160\n\'\f")
        buf.write("\'\16\'\u0163\13\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\7(\u0174\n(\f(\16(\u0177\13(\3)\3)\3)\5)\u017c")
        buf.write("\n)\3*\3*\3*\5*\u0181\n*\3+\3+\3+\3+\5+\u0187\n+\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\3,\5,\u0192\n,\3-\3-\3-\3-\3-\3-\7")
        buf.write("-\u019a\n-\f-\16-\u019d\13-\3.\3.\3.\3.\3.\3.\5.\u01a5")
        buf.write("\n.\3/\3/\5/\u01a9\n/\3\60\3\60\3\60\5\60\u01ae\n\60\3")
        buf.write("\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u01c2\n\63\3")
        buf.write("\64\3\64\5\64\u01c6\n\64\3\65\3\65\3\65\3\65\3\65\5\65")
        buf.write("\u01cd\n\65\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u01d5\n")
        buf.write("\66\3\67\3\67\38\38\38\58\u01dc\n8\38\38\39\39\3:\3:\3")
        buf.write(";\3;\3;\3;\3;\3;\5;\u01ea\n;\3<\3<\3=\3=\3=\3=\3=\5=\u01f3")
        buf.write("\n=\3>\3>\3>\3>\3>\2\6JLNX?\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\")
        buf.write("^`bdfhjlnprtvxz\2\b\3\2\33\34\4\2&&(,\3\2\35\36\6\2\5")
        buf.write("\5\r\16\20\20\26\26\5\2\5\5\r\16\20\20\3\2\24\25\2\u01fb")
        buf.write("\2|\3\2\2\2\4\u0083\3\2\2\2\6\u0085\3\2\2\2\b\u008f\3")
        buf.write("\2\2\2\n\u0095\3\2\2\2\f\u0099\3\2\2\2\16\u00a4\3\2\2")
        buf.write("\2\20\u00a9\3\2\2\2\22\u00ab\3\2\2\2\24\u00b9\3\2\2\2")
        buf.write("\26\u00bb\3\2\2\2\30\u00bd\3\2\2\2\32\u00c1\3\2\2\2\34")
        buf.write("\u00c8\3\2\2\2\36\u00cf\3\2\2\2 \u00d1\3\2\2\2\"\u00d9")
        buf.write("\3\2\2\2$\u00db\3\2\2\2&\u00e1\3\2\2\2(\u00e7\3\2\2\2")
        buf.write("*\u00f2\3\2\2\2,\u00f4\3\2\2\2.\u00fd\3\2\2\2\60\u0105")
        buf.write("\3\2\2\2\62\u0107\3\2\2\2\64\u0111\3\2\2\2\66\u0116\3")
        buf.write("\2\2\28\u0120\3\2\2\2:\u0123\3\2\2\2<\u0126\3\2\2\2>\u012c")
        buf.write("\3\2\2\2@\u012f\3\2\2\2B\u0131\3\2\2\2D\u013d\3\2\2\2")
        buf.write("F\u0144\3\2\2\2H\u0146\3\2\2\2J\u0148\3\2\2\2L\u0156\3")
        buf.write("\2\2\2N\u0164\3\2\2\2P\u017b\3\2\2\2R\u0180\3\2\2\2T\u0186")
        buf.write("\3\2\2\2V\u0191\3\2\2\2X\u0193\3\2\2\2Z\u01a4\3\2\2\2")
        buf.write("\\\u01a8\3\2\2\2^\u01ad\3\2\2\2`\u01af\3\2\2\2b\u01b3")
        buf.write("\3\2\2\2d\u01c1\3\2\2\2f\u01c5\3\2\2\2h\u01cc\3\2\2\2")
        buf.write("j\u01d4\3\2\2\2l\u01d6\3\2\2\2n\u01d8\3\2\2\2p\u01df\3")
        buf.write("\2\2\2r\u01e1\3\2\2\2t\u01e9\3\2\2\2v\u01eb\3\2\2\2x\u01f2")
        buf.write("\3\2\2\2z\u01f4\3\2\2\2|}\5\4\3\2}~\7\2\2\3~\3\3\2\2\2")
        buf.write("\177\u0080\5\6\4\2\u0080\u0081\5\4\3\2\u0081\u0084\3\2")
        buf.write("\2\2\u0082\u0084\5\6\4\2\u0083\177\3\2\2\2\u0083\u0082")
        buf.write("\3\2\2\2\u0084\5\3\2\2\2\u0085\u0086\7\7\2\2\u0086\u0087")
        buf.write("\7<\2\2\u0087\u0088\5\b\5\2\u0088\u0089\7\67\2\2\u0089")
        buf.write("\u008a\5\n\6\2\u008a\u008b\78\2\2\u008b\7\3\2\2\2\u008c")
        buf.write("\u008d\7\f\2\2\u008d\u0090\7<\2\2\u008e\u0090\3\2\2\2")
        buf.write("\u008f\u008c\3\2\2\2\u008f\u008e\3\2\2\2\u0090\t\3\2\2")
        buf.write("\2\u0091\u0092\5\f\7\2\u0092\u0093\5\n\6\2\u0093\u0096")
        buf.write("\3\2\2\2\u0094\u0096\3\2\2\2\u0095\u0091\3\2\2\2\u0095")
        buf.write("\u0094\3\2\2\2\u0096\13\3\2\2\2\u0097\u009a\5\16\b\2\u0098")
        buf.write("\u009a\5\32\16\2\u0099\u0097\3\2\2\2\u0099\u0098\3\2\2")
        buf.write("\2\u009a\r\3\2\2\2\u009b\u009d\5\20\t\2\u009c\u009b\3")
        buf.write("\2\2\2\u009c\u009d\3\2\2\2\u009d\u009f\3\2\2\2\u009e\u00a0")
        buf.write("\7\32\2\2\u009f\u009e\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0")
        buf.write("\u00a5\3\2\2\2\u00a1\u00a2\7\32\2\2\u00a2\u00a5\5\20\t")
        buf.write("\2\u00a3\u00a5\3\2\2\2\u00a4\u009c\3\2\2\2\u00a4\u00a1")
        buf.write("\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6")
        buf.write("\u00a7\5\22\n\2\u00a7\u00a8\7\65\2\2\u00a8\17\3\2\2\2")
        buf.write("\u00a9\u00aa\7\31\2\2\u00aa\21\3\2\2\2\u00ab\u00ac\5\24")
        buf.write("\13\2\u00ac\u00ad\7\65\2\2\u00ad\23\3\2\2\2\u00ae\u00b1")
        buf.write("\5\26\f\2\u00af\u00b1\5\30\r\2\u00b0\u00ae\3\2\2\2\u00b0")
        buf.write("\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3\7\64\2")
        buf.write("\2\u00b3\u00b4\5\24\13\2\u00b4\u00ba\3\2\2\2\u00b5\u00b8")
        buf.write("\5\26\f\2\u00b6\u00b8\5\30\r\2\u00b7\u00b5\3\2\2\2\u00b7")
        buf.write("\u00b6\3\2\2\2\u00b8\u00ba\3\2\2\2\u00b9\u00b0\3\2\2\2")
        buf.write("\u00b9\u00b7\3\2\2\2\u00ba\25\3\2\2\2\u00bb\u00bc\5\"")
        buf.write("\22\2\u00bc\27\3\2\2\2\u00bd\u00be\5\"\22\2\u00be\u00bf")
        buf.write("\7\'\2\2\u00bf\u00c0\5D#\2\u00c0\31\3\2\2\2\u00c1\u00c2")
        buf.write("\7\32\2\2\u00c2\u00c3\5\34\17\2\u00c3\u00c4\5\36\20\2")
        buf.write("\u00c4\33\3\2\2\2\u00c5\u00c9\5l\67\2\u00c6\u00c9\5n8")
        buf.write("\2\u00c7\u00c9\5r:\2\u00c8\u00c5\3\2\2\2\u00c8\u00c6\3")
        buf.write("\2\2\2\u00c8\u00c7\3\2\2\2\u00c9\35\3\2\2\2\u00ca\u00cb")
        buf.write("\5 \21\2\u00cb\u00cc\7\64\2\2\u00cc\u00cd\5\36\20\2\u00cd")
        buf.write("\u00d0\3\2\2\2\u00ce\u00d0\5 \21\2\u00cf\u00ca\3\2\2\2")
        buf.write("\u00cf\u00ce\3\2\2\2\u00d0\37\3\2\2\2\u00d1\u00d2\5\"")
        buf.write("\22\2\u00d2\u00d3\7\66\2\2\u00d3\u00d4\5\34\17\2\u00d4")
        buf.write("!\3\2\2\2\u00d5\u00d6\7<\2\2\u00d6\u00d7\7\64\2\2\u00d7")
        buf.write("\u00da\5\"\22\2\u00d8\u00da\7<\2\2\u00d9\u00d5\3\2\2\2")
        buf.write("\u00d9\u00d8\3\2\2\2\u00da#\3\2\2\2\u00db\u00dc\7\67\2")
        buf.write("\2\u00dc\u00dd\5&\24\2\u00dd\u00de\78\2\2\u00de%\3\2\2")
        buf.write("\2\u00df\u00e2\5(\25\2\u00e0\u00e2\3\2\2\2\u00e1\u00df")
        buf.write("\3\2\2\2\u00e1\u00e0\3\2\2\2\u00e2\'\3\2\2\2\u00e3\u00e4")
        buf.write("\5*\26\2\u00e4\u00e5\5(\25\2\u00e5\u00e8\3\2\2\2\u00e6")
        buf.write("\u00e8\5*\26\2\u00e7\u00e3\3\2\2\2\u00e7\u00e6\3\2\2\2")
        buf.write("\u00e8)\3\2\2\2\u00e9\u00f3\5\16\b\2\u00ea\u00f3\5,\27")
        buf.write("\2\u00eb\u00f3\5\62\32\2\u00ec\u00f3\5\66\34\2\u00ed\u00f3")
        buf.write("\58\35\2\u00ee\u00f3\5:\36\2\u00ef\u00f3\5<\37\2\u00f0")
        buf.write("\u00f3\5> \2\u00f1\u00f3\5$\23\2\u00f2\u00e9\3\2\2\2\u00f2")
        buf.write("\u00ea\3\2\2\2\u00f2\u00eb\3\2\2\2\u00f2\u00ec\3\2\2\2")
        buf.write("\u00f2\u00ed\3\2\2\2\u00f2\u00ee\3\2\2\2\u00f2\u00ef\3")
        buf.write("\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f1\3\2\2\2\u00f3+")
        buf.write("\3\2\2\2\u00f4\u00f5\5.\30\2\u00f5\u00f6\7\'\2\2\u00f6")
        buf.write("\u00f7\5D#\2\u00f7\u00f8\7\65\2\2\u00f8-\3\2\2\2\u00f9")
        buf.write("\u00fa\5X-\2\u00fa\u00fb\5V,\2\u00fb\u00fe\3\2\2\2\u00fc")
        buf.write("\u00fe\5\60\31\2\u00fd\u00f9\3\2\2\2\u00fd\u00fc\3\2\2")
        buf.write("\2\u00fe/\3\2\2\2\u00ff\u0106\7<\2\2\u0100\u0101\5X-\2")
        buf.write("\u0101\u0102\7\63\2\2\u0102\u0103\7<\2\2\u0103\u0106\3")
        buf.write("\2\2\2\u0104\u0106\5`\61\2\u0105\u00ff\3\2\2\2\u0105\u0100")
        buf.write("\3\2\2\2\u0105\u0104\3\2\2\2\u0106\61\3\2\2\2\u0107\u0108")
        buf.write("\7\n\2\2\u0108\u0109\5D#\2\u0109\u010c\7\21\2\2\u010a")
        buf.write("\u010d\5*\26\2\u010b\u010d\5$\23\2\u010c\u010a\3\2\2\2")
        buf.write("\u010c\u010b\3\2\2\2\u010d\u010f\3\2\2\2\u010e\u0110\5")
        buf.write("\64\33\2\u010f\u010e\3\2\2\2\u010f\u0110\3\2\2\2\u0110")
        buf.write("\63\3\2\2\2\u0111\u0114\7\13\2\2\u0112\u0115\5*\26\2\u0113")
        buf.write("\u0115\5$\23\2\u0114\u0112\3\2\2\2\u0114\u0113\3\2\2\2")
        buf.write("\u0115\65\3\2\2\2\u0116\u0117\7\22\2\2\u0117\u0118\5\60")
        buf.write("\31\2\u0118\u0119\7\'\2\2\u0119\u011a\5D#\2\u011a\u011b")
        buf.write("\t\2\2\2\u011b\u011e\5D#\2\u011c\u011f\5*\26\2\u011d\u011f")
        buf.write("\5$\23\2\u011e\u011c\3\2\2\2\u011e\u011d\3\2\2\2\u011f")
        buf.write("\67\3\2\2\2\u0120\u0121\7\6\2\2\u0121\u0122\7\65\2\2\u0122")
        buf.write("9\3\2\2\2\u0123\u0124\7\b\2\2\u0124\u0125\7\65\2\2\u0125")
        buf.write(";\3\2\2\2\u0126\u0128\7\23\2\2\u0127\u0129\5D#\2\u0128")
        buf.write("\u0127\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u012a\3\2\2\2")
        buf.write("\u012a\u012b\7\65\2\2\u012b=\3\2\2\2\u012c\u012d\5@!\2")
        buf.write("\u012d\u012e\7\65\2\2\u012e?\3\2\2\2\u012f\u0130\5B\"")
        buf.write("\2\u0130A\3\2\2\2\u0131\u0132\5X-\2\u0132\u0133\7\63\2")
        buf.write("\2\u0133\u0134\7<\2\2\u0134\u0135\7/\2\2\u0135\u0136\5")
        buf.write("f\64\2\u0136\u0137\7\60\2\2\u0137C\3\2\2\2\u0138\u0139")
        buf.write("\5F$\2\u0139\u013a\7-\2\2\u013a\u013b\5F$\2\u013b\u013e")
        buf.write("\3\2\2\2\u013c\u013e\5F$\2\u013d\u0138\3\2\2\2\u013d\u013c")
        buf.write("\3\2\2\2\u013eE\3\2\2\2\u013f\u0140\5J&\2\u0140\u0141")
        buf.write("\5H%\2\u0141\u0142\5J&\2\u0142\u0145\3\2\2\2\u0143\u0145")
        buf.write("\5J&\2\u0144\u013f\3\2\2\2\u0144\u0143\3\2\2\2\u0145G")
        buf.write("\3\2\2\2\u0146\u0147\t\3\2\2\u0147I\3\2\2\2\u0148\u0149")
        buf.write("\b&\1\2\u0149\u014a\5L\'\2\u014a\u0153\3\2\2\2\u014b\u014c")
        buf.write("\f\5\2\2\u014c\u014d\7$\2\2\u014d\u0152\5L\'\2\u014e\u014f")
        buf.write("\f\4\2\2\u014f\u0150\7%\2\2\u0150\u0152\5L\'\2\u0151\u014b")
        buf.write("\3\2\2\2\u0151\u014e\3\2\2\2\u0152\u0155\3\2\2\2\u0153")
        buf.write("\u0151\3\2\2\2\u0153\u0154\3\2\2\2\u0154K\3\2\2\2\u0155")
        buf.write("\u0153\3\2\2\2\u0156\u0157\b\'\1\2\u0157\u0158\5N(\2\u0158")
        buf.write("\u0161\3\2\2\2\u0159\u015a\f\5\2\2\u015a\u015b\7\35\2")
        buf.write("\2\u015b\u0160\5N(\2\u015c\u015d\f\4\2\2\u015d\u015e\7")
        buf.write("\36\2\2\u015e\u0160\5N(\2\u015f\u0159\3\2\2\2\u015f\u015c")
        buf.write("\3\2\2\2\u0160\u0163\3\2\2\2\u0161\u015f\3\2\2\2\u0161")
        buf.write("\u0162\3\2\2\2\u0162M\3\2\2\2\u0163\u0161\3\2\2\2\u0164")
        buf.write("\u0165\b(\1\2\u0165\u0166\5P)\2\u0166\u0175\3\2\2\2\u0167")
        buf.write("\u0168\f\7\2\2\u0168\u0169\7\37\2\2\u0169\u0174\5P)\2")
        buf.write("\u016a\u016b\f\6\2\2\u016b\u016c\7 \2\2\u016c\u0174\5")
        buf.write("P)\2\u016d\u016e\f\5\2\2\u016e\u016f\7\"\2\2\u016f\u0174")
        buf.write("\5P)\2\u0170\u0171\f\4\2\2\u0171\u0172\7!\2\2\u0172\u0174")
        buf.write("\5P)\2\u0173\u0167\3\2\2\2\u0173\u016a\3\2\2\2\u0173\u016d")
        buf.write("\3\2\2\2\u0173\u0170\3\2\2\2\u0174\u0177\3\2\2\2\u0175")
        buf.write("\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176O\3\2\2\2\u0177")
        buf.write("\u0175\3\2\2\2\u0178\u0179\7#\2\2\u0179\u017c\5P)\2\u017a")
        buf.write("\u017c\5R*\2\u017b\u0178\3\2\2\2\u017b\u017a\3\2\2\2\u017c")
        buf.write("Q\3\2\2\2\u017d\u017e\t\4\2\2\u017e\u0181\5R*\2\u017f")
        buf.write("\u0181\5T+\2\u0180\u017d\3\2\2\2\u0180\u017f\3\2\2\2\u0181")
        buf.write("S\3\2\2\2\u0182\u0183\5X-\2\u0183\u0184\5V,\2\u0184\u0187")
        buf.write("\3\2\2\2\u0185\u0187\5X-\2\u0186\u0182\3\2\2\2\u0186\u0185")
        buf.write("\3\2\2\2\u0187U\3\2\2\2\u0188\u0189\7\61\2\2\u0189\u018a")
        buf.write("\5D#\2\u018a\u018b\7\62\2\2\u018b\u018c\5V,\2\u018c\u0192")
        buf.write("\3\2\2\2\u018d\u018e\7\61\2\2\u018e\u018f\5D#\2\u018f")
        buf.write("\u0190\7\62\2\2\u0190\u0192\3\2\2\2\u0191\u0188\3\2\2")
        buf.write("\2\u0191\u018d\3\2\2\2\u0192W\3\2\2\2\u0193\u0194\b-\1")
        buf.write("\2\u0194\u0195\5\\/\2\u0195\u019b\3\2\2\2\u0196\u0197")
        buf.write("\f\4\2\2\u0197\u0198\7\63\2\2\u0198\u019a\5Z.\2\u0199")
        buf.write("\u0196\3\2\2\2\u019a\u019d\3\2\2\2\u019b\u0199\3\2\2\2")
        buf.write("\u019b\u019c\3\2\2\2\u019cY\3\2\2\2\u019d\u019b\3\2\2")
        buf.write("\2\u019e\u01a5\7<\2\2\u019f\u01a0\7<\2\2\u01a0\u01a1\7")
        buf.write("/\2\2\u01a1\u01a2\5f\64\2\u01a2\u01a3\7\60\2\2\u01a3\u01a5")
        buf.write("\3\2\2\2\u01a4\u019e\3\2\2\2\u01a4\u019f\3\2\2\2\u01a5")
        buf.write("[\3\2\2\2\u01a6\u01a9\7\30\2\2\u01a7\u01a9\5^\60\2\u01a8")
        buf.write("\u01a6\3\2\2\2\u01a8\u01a7\3\2\2\2\u01a9]\3\2\2\2\u01aa")
        buf.write("\u01ae\5`\61\2\u01ab\u01ae\5b\62\2\u01ac\u01ae\5d\63\2")
        buf.write("\u01ad\u01aa\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ac\3")
        buf.write("\2\2\2\u01ae_\3\2\2\2\u01af\u01b0\7<\2\2\u01b0\u01b1\7")
        buf.write("\63\2\2\u01b1\u01b2\7<\2\2\u01b2a\3\2\2\2\u01b3\u01b4")
        buf.write("\7<\2\2\u01b4\u01b5\7\63\2\2\u01b5\u01b6\7<\2\2\u01b6")
        buf.write("\u01b7\7/\2\2\u01b7\u01b8\5f\64\2\u01b8\u01b9\7\60\2\2")
        buf.write("\u01b9c\3\2\2\2\u01ba\u01bb\7\17\2\2\u01bb\u01bc\7<\2")
        buf.write("\2\u01bc\u01bd\7/\2\2\u01bd\u01be\5f\64\2\u01be\u01bf")
        buf.write("\7\60\2\2\u01bf\u01c2\3\2\2\2\u01c0\u01c2\5j\66\2\u01c1")
        buf.write("\u01ba\3\2\2\2\u01c1\u01c0\3\2\2\2\u01c2e\3\2\2\2\u01c3")
        buf.write("\u01c6\5h\65\2\u01c4\u01c6\3\2\2\2\u01c5\u01c3\3\2\2\2")
        buf.write("\u01c5\u01c4\3\2\2\2\u01c6g\3\2\2\2\u01c7\u01c8\5D#\2")
        buf.write("\u01c8\u01c9\7\64\2\2\u01c9\u01ca\5h\65\2\u01ca\u01cd")
        buf.write("\3\2\2\2\u01cb\u01cd\5D#\2\u01cc\u01c7\3\2\2\2\u01cc\u01cb")
        buf.write("\3\2\2\2\u01cdi\3\2\2\2\u01ce\u01d5\5t;\2\u01cf\u01d5")
        buf.write("\7<\2\2\u01d0\u01d1\7/\2\2\u01d1\u01d2\5D#\2\u01d2\u01d3")
        buf.write("\7\60\2\2\u01d3\u01d5\3\2\2\2\u01d4\u01ce\3\2\2\2\u01d4")
        buf.write("\u01cf\3\2\2\2\u01d4\u01d0\3\2\2\2\u01d5k\3\2\2\2\u01d6")
        buf.write("\u01d7\t\5\2\2\u01d7m\3\2\2\2\u01d8\u01d9\t\6\2\2\u01d9")
        buf.write("\u01db\7\61\2\2\u01da\u01dc\5p9\2\u01db\u01da\3\2\2\2")
        buf.write("\u01db\u01dc\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01de\7")
        buf.write("\62\2\2\u01deo\3\2\2\2\u01df\u01e0\79\2\2\u01e0q\3\2\2")
        buf.write("\2\u01e1\u01e2\7<\2\2\u01e2s\3\2\2\2\u01e3\u01ea\79\2")
        buf.write("\2\u01e4\u01ea\7:\2\2\u01e5\u01ea\5v<\2\u01e6\u01ea\7")
        buf.write(";\2\2\u01e7\u01ea\5z>\2\u01e8\u01ea\7\27\2\2\u01e9\u01e3")
        buf.write("\3\2\2\2\u01e9\u01e4\3\2\2\2\u01e9\u01e5\3\2\2\2\u01e9")
        buf.write("\u01e6\3\2\2\2\u01e9\u01e7\3\2\2\2\u01e9\u01e8\3\2\2\2")
        buf.write("\u01eau\3\2\2\2\u01eb\u01ec\t\7\2\2\u01ecw\3\2\2\2\u01ed")
        buf.write("\u01f3\5t;\2\u01ee\u01ef\5t;\2\u01ef\u01f0\7\64\2\2\u01f0")
        buf.write("\u01f1\5x=\2\u01f1\u01f3\3\2\2\2\u01f2\u01ed\3\2\2\2\u01f2")
        buf.write("\u01ee\3\2\2\2\u01f3y\3\2\2\2\u01f4\u01f5\7\67\2\2\u01f5")
        buf.write("\u01f6\5x=\2\u01f6\u01f7\78\2\2\u01f7{\3\2\2\2\60\u0083")
        buf.write("\u008f\u0095\u0099\u009c\u009f\u00a4\u00b0\u00b7\u00b9")
        buf.write("\u00c8\u00cf\u00d9\u00e1\u00e7\u00f2\u00fd\u0105\u010c")
        buf.write("\u010f\u0114\u011e\u0128\u013d\u0144\u0151\u0153\u015f")
        buf.write("\u0161\u0173\u0175\u017b\u0180\u0186\u0191\u019b\u01a4")
        buf.write("\u01a8\u01ad\u01c1\u01c5\u01cc\u01d4\u01db\u01e9\u01f2")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'boolean'", 
                     "'break'", "'class'", "'continue'", "'do'", "'if'", 
                     "'else'", "'extends'", "'int'", "'float'", "'new'", 
                     "'string'", "'then'", "'for'", "'return'", "'true'", 
                     "'false'", "'void'", "'nil'", "'this'", "'final'", 
                     "'static'", "'to'", "'downto'", "'+'", "'-'", "'*'", 
                     "'/'", "'\\'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
                     "'='", "'!='", "'<'", "'<='", "'>'", "'>='", "'^'", 
                     "'::'", "'('", "')'", "'['", "']'", "'.'", "','", "';'", 
                     "':'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "WS", "COMMENT", "BOOLEAN", "BREAK", 
                      "CLASS", "CONTINUE", "DO", "IF", "ELSE", "EXTENDS", 
                      "INT", "FLOAT", "NEW", "STRING", "THEN", "FOR", "RETURN", 
                      "TRUE", "FALSE", "VOID", "NIL", "THIS", "FINAL", "STATIC", 
                      "TO", "DOWNTO", "ADD", "SUB", "MUL", "DIV", "IDIV", 
                      "MOD", "NOT", "AND", "OR", "EQQ", "EQ", "NOTEQ", "LT", 
                      "LTEQ", "GT", "GTEQ", "CONCAT", "SCOPE", "LR", "RR", 
                      "LS", "RS", "DOT", "COMMA", "SEMI", "COLON", "LB", 
                      "RB", "INTLIT", "FLOATLIT", "STRING_LIT", "ID", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_class_decl = 2
    RULE_superclass = 3
    RULE_memberlist = 4
    RULE_member = 5
    RULE_variable_decl = 6
    RULE_mutable = 7
    RULE_attribute_decl = 8
    RULE_attribute_list = 9
    RULE_not_initial = 10
    RULE_initial = 11
    RULE_method_decl = 12
    RULE_type_name = 13
    RULE_paramlist = 14
    RULE_param = 15
    RULE_idlist = 16
    RULE_block_stmt = 17
    RULE_block_body = 18
    RULE_blocks = 19
    RULE_stmt = 20
    RULE_assignment_stmt = 21
    RULE_lhs = 22
    RULE_scalar_variable = 23
    RULE_if_stmt = 24
    RULE_else_stmt = 25
    RULE_for_stmt = 26
    RULE_break_stmt = 27
    RULE_continue_stmt = 28
    RULE_return_stmt = 29
    RULE_method_invo_stmt = 30
    RULE_method_invo = 31
    RULE_exp9_method = 32
    RULE_expr = 33
    RULE_exp2 = 34
    RULE_relational = 35
    RULE_exp3 = 36
    RULE_exp4 = 37
    RULE_exp5 = 38
    RULE_exp6 = 39
    RULE_exp7 = 40
    RULE_exp8 = 41
    RULE_indexop = 42
    RULE_exp9 = 43
    RULE_tail_part = 44
    RULE_exp13 = 45
    RULE_exp10 = 46
    RULE_exp10_access = 47
    RULE_exp10_call = 48
    RULE_exp11 = 49
    RULE_exp_list = 50
    RULE_exps = 51
    RULE_exp12 = 52
    RULE_primitive_type = 53
    RULE_array_type = 54
    RULE_size = 55
    RULE_class_type = 56
    RULE_literal = 57
    RULE_boolean_lit = 58
    RULE_arr_exp = 59
    RULE_indexarr_lit = 60

    ruleNames =  [ "program", "decl", "class_decl", "superclass", "memberlist", 
                   "member", "variable_decl", "mutable", "attribute_decl", 
                   "attribute_list", "not_initial", "initial", "method_decl", 
                   "type_name", "paramlist", "param", "idlist", "block_stmt", 
                   "block_body", "blocks", "stmt", "assignment_stmt", "lhs", 
                   "scalar_variable", "if_stmt", "else_stmt", "for_stmt", 
                   "break_stmt", "continue_stmt", "return_stmt", "method_invo_stmt", 
                   "method_invo", "exp9_method", "expr", "exp2", "relational", 
                   "exp3", "exp4", "exp5", "exp6", "exp7", "exp8", "indexop", 
                   "exp9", "tail_part", "exp13", "exp10", "exp10_access", 
                   "exp10_call", "exp11", "exp_list", "exps", "exp12", "primitive_type", 
                   "array_type", "size", "class_type", "literal", "boolean_lit", 
                   "arr_exp", "indexarr_lit" ]

    EOF = Token.EOF
    WS=1
    COMMENT=2
    BOOLEAN=3
    BREAK=4
    CLASS=5
    CONTINUE=6
    DO=7
    IF=8
    ELSE=9
    EXTENDS=10
    INT=11
    FLOAT=12
    NEW=13
    STRING=14
    THEN=15
    FOR=16
    RETURN=17
    TRUE=18
    FALSE=19
    VOID=20
    NIL=21
    THIS=22
    FINAL=23
    STATIC=24
    TO=25
    DOWNTO=26
    ADD=27
    SUB=28
    MUL=29
    DIV=30
    IDIV=31
    MOD=32
    NOT=33
    AND=34
    OR=35
    EQQ=36
    EQ=37
    NOTEQ=38
    LT=39
    LTEQ=40
    GT=41
    GTEQ=42
    CONCAT=43
    SCOPE=44
    LR=45
    RR=46
    LS=47
    RS=48
    DOT=49
    COMMA=50
    SEMI=51
    COLON=52
    LB=53
    RB=54
    INTLIT=55
    FLOATLIT=56
    STRING_LIT=57
    ID=58
    UNCLOSE_STRING=59
    ILLEGAL_ESCAPE=60
    ERROR_TOKEN=61

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
            self.state = 122
            self.decl()
            self.state = 123
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
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.class_decl()
                self.state = 126
                self.decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
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
            self.state = 131
            self.match(BKOOLParser.CLASS)
            self.state = 132
            self.match(BKOOLParser.ID)
            self.state = 133
            self.superclass()
            self.state = 134
            self.match(BKOOLParser.LB)
            self.state = 135
            self.memberlist()
            self.state = 136
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
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.EXTENDS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.match(BKOOLParser.EXTENDS)
                self.state = 139
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
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.FINAL, BKOOLParser.STATIC, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.member()
                self.state = 144
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
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.variable_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
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

        def attribute_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Attribute_declContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def mutable(self):
            return self.getTypedRuleContext(BKOOLParser.MutableContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.FINAL:
                    self.state = 153
                    self.mutable()


                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.STATIC:
                    self.state = 156
                    self.match(BKOOLParser.STATIC)


                pass

            elif la_ == 2:
                self.state = 159
                self.match(BKOOLParser.STATIC)
                self.state = 160
                self.mutable()
                pass

            elif la_ == 3:
                pass


            self.state = 164
            self.attribute_decl()
            self.state = 165
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MutableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_mutable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMutable" ):
                return visitor.visitMutable(self)
            else:
                return visitor.visitChildren(self)




    def mutable(self):

        localctx = BKOOLParser.MutableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_mutable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(BKOOLParser.FINAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_list(self):
            return self.getTypedRuleContext(BKOOLParser.Attribute_listContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_attribute_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_decl" ):
                return visitor.visitAttribute_decl(self)
            else:
                return visitor.visitChildren(self)




    def attribute_decl(self):

        localctx = BKOOLParser.Attribute_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attribute_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.attribute_list()
            self.state = 170
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

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def attribute_list(self):
            return self.getTypedRuleContext(BKOOLParser.Attribute_listContext,0)


        def not_initial(self):
            return self.getTypedRuleContext(BKOOLParser.Not_initialContext,0)


        def initial(self):
            return self.getTypedRuleContext(BKOOLParser.InitialContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attribute_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_list" ):
                return visitor.visitAttribute_list(self)
            else:
                return visitor.visitChildren(self)




    def attribute_list(self):

        localctx = BKOOLParser.Attribute_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attribute_list)
        try:
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 172
                    self.not_initial()
                    pass

                elif la_ == 2:
                    self.state = 173
                    self.initial()
                    pass


                self.state = 176
                self.match(BKOOLParser.COMMA)
                self.state = 177
                self.attribute_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 179
                    self.not_initial()
                    pass

                elif la_ == 2:
                    self.state = 180
                    self.initial()
                    pass


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Not_initialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_not_initial

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot_initial" ):
                return visitor.visitNot_initial(self)
            else:
                return visitor.visitChildren(self)




    def not_initial(self):

        localctx = BKOOLParser.Not_initialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_not_initial)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.idlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def EQ(self):
            return self.getToken(BKOOLParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_initial

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitial" ):
                return visitor.visitInitial(self)
            else:
                return visitor.visitChildren(self)




    def initial(self):

        localctx = BKOOLParser.InitialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_initial)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.idlist()
            self.state = 188
            self.match(BKOOLParser.EQ)
            self.state = 189
            self.expr()
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

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def type_name(self):
            return self.getTypedRuleContext(BKOOLParser.Type_nameContext,0)


        def paramlist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = BKOOLParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_method_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(BKOOLParser.STATIC)
            self.state = 192
            self.type_name()
            self.state = 193
            self.paramlist()
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

        def primitive_type(self):
            return self.getTypedRuleContext(BKOOLParser.Primitive_typeContext,0)


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
        self.enterRule(localctx, 26, self.RULE_type_name)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.primitive_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.array_type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 197
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
        self.enterRule(localctx, 28, self.RULE_paramlist)
        try:
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.param()
                self.state = 201
                self.match(BKOOLParser.COMMA)
                self.state = 202
                self.paramlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
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
        self.enterRule(localctx, 30, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.idlist()
            self.state = 208
            self.match(BKOOLParser.COLON)
            self.state = 209
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
        self.enterRule(localctx, 32, self.RULE_idlist)
        try:
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.match(BKOOLParser.ID)
                self.state = 212
                self.match(BKOOLParser.COMMA)
                self.state = 213
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
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
        self.enterRule(localctx, 34, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(BKOOLParser.LB)
            self.state = 218
            self.block_body()
            self.state = 219
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
        self.enterRule(localctx, 36, self.RULE_block_body)
        try:
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BREAK, BKOOLParser.CONTINUE, BKOOLParser.IF, BKOOLParser.NEW, BKOOLParser.FOR, BKOOLParser.RETURN, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.FINAL, BKOOLParser.STATIC, BKOOLParser.LR, BKOOLParser.LB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
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
        self.enterRule(localctx, 38, self.RULE_blocks)
        try:
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.stmt()
                self.state = 226
                self.blocks()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
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
        self.enterRule(localctx, 40, self.RULE_stmt)
        try:
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.variable_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.assignment_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 233
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 234
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 235
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 236
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 237
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 238
                self.method_invo_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 239
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


        def EQ(self):
            return self.getToken(BKOOLParser.EQ, 0)

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
        self.enterRule(localctx, 42, self.RULE_assignment_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.lhs()
            self.state = 243
            self.match(BKOOLParser.EQ)
            self.state = 244
            self.expr()
            self.state = 245
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
        self.enterRule(localctx, 44, self.RULE_lhs)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.exp9(0)
                self.state = 248
                self.indexop()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
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
        self.enterRule(localctx, 46, self.RULE_scalar_variable)
        try:
            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.exp9(0)
                self.state = 255
                self.match(BKOOLParser.DOT)
                self.state = 256
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 258
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
        self.enterRule(localctx, 48, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(BKOOLParser.IF)
            self.state = 262
            self.expr()
            self.state = 263
            self.match(BKOOLParser.THEN)
            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 264
                self.stmt()
                pass

            elif la_ == 2:
                self.state = 265
                self.block_stmt()
                pass


            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 268
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
        self.enterRule(localctx, 50, self.RULE_else_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(BKOOLParser.ELSE)
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 272
                self.stmt()
                pass

            elif la_ == 2:
                self.state = 273
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


        def EQ(self):
            return self.getToken(BKOOLParser.EQ, 0)

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
        self.enterRule(localctx, 52, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(BKOOLParser.FOR)
            self.state = 277
            self.scalar_variable()
            self.state = 278
            self.match(BKOOLParser.EQ)
            self.state = 279
            self.expr()
            self.state = 280
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 281
            self.expr()
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 282
                self.stmt()
                pass

            elif la_ == 2:
                self.state = 283
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
        self.enterRule(localctx, 54, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(BKOOLParser.BREAK)
            self.state = 287
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
        self.enterRule(localctx, 56, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(BKOOLParser.CONTINUE)
            self.state = 290
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
        self.enterRule(localctx, 58, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(BKOOLParser.RETURN)
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LR) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 293
                self.expr()


            self.state = 296
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
        self.enterRule(localctx, 60, self.RULE_method_invo_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.method_invo()
            self.state = 299
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
        self.enterRule(localctx, 62, self.RULE_method_invo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
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
        self.enterRule(localctx, 64, self.RULE_exp9_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.exp9(0)
            self.state = 304
            self.match(BKOOLParser.DOT)
            self.state = 305
            self.match(BKOOLParser.ID)
            self.state = 306
            self.match(BKOOLParser.LR)
            self.state = 307
            self.exp_list()
            self.state = 308
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
        self.enterRule(localctx, 66, self.RULE_expr)
        try:
            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.exp2()
                self.state = 311
                self.match(BKOOLParser.CONCAT)
                self.state = 312
                self.exp2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 314
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
        self.enterRule(localctx, 68, self.RULE_exp2)
        try:
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.exp3(0)
                self.state = 318
                self.relational()
                self.state = 319
                self.exp3(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
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
        self.enterRule(localctx, 70, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
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
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 337
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 335
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 329
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 330
                        self.match(BKOOLParser.AND)
                        self.state = 331
                        self.exp4(0)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 332
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 333
                        self.match(BKOOLParser.OR)
                        self.state = 334
                        self.exp4(0)
                        pass

             
                self.state = 339
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_exp4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 351
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 349
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 343
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 344
                        self.match(BKOOLParser.ADD)
                        self.state = 345
                        self.exp5(0)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 346
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 347
                        self.match(BKOOLParser.SUB)
                        self.state = 348
                        self.exp5(0)
                        pass

             
                self.state = 353
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_exp5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.exp6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 371
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 369
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                        self.state = 357
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 358
                        self.match(BKOOLParser.MUL)
                        self.state = 359
                        self.exp6()
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                        self.state = 360
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 361
                        self.match(BKOOLParser.DIV)
                        self.state = 362
                        self.exp6()
                        pass

                    elif la_ == 3:
                        localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                        self.state = 363
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 364
                        self.match(BKOOLParser.MOD)
                        self.state = 365
                        self.exp6()
                        pass

                    elif la_ == 4:
                        localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                        self.state = 366
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 367
                        self.match(BKOOLParser.IDIV)
                        self.state = 368
                        self.exp6()
                        pass

             
                self.state = 373
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
        self.enterRule(localctx, 78, self.RULE_exp6)
        try:
            self.state = 377
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.match(BKOOLParser.NOT)
                self.state = 375
                self.exp6()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.LR, BKOOLParser.LB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 376
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
        self.enterRule(localctx, 80, self.RULE_exp7)
        self._la = 0 # Token type
        try:
            self.state = 382
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADD, BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 380
                self.exp7()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.LR, BKOOLParser.LB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
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
        self.enterRule(localctx, 82, self.RULE_exp8)
        try:
            self.state = 388
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.exp9(0)
                self.state = 385
                self.indexop()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 387
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
        self.enterRule(localctx, 84, self.RULE_indexop)
        try:
            self.state = 399
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.match(BKOOLParser.LS)
                self.state = 391
                self.expr()
                self.state = 392
                self.match(BKOOLParser.RS)
                self.state = 393
                self.indexop()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.match(BKOOLParser.LS)
                self.state = 396
                self.expr()
                self.state = 397
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
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_exp9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.exp13()
            self._ctx.stop = self._input.LT(-1)
            self.state = 409
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                    self.state = 404
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 405
                    self.match(BKOOLParser.DOT)
                    self.state = 406
                    self.tail_part() 
                self.state = 411
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

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
        self.enterRule(localctx, 88, self.RULE_tail_part)
        try:
            self.state = 418
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.match(BKOOLParser.ID)
                self.state = 414
                self.match(BKOOLParser.LR)
                self.state = 415
                self.exp_list()
                self.state = 416
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
        self.enterRule(localctx, 90, self.RULE_exp13)
        try:
            self.state = 422
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 420
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.LR, BKOOLParser.LB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 421
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
        self.enterRule(localctx, 92, self.RULE_exp10)
        try:
            self.state = 427
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.exp10_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 425
                self.exp10_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 426
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
        self.enterRule(localctx, 94, self.RULE_exp10_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(BKOOLParser.ID)
            self.state = 430
            self.match(BKOOLParser.DOT)
            self.state = 431
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
        self.enterRule(localctx, 96, self.RULE_exp10_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.match(BKOOLParser.ID)
            self.state = 434
            self.match(BKOOLParser.DOT)
            self.state = 435
            self.match(BKOOLParser.ID)
            self.state = 436
            self.match(BKOOLParser.LR)
            self.state = 437
            self.exp_list()
            self.state = 438
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
        self.enterRule(localctx, 98, self.RULE_exp11)
        try:
            self.state = 447
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                self.match(BKOOLParser.NEW)
                self.state = 441
                self.match(BKOOLParser.ID)
                self.state = 442
                self.match(BKOOLParser.LR)
                self.state = 443
                self.exp_list()
                self.state = 444
                self.match(BKOOLParser.RR)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.LR, BKOOLParser.LB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 446
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
        self.enterRule(localctx, 100, self.RULE_exp_list)
        try:
            self.state = 451
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT, BKOOLParser.LR, BKOOLParser.LB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 449
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
        self.enterRule(localctx, 102, self.RULE_exps)
        try:
            self.state = 458
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 453
                self.expr()
                self.state = 454
                self.match(BKOOLParser.COMMA)
                self.state = 455
                self.exps()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 457
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
        self.enterRule(localctx, 104, self.RULE_exp12)
        try:
            self.state = 466
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.LB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 460
                self.literal()
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 461
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.LR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 462
                self.match(BKOOLParser.LR)
                self.state = 463
                self.expr()
                self.state = 464
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
        self.enterRule(localctx, 106, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
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

        def LS(self):
            return self.getToken(BKOOLParser.LS, 0)

        def RS(self):
            return self.getToken(BKOOLParser.RS, 0)

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

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
        self.enterRule(localctx, 108, self.RULE_array_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 471
            self.match(BKOOLParser.LS)
            self.state = 473
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.INTLIT:
                self.state = 472
                self.size()


            self.state = 475
            self.match(BKOOLParser.RS)
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
        self.enterRule(localctx, 110, self.RULE_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
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
        self.enterRule(localctx, 112, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
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
        self.enterRule(localctx, 114, self.RULE_literal)
        try:
            self.state = 487
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 481
                self.match(BKOOLParser.INTLIT)
                pass
            elif token in [BKOOLParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 482
                self.match(BKOOLParser.FLOATLIT)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 483
                self.boolean_lit()
                pass
            elif token in [BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 484
                self.match(BKOOLParser.STRING_LIT)
                pass
            elif token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 485
                self.indexarr_lit()
                pass
            elif token in [BKOOLParser.NIL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 486
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
        self.enterRule(localctx, 116, self.RULE_boolean_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
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
        self.enterRule(localctx, 118, self.RULE_arr_exp)
        try:
            self.state = 496
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 491
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 492
                self.literal()
                self.state = 493
                self.match(BKOOLParser.COMMA)
                self.state = 494
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
        self.enterRule(localctx, 120, self.RULE_indexarr_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.match(BKOOLParser.LB)
            self.state = 499
            self.arr_exp()
            self.state = 500
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
        self._predicates[36] = self.exp3_sempred
        self._predicates[37] = self.exp4_sempred
        self._predicates[38] = self.exp5_sempred
        self._predicates[43] = self.exp9_sempred
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
         




