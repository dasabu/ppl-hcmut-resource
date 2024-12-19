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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u01b7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5")
        buf.write("\3j\n\3\3\4\3\4\3\4\3\4\5\4p\n\4\3\4\3\4\3\5\3\5\5\5v")
        buf.write("\n\5\3\5\3\5\3\6\6\6{\n\6\r\6\16\6|\3\7\3\7\5\7\u0081")
        buf.write("\n\7\3\b\5\b\u0084\n\b\3\b\5\b\u0087\n\b\3\b\3\b\3\b\5")
        buf.write("\b\u008c\n\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\5\t\u0096")
        buf.write("\n\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\5\13\u009f\n\13\3")
        buf.write("\f\3\f\7\f\u00a3\n\f\f\f\16\f\u00a6\13\f\3\f\7\f\u00a9")
        buf.write("\n\f\f\f\16\f\u00ac\13\f\3\f\3\f\3\r\5\r\u00b1\n\r\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00bd")
        buf.write("\n\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\5\17")
        buf.write("\u00c8\n\17\3\20\3\20\3\20\5\20\u00cd\n\20\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\5\21\u00e1\n\21\3\22\3\22\3")
        buf.write("\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u00f9")
        buf.write("\n\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u010e")
        buf.write("\n\31\3\32\3\32\3\32\3\32\3\32\5\32\u0115\n\32\3\33\3")
        buf.write("\33\3\33\3\33\3\33\5\33\u011c\n\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\7\34\u0124\n\34\f\34\16\34\u0127\13\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\7\35\u012f\n\35\f\35\16\35\u0132")
        buf.write("\13\35\3\36\3\36\3\36\3\36\3\36\3\36\7\36\u013a\n\36\f")
        buf.write("\36\16\36\u013d\13\36\3\37\3\37\3\37\3\37\3\37\3\37\7")
        buf.write("\37\u0145\n\37\f\37\16\37\u0148\13\37\3 \3 \3 \5 \u014d")
        buf.write("\n \3!\3!\3!\5!\u0152\n!\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u015a")
        buf.write("\n\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\7#\u0166\n#\f#\16#")
        buf.write("\u0169\13#\3$\3$\3$\3$\5$\u016f\n$\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\5%\u0179\n%\3&\3&\5&\u017d\n&\3&\3&\3\'\3\'\3\'\3")
        buf.write("\'\3\'\5\'\u0186\n\'\3(\3(\3(\5(\u018b\n(\3)\3)\3*\3*")
        buf.write("\5*\u0191\n*\3*\3*\3*\3*\3+\3+\3,\3,\3-\3-\3-\3-\3.\3")
        buf.write(".\3.\3.\3.\5.\u01a4\n.\3/\3/\3/\3/\3/\3/\5/\u01ac\n/\3")
        buf.write("\60\3\60\3\60\3\60\3\60\5\60\u01b3\n\60\3\61\3\61\3\61")
        buf.write("\2\7\668:<D\62\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`\2\n\3\2\32")
        buf.write("\33\3\2$\'\3\2\"#\3\2()\3\2\34\35\3\2\36!\7\2\4\4\13\13")
        buf.write("\r\r\17\17\25\25\3\2\23\24\2\u01c2\2b\3\2\2\2\4i\3\2\2")
        buf.write("\2\6k\3\2\2\2\bs\3\2\2\2\nz\3\2\2\2\f\u0080\3\2\2\2\16")
        buf.write("\u0086\3\2\2\2\20\u0095\3\2\2\2\22\u0097\3\2\2\2\24\u009e")
        buf.write("\3\2\2\2\26\u00a0\3\2\2\2\30\u00b0\3\2\2\2\32\u00bc\3")
        buf.write("\2\2\2\34\u00c7\3\2\2\2\36\u00c9\3\2\2\2 \u00e0\3\2\2")
        buf.write("\2\"\u00e2\3\2\2\2$\u00e4\3\2\2\2&\u00e6\3\2\2\2(\u00e9")
        buf.write("\3\2\2\2*\u00ee\3\2\2\2,\u00f2\3\2\2\2.\u00fa\3\2\2\2")
        buf.write("\60\u010d\3\2\2\2\62\u0114\3\2\2\2\64\u011b\3\2\2\2\66")
        buf.write("\u011d\3\2\2\28\u0128\3\2\2\2:\u0133\3\2\2\2<\u013e\3")
        buf.write("\2\2\2>\u014c\3\2\2\2@\u0151\3\2\2\2B\u0159\3\2\2\2D\u015b")
        buf.write("\3\2\2\2F\u016e\3\2\2\2H\u0178\3\2\2\2J\u017a\3\2\2\2")
        buf.write("L\u0185\3\2\2\2N\u018a\3\2\2\2P\u018c\3\2\2\2R\u0190\3")
        buf.write("\2\2\2T\u0196\3\2\2\2V\u0198\3\2\2\2X\u019a\3\2\2\2Z\u01a3")
        buf.write("\3\2\2\2\\\u01ab\3\2\2\2^\u01b2\3\2\2\2`\u01b4\3\2\2\2")
        buf.write("bc\5\4\3\2cd\7\2\2\3d\3\3\2\2\2ef\5\6\4\2fg\5\4\3\2gj")
        buf.write("\3\2\2\2hj\5\6\4\2ie\3\2\2\2ih\3\2\2\2j\5\3\2\2\2kl\7")
        buf.write("\6\2\2lo\7<\2\2mn\7\n\2\2np\7<\2\2om\3\2\2\2op\3\2\2\2")
        buf.write("pq\3\2\2\2qr\5\b\5\2r\7\3\2\2\2su\7-\2\2tv\5\n\6\2ut\3")
        buf.write("\2\2\2uv\3\2\2\2vw\3\2\2\2wx\7.\2\2x\t\3\2\2\2y{\5\f\7")
        buf.write("\2zy\3\2\2\2{|\3\2\2\2|z\3\2\2\2|}\3\2\2\2}\13\3\2\2\2")
        buf.write("~\u0081\5\32\16\2\177\u0081\5\16\b\2\u0080~\3\2\2\2\u0080")
        buf.write("\177\3\2\2\2\u0081\r\3\2\2\2\u0082\u0084\7\31\2\2\u0083")
        buf.write("\u0082\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0085\3\2\2\2")
        buf.write("\u0085\u0087\5P)\2\u0086\u0083\3\2\2\2\u0086\u0087\3\2")
        buf.write("\2\2\u0087\u0088\3\2\2\2\u0088\u0089\7<\2\2\u0089\u008b")
        buf.write("\7\61\2\2\u008a\u008c\5\20\t\2\u008b\u008a\3\2\2\2\u008b")
        buf.write("\u008c\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008e\7\62\2")
        buf.write("\2\u008e\u008f\5\26\f\2\u008f\17\3\2\2\2\u0090\u0091\5")
        buf.write("\22\n\2\u0091\u0092\7\63\2\2\u0092\u0093\5\20\t\2\u0093")
        buf.write("\u0096\3\2\2\2\u0094\u0096\5\22\n\2\u0095\u0090\3\2\2")
        buf.write("\2\u0095\u0094\3\2\2\2\u0096\21\3\2\2\2\u0097\u0098\5")
        buf.write("N(\2\u0098\u0099\5\24\13\2\u0099\23\3\2\2\2\u009a\u009b")
        buf.write("\7<\2\2\u009b\u009c\7\65\2\2\u009c\u009f\5\24\13\2\u009d")
        buf.write("\u009f\7<\2\2\u009e\u009a\3\2\2\2\u009e\u009d\3\2\2\2")
        buf.write("\u009f\25\3\2\2\2\u00a0\u00a4\7-\2\2\u00a1\u00a3\5\30")
        buf.write("\r\2\u00a2\u00a1\3\2\2\2\u00a3\u00a6\3\2\2\2\u00a4\u00a2")
        buf.write("\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00aa\3\2\2\2\u00a6")
        buf.write("\u00a4\3\2\2\2\u00a7\u00a9\5 \21\2\u00a8\u00a7\3\2\2\2")
        buf.write("\u00a9\u00ac\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00ab\3")
        buf.write("\2\2\2\u00ab\u00ad\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ad\u00ae")
        buf.write("\7.\2\2\u00ae\27\3\2\2\2\u00af\u00b1\7\30\2\2\u00b0\u00af")
        buf.write("\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2")
        buf.write("\u00b3\5N(\2\u00b3\u00b4\5\34\17\2\u00b4\u00b5\7\63\2")
        buf.write("\2\u00b5\31\3\2\2\2\u00b6\u00bd\7\31\2\2\u00b7\u00bd\7")
        buf.write("\30\2\2\u00b8\u00b9\7\31\2\2\u00b9\u00bd\7\30\2\2\u00ba")
        buf.write("\u00bb\7\30\2\2\u00bb\u00bd\7\31\2\2\u00bc\u00b6\3\2\2")
        buf.write("\2\u00bc\u00b7\3\2\2\2\u00bc\u00b8\3\2\2\2\u00bc\u00ba")
        buf.write("\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00be\3\2\2\2\u00be")
        buf.write("\u00bf\5N(\2\u00bf\u00c0\5\34\17\2\u00c0\u00c1\7\63\2")
        buf.write("\2\u00c1\33\3\2\2\2\u00c2\u00c3\5\36\20\2\u00c3\u00c4")
        buf.write("\7\65\2\2\u00c4\u00c5\5\34\17\2\u00c5\u00c8\3\2\2\2\u00c6")
        buf.write("\u00c8\5\36\20\2\u00c7\u00c2\3\2\2\2\u00c7\u00c6\3\2\2")
        buf.write("\2\u00c8\35\3\2\2\2\u00c9\u00cc\7<\2\2\u00ca\u00cb\7\3")
        buf.write("\2\2\u00cb\u00cd\5\62\32\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd")
        buf.write("\3\2\2\2\u00cd\37\3\2\2\2\u00ce\u00e1\5\26\f\2\u00cf\u00d0")
        buf.write("\5*\26\2\u00d0\u00d1\7\63\2\2\u00d1\u00e1\3\2\2\2\u00d2")
        buf.write("\u00e1\5,\27\2\u00d3\u00e1\5.\30\2\u00d4\u00d5\5\"\22")
        buf.write("\2\u00d5\u00d6\7\63\2\2\u00d6\u00e1\3\2\2\2\u00d7\u00d8")
        buf.write("\5$\23\2\u00d8\u00d9\7\63\2\2\u00d9\u00e1\3\2\2\2\u00da")
        buf.write("\u00db\5&\24\2\u00db\u00dc\7\63\2\2\u00dc\u00e1\3\2\2")
        buf.write("\2\u00dd\u00de\5(\25\2\u00de\u00df\7\63\2\2\u00df\u00e1")
        buf.write("\3\2\2\2\u00e0\u00ce\3\2\2\2\u00e0\u00cf\3\2\2\2\u00e0")
        buf.write("\u00d2\3\2\2\2\u00e0\u00d3\3\2\2\2\u00e0\u00d4\3\2\2\2")
        buf.write("\u00e0\u00d7\3\2\2\2\u00e0\u00da\3\2\2\2\u00e0\u00dd\3")
        buf.write("\2\2\2\u00e1!\3\2\2\2\u00e2\u00e3\7\5\2\2\u00e3#\3\2\2")
        buf.write("\2\u00e4\u00e5\7\7\2\2\u00e5%\3\2\2\2\u00e6\u00e7\7\22")
        buf.write("\2\2\u00e7\u00e8\5\62\32\2\u00e8\'\3\2\2\2\u00e9\u00ea")
        buf.write("\5D#\2\u00ea\u00eb\7\66\2\2\u00eb\u00ec\7<\2\2\u00ec\u00ed")
        buf.write("\5J&\2\u00ed)\3\2\2\2\u00ee\u00ef\5\60\31\2\u00ef\u00f0")
        buf.write("\7,\2\2\u00f0\u00f1\5\62\32\2\u00f1+\3\2\2\2\u00f2\u00f3")
        buf.write("\7\f\2\2\u00f3\u00f4\5\62\32\2\u00f4\u00f5\7\20\2\2\u00f5")
        buf.write("\u00f8\5 \21\2\u00f6\u00f7\7\t\2\2\u00f7\u00f9\5 \21\2")
        buf.write("\u00f8\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9-\3\2\2")
        buf.write("\2\u00fa\u00fb\7\21\2\2\u00fb\u00fc\7<\2\2\u00fc\u00fd")
        buf.write("\7,\2\2\u00fd\u00fe\5\62\32\2\u00fe\u00ff\t\2\2\2\u00ff")
        buf.write("\u0100\5\62\32\2\u0100\u0101\7\b\2\2\u0101\u0102\5 \21")
        buf.write("\2\u0102/\3\2\2\2\u0103\u010e\7<\2\2\u0104\u0105\5D#\2")
        buf.write("\u0105\u0106\7\66\2\2\u0106\u0107\7<\2\2\u0107\u010e\3")
        buf.write("\2\2\2\u0108\u0109\5D#\2\u0109\u010a\7/\2\2\u010a\u010b")
        buf.write("\5\62\32\2\u010b\u010c\7\60\2\2\u010c\u010e\3\2\2\2\u010d")
        buf.write("\u0103\3\2\2\2\u010d\u0104\3\2\2\2\u010d\u0108\3\2\2\2")
        buf.write("\u010e\61\3\2\2\2\u010f\u0110\5\64\33\2\u0110\u0111\t")
        buf.write("\3\2\2\u0111\u0112\5\64\33\2\u0112\u0115\3\2\2\2\u0113")
        buf.write("\u0115\5\64\33\2\u0114\u010f\3\2\2\2\u0114\u0113\3\2\2")
        buf.write("\2\u0115\63\3\2\2\2\u0116\u0117\5\66\34\2\u0117\u0118")
        buf.write("\t\4\2\2\u0118\u0119\5\66\34\2\u0119\u011c\3\2\2\2\u011a")
        buf.write("\u011c\5\66\34\2\u011b\u0116\3\2\2\2\u011b\u011a\3\2\2")
        buf.write("\2\u011c\65\3\2\2\2\u011d\u011e\b\34\1\2\u011e\u011f\5")
        buf.write("8\35\2\u011f\u0125\3\2\2\2\u0120\u0121\f\4\2\2\u0121\u0122")
        buf.write("\t\5\2\2\u0122\u0124\58\35\2\u0123\u0120\3\2\2\2\u0124")
        buf.write("\u0127\3\2\2\2\u0125\u0123\3\2\2\2\u0125\u0126\3\2\2\2")
        buf.write("\u0126\67\3\2\2\2\u0127\u0125\3\2\2\2\u0128\u0129\b\35")
        buf.write("\1\2\u0129\u012a\5:\36\2\u012a\u0130\3\2\2\2\u012b\u012c")
        buf.write("\f\4\2\2\u012c\u012d\t\6\2\2\u012d\u012f\5:\36\2\u012e")
        buf.write("\u012b\3\2\2\2\u012f\u0132\3\2\2\2\u0130\u012e\3\2\2\2")
        buf.write("\u0130\u0131\3\2\2\2\u01319\3\2\2\2\u0132\u0130\3\2\2")
        buf.write("\2\u0133\u0134\b\36\1\2\u0134\u0135\5<\37\2\u0135\u013b")
        buf.write("\3\2\2\2\u0136\u0137\f\4\2\2\u0137\u0138\t\7\2\2\u0138")
        buf.write("\u013a\5<\37\2\u0139\u0136\3\2\2\2\u013a\u013d\3\2\2\2")
        buf.write("\u013b\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c;\3\2\2")
        buf.write("\2\u013d\u013b\3\2\2\2\u013e\u013f\b\37\1\2\u013f\u0140")
        buf.write("\5> \2\u0140\u0146\3\2\2\2\u0141\u0142\f\4\2\2\u0142\u0143")
        buf.write("\7+\2\2\u0143\u0145\5> \2\u0144\u0141\3\2\2\2\u0145\u0148")
        buf.write("\3\2\2\2\u0146\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147")
        buf.write("=\3\2\2\2\u0148\u0146\3\2\2\2\u0149\u014a\7*\2\2\u014a")
        buf.write("\u014d\5> \2\u014b\u014d\5@!\2\u014c\u0149\3\2\2\2\u014c")
        buf.write("\u014b\3\2\2\2\u014d?\3\2\2\2\u014e\u014f\t\6\2\2\u014f")
        buf.write("\u0152\5@!\2\u0150\u0152\5B\"\2\u0151\u014e\3\2\2\2\u0151")
        buf.write("\u0150\3\2\2\2\u0152A\3\2\2\2\u0153\u0154\5D#\2\u0154")
        buf.write("\u0155\7/\2\2\u0155\u0156\5\62\32\2\u0156\u0157\7\60\2")
        buf.write("\2\u0157\u015a\3\2\2\2\u0158\u015a\5D#\2\u0159\u0153\3")
        buf.write("\2\2\2\u0159\u0158\3\2\2\2\u015aC\3\2\2\2\u015b\u015c")
        buf.write("\b#\1\2\u015c\u015d\5F$\2\u015d\u0167\3\2\2\2\u015e\u015f")
        buf.write("\f\5\2\2\u015f\u0160\7\66\2\2\u0160\u0161\7<\2\2\u0161")
        buf.write("\u0166\5J&\2\u0162\u0163\f\3\2\2\u0163\u0164\7\66\2\2")
        buf.write("\u0164\u0166\7<\2\2\u0165\u015e\3\2\2\2\u0165\u0162\3")
        buf.write("\2\2\2\u0166\u0169\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0168")
        buf.write("\3\2\2\2\u0168E\3\2\2\2\u0169\u0167\3\2\2\2\u016a\u016b")
        buf.write("\7\16\2\2\u016b\u016c\7<\2\2\u016c\u016f\5J&\2\u016d\u016f")
        buf.write("\5H%\2\u016e\u016a\3\2\2\2\u016e\u016d\3\2\2\2\u016fG")
        buf.write("\3\2\2\2\u0170\u0179\5^\60\2\u0171\u0179\5X-\2\u0172\u0179")
        buf.write("\7\27\2\2\u0173\u0174\7\61\2\2\u0174\u0175\5\62\32\2\u0175")
        buf.write("\u0176\7\62\2\2\u0176\u0179\3\2\2\2\u0177\u0179\7<\2\2")
        buf.write("\u0178\u0170\3\2\2\2\u0178\u0171\3\2\2\2\u0178\u0172\3")
        buf.write("\2\2\2\u0178\u0173\3\2\2\2\u0178\u0177\3\2\2\2\u0179I")
        buf.write("\3\2\2\2\u017a\u017c\7\61\2\2\u017b\u017d\5L\'\2\u017c")
        buf.write("\u017b\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u017e\3\2\2\2")
        buf.write("\u017e\u017f\7\62\2\2\u017fK\3\2\2\2\u0180\u0181\5\62")
        buf.write("\32\2\u0181\u0182\7\65\2\2\u0182\u0183\5L\'\2\u0183\u0186")
        buf.write("\3\2\2\2\u0184\u0186\5\62\32\2\u0185\u0180\3\2\2\2\u0185")
        buf.write("\u0184\3\2\2\2\u0186M\3\2\2\2\u0187\u018b\5T+\2\u0188")
        buf.write("\u018b\5R*\2\u0189\u018b\5V,\2\u018a\u0187\3\2\2\2\u018a")
        buf.write("\u0188\3\2\2\2\u018a\u0189\3\2\2\2\u018bO\3\2\2\2\u018c")
        buf.write("\u018d\5N(\2\u018dQ\3\2\2\2\u018e\u0191\5T+\2\u018f\u0191")
        buf.write("\7<\2\2\u0190\u018e\3\2\2\2\u0190\u018f\3\2\2\2\u0191")
        buf.write("\u0192\3\2\2\2\u0192\u0193\7/\2\2\u0193\u0194\7:\2\2\u0194")
        buf.write("\u0195\7\60\2\2\u0195S\3\2\2\2\u0196\u0197\t\b\2\2\u0197")
        buf.write("U\3\2\2\2\u0198\u0199\7<\2\2\u0199W\3\2\2\2\u019a\u019b")
        buf.write("\7-\2\2\u019b\u019c\5Z.\2\u019c\u019d\7.\2\2\u019dY\3")
        buf.write("\2\2\2\u019e\u019f\5\\/\2\u019f\u01a0\7\65\2\2\u01a0\u01a1")
        buf.write("\5Z.\2\u01a1\u01a4\3\2\2\2\u01a2\u01a4\5\\/\2\u01a3\u019e")
        buf.write("\3\2\2\2\u01a3\u01a2\3\2\2\2\u01a4[\3\2\2\2\u01a5\u01ac")
        buf.write("\7:\2\2\u01a6\u01ac\7;\2\2\u01a7\u01ac\5`\61\2\u01a8\u01ac")
        buf.write("\7=\2\2\u01a9\u01ac\7\26\2\2\u01aa\u01ac\7\27\2\2\u01ab")
        buf.write("\u01a5\3\2\2\2\u01ab\u01a6\3\2\2\2\u01ab\u01a7\3\2\2\2")
        buf.write("\u01ab\u01a8\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ab\u01aa\3")
        buf.write("\2\2\2\u01ac]\3\2\2\2\u01ad\u01b3\7:\2\2\u01ae\u01b3\7")
        buf.write(";\2\2\u01af\u01b3\5`\61\2\u01b0\u01b3\7=\2\2\u01b1\u01b3")
        buf.write("\7\26\2\2\u01b2\u01ad\3\2\2\2\u01b2\u01ae\3\2\2\2\u01b2")
        buf.write("\u01af\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b1\3\2\2\2")
        buf.write("\u01b3_\3\2\2\2\u01b4\u01b5\t\t\2\2\u01b5a\3\2\2\2)io")
        buf.write("u|\u0080\u0083\u0086\u008b\u0095\u009e\u00a4\u00aa\u00b0")
        buf.write("\u00bc\u00c7\u00cc\u00e0\u00f8\u010d\u0114\u011b\u0125")
        buf.write("\u0130\u013b\u0146\u014c\u0151\u0159\u0165\u0167\u016e")
        buf.write("\u0178\u017c\u0185\u018a\u0190\u01a3\u01ab\u01b2")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'boolean'", "'break'", "'class'", 
                     "'continue'", "'do'", "'else'", "'extends'", "'float'", 
                     "'if'", "'int'", "'new'", "'string'", "'then'", "'for'", 
                     "'return'", "'true'", "'false'", "'void'", "'nil'", 
                     "'this'", "'final'", "'static'", "'to'", "'downto'", 
                     "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", "'!='", 
                     "'=='", "'<'", "'>'", "'<='", "'>='", "'||'", "'&&'", 
                     "'!'", "'^'", "':='", "'{'", "'}'", "'['", "']'", "'('", 
                     "')'", "';'", "':'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "BOOLEAN", "BREAK", "CLASS", 
                      "CONTINUE", "DO", "ELSE", "EXTENDS", "FLOAT", "IF", 
                      "INT", "NEW", "STRING", "THEN", "FOR", "RETURN", "TRUE", 
                      "FALSE", "VOID", "NIL", "THIS", "FINAL", "STATIC", 
                      "TO", "DOWNTO", "ADD", "SUB", "MUL", "FDIV", "IDIV", 
                      "MOD", "NEQUAL", "EQUAL", "LT", "GT", "LTE", "GTE", 
                      "OR", "AND", "NOT", "CONCAT", "ASS", "LP", "RP", "LSB", 
                      "RSB", "LB", "RB", "SM", "COLON", "COMMA", "DOT", 
                      "WS", "LINE_COMMENT", "BLOCK_COMMENT", "INTLIT", "FLOATLIT", 
                      "ID", "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_classDeclList = 1
    RULE_classDecl = 2
    RULE_classBody = 3
    RULE_classBodyDeclList = 4
    RULE_classBodyDecl = 5
    RULE_methodDecl = 6
    RULE_paramList = 7
    RULE_param = 8
    RULE_ids = 9
    RULE_blockStmt = 10
    RULE_varDecl = 11
    RULE_attributeDecl = 12
    RULE_variableDeclList = 13
    RULE_variableDeclarator = 14
    RULE_statement = 15
    RULE_breakStmt = 16
    RULE_continueStmt = 17
    RULE_returnStmt = 18
    RULE_methodInvoStmt = 19
    RULE_assignStmt = 20
    RULE_ifStmt = 21
    RULE_forStmt = 22
    RULE_lhsAssign = 23
    RULE_expression = 24
    RULE_expression1 = 25
    RULE_expression2 = 26
    RULE_expression3 = 27
    RULE_expression4 = 28
    RULE_expression5 = 29
    RULE_expression6 = 30
    RULE_expression7 = 31
    RULE_expression8 = 32
    RULE_expression9 = 33
    RULE_expression10 = 34
    RULE_expression11 = 35
    RULE_args = 36
    RULE_expList = 37
    RULE_typeType = 38
    RULE_returnType = 39
    RULE_arrayType = 40
    RULE_primitiveType = 41
    RULE_classType = 42
    RULE_arrayLit = 43
    RULE_elemArrays = 44
    RULE_elemArray = 45
    RULE_elem = 46
    RULE_booleanlit = 47

    ruleNames =  [ "program", "classDeclList", "classDecl", "classBody", 
                   "classBodyDeclList", "classBodyDecl", "methodDecl", "paramList", 
                   "param", "ids", "blockStmt", "varDecl", "attributeDecl", 
                   "variableDeclList", "variableDeclarator", "statement", 
                   "breakStmt", "continueStmt", "returnStmt", "methodInvoStmt", 
                   "assignStmt", "ifStmt", "forStmt", "lhsAssign", "expression", 
                   "expression1", "expression2", "expression3", "expression4", 
                   "expression5", "expression6", "expression7", "expression8", 
                   "expression9", "expression10", "expression11", "args", 
                   "expList", "typeType", "returnType", "arrayType", "primitiveType", 
                   "classType", "arrayLit", "elemArrays", "elemArray", "elem", 
                   "booleanlit" ]

    EOF = Token.EOF
    T__0=1
    BOOLEAN=2
    BREAK=3
    CLASS=4
    CONTINUE=5
    DO=6
    ELSE=7
    EXTENDS=8
    FLOAT=9
    IF=10
    INT=11
    NEW=12
    STRING=13
    THEN=14
    FOR=15
    RETURN=16
    TRUE=17
    FALSE=18
    VOID=19
    NIL=20
    THIS=21
    FINAL=22
    STATIC=23
    TO=24
    DOWNTO=25
    ADD=26
    SUB=27
    MUL=28
    FDIV=29
    IDIV=30
    MOD=31
    NEQUAL=32
    EQUAL=33
    LT=34
    GT=35
    LTE=36
    GTE=37
    OR=38
    AND=39
    NOT=40
    CONCAT=41
    ASS=42
    LP=43
    RP=44
    LSB=45
    RSB=46
    LB=47
    RB=48
    SM=49
    COLON=50
    COMMA=51
    DOT=52
    WS=53
    LINE_COMMENT=54
    BLOCK_COMMENT=55
    INTLIT=56
    FLOATLIT=57
    ID=58
    STRINGLIT=59
    UNCLOSE_STRING=60
    ILLEGAL_ESCAPE=61
    ERROR_CHAR=62

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

        def classDeclList(self):
            return self.getTypedRuleContext(BKOOLParser.ClassDeclListContext,0)


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
            self.state = 96
            self.classDeclList()
            self.state = 97
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDecl(self):
            return self.getTypedRuleContext(BKOOLParser.ClassDeclContext,0)


        def classDeclList(self):
            return self.getTypedRuleContext(BKOOLParser.ClassDeclListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_classDeclList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDeclList" ):
                return visitor.visitClassDeclList(self)
            else:
                return visitor.visitChildren(self)




    def classDeclList(self):

        localctx = BKOOLParser.ClassDeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classDeclList)
        try:
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.classDecl()
                self.state = 100
                self.classDeclList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.classDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(BKOOLParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def classBody(self):
            return self.getTypedRuleContext(BKOOLParser.ClassBodyContext,0)


        def EXTENDS(self):
            return self.getToken(BKOOLParser.EXTENDS, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_classDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDecl" ):
                return visitor.visitClassDecl(self)
            else:
                return visitor.visitChildren(self)




    def classDecl(self):

        localctx = BKOOLParser.ClassDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(BKOOLParser.CLASS)
            self.state = 106
            self.match(BKOOLParser.ID)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 107
                self.match(BKOOLParser.EXTENDS)
                self.state = 108
                self.match(BKOOLParser.ID)


            self.state = 111
            self.classBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def classBodyDeclList(self):
            return self.getTypedRuleContext(BKOOLParser.ClassBodyDeclListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_classBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassBody" ):
                return visitor.visitClassBody(self)
            else:
                return visitor.visitChildren(self)




    def classBody(self):

        localctx = BKOOLParser.ClassBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_classBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(BKOOLParser.LP)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.ID))) != 0):
                self.state = 114
                self.classBodyDeclList()


            self.state = 117
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassBodyDeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classBodyDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ClassBodyDeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ClassBodyDeclContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_classBodyDeclList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassBodyDeclList" ):
                return visitor.visitClassBodyDeclList(self)
            else:
                return visitor.visitChildren(self)




    def classBodyDeclList(self):

        localctx = BKOOLParser.ClassBodyDeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_classBodyDeclList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 119
                self.classBodyDecl()
                self.state = 122 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.ID))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassBodyDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributeDecl(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeDeclContext,0)


        def methodDecl(self):
            return self.getTypedRuleContext(BKOOLParser.MethodDeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_classBodyDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassBodyDecl" ):
                return visitor.visitClassBodyDecl(self)
            else:
                return visitor.visitChildren(self)




    def classBodyDecl(self):

        localctx = BKOOLParser.ClassBodyDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_classBodyDecl)
        try:
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.attributeDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.methodDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclContext(ParserRuleContext):
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

        def blockStmt(self):
            return self.getTypedRuleContext(BKOOLParser.BlockStmtContext,0)


        def returnType(self):
            return self.getTypedRuleContext(BKOOLParser.ReturnTypeContext,0)


        def paramList(self):
            return self.getTypedRuleContext(BKOOLParser.ParamListContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_methodDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDecl" ):
                return visitor.visitMethodDecl(self)
            else:
                return visitor.visitChildren(self)




    def methodDecl(self):

        localctx = BKOOLParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_methodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.STATIC:
                    self.state = 128
                    self.match(BKOOLParser.STATIC)


                self.state = 131
                self.returnType()


            self.state = 134
            self.match(BKOOLParser.ID)
            self.state = 135
            self.match(BKOOLParser.LB)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.ID))) != 0):
                self.state = 136
                self.paramList()


            self.state = 139
            self.match(BKOOLParser.RB)
            self.state = 140
            self.blockStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def SM(self):
            return self.getToken(BKOOLParser.SM, 0)

        def paramList(self):
            return self.getTypedRuleContext(BKOOLParser.ParamListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = BKOOLParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_paramList)
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.param()
                self.state = 143
                self.match(BKOOLParser.SM)
                self.state = 144
                self.paramList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
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

        def typeType(self):
            return self.getTypedRuleContext(BKOOLParser.TypeTypeContext,0)


        def ids(self):
            return self.getTypedRuleContext(BKOOLParser.IdsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = BKOOLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.typeType()
            self.state = 150
            self.ids()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def ids(self):
            return self.getTypedRuleContext(BKOOLParser.IdsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_ids

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIds" ):
                return visitor.visitIds(self)
            else:
                return visitor.visitChildren(self)




    def ids(self):

        localctx = BKOOLParser.IdsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ids)
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.match(BKOOLParser.ID)
                self.state = 153
                self.match(BKOOLParser.COMMA)
                self.state = 154
                self.ids()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def varDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.VarDeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.VarDeclContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StatementContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_blockStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStmt" ):
                return visitor.visitBlockStmt(self)
            else:
                return visitor.visitChildren(self)




    def blockStmt(self):

        localctx = BKOOLParser.BlockStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_blockStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(BKOOLParser.LP)
            self.state = 162
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 159
                    self.varDecl() 
                self.state = 164
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BREAK) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.STRINGLIT))) != 0):
                self.state = 165
                self.statement()
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 171
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeType(self):
            return self.getTypedRuleContext(BKOOLParser.TypeTypeContext,0)


        def variableDeclList(self):
            return self.getTypedRuleContext(BKOOLParser.VariableDeclListContext,0)


        def SM(self):
            return self.getToken(BKOOLParser.SM, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_varDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = BKOOLParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.FINAL:
                self.state = 173
                self.match(BKOOLParser.FINAL)


            self.state = 176
            self.typeType()
            self.state = 177
            self.variableDeclList()
            self.state = 178
            self.match(BKOOLParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeType(self):
            return self.getTypedRuleContext(BKOOLParser.TypeTypeContext,0)


        def variableDeclList(self):
            return self.getTypedRuleContext(BKOOLParser.VariableDeclListContext,0)


        def SM(self):
            return self.getToken(BKOOLParser.SM, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_attributeDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributeDecl" ):
                return visitor.visitAttributeDecl(self)
            else:
                return visitor.visitChildren(self)




    def attributeDecl(self):

        localctx = BKOOLParser.AttributeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_attributeDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 180
                self.match(BKOOLParser.STATIC)

            elif la_ == 2:
                self.state = 181
                self.match(BKOOLParser.FINAL)

            elif la_ == 3:
                self.state = 182
                self.match(BKOOLParser.STATIC)
                self.state = 183
                self.match(BKOOLParser.FINAL)

            elif la_ == 4:
                self.state = 184
                self.match(BKOOLParser.FINAL)
                self.state = 185
                self.match(BKOOLParser.STATIC)


            self.state = 188
            self.typeType()
            self.state = 189
            self.variableDeclList()
            self.state = 190
            self.match(BKOOLParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclarator(self):
            return self.getTypedRuleContext(BKOOLParser.VariableDeclaratorContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def variableDeclList(self):
            return self.getTypedRuleContext(BKOOLParser.VariableDeclListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_variableDeclList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclList" ):
                return visitor.visitVariableDeclList(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclList(self):

        localctx = BKOOLParser.VariableDeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_variableDeclList)
        try:
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.variableDeclarator()
                self.state = 193
                self.match(BKOOLParser.COMMA)
                self.state = 194
                self.variableDeclList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.variableDeclarator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclaratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_variableDeclarator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclarator" ):
                return visitor.visitVariableDeclarator(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclarator(self):

        localctx = BKOOLParser.VariableDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_variableDeclarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(BKOOLParser.ID)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.T__0:
                self.state = 200
                self.match(BKOOLParser.T__0)
                self.state = 201
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockStmt(self):
            return self.getTypedRuleContext(BKOOLParser.BlockStmtContext,0)


        def assignStmt(self):
            return self.getTypedRuleContext(BKOOLParser.AssignStmtContext,0)


        def SM(self):
            return self.getToken(BKOOLParser.SM, 0)

        def ifStmt(self):
            return self.getTypedRuleContext(BKOOLParser.IfStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(BKOOLParser.ForStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(BKOOLParser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(BKOOLParser.ContinueStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(BKOOLParser.ReturnStmtContext,0)


        def methodInvoStmt(self):
            return self.getTypedRuleContext(BKOOLParser.MethodInvoStmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BKOOLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_statement)
        try:
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.blockStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.assignStmt()
                self.state = 206
                self.match(BKOOLParser.SM)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 208
                self.ifStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 209
                self.forStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 210
                self.breakStmt()
                self.state = 211
                self.match(BKOOLParser.SM)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 213
                self.continueStmt()
                self.state = 214
                self.match(BKOOLParser.SM)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 216
                self.returnStmt()
                self.state = 217
                self.match(BKOOLParser.SM)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 219
                self.methodInvoStmt()
                self.state = 220
                self.match(BKOOLParser.SM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_breakStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)




    def breakStmt(self):

        localctx = BKOOLParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(BKOOLParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKOOLParser.CONTINUE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_continueStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStmt" ):
                return visitor.visitContinueStmt(self)
            else:
                return visitor.visitChildren(self)




    def continueStmt(self):

        localctx = BKOOLParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(BKOOLParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_returnStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = BKOOLParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(BKOOLParser.RETURN)
            self.state = 229
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodInvoStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression9(self):
            return self.getTypedRuleContext(BKOOLParser.Expression9Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def args(self):
            return self.getTypedRuleContext(BKOOLParser.ArgsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_methodInvoStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodInvoStmt" ):
                return visitor.visitMethodInvoStmt(self)
            else:
                return visitor.visitChildren(self)




    def methodInvoStmt(self):

        localctx = BKOOLParser.MethodInvoStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_methodInvoStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.expression9(0)
            self.state = 232
            self.match(BKOOLParser.DOT)
            self.state = 233
            self.match(BKOOLParser.ID)
            self.state = 234
            self.args()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhsAssign(self):
            return self.getTypedRuleContext(BKOOLParser.LhsAssignContext,0)


        def ASS(self):
            return self.getToken(BKOOLParser.ASS, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_assignStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)




    def assignStmt(self):

        localctx = BKOOLParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.lhsAssign()
            self.state = 237
            self.match(BKOOLParser.ASS)
            self.state = 238
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_ifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = BKOOLParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(BKOOLParser.IF)
            self.state = 241
            self.expression()
            self.state = 242
            self.match(BKOOLParser.THEN)
            self.state = 243
            self.statement()
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 244
                self.match(BKOOLParser.ELSE)
                self.state = 245
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ASS(self):
            return self.getToken(BKOOLParser.ASS, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpressionContext,i)


        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def statement(self):
            return self.getTypedRuleContext(BKOOLParser.StatementContext,0)


        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_forStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = BKOOLParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(BKOOLParser.FOR)
            self.state = 249
            self.match(BKOOLParser.ID)
            self.state = 250
            self.match(BKOOLParser.ASS)
            self.state = 251
            self.expression()
            self.state = 252
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 253
            self.expression()
            self.state = 254
            self.match(BKOOLParser.DO)
            self.state = 255
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def expression9(self):
            return self.getTypedRuleContext(BKOOLParser.Expression9Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_lhsAssign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhsAssign" ):
                return visitor.visitLhsAssign(self)
            else:
                return visitor.visitChildren(self)




    def lhsAssign(self):

        localctx = BKOOLParser.LhsAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_lhsAssign)
        try:
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
                self.expression9(0)
                self.state = 259
                self.match(BKOOLParser.DOT)
                self.state = 260
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 262
                self.expression9(0)
                self.state = 263
                self.match(BKOOLParser.LSB)
                self.state = 264
                self.expression()
                self.state = 265
                self.match(BKOOLParser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Expression1Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expression1Context,i)


        def GT(self):
            return self.getToken(BKOOLParser.GT, 0)

        def LT(self):
            return self.getToken(BKOOLParser.LT, 0)

        def GTE(self):
            return self.getToken(BKOOLParser.GTE, 0)

        def LTE(self):
            return self.getToken(BKOOLParser.LTE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = BKOOLParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.expression1()
                self.state = 270
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LT) | (1 << BKOOLParser.GT) | (1 << BKOOLParser.LTE) | (1 << BKOOLParser.GTE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 271
                self.expression1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.expression1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Expression2Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expression2Context,i)


        def EQUAL(self):
            return self.getToken(BKOOLParser.EQUAL, 0)

        def NEQUAL(self):
            return self.getToken(BKOOLParser.NEQUAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)




    def expression1(self):

        localctx = BKOOLParser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expression1)
        self._la = 0 # Token type
        try:
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.expression2(0)
                self.state = 277
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.NEQUAL or _la==BKOOLParser.EQUAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 278
                self.expression2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.expression2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(BKOOLParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(BKOOLParser.Expression2Context,0)


        def AND(self):
            return self.getToken(BKOOLParser.AND, 0)

        def OR(self):
            return self.getToken(BKOOLParser.OR, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 286
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 287
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.OR or _la==BKOOLParser.AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 288
                    self.expression3(0) 
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(BKOOLParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(BKOOLParser.Expression3Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 302
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 297
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 298
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 299
                    self.expression4(0) 
                self.state = 304
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(BKOOLParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(BKOOLParser.Expression4Context,0)


        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def FDIV(self):
            return self.getToken(BKOOLParser.FDIV, 0)

        def IDIV(self):
            return self.getToken(BKOOLParser.IDIV, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.expression5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 313
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 308
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 309
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL) | (1 << BKOOLParser.FDIV) | (1 << BKOOLParser.IDIV) | (1 << BKOOLParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 310
                    self.expression5(0) 
                self.state = 315
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression6(self):
            return self.getTypedRuleContext(BKOOLParser.Expression6Context,0)


        def expression5(self):
            return self.getTypedRuleContext(BKOOLParser.Expression5Context,0)


        def CONCAT(self):
            return self.getToken(BKOOLParser.CONCAT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)



    def expression5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expression5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_expression5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.expression6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 324
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expression5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression5)
                    self.state = 319
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 320
                    self.match(BKOOLParser.CONCAT)
                    self.state = 321
                    self.expression6() 
                self.state = 326
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

        def expression6(self):
            return self.getTypedRuleContext(BKOOLParser.Expression6Context,0)


        def expression7(self):
            return self.getTypedRuleContext(BKOOLParser.Expression7Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)




    def expression6(self):

        localctx = BKOOLParser.Expression6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expression6)
        try:
            self.state = 330
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.match(BKOOLParser.NOT)
                self.state = 328
                self.expression6()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.LP, BKOOLParser.LB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.ID, BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 329
                self.expression7()
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


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression7(self):
            return self.getTypedRuleContext(BKOOLParser.Expression7Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def expression8(self):
            return self.getTypedRuleContext(BKOOLParser.Expression8Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)




    def expression7(self):

        localctx = BKOOLParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expression7)
        self._la = 0 # Token type
        try:
            self.state = 335
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADD, BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 333
                self.expression7()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.LP, BKOOLParser.LB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.ID, BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
                self.expression8()
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


    class Expression8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression9(self):
            return self.getTypedRuleContext(BKOOLParser.Expression9Context,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expression8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression8" ):
                return visitor.visitExpression8(self)
            else:
                return visitor.visitChildren(self)




    def expression8(self):

        localctx = BKOOLParser.Expression8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expression8)
        try:
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.expression9(0)
                self.state = 338
                self.match(BKOOLParser.LSB)
                self.state = 339
                self.expression()
                self.state = 340
                self.match(BKOOLParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
                self.expression9(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression10(self):
            return self.getTypedRuleContext(BKOOLParser.Expression10Context,0)


        def expression9(self):
            return self.getTypedRuleContext(BKOOLParser.Expression9Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def args(self):
            return self.getTypedRuleContext(BKOOLParser.ArgsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expression9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression9" ):
                return visitor.visitExpression9(self)
            else:
                return visitor.visitChildren(self)



    def expression9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expression9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expression9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.expression10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 357
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 355
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Expression9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression9)
                        self.state = 348
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 349
                        self.match(BKOOLParser.DOT)
                        self.state = 350
                        self.match(BKOOLParser.ID)
                        self.state = 351
                        self.args()
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Expression9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression9)
                        self.state = 352
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 353
                        self.match(BKOOLParser.DOT)
                        self.state = 354
                        self.match(BKOOLParser.ID)
                        pass

             
                self.state = 359
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(BKOOLParser.NEW, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def args(self):
            return self.getTypedRuleContext(BKOOLParser.ArgsContext,0)


        def expression11(self):
            return self.getTypedRuleContext(BKOOLParser.Expression11Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expression10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression10" ):
                return visitor.visitExpression10(self)
            else:
                return visitor.visitChildren(self)




    def expression10(self):

        localctx = BKOOLParser.Expression10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expression10)
        try:
            self.state = 364
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.match(BKOOLParser.NEW)
                self.state = 361
                self.match(BKOOLParser.ID)
                self.state = 362
                self.args()
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.LP, BKOOLParser.LB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.ID, BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                self.expression11()
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


    class Expression11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elem(self):
            return self.getTypedRuleContext(BKOOLParser.ElemContext,0)


        def arrayLit(self):
            return self.getTypedRuleContext(BKOOLParser.ArrayLitContext,0)


        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expression11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression11" ):
                return visitor.visitExpression11(self)
            else:
                return visitor.visitChildren(self)




    def expression11(self):

        localctx = BKOOLParser.Expression11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expression11)
        try:
            self.state = 374
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.elem()
                pass
            elif token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 367
                self.arrayLit()
                pass
            elif token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 368
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 4)
                self.state = 369
                self.match(BKOOLParser.LB)
                self.state = 370
                self.expression()
                self.state = 371
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 373
                self.match(BKOOLParser.ID)
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


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def expList(self):
            return self.getTypedRuleContext(BKOOLParser.ExpListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = BKOOLParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(BKOOLParser.LB)
            self.state = 378
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.STRINGLIT))) != 0):
                self.state = 377
                self.expList()


            self.state = 380
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def expList(self):
            return self.getTypedRuleContext(BKOOLParser.ExpListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpList" ):
                return visitor.visitExpList(self)
            else:
                return visitor.visitChildren(self)




    def expList(self):

        localctx = BKOOLParser.ExpListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expList)
        try:
            self.state = 387
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.expression()
                self.state = 383
                self.match(BKOOLParser.COMMA)
                self.state = 384
                self.expList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 386
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitiveType(self):
            return self.getTypedRuleContext(BKOOLParser.PrimitiveTypeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(BKOOLParser.ArrayTypeContext,0)


        def classType(self):
            return self.getTypedRuleContext(BKOOLParser.ClassTypeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_typeType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeType" ):
                return visitor.visitTypeType(self)
            else:
                return visitor.visitChildren(self)




    def typeType(self):

        localctx = BKOOLParser.TypeTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_typeType)
        try:
            self.state = 392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self.primitiveType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 390
                self.arrayType()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 391
                self.classType()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeType(self):
            return self.getTypedRuleContext(BKOOLParser.TypeTypeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_returnType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnType" ):
                return visitor.visitReturnType(self)
            else:
                return visitor.visitChildren(self)




    def returnType(self):

        localctx = BKOOLParser.ReturnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_returnType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.typeType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def primitiveType(self):
            return self.getTypedRuleContext(BKOOLParser.PrimitiveTypeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arrayType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = BKOOLParser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.VOID]:
                self.state = 396
                self.primitiveType()
                pass
            elif token in [BKOOLParser.ID]:
                self.state = 397
                self.match(BKOOLParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 400
            self.match(BKOOLParser.LSB)
            self.state = 401
            self.match(BKOOLParser.INTLIT)
            self.state = 402
            self.match(BKOOLParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveTypeContext(ParserRuleContext):
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
            return BKOOLParser.RULE_primitiveType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveType" ):
                return visitor.visitPrimitiveType(self)
            else:
                return visitor.visitChildren(self)




    def primitiveType(self):

        localctx = BKOOLParser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID))) != 0)):
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


    class ClassTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_classType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassType" ):
                return visitor.visitClassType(self)
            else:
                return visitor.visitChildren(self)




    def classType(self):

        localctx = BKOOLParser.ClassTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_classType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(BKOOLParser.ID)
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

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def elemArrays(self):
            return self.getTypedRuleContext(BKOOLParser.ElemArraysContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arrayLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLit" ):
                return visitor.visitArrayLit(self)
            else:
                return visitor.visitChildren(self)




    def arrayLit(self):

        localctx = BKOOLParser.ArrayLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(BKOOLParser.LP)
            self.state = 409
            self.elemArrays()
            self.state = 410
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElemArraysContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elemArray(self):
            return self.getTypedRuleContext(BKOOLParser.ElemArrayContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def elemArrays(self):
            return self.getTypedRuleContext(BKOOLParser.ElemArraysContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_elemArrays

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElemArrays" ):
                return visitor.visitElemArrays(self)
            else:
                return visitor.visitChildren(self)




    def elemArrays(self):

        localctx = BKOOLParser.ElemArraysContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_elemArrays)
        try:
            self.state = 417
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.elemArray()
                self.state = 413
                self.match(BKOOLParser.COMMA)
                self.state = 414
                self.elemArrays()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 416
                self.elemArray()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElemArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def booleanlit(self):
            return self.getTypedRuleContext(BKOOLParser.BooleanlitContext,0)


        def STRINGLIT(self):
            return self.getToken(BKOOLParser.STRINGLIT, 0)

        def NIL(self):
            return self.getToken(BKOOLParser.NIL, 0)

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_elemArray

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElemArray" ):
                return visitor.visitElemArray(self)
            else:
                return visitor.visitChildren(self)




    def elemArray(self):

        localctx = BKOOLParser.ElemArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_elemArray)
        try:
            self.state = 425
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 419
                self.match(BKOOLParser.INTLIT)
                pass
            elif token in [BKOOLParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 420
                self.match(BKOOLParser.FLOATLIT)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 421
                self.booleanlit()
                pass
            elif token in [BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 422
                self.match(BKOOLParser.STRINGLIT)
                pass
            elif token in [BKOOLParser.NIL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 423
                self.match(BKOOLParser.NIL)
                pass
            elif token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 6)
                self.state = 424
                self.match(BKOOLParser.THIS)
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


    class ElemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def booleanlit(self):
            return self.getTypedRuleContext(BKOOLParser.BooleanlitContext,0)


        def STRINGLIT(self):
            return self.getToken(BKOOLParser.STRINGLIT, 0)

        def NIL(self):
            return self.getToken(BKOOLParser.NIL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_elem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElem" ):
                return visitor.visitElem(self)
            else:
                return visitor.visitChildren(self)




    def elem(self):

        localctx = BKOOLParser.ElemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_elem)
        try:
            self.state = 432
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.match(BKOOLParser.INTLIT)
                pass
            elif token in [BKOOLParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.match(BKOOLParser.FLOATLIT)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 429
                self.booleanlit()
                pass
            elif token in [BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 430
                self.match(BKOOLParser.STRINGLIT)
                pass
            elif token in [BKOOLParser.NIL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 431
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


    class BooleanlitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(BKOOLParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKOOLParser.FALSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_booleanlit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanlit" ):
                return visitor.visitBooleanlit(self)
            else:
                return visitor.visitChildren(self)




    def booleanlit(self):

        localctx = BKOOLParser.BooleanlitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_booleanlit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[26] = self.expression2_sempred
        self._predicates[27] = self.expression3_sempred
        self._predicates[28] = self.expression4_sempred
        self._predicates[29] = self.expression5_sempred
        self._predicates[33] = self.expression9_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expression5_sempred(self, localctx:Expression5Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expression9_sempred(self, localctx:Expression9Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 1)
         




