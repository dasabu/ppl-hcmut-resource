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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u01d5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\6\2\u0091\n\2\r\2\16\2\u0092")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u009b\n\3\f\3\16\3\u009e")
        buf.write("\13\3\3\3\3\3\3\3\3\3\7\3\u00a4\n\3\f\3\16\3\u00a7\13")
        buf.write("\3\3\3\5\3\u00aa\n\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#")
        buf.write("\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3)\3")
        buf.write(")\3)\3*\3*\3+\3+\3+\3,\3,\3-\3-\3-\3.\3.\3/\3/\3\60\3")
        buf.write("\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\68\u0173\n8\r8\168\u0174\39\3")
        buf.write("9\39\39\39\39\39\39\39\39\59\u0181\n9\3:\3:\3;\3;\7;\u0187")
        buf.write("\n;\f;\16;\u018a\13;\3<\3<\5<\u018e\n<\3<\6<\u0191\n<")
        buf.write("\r<\16<\u0192\3=\3=\3=\3=\5=\u0199\n=\3>\3>\3>\3?\3?\7")
        buf.write("?\u01a0\n?\f?\16?\u01a3\13?\3?\3?\3?\3@\3@\5@\u01aa\n")
        buf.write("@\3@\3@\3@\7@\u01af\n@\f@\16@\u01b2\13@\3A\3A\3B\3B\3")
        buf.write("C\3C\3D\3D\3D\3E\3E\7E\u01bf\nE\fE\16E\u01c2\13E\3E\5")
        buf.write("E\u01c5\nE\3E\3E\3F\3F\7F\u01cb\nF\fF\16F\u01ce\13F\3")
        buf.write("F\3F\3F\3G\3G\3G\4\u009c\u00a5\2H\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m8o9q:s\2u\2w\2y\2{\2};\177<\u0081")
        buf.write("\2\u0083\2\u0085\2\u0087\2\u0089=\u008b>\u008d?\3\2\n")
        buf.write("\5\2\13\f\16\17\"\"\3\2\62;\4\2GGgg\4\2--//\6\2\n\f\16")
        buf.write("\17$$^^\t\2))^^ddhhppttvv\4\2C\\c|\4\3\n\f\16\17\2\u01de")
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
        buf.write("\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\3\u0090\3\2\2\2\5\u00a9\3\2\2")
        buf.write("\2\7\u00ad\3\2\2\2\t\u00b5\3\2\2\2\13\u00bb\3\2\2\2\r")
        buf.write("\u00c1\3\2\2\2\17\u00ca\3\2\2\2\21\u00cd\3\2\2\2\23\u00d0")
        buf.write("\3\2\2\2\25\u00d5\3\2\2\2\27\u00dd\3\2\2\2\31\u00e1\3")
        buf.write("\2\2\2\33\u00e7\3\2\2\2\35\u00eb\3\2\2\2\37\u00f2\3\2")
        buf.write("\2\2!\u00f7\3\2\2\2#\u00fb\3\2\2\2%\u0102\3\2\2\2\'\u0107")
        buf.write("\3\2\2\2)\u010d\3\2\2\2+\u0112\3\2\2\2-\u0116\3\2\2\2")
        buf.write("/\u011b\3\2\2\2\61\u0121\3\2\2\2\63\u0128\3\2\2\2\65\u012b")
        buf.write("\3\2\2\2\67\u0132\3\2\2\29\u0134\3\2\2\2;\u0136\3\2\2")
        buf.write("\2=\u0138\3\2\2\2?\u013a\3\2\2\2A\u013c\3\2\2\2C\u013e")
        buf.write("\3\2\2\2E\u0140\3\2\2\2G\u0143\3\2\2\2I\u0146\3\2\2\2")
        buf.write("K\u0149\3\2\2\2M\u014b\3\2\2\2O\u014e\3\2\2\2Q\u0150\3")
        buf.write("\2\2\2S\u0153\3\2\2\2U\u0155\3\2\2\2W\u0158\3\2\2\2Y\u015a")
        buf.write("\3\2\2\2[\u015d\3\2\2\2]\u015f\3\2\2\2_\u0161\3\2\2\2")
        buf.write("a\u0163\3\2\2\2c\u0165\3\2\2\2e\u0167\3\2\2\2g\u0169\3")
        buf.write("\2\2\2i\u016b\3\2\2\2k\u016d\3\2\2\2m\u016f\3\2\2\2o\u0172")
        buf.write("\3\2\2\2q\u0180\3\2\2\2s\u0182\3\2\2\2u\u0184\3\2\2\2")
        buf.write("w\u018b\3\2\2\2y\u0198\3\2\2\2{\u019a\3\2\2\2}\u019d\3")
        buf.write("\2\2\2\177\u01a9\3\2\2\2\u0081\u01b3\3\2\2\2\u0083\u01b5")
        buf.write("\3\2\2\2\u0085\u01b7\3\2\2\2\u0087\u01b9\3\2\2\2\u0089")
        buf.write("\u01bc\3\2\2\2\u008b\u01c8\3\2\2\2\u008d\u01d2\3\2\2\2")
        buf.write("\u008f\u0091\t\2\2\2\u0090\u008f\3\2\2\2\u0091\u0092\3")
        buf.write("\2\2\2\u0092\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0094")
        buf.write("\3\2\2\2\u0094\u0095\b\2\2\2\u0095\4\3\2\2\2\u0096\u0097")
        buf.write("\7\61\2\2\u0097\u0098\7,\2\2\u0098\u009c\3\2\2\2\u0099")
        buf.write("\u009b\13\2\2\2\u009a\u0099\3\2\2\2\u009b\u009e\3\2\2")
        buf.write("\2\u009c\u009d\3\2\2\2\u009c\u009a\3\2\2\2\u009d\u009f")
        buf.write("\3\2\2\2\u009e\u009c\3\2\2\2\u009f\u00a0\7,\2\2\u00a0")
        buf.write("\u00aa\7\61\2\2\u00a1\u00a5\7%\2\2\u00a2\u00a4\13\2\2")
        buf.write("\2\u00a3\u00a2\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5\u00a6")
        buf.write("\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00a8\3\2\2\2\u00a7")
        buf.write("\u00a5\3\2\2\2\u00a8\u00aa\7\2\2\3\u00a9\u0096\3\2\2\2")
        buf.write("\u00a9\u00a1\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ac\b")
        buf.write("\3\2\2\u00ac\6\3\2\2\2\u00ad\u00ae\7d\2\2\u00ae\u00af")
        buf.write("\7q\2\2\u00af\u00b0\7q\2\2\u00b0\u00b1\7n\2\2\u00b1\u00b2")
        buf.write("\7g\2\2\u00b2\u00b3\7c\2\2\u00b3\u00b4\7p\2\2\u00b4\b")
        buf.write("\3\2\2\2\u00b5\u00b6\7d\2\2\u00b6\u00b7\7t\2\2\u00b7\u00b8")
        buf.write("\7g\2\2\u00b8\u00b9\7c\2\2\u00b9\u00ba\7m\2\2\u00ba\n")
        buf.write("\3\2\2\2\u00bb\u00bc\7e\2\2\u00bc\u00bd\7n\2\2\u00bd\u00be")
        buf.write("\7c\2\2\u00be\u00bf\7u\2\2\u00bf\u00c0\7u\2\2\u00c0\f")
        buf.write("\3\2\2\2\u00c1\u00c2\7e\2\2\u00c2\u00c3\7q\2\2\u00c3\u00c4")
        buf.write("\7p\2\2\u00c4\u00c5\7v\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7")
        buf.write("\7p\2\2\u00c7\u00c8\7w\2\2\u00c8\u00c9\7g\2\2\u00c9\16")
        buf.write("\3\2\2\2\u00ca\u00cb\7f\2\2\u00cb\u00cc\7q\2\2\u00cc\20")
        buf.write("\3\2\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf\7h\2\2\u00cf\22")
        buf.write("\3\2\2\2\u00d0\u00d1\7g\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3")
        buf.write("\7u\2\2\u00d3\u00d4\7g\2\2\u00d4\24\3\2\2\2\u00d5\u00d6")
        buf.write("\7g\2\2\u00d6\u00d7\7z\2\2\u00d7\u00d8\7v\2\2\u00d8\u00d9")
        buf.write("\7g\2\2\u00d9\u00da\7p\2\2\u00da\u00db\7f\2\2\u00db\u00dc")
        buf.write("\7u\2\2\u00dc\26\3\2\2\2\u00dd\u00de\7k\2\2\u00de\u00df")
        buf.write("\7p\2\2\u00df\u00e0\7v\2\2\u00e0\30\3\2\2\2\u00e1\u00e2")
        buf.write("\7h\2\2\u00e2\u00e3\7n\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5")
        buf.write("\7c\2\2\u00e5\u00e6\7v\2\2\u00e6\32\3\2\2\2\u00e7\u00e8")
        buf.write("\7p\2\2\u00e8\u00e9\7g\2\2\u00e9\u00ea\7y\2\2\u00ea\34")
        buf.write("\3\2\2\2\u00eb\u00ec\7u\2\2\u00ec\u00ed\7v\2\2\u00ed\u00ee")
        buf.write("\7t\2\2\u00ee\u00ef\7k\2\2\u00ef\u00f0\7p\2\2\u00f0\u00f1")
        buf.write("\7i\2\2\u00f1\36\3\2\2\2\u00f2\u00f3\7v\2\2\u00f3\u00f4")
        buf.write("\7j\2\2\u00f4\u00f5\7g\2\2\u00f5\u00f6\7p\2\2\u00f6 \3")
        buf.write("\2\2\2\u00f7\u00f8\7h\2\2\u00f8\u00f9\7q\2\2\u00f9\u00fa")
        buf.write("\7t\2\2\u00fa\"\3\2\2\2\u00fb\u00fc\7t\2\2\u00fc\u00fd")
        buf.write("\7g\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7w\2\2\u00ff\u0100")
        buf.write("\7t\2\2\u0100\u0101\7p\2\2\u0101$\3\2\2\2\u0102\u0103")
        buf.write("\7v\2\2\u0103\u0104\7t\2\2\u0104\u0105\7w\2\2\u0105\u0106")
        buf.write("\7g\2\2\u0106&\3\2\2\2\u0107\u0108\7h\2\2\u0108\u0109")
        buf.write("\7c\2\2\u0109\u010a\7n\2\2\u010a\u010b\7u\2\2\u010b\u010c")
        buf.write("\7g\2\2\u010c(\3\2\2\2\u010d\u010e\7x\2\2\u010e\u010f")
        buf.write("\7q\2\2\u010f\u0110\7k\2\2\u0110\u0111\7f\2\2\u0111*\3")
        buf.write("\2\2\2\u0112\u0113\7p\2\2\u0113\u0114\7k\2\2\u0114\u0115")
        buf.write("\7n\2\2\u0115,\3\2\2\2\u0116\u0117\7v\2\2\u0117\u0118")
        buf.write("\7j\2\2\u0118\u0119\7k\2\2\u0119\u011a\7u\2\2\u011a.\3")
        buf.write("\2\2\2\u011b\u011c\7h\2\2\u011c\u011d\7k\2\2\u011d\u011e")
        buf.write("\7p\2\2\u011e\u011f\7c\2\2\u011f\u0120\7n\2\2\u0120\60")
        buf.write("\3\2\2\2\u0121\u0122\7u\2\2\u0122\u0123\7v\2\2\u0123\u0124")
        buf.write("\7c\2\2\u0124\u0125\7v\2\2\u0125\u0126\7k\2\2\u0126\u0127")
        buf.write("\7e\2\2\u0127\62\3\2\2\2\u0128\u0129\7v\2\2\u0129\u012a")
        buf.write("\7q\2\2\u012a\64\3\2\2\2\u012b\u012c\7f\2\2\u012c\u012d")
        buf.write("\7q\2\2\u012d\u012e\7y\2\2\u012e\u012f\7p\2\2\u012f\u0130")
        buf.write("\7v\2\2\u0130\u0131\7q\2\2\u0131\66\3\2\2\2\u0132\u0133")
        buf.write("\7-\2\2\u01338\3\2\2\2\u0134\u0135\7/\2\2\u0135:\3\2\2")
        buf.write("\2\u0136\u0137\7,\2\2\u0137<\3\2\2\2\u0138\u0139\7\61")
        buf.write("\2\2\u0139>\3\2\2\2\u013a\u013b\7^\2\2\u013b@\3\2\2\2")
        buf.write("\u013c\u013d\7\'\2\2\u013dB\3\2\2\2\u013e\u013f\7#\2\2")
        buf.write("\u013fD\3\2\2\2\u0140\u0141\7(\2\2\u0141\u0142\7(\2\2")
        buf.write("\u0142F\3\2\2\2\u0143\u0144\7~\2\2\u0144\u0145\7~\2\2")
        buf.write("\u0145H\3\2\2\2\u0146\u0147\7?\2\2\u0147\u0148\7?\2\2")
        buf.write("\u0148J\3\2\2\2\u0149\u014a\7?\2\2\u014aL\3\2\2\2\u014b")
        buf.write("\u014c\7#\2\2\u014c\u014d\7?\2\2\u014dN\3\2\2\2\u014e")
        buf.write("\u014f\7>\2\2\u014fP\3\2\2\2\u0150\u0151\7>\2\2\u0151")
        buf.write("\u0152\7?\2\2\u0152R\3\2\2\2\u0153\u0154\7@\2\2\u0154")
        buf.write("T\3\2\2\2\u0155\u0156\7@\2\2\u0156\u0157\7?\2\2\u0157")
        buf.write("V\3\2\2\2\u0158\u0159\7`\2\2\u0159X\3\2\2\2\u015a\u015b")
        buf.write("\7<\2\2\u015b\u015c\7<\2\2\u015cZ\3\2\2\2\u015d\u015e")
        buf.write("\7*\2\2\u015e\\\3\2\2\2\u015f\u0160\7+\2\2\u0160^\3\2")
        buf.write("\2\2\u0161\u0162\7]\2\2\u0162`\3\2\2\2\u0163\u0164\7_")
        buf.write("\2\2\u0164b\3\2\2\2\u0165\u0166\7\60\2\2\u0166d\3\2\2")
        buf.write("\2\u0167\u0168\7.\2\2\u0168f\3\2\2\2\u0169\u016a\7=\2")
        buf.write("\2\u016ah\3\2\2\2\u016b\u016c\7<\2\2\u016cj\3\2\2\2\u016d")
        buf.write("\u016e\7}\2\2\u016el\3\2\2\2\u016f\u0170\7\177\2\2\u0170")
        buf.write("n\3\2\2\2\u0171\u0173\5\u0083B\2\u0172\u0171\3\2\2\2\u0173")
        buf.write("\u0174\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2")
        buf.write("\u0175p\3\2\2\2\u0176\u0177\5s:\2\u0177\u0178\5u;\2\u0178")
        buf.write("\u0181\3\2\2\2\u0179\u017a\5s:\2\u017a\u017b\5w<\2\u017b")
        buf.write("\u0181\3\2\2\2\u017c\u017d\5s:\2\u017d\u017e\5u;\2\u017e")
        buf.write("\u017f\5w<\2\u017f\u0181\3\2\2\2\u0180\u0176\3\2\2\2\u0180")
        buf.write("\u0179\3\2\2\2\u0180\u017c\3\2\2\2\u0181r\3\2\2\2\u0182")
        buf.write("\u0183\5o8\2\u0183t\3\2\2\2\u0184\u0188\7\60\2\2\u0185")
        buf.write("\u0187\t\3\2\2\u0186\u0185\3\2\2\2\u0187\u018a\3\2\2\2")
        buf.write("\u0188\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189v\3\2\2")
        buf.write("\2\u018a\u0188\3\2\2\2\u018b\u018d\t\4\2\2\u018c\u018e")
        buf.write("\t\5\2\2\u018d\u018c\3\2\2\2\u018d\u018e\3\2\2\2\u018e")
        buf.write("\u0190\3\2\2\2\u018f\u0191\t\3\2\2\u0190\u018f\3\2\2\2")
        buf.write("\u0191\u0192\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0193\3")
        buf.write("\2\2\2\u0193x\3\2\2\2\u0194\u0199\n\6\2\2\u0195\u0199")
        buf.write("\5{>\2\u0196\u0197\7)\2\2\u0197\u0199\7$\2\2\u0198\u0194")
        buf.write("\3\2\2\2\u0198\u0195\3\2\2\2\u0198\u0196\3\2\2\2\u0199")
        buf.write("z\3\2\2\2\u019a\u019b\7^\2\2\u019b\u019c\t\7\2\2\u019c")
        buf.write("|\3\2\2\2\u019d\u01a1\7$\2\2\u019e\u01a0\5y=\2\u019f\u019e")
        buf.write("\3\2\2\2\u01a0\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1")
        buf.write("\u01a2\3\2\2\2\u01a2\u01a4\3\2\2\2\u01a3\u01a1\3\2\2\2")
        buf.write("\u01a4\u01a5\7$\2\2\u01a5\u01a6\b?\3\2\u01a6~\3\2\2\2")
        buf.write("\u01a7\u01aa\5\u0081A\2\u01a8\u01aa\5\u0085C\2\u01a9\u01a7")
        buf.write("\3\2\2\2\u01a9\u01a8\3\2\2\2\u01aa\u01b0\3\2\2\2\u01ab")
        buf.write("\u01af\5\u0081A\2\u01ac\u01af\5\u0083B\2\u01ad\u01af\5")
        buf.write("\u0085C\2\u01ae\u01ab\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae")
        buf.write("\u01ad\3\2\2\2\u01af\u01b2\3\2\2\2\u01b0\u01ae\3\2\2\2")
        buf.write("\u01b0\u01b1\3\2\2\2\u01b1\u0080\3\2\2\2\u01b2\u01b0\3")
        buf.write("\2\2\2\u01b3\u01b4\t\b\2\2\u01b4\u0082\3\2\2\2\u01b5\u01b6")
        buf.write("\t\3\2\2\u01b6\u0084\3\2\2\2\u01b7\u01b8\7a\2\2\u01b8")
        buf.write("\u0086\3\2\2\2\u01b9\u01ba\7^\2\2\u01ba\u01bb\n\7\2\2")
        buf.write("\u01bb\u0088\3\2\2\2\u01bc\u01c0\7$\2\2\u01bd\u01bf\5")
        buf.write("y=\2\u01be\u01bd\3\2\2\2\u01bf\u01c2\3\2\2\2\u01c0\u01be")
        buf.write("\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01c4\3\2\2\2\u01c2")
        buf.write("\u01c0\3\2\2\2\u01c3\u01c5\t\t\2\2\u01c4\u01c3\3\2\2\2")
        buf.write("\u01c5\u01c6\3\2\2\2\u01c6\u01c7\bE\4\2\u01c7\u008a\3")
        buf.write("\2\2\2\u01c8\u01cc\7$\2\2\u01c9\u01cb\5y=\2\u01ca\u01c9")
        buf.write("\3\2\2\2\u01cb\u01ce\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cc")
        buf.write("\u01cd\3\2\2\2\u01cd\u01cf\3\2\2\2\u01ce\u01cc\3\2\2\2")
        buf.write("\u01cf\u01d0\5\u0087D\2\u01d0\u01d1\bF\5\2\u01d1\u008c")
        buf.write("\3\2\2\2\u01d2\u01d3\13\2\2\2\u01d3\u01d4\bG\6\2\u01d4")
        buf.write("\u008e\3\2\2\2\24\2\u0092\u009c\u00a5\u00a9\u0174\u0180")
        buf.write("\u0188\u018d\u0192\u0198\u01a1\u01a9\u01ae\u01b0\u01c0")
        buf.write("\u01c4\u01cc\7\b\2\2\3?\2\3E\3\3F\4\3G\5")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    COMMENT = 2
    BOOLEAN = 3
    BREAK = 4
    CLASS = 5
    CONTINUE = 6
    DO = 7
    IF = 8
    ELSE = 9
    EXTENDS = 10
    INT = 11
    FLOAT = 12
    NEW = 13
    STRING = 14
    THEN = 15
    FOR = 16
    RETURN = 17
    TRUE = 18
    FALSE = 19
    VOID = 20
    NIL = 21
    THIS = 22
    FINAL = 23
    STATIC = 24
    TO = 25
    DOWNTO = 26
    ADD = 27
    SUB = 28
    MUL = 29
    DIV = 30
    IDIV = 31
    MOD = 32
    NOT = 33
    AND = 34
    OR = 35
    EQQ = 36
    EQ = 37
    NOTEQ = 38
    LT = 39
    LTEQ = 40
    GT = 41
    GTEQ = 42
    CONCAT = 43
    SCOPE = 44
    LR = 45
    RR = 46
    LS = 47
    RS = 48
    DOT = 49
    COMMA = 50
    SEMI = 51
    COLON = 52
    LB = 53
    RB = 54
    INTLIT = 55
    FLOATLIT = 56
    STRING_LIT = 57
    ID = 58
    UNCLOSE_STRING = 59
    ILLEGAL_ESCAPE = 60
    ERROR_TOKEN = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'boolean'", "'break'", "'class'", "'continue'", "'do'", "'if'", 
            "'else'", "'extends'", "'int'", "'float'", "'new'", "'string'", 
            "'then'", "'for'", "'return'", "'true'", "'false'", "'void'", 
            "'nil'", "'this'", "'final'", "'static'", "'to'", "'downto'", 
            "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", "'!'", "'&&'", "'||'", 
            "'=='", "'='", "'!='", "'<'", "'<='", "'>'", "'>='", "'^'", 
            "'::'", "'('", "')'", "'['", "']'", "'.'", "','", "';'", "':'", 
            "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "COMMENT", "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", 
            "IF", "ELSE", "EXTENDS", "INT", "FLOAT", "NEW", "STRING", "THEN", 
            "FOR", "RETURN", "TRUE", "FALSE", "VOID", "NIL", "THIS", "FINAL", 
            "STATIC", "TO", "DOWNTO", "ADD", "SUB", "MUL", "DIV", "IDIV", 
            "MOD", "NOT", "AND", "OR", "EQQ", "EQ", "NOTEQ", "LT", "LTEQ", 
            "GT", "GTEQ", "CONCAT", "SCOPE", "LR", "RR", "LS", "RS", "DOT", 
            "COMMA", "SEMI", "COLON", "LB", "RB", "INTLIT", "FLOATLIT", 
            "STRING_LIT", "ID", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    ruleNames = [ "WS", "COMMENT", "BOOLEAN", "BREAK", "CLASS", "CONTINUE", 
                  "DO", "IF", "ELSE", "EXTENDS", "INT", "FLOAT", "NEW", 
                  "STRING", "THEN", "FOR", "RETURN", "TRUE", "FALSE", "VOID", 
                  "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", "ADD", 
                  "SUB", "MUL", "DIV", "IDIV", "MOD", "NOT", "AND", "OR", 
                  "EQQ", "EQ", "NOTEQ", "LT", "LTEQ", "GT", "GTEQ", "CONCAT", 
                  "SCOPE", "LR", "RR", "LS", "RS", "DOT", "COMMA", "SEMI", 
                  "COLON", "LB", "RB", "INTLIT", "FLOATLIT", "INT_PART", 
                  "DEC_PART", "EXP_PART", "STR_CHAR", "ESC_SEQUENCE", "STRING_LIT", 
                  "ID", "LETTER", "DIGIT", "UNDERSCORE", "ILL_ESCAPE", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

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
            actions[61] = self.STRING_LIT_action 
            actions[67] = self.UNCLOSE_STRING_action 
            actions[68] = self.ILLEGAL_ESCAPE_action 
            actions[69] = self.ERROR_TOKEN_action 
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

     


