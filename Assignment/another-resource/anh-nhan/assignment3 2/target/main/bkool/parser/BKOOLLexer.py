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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u01e6\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\3\6\3\u009a\n\3\r\3\16\3\u009b\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\4\7\4\u00a4\n\4\f\4\16\4\u00a7\13\4\3\4\3\4\3\4")
        buf.write("\3\4\7\4\u00ad\n\4\f\4\16\4\u00b0\13\4\3\4\5\4\u00b3\n")
        buf.write("\4\3\4\3\4\5\4\u00b7\n\4\5\4\u00b9\n\4\3\4\3\4\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(")
        buf.write("\3(\3)\3)\3*\3*\3*\3+\3+\3,\3,\3,\3-\3-\3.\3.\3.\3/\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\6:\u0185")
        buf.write("\n:\r:\16:\u0186\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\5;\u0193")
        buf.write("\n;\3<\3<\3=\3=\7=\u0199\n=\f=\16=\u019c\13=\3>\3>\5>")
        buf.write("\u01a0\n>\3>\6>\u01a3\n>\r>\16>\u01a4\3?\3?\5?\u01a9\n")
        buf.write("?\3@\3@\3@\3A\3A\7A\u01b0\nA\fA\16A\u01b3\13A\3A\3A\3")
        buf.write("A\3B\3B\5B\u01ba\nB\3B\3B\3B\7B\u01bf\nB\fB\16B\u01c2")
        buf.write("\13B\3C\3C\3D\3D\3E\3E\3F\3F\3F\3G\3G\7G\u01cf\nG\fG\16")
        buf.write("G\u01d2\13G\3G\3G\5G\u01d6\nG\3G\3G\3H\3H\7H\u01dc\nH")
        buf.write("\fH\16H\u01df\13H\3H\3H\3H\3I\3I\3I\3\u00a5\2J\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w\2y\2{")
        buf.write("\2}\2\177\2\u0081=\u0083>\u0085\2\u0087\2\u0089\2\u008b")
        buf.write("\2\u008d?\u008f@\u0091A\3\2\f\5\2\13\f\16\17\"\"\4\2\f")
        buf.write("\f\17\17\3\2\62;\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\t\2")
        buf.write("$$^^ddhhppttvv\4\2C\\c|\6\2\f\f\17\17GHQQ\3\2$$\2\u01f1")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\3\u0093\3\2\2\2\5\u0099\3\2\2\2\7\u00b8\3\2\2\2\t\u00bc")
        buf.write("\3\2\2\2\13\u00c4\3\2\2\2\r\u00ca\3\2\2\2\17\u00d0\3\2")
        buf.write("\2\2\21\u00d9\3\2\2\2\23\u00dc\3\2\2\2\25\u00df\3\2\2")
        buf.write("\2\27\u00e4\3\2\2\2\31\u00ec\3\2\2\2\33\u00f0\3\2\2\2")
        buf.write("\35\u00f6\3\2\2\2\37\u00fa\3\2\2\2!\u0101\3\2\2\2#\u0106")
        buf.write("\3\2\2\2%\u010a\3\2\2\2\'\u0111\3\2\2\2)\u0116\3\2\2\2")
        buf.write("+\u011c\3\2\2\2-\u0121\3\2\2\2/\u0125\3\2\2\2\61\u012a")
        buf.write("\3\2\2\2\63\u0130\3\2\2\2\65\u0137\3\2\2\2\67\u013a\3")
        buf.write("\2\2\29\u0141\3\2\2\2;\u0143\3\2\2\2=\u0145\3\2\2\2?\u0147")
        buf.write("\3\2\2\2A\u0149\3\2\2\2C\u014b\3\2\2\2E\u014d\3\2\2\2")
        buf.write("G\u014f\3\2\2\2I\u0152\3\2\2\2K\u0155\3\2\2\2M\u0158\3")
        buf.write("\2\2\2O\u015a\3\2\2\2Q\u015d\3\2\2\2S\u015f\3\2\2\2U\u0162")
        buf.write("\3\2\2\2W\u0164\3\2\2\2Y\u0167\3\2\2\2[\u0169\3\2\2\2")
        buf.write("]\u016c\3\2\2\2_\u016f\3\2\2\2a\u0171\3\2\2\2c\u0173\3")
        buf.write("\2\2\2e\u0175\3\2\2\2g\u0177\3\2\2\2i\u0179\3\2\2\2k\u017b")
        buf.write("\3\2\2\2m\u017d\3\2\2\2o\u017f\3\2\2\2q\u0181\3\2\2\2")
        buf.write("s\u0184\3\2\2\2u\u0192\3\2\2\2w\u0194\3\2\2\2y\u0196\3")
        buf.write("\2\2\2{\u019d\3\2\2\2}\u01a8\3\2\2\2\177\u01aa\3\2\2\2")
        buf.write("\u0081\u01ad\3\2\2\2\u0083\u01b9\3\2\2\2\u0085\u01c3\3")
        buf.write("\2\2\2\u0087\u01c5\3\2\2\2\u0089\u01c7\3\2\2\2\u008b\u01c9")
        buf.write("\3\2\2\2\u008d\u01cc\3\2\2\2\u008f\u01d9\3\2\2\2\u0091")
        buf.write("\u01e3\3\2\2\2\u0093\u0094\7o\2\2\u0094\u0095\7c\2\2\u0095")
        buf.write("\u0096\7k\2\2\u0096\u0097\7p\2\2\u0097\4\3\2\2\2\u0098")
        buf.write("\u009a\t\2\2\2\u0099\u0098\3\2\2\2\u009a\u009b\3\2\2\2")
        buf.write("\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009d\3")
        buf.write("\2\2\2\u009d\u009e\b\3\2\2\u009e\6\3\2\2\2\u009f\u00a0")
        buf.write("\7\61\2\2\u00a0\u00a1\7,\2\2\u00a1\u00a5\3\2\2\2\u00a2")
        buf.write("\u00a4\13\2\2\2\u00a3\u00a2\3\2\2\2\u00a4\u00a7\3\2\2")
        buf.write("\2\u00a5\u00a6\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00a8")
        buf.write("\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a8\u00a9\7,\2\2\u00a9")
        buf.write("\u00b9\7\61\2\2\u00aa\u00ae\7%\2\2\u00ab\u00ad\n\3\2\2")
        buf.write("\u00ac\u00ab\3\2\2\2\u00ad\u00b0\3\2\2\2\u00ae\u00ac\3")
        buf.write("\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b6\3\2\2\2\u00b0\u00ae")
        buf.write("\3\2\2\2\u00b1\u00b3\7\17\2\2\u00b2\u00b1\3\2\2\2\u00b2")
        buf.write("\u00b3\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b7\7\f\2\2")
        buf.write("\u00b5\u00b7\7\2\2\3\u00b6\u00b2\3\2\2\2\u00b6\u00b5\3")
        buf.write("\2\2\2\u00b7\u00b9\3\2\2\2\u00b8\u009f\3\2\2\2\u00b8\u00aa")
        buf.write("\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb\b\4\2\2\u00bb")
        buf.write("\b\3\2\2\2\u00bc\u00bd\7d\2\2\u00bd\u00be\7q\2\2\u00be")
        buf.write("\u00bf\7q\2\2\u00bf\u00c0\7n\2\2\u00c0\u00c1\7g\2\2\u00c1")
        buf.write("\u00c2\7c\2\2\u00c2\u00c3\7p\2\2\u00c3\n\3\2\2\2\u00c4")
        buf.write("\u00c5\7d\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7\7g\2\2\u00c7")
        buf.write("\u00c8\7c\2\2\u00c8\u00c9\7m\2\2\u00c9\f\3\2\2\2\u00ca")
        buf.write("\u00cb\7e\2\2\u00cb\u00cc\7n\2\2\u00cc\u00cd\7c\2\2\u00cd")
        buf.write("\u00ce\7u\2\2\u00ce\u00cf\7u\2\2\u00cf\16\3\2\2\2\u00d0")
        buf.write("\u00d1\7e\2\2\u00d1\u00d2\7q\2\2\u00d2\u00d3\7p\2\2\u00d3")
        buf.write("\u00d4\7v\2\2\u00d4\u00d5\7k\2\2\u00d5\u00d6\7p\2\2\u00d6")
        buf.write("\u00d7\7w\2\2\u00d7\u00d8\7g\2\2\u00d8\20\3\2\2\2\u00d9")
        buf.write("\u00da\7f\2\2\u00da\u00db\7q\2\2\u00db\22\3\2\2\2\u00dc")
        buf.write("\u00dd\7k\2\2\u00dd\u00de\7h\2\2\u00de\24\3\2\2\2\u00df")
        buf.write("\u00e0\7g\2\2\u00e0\u00e1\7n\2\2\u00e1\u00e2\7u\2\2\u00e2")
        buf.write("\u00e3\7g\2\2\u00e3\26\3\2\2\2\u00e4\u00e5\7g\2\2\u00e5")
        buf.write("\u00e6\7z\2\2\u00e6\u00e7\7v\2\2\u00e7\u00e8\7g\2\2\u00e8")
        buf.write("\u00e9\7p\2\2\u00e9\u00ea\7f\2\2\u00ea\u00eb\7u\2\2\u00eb")
        buf.write("\30\3\2\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee\7p\2\2\u00ee")
        buf.write("\u00ef\7v\2\2\u00ef\32\3\2\2\2\u00f0\u00f1\7h\2\2\u00f1")
        buf.write("\u00f2\7n\2\2\u00f2\u00f3\7q\2\2\u00f3\u00f4\7c\2\2\u00f4")
        buf.write("\u00f5\7v\2\2\u00f5\34\3\2\2\2\u00f6\u00f7\7p\2\2\u00f7")
        buf.write("\u00f8\7g\2\2\u00f8\u00f9\7y\2\2\u00f9\36\3\2\2\2\u00fa")
        buf.write("\u00fb\7u\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd\7t\2\2\u00fd")
        buf.write("\u00fe\7k\2\2\u00fe\u00ff\7p\2\2\u00ff\u0100\7i\2\2\u0100")
        buf.write(" \3\2\2\2\u0101\u0102\7v\2\2\u0102\u0103\7j\2\2\u0103")
        buf.write("\u0104\7g\2\2\u0104\u0105\7p\2\2\u0105\"\3\2\2\2\u0106")
        buf.write("\u0107\7h\2\2\u0107\u0108\7q\2\2\u0108\u0109\7t\2\2\u0109")
        buf.write("$\3\2\2\2\u010a\u010b\7t\2\2\u010b\u010c\7g\2\2\u010c")
        buf.write("\u010d\7v\2\2\u010d\u010e\7w\2\2\u010e\u010f\7t\2\2\u010f")
        buf.write("\u0110\7p\2\2\u0110&\3\2\2\2\u0111\u0112\7v\2\2\u0112")
        buf.write("\u0113\7t\2\2\u0113\u0114\7w\2\2\u0114\u0115\7g\2\2\u0115")
        buf.write("(\3\2\2\2\u0116\u0117\7h\2\2\u0117\u0118\7c\2\2\u0118")
        buf.write("\u0119\7n\2\2\u0119\u011a\7u\2\2\u011a\u011b\7g\2\2\u011b")
        buf.write("*\3\2\2\2\u011c\u011d\7x\2\2\u011d\u011e\7q\2\2\u011e")
        buf.write("\u011f\7k\2\2\u011f\u0120\7f\2\2\u0120,\3\2\2\2\u0121")
        buf.write("\u0122\7p\2\2\u0122\u0123\7k\2\2\u0123\u0124\7n\2\2\u0124")
        buf.write(".\3\2\2\2\u0125\u0126\7v\2\2\u0126\u0127\7j\2\2\u0127")
        buf.write("\u0128\7k\2\2\u0128\u0129\7u\2\2\u0129\60\3\2\2\2\u012a")
        buf.write("\u012b\7h\2\2\u012b\u012c\7k\2\2\u012c\u012d\7p\2\2\u012d")
        buf.write("\u012e\7c\2\2\u012e\u012f\7n\2\2\u012f\62\3\2\2\2\u0130")
        buf.write("\u0131\7u\2\2\u0131\u0132\7v\2\2\u0132\u0133\7c\2\2\u0133")
        buf.write("\u0134\7v\2\2\u0134\u0135\7k\2\2\u0135\u0136\7e\2\2\u0136")
        buf.write("\64\3\2\2\2\u0137\u0138\7v\2\2\u0138\u0139\7q\2\2\u0139")
        buf.write("\66\3\2\2\2\u013a\u013b\7f\2\2\u013b\u013c\7q\2\2\u013c")
        buf.write("\u013d\7y\2\2\u013d\u013e\7p\2\2\u013e\u013f\7v\2\2\u013f")
        buf.write("\u0140\7q\2\2\u01408\3\2\2\2\u0141\u0142\7-\2\2\u0142")
        buf.write(":\3\2\2\2\u0143\u0144\7/\2\2\u0144<\3\2\2\2\u0145\u0146")
        buf.write("\7,\2\2\u0146>\3\2\2\2\u0147\u0148\7\61\2\2\u0148@\3\2")
        buf.write("\2\2\u0149\u014a\7^\2\2\u014aB\3\2\2\2\u014b\u014c\7\'")
        buf.write("\2\2\u014cD\3\2\2\2\u014d\u014e\7#\2\2\u014eF\3\2\2\2")
        buf.write("\u014f\u0150\7(\2\2\u0150\u0151\7(\2\2\u0151H\3\2\2\2")
        buf.write("\u0152\u0153\7~\2\2\u0153\u0154\7~\2\2\u0154J\3\2\2\2")
        buf.write("\u0155\u0156\7?\2\2\u0156\u0157\7?\2\2\u0157L\3\2\2\2")
        buf.write("\u0158\u0159\7?\2\2\u0159N\3\2\2\2\u015a\u015b\7#\2\2")
        buf.write("\u015b\u015c\7?\2\2\u015cP\3\2\2\2\u015d\u015e\7>\2\2")
        buf.write("\u015eR\3\2\2\2\u015f\u0160\7>\2\2\u0160\u0161\7?\2\2")
        buf.write("\u0161T\3\2\2\2\u0162\u0163\7@\2\2\u0163V\3\2\2\2\u0164")
        buf.write("\u0165\7@\2\2\u0165\u0166\7?\2\2\u0166X\3\2\2\2\u0167")
        buf.write("\u0168\7`\2\2\u0168Z\3\2\2\2\u0169\u016a\7<\2\2\u016a")
        buf.write("\u016b\7<\2\2\u016b\\\3\2\2\2\u016c\u016d\7<\2\2\u016d")
        buf.write("\u016e\7?\2\2\u016e^\3\2\2\2\u016f\u0170\7*\2\2\u0170")
        buf.write("`\3\2\2\2\u0171\u0172\7+\2\2\u0172b\3\2\2\2\u0173\u0174")
        buf.write("\7]\2\2\u0174d\3\2\2\2\u0175\u0176\7_\2\2\u0176f\3\2\2")
        buf.write("\2\u0177\u0178\7\60\2\2\u0178h\3\2\2\2\u0179\u017a\7.")
        buf.write("\2\2\u017aj\3\2\2\2\u017b\u017c\7=\2\2\u017cl\3\2\2\2")
        buf.write("\u017d\u017e\7<\2\2\u017en\3\2\2\2\u017f\u0180\7}\2\2")
        buf.write("\u0180p\3\2\2\2\u0181\u0182\7\177\2\2\u0182r\3\2\2\2\u0183")
        buf.write("\u0185\5\u0087D\2\u0184\u0183\3\2\2\2\u0185\u0186\3\2")
        buf.write("\2\2\u0186\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187t\3")
        buf.write("\2\2\2\u0188\u0189\5w<\2\u0189\u018a\5y=\2\u018a\u0193")
        buf.write("\3\2\2\2\u018b\u018c\5w<\2\u018c\u018d\5{>\2\u018d\u0193")
        buf.write("\3\2\2\2\u018e\u018f\5w<\2\u018f\u0190\5y=\2\u0190\u0191")
        buf.write("\5{>\2\u0191\u0193\3\2\2\2\u0192\u0188\3\2\2\2\u0192\u018b")
        buf.write("\3\2\2\2\u0192\u018e\3\2\2\2\u0193v\3\2\2\2\u0194\u0195")
        buf.write("\5s:\2\u0195x\3\2\2\2\u0196\u019a\7\60\2\2\u0197\u0199")
        buf.write("\t\4\2\2\u0198\u0197\3\2\2\2\u0199\u019c\3\2\2\2\u019a")
        buf.write("\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019bz\3\2\2\2\u019c")
        buf.write("\u019a\3\2\2\2\u019d\u019f\t\5\2\2\u019e\u01a0\t\6\2\2")
        buf.write("\u019f\u019e\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a2\3")
        buf.write("\2\2\2\u01a1\u01a3\t\4\2\2\u01a2\u01a1\3\2\2\2\u01a3\u01a4")
        buf.write("\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5")
        buf.write("|\3\2\2\2\u01a6\u01a9\n\7\2\2\u01a7\u01a9\5\177@\2\u01a8")
        buf.write("\u01a6\3\2\2\2\u01a8\u01a7\3\2\2\2\u01a9~\3\2\2\2\u01aa")
        buf.write("\u01ab\7^\2\2\u01ab\u01ac\t\b\2\2\u01ac\u0080\3\2\2\2")
        buf.write("\u01ad\u01b1\7$\2\2\u01ae\u01b0\5}?\2\u01af\u01ae\3\2")
        buf.write("\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1\u01b2")
        buf.write("\3\2\2\2\u01b2\u01b4\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b4")
        buf.write("\u01b5\7$\2\2\u01b5\u01b6\bA\3\2\u01b6\u0082\3\2\2\2\u01b7")
        buf.write("\u01ba\5\u0085C\2\u01b8\u01ba\5\u0089E\2\u01b9\u01b7\3")
        buf.write("\2\2\2\u01b9\u01b8\3\2\2\2\u01ba\u01c0\3\2\2\2\u01bb\u01bf")
        buf.write("\5\u0085C\2\u01bc\u01bf\5\u0087D\2\u01bd\u01bf\5\u0089")
        buf.write("E\2\u01be\u01bb\3\2\2\2\u01be\u01bc\3\2\2\2\u01be\u01bd")
        buf.write("\3\2\2\2\u01bf\u01c2\3\2\2\2\u01c0\u01be\3\2\2\2\u01c0")
        buf.write("\u01c1\3\2\2\2\u01c1\u0084\3\2\2\2\u01c2\u01c0\3\2\2\2")
        buf.write("\u01c3\u01c4\t\t\2\2\u01c4\u0086\3\2\2\2\u01c5\u01c6\t")
        buf.write("\4\2\2\u01c6\u0088\3\2\2\2\u01c7\u01c8\7a\2\2\u01c8\u008a")
        buf.write("\3\2\2\2\u01c9\u01ca\7^\2\2\u01ca\u01cb\n\b\2\2\u01cb")
        buf.write("\u008c\3\2\2\2\u01cc\u01d0\7$\2\2\u01cd\u01cf\5}?\2\u01ce")
        buf.write("\u01cd\3\2\2\2\u01cf\u01d2\3\2\2\2\u01d0\u01ce\3\2\2\2")
        buf.write("\u01d0\u01d1\3\2\2\2\u01d1\u01d5\3\2\2\2\u01d2\u01d0\3")
        buf.write("\2\2\2\u01d3\u01d6\t\n\2\2\u01d4\u01d6\n\13\2\2\u01d5")
        buf.write("\u01d3\3\2\2\2\u01d5\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2")
        buf.write("\u01d7\u01d8\bG\4\2\u01d8\u008e\3\2\2\2\u01d9\u01dd\7")
        buf.write("$\2\2\u01da\u01dc\5}?\2\u01db\u01da\3\2\2\2\u01dc\u01df")
        buf.write("\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01de\3\2\2\2\u01de")
        buf.write("\u01e0\3\2\2\2\u01df\u01dd\3\2\2\2\u01e0\u01e1\5\u008b")
        buf.write("F\2\u01e1\u01e2\bH\5\2\u01e2\u0090\3\2\2\2\u01e3\u01e4")
        buf.write("\13\2\2\2\u01e4\u01e5\bI\6\2\u01e5\u0092\3\2\2\2\26\2")
        buf.write("\u009b\u00a5\u00ae\u00b2\u00b6\u00b8\u0186\u0192\u019a")
        buf.write("\u019f\u01a4\u01a8\u01b1\u01b9\u01be\u01c0\u01d0\u01d5")
        buf.write("\u01dd\7\b\2\2\3A\2\3G\3\3H\4\3I\5")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    WS = 2
    COMMENT = 3
    BOOLEAN = 4
    BREAK = 5
    CLASS = 6
    CONTINUE = 7
    DO = 8
    IF = 9
    ELSE = 10
    EXTENDS = 11
    INT = 12
    FLOAT = 13
    NEW = 14
    STRING = 15
    THEN = 16
    FOR = 17
    RETURN = 18
    TRUE = 19
    FALSE = 20
    VOID = 21
    NIL = 22
    THIS = 23
    FINAL = 24
    STATIC = 25
    TO = 26
    DOWNTO = 27
    ADD = 28
    SUB = 29
    MUL = 30
    DIV = 31
    IDIV = 32
    MOD = 33
    NOT = 34
    AND = 35
    OR = 36
    EQQ = 37
    EQ = 38
    NOTEQ = 39
    LT = 40
    LTEQ = 41
    GT = 42
    GTEQ = 43
    CONCAT = 44
    SCOPE = 45
    ASSIGN = 46
    LB = 47
    RB = 48
    LSB = 49
    RSB = 50
    DOT = 51
    COMMA = 52
    SEMI = 53
    COLON = 54
    LP = 55
    RP = 56
    INTLIT = 57
    FLOATLIT = 58
    STRING_LIT = 59
    ID = 60
    UNCLOSE_STRING = 61
    ILLEGAL_ESCAPE = 62
    ERROR_TOKEN = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'boolean'", "'break'", "'class'", "'continue'", "'do'", 
            "'if'", "'else'", "'extends'", "'int'", "'float'", "'new'", 
            "'string'", "'then'", "'for'", "'return'", "'true'", "'false'", 
            "'void'", "'nil'", "'this'", "'final'", "'static'", "'to'", 
            "'downto'", "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", "'!'", 
            "'&&'", "'||'", "'=='", "'='", "'!='", "'<'", "'<='", "'>'", 
            "'>='", "'^'", "'::'", "':='", "'('", "')'", "'['", "']'", "'.'", 
            "','", "';'", "':'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "COMMENT", "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", 
            "IF", "ELSE", "EXTENDS", "INT", "FLOAT", "NEW", "STRING", "THEN", 
            "FOR", "RETURN", "TRUE", "FALSE", "VOID", "NIL", "THIS", "FINAL", 
            "STATIC", "TO", "DOWNTO", "ADD", "SUB", "MUL", "DIV", "IDIV", 
            "MOD", "NOT", "AND", "OR", "EQQ", "EQ", "NOTEQ", "LT", "LTEQ", 
            "GT", "GTEQ", "CONCAT", "SCOPE", "ASSIGN", "LB", "RB", "LSB", 
            "RSB", "DOT", "COMMA", "SEMI", "COLON", "LP", "RP", "INTLIT", 
            "FLOATLIT", "STRING_LIT", "ID", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_TOKEN" ]

    ruleNames = [ "T__0", "WS", "COMMENT", "BOOLEAN", "BREAK", "CLASS", 
                  "CONTINUE", "DO", "IF", "ELSE", "EXTENDS", "INT", "FLOAT", 
                  "NEW", "STRING", "THEN", "FOR", "RETURN", "TRUE", "FALSE", 
                  "VOID", "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", 
                  "ADD", "SUB", "MUL", "DIV", "IDIV", "MOD", "NOT", "AND", 
                  "OR", "EQQ", "EQ", "NOTEQ", "LT", "LTEQ", "GT", "GTEQ", 
                  "CONCAT", "SCOPE", "ASSIGN", "LB", "RB", "LSB", "RSB", 
                  "DOT", "COMMA", "SEMI", "COLON", "LP", "RP", "INTLIT", 
                  "FLOATLIT", "INT_PART", "DEC_PART", "EXP_PART", "STR_CHAR", 
                  "ESC_SEQUENCE", "STRING_LIT", "ID", "LETTER", "DIGIT", 
                  "UNDERSCORE", "ILL_ESCAPE", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_TOKEN" ]

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
            actions[63] = self.STRING_LIT_action 
            actions[69] = self.UNCLOSE_STRING_action 
            actions[70] = self.ILLEGAL_ESCAPE_action 
            actions[71] = self.ERROR_TOKEN_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                self.text = self.text[1:-1]
                
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	err_char = ['\r','\n',EOFError]
            	if self.text[-1] in err_char:
            		raise UncloseString(self.text[1:-1])
            	else:
            		raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                raise IllegalEscape(self.text[1:])

     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise ErrorToken(self.text)

     


