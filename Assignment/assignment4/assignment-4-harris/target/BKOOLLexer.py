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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u01bb\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3%\3")
        buf.write("%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3+\3+\3")
        buf.write("+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\3\66\6\66\u014d\n\66\r")
        buf.write("\66\16\66\u014e\3\66\3\66\3\67\3\67\7\67\u0155\n\67\f")
        buf.write("\67\16\67\u0158\13\67\3\67\3\67\38\38\38\38\78\u0160\n")
        buf.write("8\f8\168\u0163\138\38\38\38\38\38\39\69\u016b\n9\r9\16")
        buf.write("9\u016c\3:\6:\u0170\n:\r:\16:\u0171\3:\3:\5:\u0176\n:")
        buf.write("\3:\5:\u0179\n:\3;\3;\7;\u017d\n;\f;\16;\u0180\13;\3<")
        buf.write("\3<\5<\u0184\n<\3<\6<\u0187\n<\r<\16<\u0188\3=\3=\7=\u018d")
        buf.write("\n=\f=\16=\u0190\13=\3>\3>\5>\u0194\n>\3>\3>\3?\3?\6?")
        buf.write("\u019a\n?\r?\16?\u019b\3@\3@\3@\3A\3A\7A\u01a3\nA\fA\16")
        buf.write("A\u01a6\13A\3A\5A\u01a9\nA\3A\3A\3B\3B\7B\u01af\nB\fB")
        buf.write("\16B\u01b2\13B\3B\3B\3B\3B\3B\3C\3C\3C\3\u0161\2D\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u\2")
        buf.write("w\2y<{=}\2\177\2\u0081>\u0083?\u0085@\3\2\f\5\2\13\f\17")
        buf.write("\17\"\"\4\2\f\f\17\17\3\2\62;\4\2GGgg\4\2--//\5\2C\\a")
        buf.write("ac|\6\2\62;C\\aac|\6\2\f\f\17\17$$^^\n\2$$))^^ddhhppt")
        buf.write("tvv\t\2$$^^ddhhppttvv\2\u01c7\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write("\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2")
        buf.write("\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2y\3")
        buf.write("\2\2\2\2{\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\3\u0087\3\2\2\2\5\u0089\3\2\2\2\7\u0091\3\2\2")
        buf.write("\2\t\u0097\3\2\2\2\13\u009d\3\2\2\2\r\u00a6\3\2\2\2\17")
        buf.write("\u00a9\3\2\2\2\21\u00ae\3\2\2\2\23\u00b6\3\2\2\2\25\u00bc")
        buf.write("\3\2\2\2\27\u00bf\3\2\2\2\31\u00c3\3\2\2\2\33\u00c7\3")
        buf.write("\2\2\2\35\u00ce\3\2\2\2\37\u00d3\3\2\2\2!\u00d7\3\2\2")
        buf.write("\2#\u00de\3\2\2\2%\u00e3\3\2\2\2\'\u00e9\3\2\2\2)\u00ee")
        buf.write("\3\2\2\2+\u00f2\3\2\2\2-\u00f7\3\2\2\2/\u00fd\3\2\2\2")
        buf.write("\61\u0104\3\2\2\2\63\u0107\3\2\2\2\65\u010e\3\2\2\2\67")
        buf.write("\u0110\3\2\2\29\u0112\3\2\2\2;\u0114\3\2\2\2=\u0116\3")
        buf.write("\2\2\2?\u0118\3\2\2\2A\u011a\3\2\2\2C\u011d\3\2\2\2E\u0120")
        buf.write("\3\2\2\2G\u0122\3\2\2\2I\u0124\3\2\2\2K\u0127\3\2\2\2")
        buf.write("M\u012a\3\2\2\2O\u012d\3\2\2\2Q\u0130\3\2\2\2S\u0132\3")
        buf.write("\2\2\2U\u0134\3\2\2\2W\u0137\3\2\2\2Y\u0139\3\2\2\2[\u013b")
        buf.write("\3\2\2\2]\u013d\3\2\2\2_\u013f\3\2\2\2a\u0141\3\2\2\2")
        buf.write("c\u0143\3\2\2\2e\u0145\3\2\2\2g\u0147\3\2\2\2i\u0149\3")
        buf.write("\2\2\2k\u014c\3\2\2\2m\u0152\3\2\2\2o\u015b\3\2\2\2q\u016a")
        buf.write("\3\2\2\2s\u016f\3\2\2\2u\u017a\3\2\2\2w\u0181\3\2\2\2")
        buf.write("y\u018a\3\2\2\2{\u0191\3\2\2\2}\u0199\3\2\2\2\177\u019d")
        buf.write("\3\2\2\2\u0081\u01a0\3\2\2\2\u0083\u01ac\3\2\2\2\u0085")
        buf.write("\u01b8\3\2\2\2\u0087\u0088\7?\2\2\u0088\4\3\2\2\2\u0089")
        buf.write("\u008a\7d\2\2\u008a\u008b\7q\2\2\u008b\u008c\7q\2\2\u008c")
        buf.write("\u008d\7n\2\2\u008d\u008e\7g\2\2\u008e\u008f\7c\2\2\u008f")
        buf.write("\u0090\7p\2\2\u0090\6\3\2\2\2\u0091\u0092\7d\2\2\u0092")
        buf.write("\u0093\7t\2\2\u0093\u0094\7g\2\2\u0094\u0095\7c\2\2\u0095")
        buf.write("\u0096\7m\2\2\u0096\b\3\2\2\2\u0097\u0098\7e\2\2\u0098")
        buf.write("\u0099\7n\2\2\u0099\u009a\7c\2\2\u009a\u009b\7u\2\2\u009b")
        buf.write("\u009c\7u\2\2\u009c\n\3\2\2\2\u009d\u009e\7e\2\2\u009e")
        buf.write("\u009f\7q\2\2\u009f\u00a0\7p\2\2\u00a0\u00a1\7v\2\2\u00a1")
        buf.write("\u00a2\7k\2\2\u00a2\u00a3\7p\2\2\u00a3\u00a4\7w\2\2\u00a4")
        buf.write("\u00a5\7g\2\2\u00a5\f\3\2\2\2\u00a6\u00a7\7f\2\2\u00a7")
        buf.write("\u00a8\7q\2\2\u00a8\16\3\2\2\2\u00a9\u00aa\7g\2\2\u00aa")
        buf.write("\u00ab\7n\2\2\u00ab\u00ac\7u\2\2\u00ac\u00ad\7g\2\2\u00ad")
        buf.write("\20\3\2\2\2\u00ae\u00af\7g\2\2\u00af\u00b0\7z\2\2\u00b0")
        buf.write("\u00b1\7v\2\2\u00b1\u00b2\7g\2\2\u00b2\u00b3\7p\2\2\u00b3")
        buf.write("\u00b4\7f\2\2\u00b4\u00b5\7u\2\2\u00b5\22\3\2\2\2\u00b6")
        buf.write("\u00b7\7h\2\2\u00b7\u00b8\7n\2\2\u00b8\u00b9\7q\2\2\u00b9")
        buf.write("\u00ba\7c\2\2\u00ba\u00bb\7v\2\2\u00bb\24\3\2\2\2\u00bc")
        buf.write("\u00bd\7k\2\2\u00bd\u00be\7h\2\2\u00be\26\3\2\2\2\u00bf")
        buf.write("\u00c0\7k\2\2\u00c0\u00c1\7p\2\2\u00c1\u00c2\7v\2\2\u00c2")
        buf.write("\30\3\2\2\2\u00c3\u00c4\7p\2\2\u00c4\u00c5\7g\2\2\u00c5")
        buf.write("\u00c6\7y\2\2\u00c6\32\3\2\2\2\u00c7\u00c8\7u\2\2\u00c8")
        buf.write("\u00c9\7v\2\2\u00c9\u00ca\7t\2\2\u00ca\u00cb\7k\2\2\u00cb")
        buf.write("\u00cc\7p\2\2\u00cc\u00cd\7i\2\2\u00cd\34\3\2\2\2\u00ce")
        buf.write("\u00cf\7v\2\2\u00cf\u00d0\7j\2\2\u00d0\u00d1\7g\2\2\u00d1")
        buf.write("\u00d2\7p\2\2\u00d2\36\3\2\2\2\u00d3\u00d4\7h\2\2\u00d4")
        buf.write("\u00d5\7q\2\2\u00d5\u00d6\7t\2\2\u00d6 \3\2\2\2\u00d7")
        buf.write("\u00d8\7t\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da\7v\2\2\u00da")
        buf.write("\u00db\7w\2\2\u00db\u00dc\7t\2\2\u00dc\u00dd\7p\2\2\u00dd")
        buf.write("\"\3\2\2\2\u00de\u00df\7v\2\2\u00df\u00e0\7t\2\2\u00e0")
        buf.write("\u00e1\7w\2\2\u00e1\u00e2\7g\2\2\u00e2$\3\2\2\2\u00e3")
        buf.write("\u00e4\7h\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6\7n\2\2\u00e6")
        buf.write("\u00e7\7u\2\2\u00e7\u00e8\7g\2\2\u00e8&\3\2\2\2\u00e9")
        buf.write("\u00ea\7x\2\2\u00ea\u00eb\7q\2\2\u00eb\u00ec\7k\2\2\u00ec")
        buf.write("\u00ed\7f\2\2\u00ed(\3\2\2\2\u00ee\u00ef\7p\2\2\u00ef")
        buf.write("\u00f0\7k\2\2\u00f0\u00f1\7n\2\2\u00f1*\3\2\2\2\u00f2")
        buf.write("\u00f3\7v\2\2\u00f3\u00f4\7j\2\2\u00f4\u00f5\7k\2\2\u00f5")
        buf.write("\u00f6\7u\2\2\u00f6,\3\2\2\2\u00f7\u00f8\7h\2\2\u00f8")
        buf.write("\u00f9\7k\2\2\u00f9\u00fa\7p\2\2\u00fa\u00fb\7c\2\2\u00fb")
        buf.write("\u00fc\7n\2\2\u00fc.\3\2\2\2\u00fd\u00fe\7u\2\2\u00fe")
        buf.write("\u00ff\7v\2\2\u00ff\u0100\7c\2\2\u0100\u0101\7v\2\2\u0101")
        buf.write("\u0102\7k\2\2\u0102\u0103\7e\2\2\u0103\60\3\2\2\2\u0104")
        buf.write("\u0105\7v\2\2\u0105\u0106\7q\2\2\u0106\62\3\2\2\2\u0107")
        buf.write("\u0108\7f\2\2\u0108\u0109\7q\2\2\u0109\u010a\7y\2\2\u010a")
        buf.write("\u010b\7p\2\2\u010b\u010c\7v\2\2\u010c\u010d\7q\2\2\u010d")
        buf.write("\64\3\2\2\2\u010e\u010f\7-\2\2\u010f\66\3\2\2\2\u0110")
        buf.write("\u0111\7/\2\2\u01118\3\2\2\2\u0112\u0113\7,\2\2\u0113")
        buf.write(":\3\2\2\2\u0114\u0115\7\61\2\2\u0115<\3\2\2\2\u0116\u0117")
        buf.write("\7^\2\2\u0117>\3\2\2\2\u0118\u0119\7\'\2\2\u0119@\3\2")
        buf.write("\2\2\u011a\u011b\7#\2\2\u011b\u011c\7?\2\2\u011cB\3\2")
        buf.write("\2\2\u011d\u011e\7?\2\2\u011e\u011f\7?\2\2\u011fD\3\2")
        buf.write("\2\2\u0120\u0121\7>\2\2\u0121F\3\2\2\2\u0122\u0123\7@")
        buf.write("\2\2\u0123H\3\2\2\2\u0124\u0125\7>\2\2\u0125\u0126\7?")
        buf.write("\2\2\u0126J\3\2\2\2\u0127\u0128\7@\2\2\u0128\u0129\7?")
        buf.write("\2\2\u0129L\3\2\2\2\u012a\u012b\7~\2\2\u012b\u012c\7~")
        buf.write("\2\2\u012cN\3\2\2\2\u012d\u012e\7(\2\2\u012e\u012f\7(")
        buf.write("\2\2\u012fP\3\2\2\2\u0130\u0131\7#\2\2\u0131R\3\2\2\2")
        buf.write("\u0132\u0133\7`\2\2\u0133T\3\2\2\2\u0134\u0135\7<\2\2")
        buf.write("\u0135\u0136\7?\2\2\u0136V\3\2\2\2\u0137\u0138\7}\2\2")
        buf.write("\u0138X\3\2\2\2\u0139\u013a\7\177\2\2\u013aZ\3\2\2\2\u013b")
        buf.write("\u013c\7]\2\2\u013c\\\3\2\2\2\u013d\u013e\7_\2\2\u013e")
        buf.write("^\3\2\2\2\u013f\u0140\7*\2\2\u0140`\3\2\2\2\u0141\u0142")
        buf.write("\7+\2\2\u0142b\3\2\2\2\u0143\u0144\7=\2\2\u0144d\3\2\2")
        buf.write("\2\u0145\u0146\7<\2\2\u0146f\3\2\2\2\u0147\u0148\7.\2")
        buf.write("\2\u0148h\3\2\2\2\u0149\u014a\7\60\2\2\u014aj\3\2\2\2")
        buf.write("\u014b\u014d\t\2\2\2\u014c\u014b\3\2\2\2\u014d\u014e\3")
        buf.write("\2\2\2\u014e\u014c\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0150")
        buf.write("\3\2\2\2\u0150\u0151\b\66\2\2\u0151l\3\2\2\2\u0152\u0156")
        buf.write("\7%\2\2\u0153\u0155\n\3\2\2\u0154\u0153\3\2\2\2\u0155")
        buf.write("\u0158\3\2\2\2\u0156\u0154\3\2\2\2\u0156\u0157\3\2\2\2")
        buf.write("\u0157\u0159\3\2\2\2\u0158\u0156\3\2\2\2\u0159\u015a\b")
        buf.write("\67\2\2\u015an\3\2\2\2\u015b\u015c\7\61\2\2\u015c\u015d")
        buf.write("\7,\2\2\u015d\u0161\3\2\2\2\u015e\u0160\13\2\2\2\u015f")
        buf.write("\u015e\3\2\2\2\u0160\u0163\3\2\2\2\u0161\u0162\3\2\2\2")
        buf.write("\u0161\u015f\3\2\2\2\u0162\u0164\3\2\2\2\u0163\u0161\3")
        buf.write("\2\2\2\u0164\u0165\7,\2\2\u0165\u0166\7\61\2\2\u0166\u0167")
        buf.write("\3\2\2\2\u0167\u0168\b8\2\2\u0168p\3\2\2\2\u0169\u016b")
        buf.write("\t\4\2\2\u016a\u0169\3\2\2\2\u016b\u016c\3\2\2\2\u016c")
        buf.write("\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016dr\3\2\2\2\u016e")
        buf.write("\u0170\t\4\2\2\u016f\u016e\3\2\2\2\u0170\u0171\3\2\2\2")
        buf.write("\u0171\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0178\3")
        buf.write("\2\2\2\u0173\u0179\5u;\2\u0174\u0176\5u;\2\u0175\u0174")
        buf.write("\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0177\3\2\2\2\u0177")
        buf.write("\u0179\5w<\2\u0178\u0173\3\2\2\2\u0178\u0175\3\2\2\2\u0179")
        buf.write("t\3\2\2\2\u017a\u017e\7\60\2\2\u017b\u017d\t\4\2\2\u017c")
        buf.write("\u017b\3\2\2\2\u017d\u0180\3\2\2\2\u017e\u017c\3\2\2\2")
        buf.write("\u017e\u017f\3\2\2\2\u017fv\3\2\2\2\u0180\u017e\3\2\2")
        buf.write("\2\u0181\u0183\t\5\2\2\u0182\u0184\t\6\2\2\u0183\u0182")
        buf.write("\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0186\3\2\2\2\u0185")
        buf.write("\u0187\t\4\2\2\u0186\u0185\3\2\2\2\u0187\u0188\3\2\2\2")
        buf.write("\u0188\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189x\3\2\2")
        buf.write("\2\u018a\u018e\t\7\2\2\u018b\u018d\t\b\2\2\u018c\u018b")
        buf.write("\3\2\2\2\u018d\u0190\3\2\2\2\u018e\u018c\3\2\2\2\u018e")
        buf.write("\u018f\3\2\2\2\u018fz\3\2\2\2\u0190\u018e\3\2\2\2\u0191")
        buf.write("\u0193\7$\2\2\u0192\u0194\5}?\2\u0193\u0192\3\2\2\2\u0193")
        buf.write("\u0194\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0196\7$\2\2")
        buf.write("\u0196|\3\2\2\2\u0197\u019a\n\t\2\2\u0198\u019a\5\177")
        buf.write("@\2\u0199\u0197\3\2\2\2\u0199\u0198\3\2\2\2\u019a\u019b")
        buf.write("\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019c")
        buf.write("~\3\2\2\2\u019d\u019e\7^\2\2\u019e\u019f\t\n\2\2\u019f")
        buf.write("\u0080\3\2\2\2\u01a0\u01a4\7$\2\2\u01a1\u01a3\5}?\2\u01a2")
        buf.write("\u01a1\3\2\2\2\u01a3\u01a6\3\2\2\2\u01a4\u01a2\3\2\2\2")
        buf.write("\u01a4\u01a5\3\2\2\2\u01a5\u01a8\3\2\2\2\u01a6\u01a4\3")
        buf.write("\2\2\2\u01a7\u01a9\7\2\2\3\u01a8\u01a7\3\2\2\2\u01a8\u01a9")
        buf.write("\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ab\bA\3\2\u01ab")
        buf.write("\u0082\3\2\2\2\u01ac\u01b0\7$\2\2\u01ad\u01af\5}?\2\u01ae")
        buf.write("\u01ad\3\2\2\2\u01af\u01b2\3\2\2\2\u01b0\u01ae\3\2\2\2")
        buf.write("\u01b0\u01b1\3\2\2\2\u01b1\u01b3\3\2\2\2\u01b2\u01b0\3")
        buf.write("\2\2\2\u01b3\u01b4\7^\2\2\u01b4\u01b5\n\13\2\2\u01b5\u01b6")
        buf.write("\3\2\2\2\u01b6\u01b7\bB\4\2\u01b7\u0084\3\2\2\2\u01b8")
        buf.write("\u01b9\13\2\2\2\u01b9\u01ba\bC\5\2\u01ba\u0086\3\2\2\2")
        buf.write("\24\2\u014e\u0156\u0161\u016c\u0171\u0175\u0178\u017e")
        buf.write("\u0183\u0188\u018e\u0193\u0199\u019b\u01a4\u01a8\u01b0")
        buf.write("\6\b\2\2\3A\2\3B\3\3C\4")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    BOOLEAN = 2
    BREAK = 3
    CLASS = 4
    CONTINUE = 5
    DO = 6
    ELSE = 7
    EXTENDS = 8
    FLOAT = 9
    IF = 10
    INT = 11
    NEW = 12
    STRING = 13
    THEN = 14
    FOR = 15
    RETURN = 16
    TRUE = 17
    FALSE = 18
    VOID = 19
    NIL = 20
    THIS = 21
    FINAL = 22
    STATIC = 23
    TO = 24
    DOWNTO = 25
    ADD = 26
    SUB = 27
    MUL = 28
    FDIV = 29
    IDIV = 30
    MOD = 31
    NEQUAL = 32
    EQUAL = 33
    LT = 34
    GT = 35
    LTE = 36
    GTE = 37
    OR = 38
    AND = 39
    NOT = 40
    CONCAT = 41
    ASS = 42
    LP = 43
    RP = 44
    LSB = 45
    RSB = 46
    LB = 47
    RB = 48
    SM = 49
    COLON = 50
    COMMA = 51
    DOT = 52
    WS = 53
    LINE_COMMENT = 54
    BLOCK_COMMENT = 55
    INTLIT = 56
    FLOATLIT = 57
    ID = 58
    STRINGLIT = 59
    UNCLOSE_STRING = 60
    ILLEGAL_ESCAPE = 61
    ERROR_CHAR = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'boolean'", "'break'", "'class'", "'continue'", "'do'", 
            "'else'", "'extends'", "'float'", "'if'", "'int'", "'new'", 
            "'string'", "'then'", "'for'", "'return'", "'true'", "'false'", 
            "'void'", "'nil'", "'this'", "'final'", "'static'", "'to'", 
            "'downto'", "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", "'!='", 
            "'=='", "'<'", "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", 
            "'^'", "':='", "'{'", "'}'", "'['", "']'", "'('", "')'", "';'", 
            "':'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", "ELSE", "EXTENDS", 
            "FLOAT", "IF", "INT", "NEW", "STRING", "THEN", "FOR", "RETURN", 
            "TRUE", "FALSE", "VOID", "NIL", "THIS", "FINAL", "STATIC", "TO", 
            "DOWNTO", "ADD", "SUB", "MUL", "FDIV", "IDIV", "MOD", "NEQUAL", 
            "EQUAL", "LT", "GT", "LTE", "GTE", "OR", "AND", "NOT", "CONCAT", 
            "ASS", "LP", "RP", "LSB", "RSB", "LB", "RB", "SM", "COLON", 
            "COMMA", "DOT", "WS", "LINE_COMMENT", "BLOCK_COMMENT", "INTLIT", 
            "FLOATLIT", "ID", "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "T__0", "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", 
                  "ELSE", "EXTENDS", "FLOAT", "IF", "INT", "NEW", "STRING", 
                  "THEN", "FOR", "RETURN", "TRUE", "FALSE", "VOID", "NIL", 
                  "THIS", "FINAL", "STATIC", "TO", "DOWNTO", "ADD", "SUB", 
                  "MUL", "FDIV", "IDIV", "MOD", "NEQUAL", "EQUAL", "LT", 
                  "GT", "LTE", "GTE", "OR", "AND", "NOT", "CONCAT", "ASS", 
                  "LP", "RP", "LSB", "RSB", "LB", "RB", "SM", "COLON", "COMMA", 
                  "DOT", "WS", "LINE_COMMENT", "BLOCK_COMMENT", "INTLIT", 
                  "FLOATLIT", "DecimalPart", "ExponentPart", "ID", "STRINGLIT", 
                  "StringCharacter", "EscapeSequence", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[63] = self.UNCLOSE_STRING_action 
            actions[64] = self.ILLEGAL_ESCAPE_action 
            actions[65] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		y = str(self.text)
            		raise UncloseString(y[0:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            		y = str(self.text)
            		raise IllegalEscape(y[0:])
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		raise ErrorToken(self.text)
            	
     


