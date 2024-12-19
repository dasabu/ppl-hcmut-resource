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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u01e1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3")
        buf.write("&\3&\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3*\3+\3+\3,\3,\3,\3")
        buf.write("-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3")
        buf.write("\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\3")
        buf.write("8\39\39\3:\6:\u017f\n:\r:\16:\u0180\3;\3;\3;\3;\3;\3;")
        buf.write("\3;\3;\3;\3;\5;\u018d\n;\3<\3<\3=\3=\7=\u0193\n=\f=\16")
        buf.write("=\u0196\13=\3>\3>\5>\u019a\n>\3>\6>\u019d\n>\r>\16>\u019e")
        buf.write("\3?\3?\3?\3?\5?\u01a5\n?\3@\3@\3@\3A\3A\7A\u01ac\nA\f")
        buf.write("A\16A\u01af\13A\3A\3A\3A\3B\3B\5B\u01b6\nB\3B\3B\3B\7")
        buf.write("B\u01bb\nB\fB\16B\u01be\13B\3C\3C\3D\3D\3E\3E\3F\3F\3")
        buf.write("F\3G\3G\7G\u01cb\nG\fG\16G\u01ce\13G\3G\5G\u01d1\nG\3")
        buf.write("G\3G\3H\3H\7H\u01d7\nH\fH\16H\u01da\13H\3H\3H\3H\3I\3")
        buf.write("I\3I\4\u00a5\u00ae\2J\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64")
        buf.write("g\65i\66k\67m8o9q:s;u<w\2y\2{\2}\2\177\2\u0081=\u0083")
        buf.write(">\u0085?\u0087@\u0089A\u008b\2\u008dB\u008fC\u0091D\3")
        buf.write("\2\n\5\2\13\f\16\17\"\"\3\2\62;\4\2GGgg\4\2--//\6\2\n")
        buf.write("\f\16\17$$^^\t\2))^^ddhhppttvv\4\2C\\c|\4\3\n\f\16\17")
        buf.write("\2\u01ed\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write("\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3")
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o")
        buf.write("\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2\u0081\3\2")
        buf.write("\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2")
        buf.write("\u0089\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\3\u0093\3\2\2\2\5\u0099\3\2\2\2\7\u00b2\3\2\2")
        buf.write("\2\t\u00b6\3\2\2\2\13\u00be\3\2\2\2\r\u00c4\3\2\2\2\17")
        buf.write("\u00ca\3\2\2\2\21\u00d3\3\2\2\2\23\u00d6\3\2\2\2\25\u00d9")
        buf.write("\3\2\2\2\27\u00de\3\2\2\2\31\u00e6\3\2\2\2\33\u00ea\3")
        buf.write("\2\2\2\35\u00f0\3\2\2\2\37\u00f4\3\2\2\2!\u00fb\3\2\2")
        buf.write("\2#\u0100\3\2\2\2%\u0104\3\2\2\2\'\u010b\3\2\2\2)\u0110")
        buf.write("\3\2\2\2+\u0116\3\2\2\2-\u011b\3\2\2\2/\u011f\3\2\2\2")
        buf.write("\61\u0124\3\2\2\2\63\u012a\3\2\2\2\65\u0131\3\2\2\2\67")
        buf.write("\u0134\3\2\2\29\u013b\3\2\2\2;\u013d\3\2\2\2=\u013f\3")
        buf.write("\2\2\2?\u0141\3\2\2\2A\u0143\3\2\2\2C\u0145\3\2\2\2E\u0147")
        buf.write("\3\2\2\2G\u0149\3\2\2\2I\u014c\3\2\2\2K\u014f\3\2\2\2")
        buf.write("M\u0152\3\2\2\2O\u0154\3\2\2\2Q\u0157\3\2\2\2S\u0159\3")
        buf.write("\2\2\2U\u015c\3\2\2\2W\u015e\3\2\2\2Y\u0161\3\2\2\2[\u0163")
        buf.write("\3\2\2\2]\u0166\3\2\2\2_\u0169\3\2\2\2a\u016b\3\2\2\2")
        buf.write("c\u016d\3\2\2\2e\u016f\3\2\2\2g\u0171\3\2\2\2i\u0173\3")
        buf.write("\2\2\2k\u0175\3\2\2\2m\u0177\3\2\2\2o\u0179\3\2\2\2q\u017b")
        buf.write("\3\2\2\2s\u017e\3\2\2\2u\u018c\3\2\2\2w\u018e\3\2\2\2")
        buf.write("y\u0190\3\2\2\2{\u0197\3\2\2\2}\u01a4\3\2\2\2\177\u01a6")
        buf.write("\3\2\2\2\u0081\u01a9\3\2\2\2\u0083\u01b5\3\2\2\2\u0085")
        buf.write("\u01bf\3\2\2\2\u0087\u01c1\3\2\2\2\u0089\u01c3\3\2\2\2")
        buf.write("\u008b\u01c5\3\2\2\2\u008d\u01c8\3\2\2\2\u008f\u01d4\3")
        buf.write("\2\2\2\u0091\u01de\3\2\2\2\u0093\u0094\7o\2\2\u0094\u0095")
        buf.write("\7c\2\2\u0095\u0096\7k\2\2\u0096\u0097\7p\2\2\u0097\4")
        buf.write("\3\2\2\2\u0098\u009a\t\2\2\2\u0099\u0098\3\2\2\2\u009a")
        buf.write("\u009b\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2")
        buf.write("\u009c\u009d\3\2\2\2\u009d\u009e\b\3\2\2\u009e\6\3\2\2")
        buf.write("\2\u009f\u00a0\7\61\2\2\u00a0\u00a1\7,\2\2\u00a1\u00a5")
        buf.write("\3\2\2\2\u00a2\u00a4\13\2\2\2\u00a3\u00a2\3\2\2\2\u00a4")
        buf.write("\u00a7\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a5\u00a3\3\2\2\2")
        buf.write("\u00a6\u00a8\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a8\u00a9\7")
        buf.write(",\2\2\u00a9\u00b3\7\61\2\2\u00aa\u00ae\7%\2\2\u00ab\u00ad")
        buf.write("\13\2\2\2\u00ac\u00ab\3\2\2\2\u00ad\u00b0\3\2\2\2\u00ae")
        buf.write("\u00af\3\2\2\2\u00ae\u00ac\3\2\2\2\u00af\u00b1\3\2\2\2")
        buf.write("\u00b0\u00ae\3\2\2\2\u00b1\u00b3\7\2\2\3\u00b2\u009f\3")
        buf.write("\2\2\2\u00b2\u00aa\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5")
        buf.write("\b\4\2\2\u00b5\b\3\2\2\2\u00b6\u00b7\7d\2\2\u00b7\u00b8")
        buf.write("\7q\2\2\u00b8\u00b9\7q\2\2\u00b9\u00ba\7n\2\2\u00ba\u00bb")
        buf.write("\7g\2\2\u00bb\u00bc\7c\2\2\u00bc\u00bd\7p\2\2\u00bd\n")
        buf.write("\3\2\2\2\u00be\u00bf\7d\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1")
        buf.write("\7g\2\2\u00c1\u00c2\7c\2\2\u00c2\u00c3\7m\2\2\u00c3\f")
        buf.write("\3\2\2\2\u00c4\u00c5\7e\2\2\u00c5\u00c6\7n\2\2\u00c6\u00c7")
        buf.write("\7c\2\2\u00c7\u00c8\7u\2\2\u00c8\u00c9\7u\2\2\u00c9\16")
        buf.write("\3\2\2\2\u00ca\u00cb\7e\2\2\u00cb\u00cc\7q\2\2\u00cc\u00cd")
        buf.write("\7p\2\2\u00cd\u00ce\7v\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0")
        buf.write("\7p\2\2\u00d0\u00d1\7w\2\2\u00d1\u00d2\7g\2\2\u00d2\20")
        buf.write("\3\2\2\2\u00d3\u00d4\7f\2\2\u00d4\u00d5\7q\2\2\u00d5\22")
        buf.write("\3\2\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8\7h\2\2\u00d8\24")
        buf.write("\3\2\2\2\u00d9\u00da\7g\2\2\u00da\u00db\7n\2\2\u00db\u00dc")
        buf.write("\7u\2\2\u00dc\u00dd\7g\2\2\u00dd\26\3\2\2\2\u00de\u00df")
        buf.write("\7g\2\2\u00df\u00e0\7z\2\2\u00e0\u00e1\7v\2\2\u00e1\u00e2")
        buf.write("\7g\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4\7f\2\2\u00e4\u00e5")
        buf.write("\7u\2\2\u00e5\30\3\2\2\2\u00e6\u00e7\7k\2\2\u00e7\u00e8")
        buf.write("\7p\2\2\u00e8\u00e9\7v\2\2\u00e9\32\3\2\2\2\u00ea\u00eb")
        buf.write("\7h\2\2\u00eb\u00ec\7n\2\2\u00ec\u00ed\7q\2\2\u00ed\u00ee")
        buf.write("\7c\2\2\u00ee\u00ef\7v\2\2\u00ef\34\3\2\2\2\u00f0\u00f1")
        buf.write("\7p\2\2\u00f1\u00f2\7g\2\2\u00f2\u00f3\7y\2\2\u00f3\36")
        buf.write("\3\2\2\2\u00f4\u00f5\7u\2\2\u00f5\u00f6\7v\2\2\u00f6\u00f7")
        buf.write("\7t\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9\7p\2\2\u00f9\u00fa")
        buf.write("\7i\2\2\u00fa \3\2\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd")
        buf.write("\7j\2\2\u00fd\u00fe\7g\2\2\u00fe\u00ff\7p\2\2\u00ff\"")
        buf.write("\3\2\2\2\u0100\u0101\7h\2\2\u0101\u0102\7q\2\2\u0102\u0103")
        buf.write("\7t\2\2\u0103$\3\2\2\2\u0104\u0105\7t\2\2\u0105\u0106")
        buf.write("\7g\2\2\u0106\u0107\7v\2\2\u0107\u0108\7w\2\2\u0108\u0109")
        buf.write("\7t\2\2\u0109\u010a\7p\2\2\u010a&\3\2\2\2\u010b\u010c")
        buf.write("\7v\2\2\u010c\u010d\7t\2\2\u010d\u010e\7w\2\2\u010e\u010f")
        buf.write("\7g\2\2\u010f(\3\2\2\2\u0110\u0111\7h\2\2\u0111\u0112")
        buf.write("\7c\2\2\u0112\u0113\7n\2\2\u0113\u0114\7u\2\2\u0114\u0115")
        buf.write("\7g\2\2\u0115*\3\2\2\2\u0116\u0117\7x\2\2\u0117\u0118")
        buf.write("\7q\2\2\u0118\u0119\7k\2\2\u0119\u011a\7f\2\2\u011a,\3")
        buf.write("\2\2\2\u011b\u011c\7p\2\2\u011c\u011d\7k\2\2\u011d\u011e")
        buf.write("\7n\2\2\u011e.\3\2\2\2\u011f\u0120\7v\2\2\u0120\u0121")
        buf.write("\7j\2\2\u0121\u0122\7k\2\2\u0122\u0123\7u\2\2\u0123\60")
        buf.write("\3\2\2\2\u0124\u0125\7h\2\2\u0125\u0126\7k\2\2\u0126\u0127")
        buf.write("\7p\2\2\u0127\u0128\7c\2\2\u0128\u0129\7n\2\2\u0129\62")
        buf.write("\3\2\2\2\u012a\u012b\7u\2\2\u012b\u012c\7v\2\2\u012c\u012d")
        buf.write("\7c\2\2\u012d\u012e\7v\2\2\u012e\u012f\7k\2\2\u012f\u0130")
        buf.write("\7e\2\2\u0130\64\3\2\2\2\u0131\u0132\7v\2\2\u0132\u0133")
        buf.write("\7q\2\2\u0133\66\3\2\2\2\u0134\u0135\7f\2\2\u0135\u0136")
        buf.write("\7q\2\2\u0136\u0137\7y\2\2\u0137\u0138\7p\2\2\u0138\u0139")
        buf.write("\7v\2\2\u0139\u013a\7q\2\2\u013a8\3\2\2\2\u013b\u013c")
        buf.write("\7-\2\2\u013c:\3\2\2\2\u013d\u013e\7/\2\2\u013e<\3\2\2")
        buf.write("\2\u013f\u0140\7,\2\2\u0140>\3\2\2\2\u0141\u0142\7\61")
        buf.write("\2\2\u0142@\3\2\2\2\u0143\u0144\7^\2\2\u0144B\3\2\2\2")
        buf.write("\u0145\u0146\7\'\2\2\u0146D\3\2\2\2\u0147\u0148\7#\2\2")
        buf.write("\u0148F\3\2\2\2\u0149\u014a\7(\2\2\u014a\u014b\7(\2\2")
        buf.write("\u014bH\3\2\2\2\u014c\u014d\7~\2\2\u014d\u014e\7~\2\2")
        buf.write("\u014eJ\3\2\2\2\u014f\u0150\7?\2\2\u0150\u0151\7?\2\2")
        buf.write("\u0151L\3\2\2\2\u0152\u0153\7?\2\2\u0153N\3\2\2\2\u0154")
        buf.write("\u0155\7#\2\2\u0155\u0156\7?\2\2\u0156P\3\2\2\2\u0157")
        buf.write("\u0158\7>\2\2\u0158R\3\2\2\2\u0159\u015a\7>\2\2\u015a")
        buf.write("\u015b\7?\2\2\u015bT\3\2\2\2\u015c\u015d\7@\2\2\u015d")
        buf.write("V\3\2\2\2\u015e\u015f\7@\2\2\u015f\u0160\7?\2\2\u0160")
        buf.write("X\3\2\2\2\u0161\u0162\7`\2\2\u0162Z\3\2\2\2\u0163\u0164")
        buf.write("\7<\2\2\u0164\u0165\7<\2\2\u0165\\\3\2\2\2\u0166\u0167")
        buf.write("\7<\2\2\u0167\u0168\7?\2\2\u0168^\3\2\2\2\u0169\u016a")
        buf.write("\7*\2\2\u016a`\3\2\2\2\u016b\u016c\7+\2\2\u016cb\3\2\2")
        buf.write("\2\u016d\u016e\7]\2\2\u016ed\3\2\2\2\u016f\u0170\7_\2")
        buf.write("\2\u0170f\3\2\2\2\u0171\u0172\7\60\2\2\u0172h\3\2\2\2")
        buf.write("\u0173\u0174\7.\2\2\u0174j\3\2\2\2\u0175\u0176\7=\2\2")
        buf.write("\u0176l\3\2\2\2\u0177\u0178\7<\2\2\u0178n\3\2\2\2\u0179")
        buf.write("\u017a\7}\2\2\u017ap\3\2\2\2\u017b\u017c\7\177\2\2\u017c")
        buf.write("r\3\2\2\2\u017d\u017f\5\u0087D\2\u017e\u017d\3\2\2\2\u017f")
        buf.write("\u0180\3\2\2\2\u0180\u017e\3\2\2\2\u0180\u0181\3\2\2\2")
        buf.write("\u0181t\3\2\2\2\u0182\u0183\5w<\2\u0183\u0184\5y=\2\u0184")
        buf.write("\u018d\3\2\2\2\u0185\u0186\5w<\2\u0186\u0187\5{>\2\u0187")
        buf.write("\u018d\3\2\2\2\u0188\u0189\5w<\2\u0189\u018a\5y=\2\u018a")
        buf.write("\u018b\5{>\2\u018b\u018d\3\2\2\2\u018c\u0182\3\2\2\2\u018c")
        buf.write("\u0185\3\2\2\2\u018c\u0188\3\2\2\2\u018dv\3\2\2\2\u018e")
        buf.write("\u018f\5s:\2\u018fx\3\2\2\2\u0190\u0194\7\60\2\2\u0191")
        buf.write("\u0193\t\3\2\2\u0192\u0191\3\2\2\2\u0193\u0196\3\2\2\2")
        buf.write("\u0194\u0192\3\2\2\2\u0194\u0195\3\2\2\2\u0195z\3\2\2")
        buf.write("\2\u0196\u0194\3\2\2\2\u0197\u0199\t\4\2\2\u0198\u019a")
        buf.write("\t\5\2\2\u0199\u0198\3\2\2\2\u0199\u019a\3\2\2\2\u019a")
        buf.write("\u019c\3\2\2\2\u019b\u019d\t\3\2\2\u019c\u019b\3\2\2\2")
        buf.write("\u019d\u019e\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019f\3")
        buf.write("\2\2\2\u019f|\3\2\2\2\u01a0\u01a5\n\6\2\2\u01a1\u01a5")
        buf.write("\5\177@\2\u01a2\u01a3\7)\2\2\u01a3\u01a5\7$\2\2\u01a4")
        buf.write("\u01a0\3\2\2\2\u01a4\u01a1\3\2\2\2\u01a4\u01a2\3\2\2\2")
        buf.write("\u01a5~\3\2\2\2\u01a6\u01a7\7^\2\2\u01a7\u01a8\t\7\2\2")
        buf.write("\u01a8\u0080\3\2\2\2\u01a9\u01ad\7$\2\2\u01aa\u01ac\5")
        buf.write("}?\2\u01ab\u01aa\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad\u01ab")
        buf.write("\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01b0\3\2\2\2\u01af")
        buf.write("\u01ad\3\2\2\2\u01b0\u01b1\7$\2\2\u01b1\u01b2\bA\3\2\u01b2")
        buf.write("\u0082\3\2\2\2\u01b3\u01b6\5\u0085C\2\u01b4\u01b6\5\u0089")
        buf.write("E\2\u01b5\u01b3\3\2\2\2\u01b5\u01b4\3\2\2\2\u01b6\u01bc")
        buf.write("\3\2\2\2\u01b7\u01bb\5\u0085C\2\u01b8\u01bb\5\u0087D\2")
        buf.write("\u01b9\u01bb\5\u0089E\2\u01ba\u01b7\3\2\2\2\u01ba\u01b8")
        buf.write("\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bb\u01be\3\2\2\2\u01bc")
        buf.write("\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u0084\3\2\2\2")
        buf.write("\u01be\u01bc\3\2\2\2\u01bf\u01c0\t\b\2\2\u01c0\u0086\3")
        buf.write("\2\2\2\u01c1\u01c2\t\3\2\2\u01c2\u0088\3\2\2\2\u01c3\u01c4")
        buf.write("\7a\2\2\u01c4\u008a\3\2\2\2\u01c5\u01c6\7^\2\2\u01c6\u01c7")
        buf.write("\n\7\2\2\u01c7\u008c\3\2\2\2\u01c8\u01cc\7$\2\2\u01c9")
        buf.write("\u01cb\5}?\2\u01ca\u01c9\3\2\2\2\u01cb\u01ce\3\2\2\2\u01cc")
        buf.write("\u01ca\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01d0\3\2\2\2")
        buf.write("\u01ce\u01cc\3\2\2\2\u01cf\u01d1\t\t\2\2\u01d0\u01cf\3")
        buf.write("\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d3\bG\4\2\u01d3\u008e")
        buf.write("\3\2\2\2\u01d4\u01d8\7$\2\2\u01d5\u01d7\5}?\2\u01d6\u01d5")
        buf.write("\3\2\2\2\u01d7\u01da\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8")
        buf.write("\u01d9\3\2\2\2\u01d9\u01db\3\2\2\2\u01da\u01d8\3\2\2\2")
        buf.write("\u01db\u01dc\5\u008bF\2\u01dc\u01dd\bH\5\2\u01dd\u0090")
        buf.write("\3\2\2\2\u01de\u01df\13\2\2\2\u01df\u01e0\bI\6\2\u01e0")
        buf.write("\u0092\3\2\2\2\24\2\u009b\u00a5\u00ae\u00b2\u0180\u018c")
        buf.write("\u0194\u0199\u019e\u01a4\u01ad\u01b5\u01ba\u01bc\u01cc")
        buf.write("\u01d0\u01d8\7\b\2\2\3A\2\3G\3\3H\4\3I\5")
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
    LR = 47
    RR = 48
    LS = 49
    RS = 50
    DOT = 51
    COMMA = 52
    SEMI = 53
    COLON = 54
    LB = 55
    RB = 56
    INTLIT = 57
    FLOATLIT = 58
    STRING_LIT = 59
    ID = 60
    LETTER = 61
    DIGIT = 62
    UNDERSCORE = 63
    UNCLOSE_STRING = 64
    ILLEGAL_ESCAPE = 65
    ERROR_TOKEN = 66

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
            "','", "';'", "':'", "'{'", "'}'", "'_'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "COMMENT", "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", 
            "IF", "ELSE", "EXTENDS", "INT", "FLOAT", "NEW", "STRING", "THEN", 
            "FOR", "RETURN", "TRUE", "FALSE", "VOID", "NIL", "THIS", "FINAL", 
            "STATIC", "TO", "DOWNTO", "ADD", "SUB", "MUL", "DIV", "IDIV", 
            "MOD", "NOT", "AND", "OR", "EQQ", "EQ", "NOTEQ", "LT", "LTEQ", 
            "GT", "GTEQ", "CONCAT", "SCOPE", "ASSIGN", "LR", "RR", "LS", 
            "RS", "DOT", "COMMA", "SEMI", "COLON", "LB", "RB", "INTLIT", 
            "FLOATLIT", "STRING_LIT", "ID", "LETTER", "DIGIT", "UNDERSCORE", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    ruleNames = [ "T__0", "WS", "COMMENT", "BOOLEAN", "BREAK", "CLASS", 
                  "CONTINUE", "DO", "IF", "ELSE", "EXTENDS", "INT", "FLOAT", 
                  "NEW", "STRING", "THEN", "FOR", "RETURN", "TRUE", "FALSE", 
                  "VOID", "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", 
                  "ADD", "SUB", "MUL", "DIV", "IDIV", "MOD", "NOT", "AND", 
                  "OR", "EQQ", "EQ", "NOTEQ", "LT", "LTEQ", "GT", "GTEQ", 
                  "CONCAT", "SCOPE", "ASSIGN", "LR", "RR", "LS", "RS", "DOT", 
                  "COMMA", "SEMI", "COLON", "LB", "RB", "INTLIT", "FLOATLIT", 
                  "INT_PART", "DEC_PART", "EXP_PART", "STR_CHAR", "ESC_SEQUENCE", 
                  "STRING_LIT", "ID", "LETTER", "DIGIT", "UNDERSCORE", "ILL_ESCAPE", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

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

                self.text = self.text[1:]
                if self.text[-1] in "\b\t\n\f\r":
            	    self.text=self.text[:-1]

                raise UncloseString(self.text)

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                raise IllegalEscape(self.text[1:])

     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise ErrorToken(self.text)

     


