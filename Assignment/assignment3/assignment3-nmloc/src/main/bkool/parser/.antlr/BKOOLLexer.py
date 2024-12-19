# Generated from /Users/duyanhle/Desktop/assignment2/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\u01d1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3")
        buf.write("$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3")
        buf.write("*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\7\66")
        buf.write("\u0152\n\66\f\66\16\66\u0155\13\66\3\67\6\67\u0158\n\67")
        buf.write("\r\67\16\67\u0159\3\67\3\67\38\38\78\u0160\n8\f8\168\u0163")
        buf.write("\138\38\38\39\39\39\39\79\u016b\n9\f9\169\u016e\139\3")
        buf.write("9\39\39\39\39\3:\3:\7:\u0177\n:\f:\16:\u017a\13:\3:\5")
        buf.write(":\u017d\n:\3;\3;\3;\3;\3;\5;\u0184\n;\3;\3;\5;\u0188\n")
        buf.write(";\3<\6<\u018b\n<\r<\16<\u018c\3=\3=\7=\u0191\n=\f=\16")
        buf.write("=\u0194\13=\3>\3>\5>\u0198\n>\3>\6>\u019b\n>\r>\16>\u019c")
        buf.write("\3?\3?\7?\u01a1\n?\f?\16?\u01a4\13?\3?\5?\u01a7\n?\3?")
        buf.write("\3?\3?\3@\3@\3@\3@\5@\u01b0\n@\3A\3A\3A\3B\3B\3B\3C\3")
        buf.write("C\7C\u01ba\nC\fC\16C\u01bd\13C\3C\3C\5C\u01c1\nC\3C\3")
        buf.write("C\3D\3D\7D\u01c7\nD\fD\16D\u01ca\13D\3D\3D\3D\3E\3E\3")
        buf.write("E\3\u016c\2F\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#")
        buf.write("E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66")
        buf.write("k\67m8o9q:s;u<w\2y\2{\2}=\177\2\u0081\2\u0083\2\u0085")
        buf.write(">\u0087?\u0089@\3\2\17\5\2C\\aac|\6\2\62;C\\aac|\5\2\13")
        buf.write("\f\16\17\"\"\4\2\f\f\17\17\3\2\63;\3\2\62;\3\2\62\62\4")
        buf.write("\2GGgg\4\2--//\6\2\f\f\17\17$$^^\t\2$$^^ddhhppttvv\6\2")
        buf.write("\f\f\17\17GHQQ\3\2$$\2\u01dd\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2}\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\3\u008b\3\2\2\2\5\u0093\3\2\2\2\7\u0099\3\2\2")
        buf.write("\2\t\u009f\3\2\2\2\13\u00a8\3\2\2\2\r\u00ab\3\2\2\2\17")
        buf.write("\u00b0\3\2\2\2\21\u00b8\3\2\2\2\23\u00be\3\2\2\2\25\u00c1")
        buf.write("\3\2\2\2\27\u00c5\3\2\2\2\31\u00c9\3\2\2\2\33\u00d0\3")
        buf.write("\2\2\2\35\u00d5\3\2\2\2\37\u00d9\3\2\2\2!\u00e0\3\2\2")
        buf.write("\2#\u00e5\3\2\2\2%\u00eb\3\2\2\2\'\u00f0\3\2\2\2)\u00f4")
        buf.write("\3\2\2\2+\u00f9\3\2\2\2-\u00ff\3\2\2\2/\u0106\3\2\2\2")
        buf.write("\61\u0109\3\2\2\2\63\u0110\3\2\2\2\65\u0112\3\2\2\2\67")
        buf.write("\u0114\3\2\2\29\u0116\3\2\2\2;\u0118\3\2\2\2=\u011a\3")
        buf.write("\2\2\2?\u011c\3\2\2\2A\u011f\3\2\2\2C\u0122\3\2\2\2E\u0124")
        buf.write("\3\2\2\2G\u0126\3\2\2\2I\u0129\3\2\2\2K\u012c\3\2\2\2")
        buf.write("M\u012f\3\2\2\2O\u0132\3\2\2\2Q\u0134\3\2\2\2S\u0136\3")
        buf.write("\2\2\2U\u0139\3\2\2\2W\u013b\3\2\2\2Y\u013d\3\2\2\2[\u013f")
        buf.write("\3\2\2\2]\u0141\3\2\2\2_\u0143\3\2\2\2a\u0145\3\2\2\2")
        buf.write("c\u0147\3\2\2\2e\u0149\3\2\2\2g\u014b\3\2\2\2i\u014d\3")
        buf.write("\2\2\2k\u014f\3\2\2\2m\u0157\3\2\2\2o\u015d\3\2\2\2q\u0166")
        buf.write("\3\2\2\2s\u017c\3\2\2\2u\u0187\3\2\2\2w\u018a\3\2\2\2")
        buf.write("y\u018e\3\2\2\2{\u0195\3\2\2\2}\u019e\3\2\2\2\177\u01af")
        buf.write("\3\2\2\2\u0081\u01b1\3\2\2\2\u0083\u01b4\3\2\2\2\u0085")
        buf.write("\u01b7\3\2\2\2\u0087\u01c4\3\2\2\2\u0089\u01ce\3\2\2\2")
        buf.write("\u008b\u008c\7d\2\2\u008c\u008d\7q\2\2\u008d\u008e\7q")
        buf.write("\2\2\u008e\u008f\7n\2\2\u008f\u0090\7g\2\2\u0090\u0091")
        buf.write("\7c\2\2\u0091\u0092\7p\2\2\u0092\4\3\2\2\2\u0093\u0094")
        buf.write("\7d\2\2\u0094\u0095\7t\2\2\u0095\u0096\7g\2\2\u0096\u0097")
        buf.write("\7c\2\2\u0097\u0098\7m\2\2\u0098\6\3\2\2\2\u0099\u009a")
        buf.write("\7e\2\2\u009a\u009b\7n\2\2\u009b\u009c\7c\2\2\u009c\u009d")
        buf.write("\7u\2\2\u009d\u009e\7u\2\2\u009e\b\3\2\2\2\u009f\u00a0")
        buf.write("\7e\2\2\u00a0\u00a1\7q\2\2\u00a1\u00a2\7p\2\2\u00a2\u00a3")
        buf.write("\7v\2\2\u00a3\u00a4\7k\2\2\u00a4\u00a5\7p\2\2\u00a5\u00a6")
        buf.write("\7w\2\2\u00a6\u00a7\7g\2\2\u00a7\n\3\2\2\2\u00a8\u00a9")
        buf.write("\7f\2\2\u00a9\u00aa\7q\2\2\u00aa\f\3\2\2\2\u00ab\u00ac")
        buf.write("\7g\2\2\u00ac\u00ad\7n\2\2\u00ad\u00ae\7u\2\2\u00ae\u00af")
        buf.write("\7g\2\2\u00af\16\3\2\2\2\u00b0\u00b1\7g\2\2\u00b1\u00b2")
        buf.write("\7z\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4\7g\2\2\u00b4\u00b5")
        buf.write("\7p\2\2\u00b5\u00b6\7f\2\2\u00b6\u00b7\7u\2\2\u00b7\20")
        buf.write("\3\2\2\2\u00b8\u00b9\7h\2\2\u00b9\u00ba\7n\2\2\u00ba\u00bb")
        buf.write("\7q\2\2\u00bb\u00bc\7c\2\2\u00bc\u00bd\7v\2\2\u00bd\22")
        buf.write("\3\2\2\2\u00be\u00bf\7k\2\2\u00bf\u00c0\7h\2\2\u00c0\24")
        buf.write("\3\2\2\2\u00c1\u00c2\7k\2\2\u00c2\u00c3\7p\2\2\u00c3\u00c4")
        buf.write("\7v\2\2\u00c4\26\3\2\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7")
        buf.write("\7g\2\2\u00c7\u00c8\7y\2\2\u00c8\30\3\2\2\2\u00c9\u00ca")
        buf.write("\7u\2\2\u00ca\u00cb\7v\2\2\u00cb\u00cc\7t\2\2\u00cc\u00cd")
        buf.write("\7k\2\2\u00cd\u00ce\7p\2\2\u00ce\u00cf\7i\2\2\u00cf\32")
        buf.write("\3\2\2\2\u00d0\u00d1\7v\2\2\u00d1\u00d2\7j\2\2\u00d2\u00d3")
        buf.write("\7g\2\2\u00d3\u00d4\7p\2\2\u00d4\34\3\2\2\2\u00d5\u00d6")
        buf.write("\7h\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8\7t\2\2\u00d8\36")
        buf.write("\3\2\2\2\u00d9\u00da\7t\2\2\u00da\u00db\7g\2\2\u00db\u00dc")
        buf.write("\7v\2\2\u00dc\u00dd\7w\2\2\u00dd\u00de\7t\2\2\u00de\u00df")
        buf.write("\7p\2\2\u00df \3\2\2\2\u00e0\u00e1\7v\2\2\u00e1\u00e2")
        buf.write("\7t\2\2\u00e2\u00e3\7w\2\2\u00e3\u00e4\7g\2\2\u00e4\"")
        buf.write("\3\2\2\2\u00e5\u00e6\7h\2\2\u00e6\u00e7\7c\2\2\u00e7\u00e8")
        buf.write("\7n\2\2\u00e8\u00e9\7u\2\2\u00e9\u00ea\7g\2\2\u00ea$\3")
        buf.write("\2\2\2\u00eb\u00ec\7x\2\2\u00ec\u00ed\7q\2\2\u00ed\u00ee")
        buf.write("\7k\2\2\u00ee\u00ef\7f\2\2\u00ef&\3\2\2\2\u00f0\u00f1")
        buf.write("\7p\2\2\u00f1\u00f2\7k\2\2\u00f2\u00f3\7n\2\2\u00f3(\3")
        buf.write("\2\2\2\u00f4\u00f5\7v\2\2\u00f5\u00f6\7j\2\2\u00f6\u00f7")
        buf.write("\7k\2\2\u00f7\u00f8\7u\2\2\u00f8*\3\2\2\2\u00f9\u00fa")
        buf.write("\7h\2\2\u00fa\u00fb\7k\2\2\u00fb\u00fc\7p\2\2\u00fc\u00fd")
        buf.write("\7c\2\2\u00fd\u00fe\7n\2\2\u00fe,\3\2\2\2\u00ff\u0100")
        buf.write("\7u\2\2\u0100\u0101\7v\2\2\u0101\u0102\7c\2\2\u0102\u0103")
        buf.write("\7v\2\2\u0103\u0104\7k\2\2\u0104\u0105\7e\2\2\u0105.\3")
        buf.write("\2\2\2\u0106\u0107\7v\2\2\u0107\u0108\7q\2\2\u0108\60")
        buf.write("\3\2\2\2\u0109\u010a\7f\2\2\u010a\u010b\7q\2\2\u010b\u010c")
        buf.write("\7y\2\2\u010c\u010d\7p\2\2\u010d\u010e\7v\2\2\u010e\u010f")
        buf.write("\7q\2\2\u010f\62\3\2\2\2\u0110\u0111\7-\2\2\u0111\64\3")
        buf.write("\2\2\2\u0112\u0113\7/\2\2\u0113\66\3\2\2\2\u0114\u0115")
        buf.write("\7,\2\2\u01158\3\2\2\2\u0116\u0117\7\61\2\2\u0117:\3\2")
        buf.write("\2\2\u0118\u0119\7^\2\2\u0119<\3\2\2\2\u011a\u011b\7\'")
        buf.write("\2\2\u011b>\3\2\2\2\u011c\u011d\7?\2\2\u011d\u011e\7?")
        buf.write("\2\2\u011e@\3\2\2\2\u011f\u0120\7#\2\2\u0120\u0121\7?")
        buf.write("\2\2\u0121B\3\2\2\2\u0122\u0123\7>\2\2\u0123D\3\2\2\2")
        buf.write("\u0124\u0125\7@\2\2\u0125F\3\2\2\2\u0126\u0127\7>\2\2")
        buf.write("\u0127\u0128\7?\2\2\u0128H\3\2\2\2\u0129\u012a\7@\2\2")
        buf.write("\u012a\u012b\7?\2\2\u012bJ\3\2\2\2\u012c\u012d\7~\2\2")
        buf.write("\u012d\u012e\7~\2\2\u012eL\3\2\2\2\u012f\u0130\7(\2\2")
        buf.write("\u0130\u0131\7(\2\2\u0131N\3\2\2\2\u0132\u0133\7#\2\2")
        buf.write("\u0133P\3\2\2\2\u0134\u0135\7`\2\2\u0135R\3\2\2\2\u0136")
        buf.write("\u0137\7<\2\2\u0137\u0138\7?\2\2\u0138T\3\2\2\2\u0139")
        buf.write("\u013a\7?\2\2\u013aV\3\2\2\2\u013b\u013c\7]\2\2\u013c")
        buf.write("X\3\2\2\2\u013d\u013e\7_\2\2\u013eZ\3\2\2\2\u013f\u0140")
        buf.write("\7}\2\2\u0140\\\3\2\2\2\u0141\u0142\7\177\2\2\u0142^\3")
        buf.write("\2\2\2\u0143\u0144\7*\2\2\u0144`\3\2\2\2\u0145\u0146\7")
        buf.write("+\2\2\u0146b\3\2\2\2\u0147\u0148\7=\2\2\u0148d\3\2\2\2")
        buf.write("\u0149\u014a\7<\2\2\u014af\3\2\2\2\u014b\u014c\7\60\2")
        buf.write("\2\u014ch\3\2\2\2\u014d\u014e\7.\2\2\u014ej\3\2\2\2\u014f")
        buf.write("\u0153\t\2\2\2\u0150\u0152\t\3\2\2\u0151\u0150\3\2\2\2")
        buf.write("\u0152\u0155\3\2\2\2\u0153\u0151\3\2\2\2\u0153\u0154\3")
        buf.write("\2\2\2\u0154l\3\2\2\2\u0155\u0153\3\2\2\2\u0156\u0158")
        buf.write("\t\4\2\2\u0157\u0156\3\2\2\2\u0158\u0159\3\2\2\2\u0159")
        buf.write("\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015b\3\2\2\2")
        buf.write("\u015b\u015c\b\67\2\2\u015cn\3\2\2\2\u015d\u0161\7%\2")
        buf.write("\2\u015e\u0160\n\5\2\2\u015f\u015e\3\2\2\2\u0160\u0163")
        buf.write("\3\2\2\2\u0161\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162")
        buf.write("\u0164\3\2\2\2\u0163\u0161\3\2\2\2\u0164\u0165\b8\2\2")
        buf.write("\u0165p\3\2\2\2\u0166\u0167\7\61\2\2\u0167\u0168\7,\2")
        buf.write("\2\u0168\u016c\3\2\2\2\u0169\u016b\13\2\2\2\u016a\u0169")
        buf.write("\3\2\2\2\u016b\u016e\3\2\2\2\u016c\u016d\3\2\2\2\u016c")
        buf.write("\u016a\3\2\2\2\u016d\u016f\3\2\2\2\u016e\u016c\3\2\2\2")
        buf.write("\u016f\u0170\7,\2\2\u0170\u0171\7\61\2\2\u0171\u0172\3")
        buf.write("\2\2\2\u0172\u0173\b9\2\2\u0173r\3\2\2\2\u0174\u0178\t")
        buf.write("\6\2\2\u0175\u0177\t\7\2\2\u0176\u0175\3\2\2\2\u0177\u017a")
        buf.write("\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179")
        buf.write("\u017d\3\2\2\2\u017a\u0178\3\2\2\2\u017b\u017d\t\b\2\2")
        buf.write("\u017c\u0174\3\2\2\2\u017c\u017b\3\2\2\2\u017dt\3\2\2")
        buf.write("\2\u017e\u017f\5w<\2\u017f\u0180\5y=\2\u0180\u0188\3\2")
        buf.write("\2\2\u0181\u0183\5w<\2\u0182\u0184\5y=\2\u0183\u0182\3")
        buf.write("\2\2\2\u0183\u0184\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0186")
        buf.write("\5{>\2\u0186\u0188\3\2\2\2\u0187\u017e\3\2\2\2\u0187\u0181")
        buf.write("\3\2\2\2\u0188v\3\2\2\2\u0189\u018b\t\7\2\2\u018a\u0189")
        buf.write("\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u018a\3\2\2\2\u018c")
        buf.write("\u018d\3\2\2\2\u018dx\3\2\2\2\u018e\u0192\7\60\2\2\u018f")
        buf.write("\u0191\t\7\2\2\u0190\u018f\3\2\2\2\u0191\u0194\3\2\2\2")
        buf.write("\u0192\u0190\3\2\2\2\u0192\u0193\3\2\2\2\u0193z\3\2\2")
        buf.write("\2\u0194\u0192\3\2\2\2\u0195\u0197\t\t\2\2\u0196\u0198")
        buf.write("\t\n\2\2\u0197\u0196\3\2\2\2\u0197\u0198\3\2\2\2\u0198")
        buf.write("\u019a\3\2\2\2\u0199\u019b\t\7\2\2\u019a\u0199\3\2\2\2")
        buf.write("\u019b\u019c\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019d\3")
        buf.write("\2\2\2\u019d|\3\2\2\2\u019e\u01a2\7$\2\2\u019f\u01a1\5")
        buf.write("\177@\2\u01a0\u019f\3\2\2\2\u01a1\u01a4\3\2\2\2\u01a2")
        buf.write("\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a6\3\2\2\2")
        buf.write("\u01a4\u01a2\3\2\2\2\u01a5\u01a7\5}?\2\u01a6\u01a5\3\2")
        buf.write("\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a9")
        buf.write("\7$\2\2\u01a9\u01aa\b?\3\2\u01aa~\3\2\2\2\u01ab\u01b0")
        buf.write("\5\u0081A\2\u01ac\u01ad\7^\2\2\u01ad\u01b0\7$\2\2\u01ae")
        buf.write("\u01b0\n\13\2\2\u01af\u01ab\3\2\2\2\u01af\u01ac\3\2\2")
        buf.write("\2\u01af\u01ae\3\2\2\2\u01b0\u0080\3\2\2\2\u01b1\u01b2")
        buf.write("\7^\2\2\u01b2\u01b3\t\f\2\2\u01b3\u0082\3\2\2\2\u01b4")
        buf.write("\u01b5\7^\2\2\u01b5\u01b6\n\f\2\2\u01b6\u0084\3\2\2\2")
        buf.write("\u01b7\u01bb\7$\2\2\u01b8\u01ba\5\177@\2\u01b9\u01b8\3")
        buf.write("\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb\u01bc")
        buf.write("\3\2\2\2\u01bc\u01c0\3\2\2\2\u01bd\u01bb\3\2\2\2\u01be")
        buf.write("\u01c1\t\r\2\2\u01bf\u01c1\n\16\2\2\u01c0\u01be\3\2\2")
        buf.write("\2\u01c0\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c3")
        buf.write("\bC\4\2\u01c3\u0086\3\2\2\2\u01c4\u01c8\7$\2\2\u01c5\u01c7")
        buf.write("\5\177@\2\u01c6\u01c5\3\2\2\2\u01c7\u01ca\3\2\2\2\u01c8")
        buf.write("\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01cb\3\2\2\2")
        buf.write("\u01ca\u01c8\3\2\2\2\u01cb\u01cc\5\u0083B\2\u01cc\u01cd")
        buf.write("\bD\5\2\u01cd\u0088\3\2\2\2\u01ce\u01cf\13\2\2\2\u01cf")
        buf.write("\u01d0\bE\6\2\u01d0\u008a\3\2\2\2\25\2\u0153\u0159\u0161")
        buf.write("\u016c\u0178\u017c\u0183\u0187\u018c\u0192\u0197\u019c")
        buf.write("\u01a2\u01a6\u01af\u01bb\u01c0\u01c8\7\b\2\2\3?\2\3C\3")
        buf.write("\3D\4\3E\5")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOLEAN = 1
    BREAK = 2
    CLASS = 3
    CONTINUE = 4
    DO = 5
    ELSE = 6
    EXTENDS = 7
    FLOAT = 8
    IF = 9
    INT = 10
    NEW = 11
    STRING = 12
    THEN = 13
    FOR = 14
    RETURN = 15
    TRUE = 16
    FALSE = 17
    VOID = 18
    NIL = 19
    THIS = 20
    FINAL = 21
    STATIC = 22
    TO = 23
    DOWNTO = 24
    ADD_OP = 25
    SUB_OP = 26
    MUL_OP = 27
    FLODIV_OP = 28
    INTDIV_OP = 29
    MOD_OP = 30
    EQUAL_OP = 31
    NEQUAL_OP = 32
    LT_OP = 33
    GT_OP = 34
    LTE_OP = 35
    GTE_OP = 36
    OR_OP = 37
    AND_OP = 38
    NOT_OP = 39
    CONCAT_OP = 40
    ASSIGN_OP = 41
    EQUAL_SIGN = 42
    LSB = 43
    RSB = 44
    LP = 45
    RP = 46
    LB = 47
    RB = 48
    SEMI = 49
    COLON = 50
    DOT = 51
    COMMA = 52
    ID = 53
    WS = 54
    LINE_COMMENT = 55
    BLOCK_COMMENT = 56
    INTLIT = 57
    FLOATLIT = 58
    STRINGLIT = 59
    UNCLOSE_STRING = 60
    ILLEGAL_ESCAPE = 61
    ERROR_CHAR = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'boolean'", "'break'", "'class'", "'continue'", "'do'", "'else'", 
            "'extends'", "'float'", "'if'", "'int'", "'new'", "'string'", 
            "'then'", "'for'", "'return'", "'true'", "'false'", "'void'", 
            "'nil'", "'this'", "'final'", "'static'", "'to'", "'downto'", 
            "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", "'=='", "'!='", "'<'", 
            "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", "'^'", "':='", 
            "'='", "'['", "']'", "'{'", "'}'", "'('", "')'", "';'", "':'", 
            "'.'", "','" ]

    symbolicNames = [ "<INVALID>",
            "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", "ELSE", "EXTENDS", 
            "FLOAT", "IF", "INT", "NEW", "STRING", "THEN", "FOR", "RETURN", 
            "TRUE", "FALSE", "VOID", "NIL", "THIS", "FINAL", "STATIC", "TO", 
            "DOWNTO", "ADD_OP", "SUB_OP", "MUL_OP", "FLODIV_OP", "INTDIV_OP", 
            "MOD_OP", "EQUAL_OP", "NEQUAL_OP", "LT_OP", "GT_OP", "LTE_OP", 
            "GTE_OP", "OR_OP", "AND_OP", "NOT_OP", "CONCAT_OP", "ASSIGN_OP", 
            "EQUAL_SIGN", "LSB", "RSB", "LP", "RP", "LB", "RB", "SEMI", 
            "COLON", "DOT", "COMMA", "ID", "WS", "LINE_COMMENT", "BLOCK_COMMENT", 
            "INTLIT", "FLOATLIT", "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", "ELSE", 
                  "EXTENDS", "FLOAT", "IF", "INT", "NEW", "STRING", "THEN", 
                  "FOR", "RETURN", "TRUE", "FALSE", "VOID", "NIL", "THIS", 
                  "FINAL", "STATIC", "TO", "DOWNTO", "ADD_OP", "SUB_OP", 
                  "MUL_OP", "FLODIV_OP", "INTDIV_OP", "MOD_OP", "EQUAL_OP", 
                  "NEQUAL_OP", "LT_OP", "GT_OP", "LTE_OP", "GTE_OP", "OR_OP", 
                  "AND_OP", "NOT_OP", "CONCAT_OP", "ASSIGN_OP", "EQUAL_SIGN", 
                  "LSB", "RSB", "LP", "RP", "LB", "RB", "SEMI", "COLON", 
                  "DOT", "COMMA", "ID", "WS", "LINE_COMMENT", "BLOCK_COMMENT", 
                  "INTLIT", "FLOATLIT", "INTPART", "DECPART", "EXPPART", 
                  "STRINGLIT", "CHARLIT", "ESCSEQ", "ILLESC", "UNCLOSE_STRING", 
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
            actions[61] = self.STRINGLIT_action 
            actions[65] = self.UNCLOSE_STRING_action 
            actions[66] = self.ILLEGAL_ESCAPE_action 
            actions[67] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             self.text = self.text[1:-1] 
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	if self.text[-1] in ['\n', '\r', 'EOF']:
            		raise UncloseString(self.text[1:-1])
            	else:
            		raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	raise IllegalEscape(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
             raise ErrorToken(self.text) 
     


