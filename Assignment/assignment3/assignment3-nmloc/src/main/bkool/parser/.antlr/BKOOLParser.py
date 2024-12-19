# Generated from /Users/duyanhle/Desktop/assignment2/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\u022c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0094\n")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\5\5\u009e\n\5\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\5\7\u00a8\n\7\3\b\3\b\5\b\u00ac")
        buf.write("\n\b\3\t\3\t\5\t\u00b0\n\t\3\n\3\n\3\n\3\n\3\13\3\13\5")
        buf.write("\13\u00b8\n\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\5\f\u00c3\n\f\3\r\3\r\3\r\3\r\3\16\3\16\5\16\u00cb")
        buf.write("\n\16\3\17\3\17\3\17\3\17\3\17\5\17\u00d2\n\17\3\20\3")
        buf.write("\20\3\20\3\21\3\21\3\21\3\21\5\21\u00db\n\21\3\22\3\22")
        buf.write("\5\22\u00df\n\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\25\3\25\5\25\u00ed\n\25\3\26\3\26\3\26")
        buf.write("\7\26\u00f2\n\26\f\26\16\26\u00f5\13\26\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\5\30\u00fd\n\30\3\31\3\31\3\31\3\31\3")
        buf.write("\31\5\31\u0104\n\31\3\32\3\32\3\32\3\32\3\32\5\32\u010b")
        buf.write("\n\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\5\35\u011a\n\35\3\36\3\36\3\36\3\36\5")
        buf.write("\36\u0120\n\36\3\37\3\37\3 \3 \3 \3 \3 \5 \u0129\n \3")
        buf.write("!\3!\3!\3!\3!\5!\u0130\n!\3\"\3\"\3\"\3\"\3\"\3\"\7\"")
        buf.write("\u0138\n\"\f\"\16\"\u013b\13\"\3#\3#\3#\3#\3#\3#\7#\u0143")
        buf.write("\n#\f#\16#\u0146\13#\3$\3$\3$\3$\3$\3$\7$\u014e\n$\f$")
        buf.write("\16$\u0151\13$\3%\3%\3%\3%\3%\3%\7%\u0159\n%\f%\16%\u015c")
        buf.write("\13%\3&\3&\3&\5&\u0161\n&\3\'\3\'\3\'\5\'\u0166\n\'\3")
        buf.write("(\3(\3(\3(\3(\3(\5(\u016e\n(\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\7)\u017d\n)\f)\16)\u0180\13)\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\5*\u0189\n*\3+\3+\3+\3+\3+\3+\5+\u0191\n+\3")
        buf.write(",\3,\5,\u0195\n,\3-\3-\3-\3-\3-\5-\u019c\n-\3.\3.\3.\3")
        buf.write(".\5.\u01a2\n.\3/\3/\3/\3/\3\60\3\60\3\60\3\60\5\60\u01ac")
        buf.write("\n\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\5\61")
        buf.write("\u01b7\n\61\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\5")
        buf.write("\63\u01c1\n\63\3\64\3\64\5\64\u01c5\n\64\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67")
        buf.write("\5\67\u01d5\n\67\38\38\38\38\39\39\3:\3:\3:\7:\u01e0\n")
        buf.write(":\f:\16:\u01e3\13:\3;\3;\3;\5;\u01e8\n;\3<\3<\3<\3<\3")
        buf.write("<\3=\3=\3=\3=\3=\3=\5=\u01f5\n=\3>\3>\3>\3>\3>\3>\3>\3")
        buf.write(">\3>\3>\3>\3>\5>\u0203\n>\3?\3?\3?\3?\3?\3?\3?\3?\3?\3")
        buf.write("@\3@\3@\3A\3A\3A\3B\3B\3B\3B\3C\3C\3C\3C\3C\3C\3C\3C\3")
        buf.write("D\3D\3E\3E\3F\3F\5F\u0226\nF\3F\3F\3F\3F\3F\2\7BDFHPG")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082")
        buf.write("\u0084\u0086\u0088\u008a\2\n\3\2\22\23\3\2#&\3\2!\"\3")
        buf.write("\2\'(\3\2\33\34\3\2\35 \3\2\31\32\6\2\3\3\n\n\f\f\16\16")
        buf.write("\2\u0225\2\u008c\3\2\2\2\4\u0093\3\2\2\2\6\u0095\3\2\2")
        buf.write("\2\b\u009d\3\2\2\2\n\u009f\3\2\2\2\f\u00a7\3\2\2\2\16")
        buf.write("\u00ab\3\2\2\2\20\u00af\3\2\2\2\22\u00b1\3\2\2\2\24\u00b7")
        buf.write("\3\2\2\2\26\u00c2\3\2\2\2\30\u00c4\3\2\2\2\32\u00ca\3")
        buf.write("\2\2\2\34\u00d1\3\2\2\2\36\u00d3\3\2\2\2 \u00da\3\2\2")
        buf.write("\2\"\u00de\3\2\2\2$\u00e0\3\2\2\2&\u00e5\3\2\2\2(\u00ec")
        buf.write("\3\2\2\2*\u00ee\3\2\2\2,\u00f6\3\2\2\2.\u00fc\3\2\2\2")
        buf.write("\60\u0103\3\2\2\2\62\u010a\3\2\2\2\64\u010c\3\2\2\2\66")
        buf.write("\u0110\3\2\2\28\u0119\3\2\2\2:\u011f\3\2\2\2<\u0121\3")
        buf.write("\2\2\2>\u0128\3\2\2\2@\u012f\3\2\2\2B\u0131\3\2\2\2D\u013c")
        buf.write("\3\2\2\2F\u0147\3\2\2\2H\u0152\3\2\2\2J\u0160\3\2\2\2")
        buf.write("L\u0165\3\2\2\2N\u016d\3\2\2\2P\u016f\3\2\2\2R\u0188\3")
        buf.write("\2\2\2T\u0190\3\2\2\2V\u0194\3\2\2\2X\u019b\3\2\2\2Z\u01a1")
        buf.write("\3\2\2\2\\\u01a3\3\2\2\2^\u01ab\3\2\2\2`\u01b6\3\2\2\2")
        buf.write("b\u01b8\3\2\2\2d\u01c0\3\2\2\2f\u01c4\3\2\2\2h\u01c6\3")
        buf.write("\2\2\2j\u01cb\3\2\2\2l\u01d4\3\2\2\2n\u01d6\3\2\2\2p\u01da")
        buf.write("\3\2\2\2r\u01dc\3\2\2\2t\u01e4\3\2\2\2v\u01e9\3\2\2\2")
        buf.write("x\u01f4\3\2\2\2z\u0202\3\2\2\2|\u0204\3\2\2\2~\u020d\3")
        buf.write("\2\2\2\u0080\u0210\3\2\2\2\u0082\u0213\3\2\2\2\u0084\u0217")
        buf.write("\3\2\2\2\u0086\u021f\3\2\2\2\u0088\u0221\3\2\2\2\u008a")
        buf.write("\u0225\3\2\2\2\u008c\u008d\5\4\3\2\u008d\u008e\7\2\2\3")
        buf.write("\u008e\3\3\2\2\2\u008f\u0090\5\6\4\2\u0090\u0091\5\4\3")
        buf.write("\2\u0091\u0094\3\2\2\2\u0092\u0094\5\6\4\2\u0093\u008f")
        buf.write("\3\2\2\2\u0093\u0092\3\2\2\2\u0094\5\3\2\2\2\u0095\u0096")
        buf.write("\7\5\2\2\u0096\u0097\7\67\2\2\u0097\u0098\5\b\5\2\u0098")
        buf.write("\u0099\5\n\6\2\u0099\7\3\2\2\2\u009a\u009b\7\t\2\2\u009b")
        buf.write("\u009e\7\67\2\2\u009c\u009e\3\2\2\2\u009d\u009a\3\2\2")
        buf.write("\2\u009d\u009c\3\2\2\2\u009e\t\3\2\2\2\u009f\u00a0\7/")
        buf.write("\2\2\u00a0\u00a1\5\f\7\2\u00a1\u00a2\7\60\2\2\u00a2\13")
        buf.write("\3\2\2\2\u00a3\u00a4\5\16\b\2\u00a4\u00a5\5\f\7\2\u00a5")
        buf.write("\u00a8\3\2\2\2\u00a6\u00a8\3\2\2\2\u00a7\u00a3\3\2\2\2")
        buf.write("\u00a7\u00a6\3\2\2\2\u00a8\r\3\2\2\2\u00a9\u00ac\5\"\22")
        buf.write("\2\u00aa\u00ac\5\20\t\2\u00ab\u00a9\3\2\2\2\u00ab\u00aa")
        buf.write("\3\2\2\2\u00ac\17\3\2\2\2\u00ad\u00b0\5\22\n\2\u00ae\u00b0")
        buf.write("\5\24\13\2\u00af\u00ad\3\2\2\2\u00af\u00ae\3\2\2\2\u00b0")
        buf.write("\21\3\2\2\2\u00b1\u00b2\7\67\2\2\u00b2\u00b3\5\30\r\2")
        buf.write("\u00b3\u00b4\5b\62\2\u00b4\23\3\2\2\2\u00b5\u00b8\7\30")
        buf.write("\2\2\u00b6\u00b8\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b6")
        buf.write("\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\5\26\f\2\u00ba")
        buf.write("\u00bb\7\67\2\2\u00bb\u00bc\5\30\r\2\u00bc\u00bd\5b\62")
        buf.write("\2\u00bd\25\3\2\2\2\u00be\u00c3\5\u0086D\2\u00bf\u00c3")
        buf.write("\5\u0088E\2\u00c0\u00c3\5\u008aF\2\u00c1\u00c3\7\24\2")
        buf.write("\2\u00c2\u00be\3\2\2\2\u00c2\u00bf\3\2\2\2\u00c2\u00c0")
        buf.write("\3\2\2\2\u00c2\u00c1\3\2\2\2\u00c3\27\3\2\2\2\u00c4\u00c5")
        buf.write("\7\61\2\2\u00c5\u00c6\5\32\16\2\u00c6\u00c7\7\62\2\2\u00c7")
        buf.write("\31\3\2\2\2\u00c8\u00cb\5\34\17\2\u00c9\u00cb\3\2\2\2")
        buf.write("\u00ca\u00c8\3\2\2\2\u00ca\u00c9\3\2\2\2\u00cb\33\3\2")
        buf.write("\2\2\u00cc\u00cd\5\36\20\2\u00cd\u00ce\7\63\2\2\u00ce")
        buf.write("\u00cf\5\34\17\2\u00cf\u00d2\3\2\2\2\u00d0\u00d2\5\36")
        buf.write("\20\2\u00d1\u00cc\3\2\2\2\u00d1\u00d0\3\2\2\2\u00d2\35")
        buf.write("\3\2\2\2\u00d3\u00d4\5\26\f\2\u00d4\u00d5\5 \21\2\u00d5")
        buf.write("\37\3\2\2\2\u00d6\u00d7\7\67\2\2\u00d7\u00d8\7\66\2\2")
        buf.write("\u00d8\u00db\5 \21\2\u00d9\u00db\7\67\2\2\u00da\u00d6")
        buf.write("\3\2\2\2\u00da\u00d9\3\2\2\2\u00db!\3\2\2\2\u00dc\u00df")
        buf.write("\5$\23\2\u00dd\u00df\5&\24\2\u00de\u00dc\3\2\2\2\u00de")
        buf.write("\u00dd\3\2\2\2\u00df#\3\2\2\2\u00e0\u00e1\5\60\31\2\u00e1")
        buf.write("\u00e2\5\26\f\2\u00e2\u00e3\5\62\32\2\u00e3\u00e4\7\63")
        buf.write("\2\2\u00e4%\3\2\2\2\u00e5\u00e6\5(\25\2\u00e6\u00e7\5")
        buf.write("\26\f\2\u00e7\u00e8\5*\26\2\u00e8\u00e9\7\63\2\2\u00e9")
        buf.write("\'\3\2\2\2\u00ea\u00ed\7\30\2\2\u00eb\u00ed\3\2\2\2\u00ec")
        buf.write("\u00ea\3\2\2\2\u00ec\u00eb\3\2\2\2\u00ed)\3\2\2\2\u00ee")
        buf.write("\u00f3\5,\27\2\u00ef\u00f0\7\66\2\2\u00f0\u00f2\5,\27")
        buf.write("\2\u00f1\u00ef\3\2\2\2\u00f2\u00f5\3\2\2\2\u00f3\u00f1")
        buf.write("\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4+\3\2\2\2\u00f5\u00f3")
        buf.write("\3\2\2\2\u00f6\u00f7\5 \21\2\u00f7\u00f8\5.\30\2\u00f8")
        buf.write("-\3\2\2\2\u00f9\u00fa\7,\2\2\u00fa\u00fd\5> \2\u00fb\u00fd")
        buf.write("\3\2\2\2\u00fc\u00f9\3\2\2\2\u00fc\u00fb\3\2\2\2\u00fd")
        buf.write("/\3\2\2\2\u00fe\u0104\7\27\2\2\u00ff\u0100\7\30\2\2\u0100")
        buf.write("\u0104\7\27\2\2\u0101\u0102\7\27\2\2\u0102\u0104\7\30")
        buf.write("\2\2\u0103\u00fe\3\2\2\2\u0103\u00ff\3\2\2\2\u0103\u0101")
        buf.write("\3\2\2\2\u0104\61\3\2\2\2\u0105\u0106\5\64\33\2\u0106")
        buf.write("\u0107\7\66\2\2\u0107\u0108\5\62\32\2\u0108\u010b\3\2")
        buf.write("\2\2\u0109\u010b\5\64\33\2\u010a\u0105\3\2\2\2\u010a\u0109")
        buf.write("\3\2\2\2\u010b\63\3\2\2\2\u010c\u010d\5 \21\2\u010d\u010e")
        buf.write("\7,\2\2\u010e\u010f\5> \2\u010f\65\3\2\2\2\u0110\u0111")
        buf.write("\7/\2\2\u0111\u0112\58\35\2\u0112\u0113\7\60\2\2\u0113")
        buf.write("\67\3\2\2\2\u0114\u0115\5:\36\2\u0115\u0116\7\66\2\2\u0116")
        buf.write("\u0117\58\35\2\u0117\u011a\3\2\2\2\u0118\u011a\5:\36\2")
        buf.write("\u0119\u0114\3\2\2\2\u0119\u0118\3\2\2\2\u011a9\3\2\2")
        buf.write("\2\u011b\u0120\7;\2\2\u011c\u0120\7<\2\2\u011d\u0120\7")
        buf.write("=\2\2\u011e\u0120\5<\37\2\u011f\u011b\3\2\2\2\u011f\u011c")
        buf.write("\3\2\2\2\u011f\u011d\3\2\2\2\u011f\u011e\3\2\2\2\u0120")
        buf.write(";\3\2\2\2\u0121\u0122\t\2\2\2\u0122=\3\2\2\2\u0123\u0124")
        buf.write("\5@!\2\u0124\u0125\t\3\2\2\u0125\u0126\5@!\2\u0126\u0129")
        buf.write("\3\2\2\2\u0127\u0129\5@!\2\u0128\u0123\3\2\2\2\u0128\u0127")
        buf.write("\3\2\2\2\u0129?\3\2\2\2\u012a\u012b\5B\"\2\u012b\u012c")
        buf.write("\t\4\2\2\u012c\u012d\5B\"\2\u012d\u0130\3\2\2\2\u012e")
        buf.write("\u0130\5B\"\2\u012f\u012a\3\2\2\2\u012f\u012e\3\2\2\2")
        buf.write("\u0130A\3\2\2\2\u0131\u0132\b\"\1\2\u0132\u0133\5D#\2")
        buf.write("\u0133\u0139\3\2\2\2\u0134\u0135\f\4\2\2\u0135\u0136\t")
        buf.write("\5\2\2\u0136\u0138\5D#\2\u0137\u0134\3\2\2\2\u0138\u013b")
        buf.write("\3\2\2\2\u0139\u0137\3\2\2\2\u0139\u013a\3\2\2\2\u013a")
        buf.write("C\3\2\2\2\u013b\u0139\3\2\2\2\u013c\u013d\b#\1\2\u013d")
        buf.write("\u013e\5F$\2\u013e\u0144\3\2\2\2\u013f\u0140\f\4\2\2\u0140")
        buf.write("\u0141\t\6\2\2\u0141\u0143\5F$\2\u0142\u013f\3\2\2\2\u0143")
        buf.write("\u0146\3\2\2\2\u0144\u0142\3\2\2\2\u0144\u0145\3\2\2\2")
        buf.write("\u0145E\3\2\2\2\u0146\u0144\3\2\2\2\u0147\u0148\b$\1\2")
        buf.write("\u0148\u0149\5H%\2\u0149\u014f\3\2\2\2\u014a\u014b\f\4")
        buf.write("\2\2\u014b\u014c\t\7\2\2\u014c\u014e\5H%\2\u014d\u014a")
        buf.write("\3\2\2\2\u014e\u0151\3\2\2\2\u014f\u014d\3\2\2\2\u014f")
        buf.write("\u0150\3\2\2\2\u0150G\3\2\2\2\u0151\u014f\3\2\2\2\u0152")
        buf.write("\u0153\b%\1\2\u0153\u0154\5J&\2\u0154\u015a\3\2\2\2\u0155")
        buf.write("\u0156\f\4\2\2\u0156\u0157\7*\2\2\u0157\u0159\5J&\2\u0158")
        buf.write("\u0155\3\2\2\2\u0159\u015c\3\2\2\2\u015a\u0158\3\2\2\2")
        buf.write("\u015a\u015b\3\2\2\2\u015bI\3\2\2\2\u015c\u015a\3\2\2")
        buf.write("\2\u015d\u015e\7)\2\2\u015e\u0161\5J&\2\u015f\u0161\5")
        buf.write("L\'\2\u0160\u015d\3\2\2\2\u0160\u015f\3\2\2\2\u0161K\3")
        buf.write("\2\2\2\u0162\u0163\t\6\2\2\u0163\u0166\5L\'\2\u0164\u0166")
        buf.write("\5N(\2\u0165\u0162\3\2\2\2\u0165\u0164\3\2\2\2\u0166M")
        buf.write("\3\2\2\2\u0167\u0168\5P)\2\u0168\u0169\7-\2\2\u0169\u016a")
        buf.write("\5> \2\u016a\u016b\7.\2\2\u016b\u016e\3\2\2\2\u016c\u016e")
        buf.write("\5P)\2\u016d\u0167\3\2\2\2\u016d\u016c\3\2\2\2\u016eO")
        buf.write("\3\2\2\2\u016f\u0170\b)\1\2\u0170\u0171\5R*\2\u0171\u017e")
        buf.write("\3\2\2\2\u0172\u0173\f\5\2\2\u0173\u0174\7\65\2\2\u0174")
        buf.write("\u017d\7\67\2\2\u0175\u0176\f\4\2\2\u0176\u0177\7\65\2")
        buf.write("\2\u0177\u0178\7\67\2\2\u0178\u0179\7\61\2\2\u0179\u017a")
        buf.write("\5V,\2\u017a\u017b\7\62\2\2\u017b\u017d\3\2\2\2\u017c")
        buf.write("\u0172\3\2\2\2\u017c\u0175\3\2\2\2\u017d\u0180\3\2\2\2")
        buf.write("\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017fQ\3\2\2")
        buf.write("\2\u0180\u017e\3\2\2\2\u0181\u0182\7\r\2\2\u0182\u0183")
        buf.write("\7\67\2\2\u0183\u0184\7\61\2\2\u0184\u0185\5V,\2\u0185")
        buf.write("\u0186\7\62\2\2\u0186\u0189\3\2\2\2\u0187\u0189\5T+\2")
        buf.write("\u0188\u0181\3\2\2\2\u0188\u0187\3\2\2\2\u0189S\3\2\2")
        buf.write("\2\u018a\u0191\7\26\2\2\u018b\u0191\7\67\2\2\u018c\u0191")
        buf.write("\7\25\2\2\u018d\u0191\5Z.\2\u018e\u0191\5\66\34\2\u018f")
        buf.write("\u0191\5\\/\2\u0190\u018a\3\2\2\2\u0190\u018b\3\2\2\2")
        buf.write("\u0190\u018c\3\2\2\2\u0190\u018d\3\2\2\2\u0190\u018e\3")
        buf.write("\2\2\2\u0190\u018f\3\2\2\2\u0191U\3\2\2\2\u0192\u0195")
        buf.write("\5X-\2\u0193\u0195\3\2\2\2\u0194\u0192\3\2\2\2\u0194\u0193")
        buf.write("\3\2\2\2\u0195W\3\2\2\2\u0196\u0197\5> \2\u0197\u0198")
        buf.write("\7\66\2\2\u0198\u0199\5X-\2\u0199\u019c\3\2\2\2\u019a")
        buf.write("\u019c\5> \2\u019b\u0196\3\2\2\2\u019b\u019a\3\2\2\2\u019c")
        buf.write("Y\3\2\2\2\u019d\u01a2\7;\2\2\u019e\u01a2\7<\2\2\u019f")
        buf.write("\u01a2\7=\2\2\u01a0\u01a2\5<\37\2\u01a1\u019d\3\2\2\2")
        buf.write("\u01a1\u019e\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a0\3")
        buf.write("\2\2\2\u01a2[\3\2\2\2\u01a3\u01a4\7\61\2\2\u01a4\u01a5")
        buf.write("\5> \2\u01a5\u01a6\7\62\2\2\u01a6]\3\2\2\2\u01a7\u01a8")
        buf.write("\5`\61\2\u01a8\u01a9\5^\60\2\u01a9\u01ac\3\2\2\2\u01aa")
        buf.write("\u01ac\3\2\2\2\u01ab\u01a7\3\2\2\2\u01ab\u01aa\3\2\2\2")
        buf.write("\u01ac_\3\2\2\2\u01ad\u01b7\5d\63\2\u01ae\u01b7\5b\62")
        buf.write("\2\u01af\u01b7\5v<\2\u01b0\u01b7\5z>\2\u01b1\u01b7\5|")
        buf.write("?\2\u01b2\u01b7\5~@\2\u01b3\u01b7\5\u0080A\2\u01b4\u01b7")
        buf.write("\5\u0082B\2\u01b5\u01b7\5\u0084C\2\u01b6\u01ad\3\2\2\2")
        buf.write("\u01b6\u01ae\3\2\2\2\u01b6\u01af\3\2\2\2\u01b6\u01b0\3")
        buf.write("\2\2\2\u01b6\u01b1\3\2\2\2\u01b6\u01b2\3\2\2\2\u01b6\u01b3")
        buf.write("\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b5\3\2\2\2\u01b7")
        buf.write("a\3\2\2\2\u01b8\u01b9\7/\2\2\u01b9\u01ba\5^\60\2\u01ba")
        buf.write("\u01bb\7\60\2\2\u01bbc\3\2\2\2\u01bc\u01bd\5f\64\2\u01bd")
        buf.write("\u01be\5d\63\2\u01be\u01c1\3\2\2\2\u01bf\u01c1\5f\64\2")
        buf.write("\u01c0\u01bc\3\2\2\2\u01c0\u01bf\3\2\2\2\u01c1e\3\2\2")
        buf.write("\2\u01c2\u01c5\5h\65\2\u01c3\u01c5\5j\66\2\u01c4\u01c2")
        buf.write("\3\2\2\2\u01c4\u01c3\3\2\2\2\u01c5g\3\2\2\2\u01c6\u01c7")
        buf.write("\7\27\2\2\u01c7\u01c8\5\26\f\2\u01c8\u01c9\5l\67\2\u01c9")
        buf.write("\u01ca\7\63\2\2\u01cai\3\2\2\2\u01cb\u01cc\5\26\f\2\u01cc")
        buf.write("\u01cd\5p9\2\u01cd\u01ce\7\63\2\2\u01cek\3\2\2\2\u01cf")
        buf.write("\u01d0\5n8\2\u01d0\u01d1\7\66\2\2\u01d1\u01d2\5l\67\2")
        buf.write("\u01d2\u01d5\3\2\2\2\u01d3\u01d5\5n8\2\u01d4\u01cf\3\2")
        buf.write("\2\2\u01d4\u01d3\3\2\2\2\u01d5m\3\2\2\2\u01d6\u01d7\5")
        buf.write(" \21\2\u01d7\u01d8\7,\2\2\u01d8\u01d9\5> \2\u01d9o\3\2")
        buf.write("\2\2\u01da\u01db\5r:\2\u01dbq\3\2\2\2\u01dc\u01e1\5t;")
        buf.write("\2\u01dd\u01de\7\66\2\2\u01de\u01e0\5t;\2\u01df\u01dd")
        buf.write("\3\2\2\2\u01e0\u01e3\3\2\2\2\u01e1\u01df\3\2\2\2\u01e1")
        buf.write("\u01e2\3\2\2\2\u01e2s\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e4")
        buf.write("\u01e7\5 \21\2\u01e5\u01e6\7,\2\2\u01e6\u01e8\5> \2\u01e7")
        buf.write("\u01e5\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8u\3\2\2\2\u01e9")
        buf.write("\u01ea\5x=\2\u01ea\u01eb\7+\2\2\u01eb\u01ec\5> \2\u01ec")
        buf.write("\u01ed\7\63\2\2\u01edw\3\2\2\2\u01ee\u01f5\7\67\2\2\u01ef")
        buf.write("\u01f0\5P)\2\u01f0\u01f1\7\65\2\2\u01f1\u01f2\7\67\2\2")
        buf.write("\u01f2\u01f5\3\2\2\2\u01f3\u01f5\5N(\2\u01f4\u01ee\3\2")
        buf.write("\2\2\u01f4\u01ef\3\2\2\2\u01f4\u01f3\3\2\2\2\u01f5y\3")
        buf.write("\2\2\2\u01f6\u01f7\7\13\2\2\u01f7\u01f8\5> \2\u01f8\u01f9")
        buf.write("\7\17\2\2\u01f9\u01fa\5`\61\2\u01fa\u0203\3\2\2\2\u01fb")
        buf.write("\u01fc\7\13\2\2\u01fc\u01fd\5> \2\u01fd\u01fe\7\17\2\2")
        buf.write("\u01fe\u01ff\5`\61\2\u01ff\u0200\7\b\2\2\u0200\u0201\5")
        buf.write("`\61\2\u0201\u0203\3\2\2\2\u0202\u01f6\3\2\2\2\u0202\u01fb")
        buf.write("\3\2\2\2\u0203{\3\2\2\2\u0204\u0205\7\20\2\2\u0205\u0206")
        buf.write("\7\67\2\2\u0206\u0207\7+\2\2\u0207\u0208\5> \2\u0208\u0209")
        buf.write("\t\b\2\2\u0209\u020a\5> \2\u020a\u020b\7\7\2\2\u020b\u020c")
        buf.write("\5`\61\2\u020c}\3\2\2\2\u020d\u020e\7\4\2\2\u020e\u020f")
        buf.write("\7\63\2\2\u020f\177\3\2\2\2\u0210\u0211\7\6\2\2\u0211")
        buf.write("\u0212\7\63\2\2\u0212\u0081\3\2\2\2\u0213\u0214\7\21\2")
        buf.write("\2\u0214\u0215\5> \2\u0215\u0216\7\63\2\2\u0216\u0083")
        buf.write("\3\2\2\2\u0217\u0218\5P)\2\u0218\u0219\7\65\2\2\u0219")
        buf.write("\u021a\7\67\2\2\u021a\u021b\7\61\2\2\u021b\u021c\5V,\2")
        buf.write("\u021c\u021d\7\62\2\2\u021d\u021e\7\63\2\2\u021e\u0085")
        buf.write("\3\2\2\2\u021f\u0220\t\t\2\2\u0220\u0087\3\2\2\2\u0221")
        buf.write("\u0222\7\67\2\2\u0222\u0089\3\2\2\2\u0223\u0226\5\u0086")
        buf.write("D\2\u0224\u0226\5\u0088E\2\u0225\u0223\3\2\2\2\u0225\u0224")
        buf.write("\3\2\2\2\u0226\u0227\3\2\2\2\u0227\u0228\7-\2\2\u0228")
        buf.write("\u0229\7;\2\2\u0229\u022a\7.\2\2\u022a\u008b\3\2\2\2.")
        buf.write("\u0093\u009d\u00a7\u00ab\u00af\u00b7\u00c2\u00ca\u00d1")
        buf.write("\u00da\u00de\u00ec\u00f3\u00fc\u0103\u010a\u0119\u011f")
        buf.write("\u0128\u012f\u0139\u0144\u014f\u015a\u0160\u0165\u016d")
        buf.write("\u017c\u017e\u0188\u0190\u0194\u019b\u01a1\u01ab\u01b6")
        buf.write("\u01c0\u01c4\u01d4\u01e1\u01e7\u01f4\u0202\u0225")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'boolean'", "'break'", "'class'", "'continue'", 
                     "'do'", "'else'", "'extends'", "'float'", "'if'", "'int'", 
                     "'new'", "'string'", "'then'", "'for'", "'return'", 
                     "'true'", "'false'", "'void'", "'nil'", "'this'", "'final'", 
                     "'static'", "'to'", "'downto'", "'+'", "'-'", "'*'", 
                     "'/'", "'\\'", "'%'", "'=='", "'!='", "'<'", "'>'", 
                     "'<='", "'>='", "'||'", "'&&'", "'!'", "'^'", "':='", 
                     "'='", "'['", "']'", "'{'", "'}'", "'('", "')'", "';'", 
                     "':'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>", "BOOLEAN", "BREAK", "CLASS", "CONTINUE", 
                      "DO", "ELSE", "EXTENDS", "FLOAT", "IF", "INT", "NEW", 
                      "STRING", "THEN", "FOR", "RETURN", "TRUE", "FALSE", 
                      "VOID", "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", 
                      "ADD_OP", "SUB_OP", "MUL_OP", "FLODIV_OP", "INTDIV_OP", 
                      "MOD_OP", "EQUAL_OP", "NEQUAL_OP", "LT_OP", "GT_OP", 
                      "LTE_OP", "GTE_OP", "OR_OP", "AND_OP", "NOT_OP", "CONCAT_OP", 
                      "ASSIGN_OP", "EQUAL_SIGN", "LSB", "RSB", "LP", "RP", 
                      "LB", "RB", "SEMI", "COLON", "DOT", "COMMA", "ID", 
                      "WS", "LINE_COMMENT", "BLOCK_COMMENT", "INTLIT", "FLOATLIT", 
                      "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_classDeclList = 1
    RULE_classDecl = 2
    RULE_classExtends = 3
    RULE_classBody = 4
    RULE_classMemberList = 5
    RULE_classMember = 6
    RULE_methodDecl = 7
    RULE_constructor = 8
    RULE_normalMethod = 9
    RULE_typ = 10
    RULE_paramDecl = 11
    RULE_paramList = 12
    RULE_paramPrime = 13
    RULE_param = 14
    RULE_idlist = 15
    RULE_attrDecl = 16
    RULE_immutDecl = 17
    RULE_mutDecl = 18
    RULE_mutKeyword = 19
    RULE_mutMemberList = 20
    RULE_mutMember = 21
    RULE_mutInit = 22
    RULE_immutKeywords = 23
    RULE_immutInitList = 24
    RULE_immutInit = 25
    RULE_arrayLit = 26
    RULE_arrMemberList = 27
    RULE_arrMember = 28
    RULE_booleanLit = 29
    RULE_expr = 30
    RULE_expr1 = 31
    RULE_expr2 = 32
    RULE_expr3 = 33
    RULE_expr4 = 34
    RULE_expr5 = 35
    RULE_expr6 = 36
    RULE_expr7 = 37
    RULE_expr8 = 38
    RULE_expr9 = 39
    RULE_expr10 = 40
    RULE_expr11 = 41
    RULE_arglist = 42
    RULE_argprime = 43
    RULE_primiLit = 44
    RULE_subexpr = 45
    RULE_stmtlist = 46
    RULE_stmt = 47
    RULE_blockstmt = 48
    RULE_vardecllist = 49
    RULE_vardecl = 50
    RULE_immutVardecl = 51
    RULE_mutVardecl = 52
    RULE_immutVarBody = 53
    RULE_immutVarMem = 54
    RULE_mutVarBody = 55
    RULE_mutVarMemList = 56
    RULE_mutVarMem = 57
    RULE_asmstmt = 58
    RULE_asmlhs = 59
    RULE_ifstmt = 60
    RULE_forstmt = 61
    RULE_breakstmt = 62
    RULE_contstmt = 63
    RULE_retstmt = 64
    RULE_methodivkstmt = 65
    RULE_primiTyp = 66
    RULE_classTyp = 67
    RULE_arrayTyp = 68

    ruleNames =  [ "program", "classDeclList", "classDecl", "classExtends", 
                   "classBody", "classMemberList", "classMember", "methodDecl", 
                   "constructor", "normalMethod", "typ", "paramDecl", "paramList", 
                   "paramPrime", "param", "idlist", "attrDecl", "immutDecl", 
                   "mutDecl", "mutKeyword", "mutMemberList", "mutMember", 
                   "mutInit", "immutKeywords", "immutInitList", "immutInit", 
                   "arrayLit", "arrMemberList", "arrMember", "booleanLit", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "expr8", "expr9", "expr10", "expr11", 
                   "arglist", "argprime", "primiLit", "subexpr", "stmtlist", 
                   "stmt", "blockstmt", "vardecllist", "vardecl", "immutVardecl", 
                   "mutVardecl", "immutVarBody", "immutVarMem", "mutVarBody", 
                   "mutVarMemList", "mutVarMem", "asmstmt", "asmlhs", "ifstmt", 
                   "forstmt", "breakstmt", "contstmt", "retstmt", "methodivkstmt", 
                   "primiTyp", "classTyp", "arrayTyp" ]

    EOF = Token.EOF
    BOOLEAN=1
    BREAK=2
    CLASS=3
    CONTINUE=4
    DO=5
    ELSE=6
    EXTENDS=7
    FLOAT=8
    IF=9
    INT=10
    NEW=11
    STRING=12
    THEN=13
    FOR=14
    RETURN=15
    TRUE=16
    FALSE=17
    VOID=18
    NIL=19
    THIS=20
    FINAL=21
    STATIC=22
    TO=23
    DOWNTO=24
    ADD_OP=25
    SUB_OP=26
    MUL_OP=27
    FLODIV_OP=28
    INTDIV_OP=29
    MOD_OP=30
    EQUAL_OP=31
    NEQUAL_OP=32
    LT_OP=33
    GT_OP=34
    LTE_OP=35
    GTE_OP=36
    OR_OP=37
    AND_OP=38
    NOT_OP=39
    CONCAT_OP=40
    ASSIGN_OP=41
    EQUAL_SIGN=42
    LSB=43
    RSB=44
    LP=45
    RP=46
    LB=47
    RB=48
    SEMI=49
    COLON=50
    DOT=51
    COMMA=52
    ID=53
    WS=54
    LINE_COMMENT=55
    BLOCK_COMMENT=56
    INTLIT=57
    FLOATLIT=58
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




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.classDeclList()
            self.state = 139
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




    def classDeclList(self):

        localctx = BKOOLParser.ClassDeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classDeclList)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.classDecl()
                self.state = 142
                self.classDeclList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
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

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def classExtends(self):
            return self.getTypedRuleContext(BKOOLParser.ClassExtendsContext,0)


        def classBody(self):
            return self.getTypedRuleContext(BKOOLParser.ClassBodyContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_classDecl




    def classDecl(self):

        localctx = BKOOLParser.ClassDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(BKOOLParser.CLASS)
            self.state = 148
            self.match(BKOOLParser.ID)
            self.state = 149
            self.classExtends()
            self.state = 150
            self.classBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassExtendsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXTENDS(self):
            return self.getToken(BKOOLParser.EXTENDS, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_classExtends




    def classExtends(self):

        localctx = BKOOLParser.ClassExtendsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_classExtends)
        try:
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.EXTENDS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.match(BKOOLParser.EXTENDS)
                self.state = 153
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.LP]:
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


    class ClassBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def classMemberList(self):
            return self.getTypedRuleContext(BKOOLParser.ClassMemberListContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_classBody




    def classBody(self):

        localctx = BKOOLParser.ClassBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_classBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(BKOOLParser.LP)
            self.state = 158
            self.classMemberList()
            self.state = 159
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassMemberListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classMember(self):
            return self.getTypedRuleContext(BKOOLParser.ClassMemberContext,0)


        def classMemberList(self):
            return self.getTypedRuleContext(BKOOLParser.ClassMemberListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_classMemberList




    def classMemberList(self):

        localctx = BKOOLParser.ClassMemberListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_classMemberList)
        try:
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.FINAL, BKOOLParser.STATIC, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.classMember()
                self.state = 162
                self.classMemberList()
                pass
            elif token in [BKOOLParser.RP]:
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


    class ClassMemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrDecl(self):
            return self.getTypedRuleContext(BKOOLParser.AttrDeclContext,0)


        def methodDecl(self):
            return self.getTypedRuleContext(BKOOLParser.MethodDeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_classMember




    def classMember(self):

        localctx = BKOOLParser.ClassMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_classMember)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.attrDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
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

        def constructor(self):
            return self.getTypedRuleContext(BKOOLParser.ConstructorContext,0)


        def normalMethod(self):
            return self.getTypedRuleContext(BKOOLParser.NormalMethodContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_methodDecl




    def methodDecl(self):

        localctx = BKOOLParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_methodDecl)
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.constructor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.normalMethod()
                pass


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

        def paramDecl(self):
            return self.getTypedRuleContext(BKOOLParser.ParamDeclContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(BKOOLParser.BlockstmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_constructor




    def constructor(self):

        localctx = BKOOLParser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_constructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(BKOOLParser.ID)
            self.state = 176
            self.paramDecl()
            self.state = 177
            self.blockstmt()
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

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def paramDecl(self):
            return self.getTypedRuleContext(BKOOLParser.ParamDeclContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(BKOOLParser.BlockstmtContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_normalMethod




    def normalMethod(self):

        localctx = BKOOLParser.NormalMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_normalMethod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.STATIC]:
                self.state = 179
                self.match(BKOOLParser.STATIC)
                pass
            elif token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.ID]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 183
            self.typ()
            self.state = 184
            self.match(BKOOLParser.ID)
            self.state = 185
            self.paramDecl()
            self.state = 186
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primiTyp(self):
            return self.getTypedRuleContext(BKOOLParser.PrimiTypContext,0)


        def classTyp(self):
            return self.getTypedRuleContext(BKOOLParser.ClassTypContext,0)


        def arrayTyp(self):
            return self.getTypedRuleContext(BKOOLParser.ArrayTypContext,0)


        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_typ




    def typ(self):

        localctx = BKOOLParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_typ)
        try:
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.primiTyp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.classTyp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 190
                self.arrayTyp()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 191
                self.match(BKOOLParser.VOID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def paramList(self):
            return self.getTypedRuleContext(BKOOLParser.ParamListContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_paramDecl




    def paramDecl(self):

        localctx = BKOOLParser.ParamDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_paramDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(BKOOLParser.LB)
            self.state = 195
            self.paramList()
            self.state = 196
            self.match(BKOOLParser.RB)
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

        def paramPrime(self):
            return self.getTypedRuleContext(BKOOLParser.ParamPrimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramList




    def paramList(self):

        localctx = BKOOLParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_paramList)
        try:
            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.paramPrime()
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


    class ParamPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def paramPrime(self):
            return self.getTypedRuleContext(BKOOLParser.ParamPrimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramPrime




    def paramPrime(self):

        localctx = BKOOLParser.ParamPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_paramPrime)
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.param()
                self.state = 203
                self.match(BKOOLParser.SEMI)
                self.state = 204
                self.paramPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
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

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param




    def param(self):

        localctx = BKOOLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.typ()
            self.state = 210
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




    def idlist(self):

        localctx = BKOOLParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_idlist)
        try:
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.match(BKOOLParser.ID)
                self.state = 213
                self.match(BKOOLParser.COMMA)
                self.state = 214
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def immutDecl(self):
            return self.getTypedRuleContext(BKOOLParser.ImmutDeclContext,0)


        def mutDecl(self):
            return self.getTypedRuleContext(BKOOLParser.MutDeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attrDecl




    def attrDecl(self):

        localctx = BKOOLParser.AttrDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_attrDecl)
        try:
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.immutDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.mutDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImmutDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def immutKeywords(self):
            return self.getTypedRuleContext(BKOOLParser.ImmutKeywordsContext,0)


        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def immutInitList(self):
            return self.getTypedRuleContext(BKOOLParser.ImmutInitListContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_immutDecl




    def immutDecl(self):

        localctx = BKOOLParser.ImmutDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_immutDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.immutKeywords()
            self.state = 223
            self.typ()
            self.state = 224
            self.immutInitList()
            self.state = 225
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MutDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mutKeyword(self):
            return self.getTypedRuleContext(BKOOLParser.MutKeywordContext,0)


        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def mutMemberList(self):
            return self.getTypedRuleContext(BKOOLParser.MutMemberListContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_mutDecl




    def mutDecl(self):

        localctx = BKOOLParser.MutDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_mutDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.mutKeyword()
            self.state = 228
            self.typ()
            self.state = 229
            self.mutMemberList()
            self.state = 230
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MutKeywordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_mutKeyword




    def mutKeyword(self):

        localctx = BKOOLParser.MutKeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_mutKeyword)
        try:
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.STATIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.match(BKOOLParser.STATIC)
                pass
            elif token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.ID]:
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


    class MutMemberListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mutMember(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.MutMemberContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.MutMemberContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_mutMemberList




    def mutMemberList(self):

        localctx = BKOOLParser.MutMemberListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_mutMemberList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.mutMember()
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 237
                self.match(BKOOLParser.COMMA)
                self.state = 238
                self.mutMember()
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MutMemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def mutInit(self):
            return self.getTypedRuleContext(BKOOLParser.MutInitContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_mutMember




    def mutMember(self):

        localctx = BKOOLParser.MutMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_mutMember)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.idlist()
            self.state = 245
            self.mutInit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MutInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL_SIGN(self):
            return self.getToken(BKOOLParser.EQUAL_SIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_mutInit




    def mutInit(self):

        localctx = BKOOLParser.MutInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_mutInit)
        try:
            self.state = 250
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.EQUAL_SIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.match(BKOOLParser.EQUAL_SIGN)
                self.state = 248
                self.expr()
                pass
            elif token in [BKOOLParser.SEMI, BKOOLParser.COMMA]:
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


    class ImmutKeywordsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_immutKeywords




    def immutKeywords(self):

        localctx = BKOOLParser.ImmutKeywordsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_immutKeywords)
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.match(BKOOLParser.STATIC)
                self.state = 254
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 255
                self.match(BKOOLParser.FINAL)
                self.state = 256
                self.match(BKOOLParser.STATIC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImmutInitListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def immutInit(self):
            return self.getTypedRuleContext(BKOOLParser.ImmutInitContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def immutInitList(self):
            return self.getTypedRuleContext(BKOOLParser.ImmutInitListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_immutInitList




    def immutInitList(self):

        localctx = BKOOLParser.ImmutInitListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_immutInitList)
        try:
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.immutInit()
                self.state = 260
                self.match(BKOOLParser.COMMA)
                self.state = 261
                self.immutInitList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.immutInit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImmutInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def EQUAL_SIGN(self):
            return self.getToken(BKOOLParser.EQUAL_SIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_immutInit




    def immutInit(self):

        localctx = BKOOLParser.ImmutInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_immutInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.idlist()
            self.state = 267
            self.match(BKOOLParser.EQUAL_SIGN)
            self.state = 268
            self.expr()
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

        def arrMemberList(self):
            return self.getTypedRuleContext(BKOOLParser.ArrMemberListContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arrayLit




    def arrayLit(self):

        localctx = BKOOLParser.ArrayLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(BKOOLParser.LP)
            self.state = 271
            self.arrMemberList()
            self.state = 272
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrMemberListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrMember(self):
            return self.getTypedRuleContext(BKOOLParser.ArrMemberContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def arrMemberList(self):
            return self.getTypedRuleContext(BKOOLParser.ArrMemberListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_arrMemberList




    def arrMemberList(self):

        localctx = BKOOLParser.ArrMemberListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_arrMemberList)
        try:
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.arrMember()
                self.state = 275
                self.match(BKOOLParser.COMMA)
                self.state = 276
                self.arrMemberList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.arrMember()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrMemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(BKOOLParser.STRINGLIT, 0)

        def booleanLit(self):
            return self.getTypedRuleContext(BKOOLParser.BooleanLitContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_arrMember




    def arrMember(self):

        localctx = BKOOLParser.ArrMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_arrMember)
        try:
            self.state = 285
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.match(BKOOLParser.INTLIT)
                pass
            elif token in [BKOOLParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.match(BKOOLParser.FLOATLIT)
                pass
            elif token in [BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 283
                self.match(BKOOLParser.STRINGLIT)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 284
                self.booleanLit()
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


    class BooleanLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(BKOOLParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKOOLParser.FALSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_booleanLit




    def booleanLit(self):

        localctx = BKOOLParser.BooleanLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_booleanLit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Expr1Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expr1Context,i)


        def GT_OP(self):
            return self.getToken(BKOOLParser.GT_OP, 0)

        def LT_OP(self):
            return self.getToken(BKOOLParser.LT_OP, 0)

        def GTE_OP(self):
            return self.getToken(BKOOLParser.GTE_OP, 0)

        def LTE_OP(self):
            return self.getToken(BKOOLParser.LTE_OP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.expr1()
                self.state = 290
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LT_OP) | (1 << BKOOLParser.GT_OP) | (1 << BKOOLParser.LTE_OP) | (1 << BKOOLParser.GTE_OP))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 291
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Expr2Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expr2Context,i)


        def EQUAL_OP(self):
            return self.getToken(BKOOLParser.EQUAL_OP, 0)

        def NEQUAL_OP(self):
            return self.getToken(BKOOLParser.NEQUAL_OP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr1




    def expr1(self):

        localctx = BKOOLParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.expr2(0)
                self.state = 297
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.EQUAL_OP or _la==BKOOLParser.NEQUAL_OP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 298
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(BKOOLParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(BKOOLParser.Expr2Context,0)


        def AND_OP(self):
            return self.getToken(BKOOLParser.AND_OP, 0)

        def OR_OP(self):
            return self.getToken(BKOOLParser.OR_OP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 311
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 306
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 307
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.OR_OP or _la==BKOOLParser.AND_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 308
                    self.expr3(0) 
                self.state = 313
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(BKOOLParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(BKOOLParser.Expr3Context,0)


        def ADD_OP(self):
            return self.getToken(BKOOLParser.ADD_OP, 0)

        def SUB_OP(self):
            return self.getToken(BKOOLParser.SUB_OP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr3



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 322
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 317
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 318
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.ADD_OP or _la==BKOOLParser.SUB_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 319
                    self.expr4(0) 
                self.state = 324
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(BKOOLParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(BKOOLParser.Expr4Context,0)


        def MUL_OP(self):
            return self.getToken(BKOOLParser.MUL_OP, 0)

        def INTDIV_OP(self):
            return self.getToken(BKOOLParser.INTDIV_OP, 0)

        def FLODIV_OP(self):
            return self.getToken(BKOOLParser.FLODIV_OP, 0)

        def MOD_OP(self):
            return self.getToken(BKOOLParser.MOD_OP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr4



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.expr5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 333
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 328
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 329
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL_OP) | (1 << BKOOLParser.FLODIV_OP) | (1 << BKOOLParser.INTDIV_OP) | (1 << BKOOLParser.MOD_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 330
                    self.expr5(0) 
                self.state = 335
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(BKOOLParser.Expr6Context,0)


        def expr5(self):
            return self.getTypedRuleContext(BKOOLParser.Expr5Context,0)


        def CONCAT_OP(self):
            return self.getToken(BKOOLParser.CONCAT_OP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr5



    def expr5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expr5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.expr6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 344
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                    self.state = 339
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                    self.state = 340
                    self.match(BKOOLParser.CONCAT_OP)
                    self.state = 341
                    self.expr6() 
                self.state = 346
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(BKOOLParser.Expr6Context,0)


        def NOT_OP(self):
            return self.getToken(BKOOLParser.NOT_OP, 0)

        def expr7(self):
            return self.getTypedRuleContext(BKOOLParser.Expr7Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr6




    def expr6(self):

        localctx = BKOOLParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expr6)
        try:
            self.state = 350
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.match(BKOOLParser.NOT_OP)
                self.state = 348
                self.expr6()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.ADD_OP, BKOOLParser.SUB_OP, BKOOLParser.LP, BKOOLParser.LB, BKOOLParser.ID, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
                self.expr7()
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


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(BKOOLParser.Expr7Context,0)


        def ADD_OP(self):
            return self.getToken(BKOOLParser.ADD_OP, 0)

        def SUB_OP(self):
            return self.getToken(BKOOLParser.SUB_OP, 0)

        def expr8(self):
            return self.getTypedRuleContext(BKOOLParser.Expr8Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr7




    def expr7(self):

        localctx = BKOOLParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expr7)
        self._la = 0 # Token type
        try:
            self.state = 355
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADD_OP, BKOOLParser.SUB_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD_OP or _la==BKOOLParser.SUB_OP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 353
                self.expr7()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.LP, BKOOLParser.LB, BKOOLParser.ID, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.expr8()
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


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(BKOOLParser.Expr9Context,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr8




    def expr8(self):

        localctx = BKOOLParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expr8)
        try:
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.expr9(0)
                self.state = 358
                self.match(BKOOLParser.LSB)
                self.state = 359
                self.expr()
                self.state = 360
                self.match(BKOOLParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.expr9(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr10(self):
            return self.getTypedRuleContext(BKOOLParser.Expr10Context,0)


        def expr9(self):
            return self.getTypedRuleContext(BKOOLParser.Expr9Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def arglist(self):
            return self.getTypedRuleContext(BKOOLParser.ArglistContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr9



    def expr9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.expr10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 380
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 378
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Expr9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                        self.state = 368
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 369
                        self.match(BKOOLParser.DOT)
                        self.state = 370
                        self.match(BKOOLParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Expr9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                        self.state = 371
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 372
                        self.match(BKOOLParser.DOT)
                        self.state = 373
                        self.match(BKOOLParser.ID)
                        self.state = 374
                        self.match(BKOOLParser.LB)
                        self.state = 375
                        self.arglist()
                        self.state = 376
                        self.match(BKOOLParser.RB)
                        pass

             
                self.state = 382
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(BKOOLParser.NEW, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def arglist(self):
            return self.getTypedRuleContext(BKOOLParser.ArglistContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def expr11(self):
            return self.getTypedRuleContext(BKOOLParser.Expr11Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr10




    def expr10(self):

        localctx = BKOOLParser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expr10)
        try:
            self.state = 390
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self.match(BKOOLParser.NEW)
                self.state = 384
                self.match(BKOOLParser.ID)
                self.state = 385
                self.match(BKOOLParser.LB)
                self.state = 386
                self.arglist()
                self.state = 387
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.LP, BKOOLParser.LB, BKOOLParser.ID, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
                self.expr11()
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


    class Expr11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def NIL(self):
            return self.getToken(BKOOLParser.NIL, 0)

        def primiLit(self):
            return self.getTypedRuleContext(BKOOLParser.PrimiLitContext,0)


        def arrayLit(self):
            return self.getTypedRuleContext(BKOOLParser.ArrayLitContext,0)


        def subexpr(self):
            return self.getTypedRuleContext(BKOOLParser.SubexprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr11




    def expr11(self):

        localctx = BKOOLParser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expr11)
        try:
            self.state = 398
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.NIL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 394
                self.match(BKOOLParser.NIL)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 395
                self.primiLit()
                pass
            elif token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 396
                self.arrayLit()
                pass
            elif token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 6)
                self.state = 397
                self.subexpr()
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


    class ArglistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argprime(self):
            return self.getTypedRuleContext(BKOOLParser.ArgprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_arglist




    def arglist(self):

        localctx = BKOOLParser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_arglist)
        try:
            self.state = 402
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.ADD_OP, BKOOLParser.SUB_OP, BKOOLParser.NOT_OP, BKOOLParser.LP, BKOOLParser.LB, BKOOLParser.ID, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                self.argprime()
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


    class ArgprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def argprime(self):
            return self.getTypedRuleContext(BKOOLParser.ArgprimeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_argprime




    def argprime(self):

        localctx = BKOOLParser.ArgprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_argprime)
        try:
            self.state = 409
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                self.expr()
                self.state = 405
                self.match(BKOOLParser.COMMA)
                self.state = 406
                self.argprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimiLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(BKOOLParser.STRINGLIT, 0)

        def booleanLit(self):
            return self.getTypedRuleContext(BKOOLParser.BooleanLitContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_primiLit




    def primiLit(self):

        localctx = BKOOLParser.PrimiLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_primiLit)
        try:
            self.state = 415
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 411
                self.match(BKOOLParser.INTLIT)
                pass
            elif token in [BKOOLParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
                self.match(BKOOLParser.FLOATLIT)
                pass
            elif token in [BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 413
                self.match(BKOOLParser.STRINGLIT)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 414
                self.booleanLit()
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


    class SubexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_subexpr




    def subexpr(self):

        localctx = BKOOLParser.SubexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.match(BKOOLParser.LB)
            self.state = 418
            self.expr()
            self.state = 419
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(BKOOLParser.StmtlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmtlist




    def stmtlist(self):

        localctx = BKOOLParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_stmtlist)
        try:
            self.state = 425
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.BREAK, BKOOLParser.CONTINUE, BKOOLParser.FLOAT, BKOOLParser.IF, BKOOLParser.INT, BKOOLParser.NEW, BKOOLParser.STRING, BKOOLParser.FOR, BKOOLParser.RETURN, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.VOID, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.FINAL, BKOOLParser.LP, BKOOLParser.LB, BKOOLParser.ID, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.stmt()
                self.state = 422
                self.stmtlist()
                pass
            elif token in [BKOOLParser.RP]:
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


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecllist(self):
            return self.getTypedRuleContext(BKOOLParser.VardecllistContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(BKOOLParser.BlockstmtContext,0)


        def asmstmt(self):
            return self.getTypedRuleContext(BKOOLParser.AsmstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(BKOOLParser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(BKOOLParser.ForstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(BKOOLParser.BreakstmtContext,0)


        def contstmt(self):
            return self.getTypedRuleContext(BKOOLParser.ContstmtContext,0)


        def retstmt(self):
            return self.getTypedRuleContext(BKOOLParser.RetstmtContext,0)


        def methodivkstmt(self):
            return self.getTypedRuleContext(BKOOLParser.MethodivkstmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_stmt)
        try:
            self.state = 436
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.vardecllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.blockstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 429
                self.asmstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 430
                self.ifstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 431
                self.forstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 432
                self.breakstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 433
                self.contstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 434
                self.retstmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 435
                self.methodivkstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(BKOOLParser.StmtlistContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_blockstmt




    def blockstmt(self):

        localctx = BKOOLParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.match(BKOOLParser.LP)
            self.state = 439
            self.stmtlist()
            self.state = 440
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def vardecllist(self):
            return self.getTypedRuleContext(BKOOLParser.VardecllistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_vardecllist




    def vardecllist(self):

        localctx = BKOOLParser.VardecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_vardecllist)
        try:
            self.state = 446
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.vardecl()
                self.state = 443
                self.vardecllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 445
                self.vardecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def immutVardecl(self):
            return self.getTypedRuleContext(BKOOLParser.ImmutVardeclContext,0)


        def mutVardecl(self):
            return self.getTypedRuleContext(BKOOLParser.MutVardeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_vardecl




    def vardecl(self):

        localctx = BKOOLParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_vardecl)
        try:
            self.state = 450
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.FINAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 448
                self.immutVardecl()
                pass
            elif token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 449
                self.mutVardecl()
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


    class ImmutVardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def immutVarBody(self):
            return self.getTypedRuleContext(BKOOLParser.ImmutVarBodyContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_immutVardecl




    def immutVardecl(self):

        localctx = BKOOLParser.ImmutVardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_immutVardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self.match(BKOOLParser.FINAL)
            self.state = 453
            self.typ()
            self.state = 454
            self.immutVarBody()
            self.state = 455
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MutVardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def mutVarBody(self):
            return self.getTypedRuleContext(BKOOLParser.MutVarBodyContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_mutVardecl




    def mutVardecl(self):

        localctx = BKOOLParser.MutVardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_mutVardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.typ()
            self.state = 458
            self.mutVarBody()
            self.state = 459
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImmutVarBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def immutVarMem(self):
            return self.getTypedRuleContext(BKOOLParser.ImmutVarMemContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def immutVarBody(self):
            return self.getTypedRuleContext(BKOOLParser.ImmutVarBodyContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_immutVarBody




    def immutVarBody(self):

        localctx = BKOOLParser.ImmutVarBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_immutVarBody)
        try:
            self.state = 466
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 461
                self.immutVarMem()
                self.state = 462
                self.match(BKOOLParser.COMMA)
                self.state = 463
                self.immutVarBody()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 465
                self.immutVarMem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImmutVarMemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def EQUAL_SIGN(self):
            return self.getToken(BKOOLParser.EQUAL_SIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_immutVarMem




    def immutVarMem(self):

        localctx = BKOOLParser.ImmutVarMemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_immutVarMem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.idlist()
            self.state = 469
            self.match(BKOOLParser.EQUAL_SIGN)
            self.state = 470
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MutVarBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mutVarMemList(self):
            return self.getTypedRuleContext(BKOOLParser.MutVarMemListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_mutVarBody




    def mutVarBody(self):

        localctx = BKOOLParser.MutVarBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_mutVarBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.mutVarMemList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MutVarMemListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mutVarMem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.MutVarMemContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.MutVarMemContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_mutVarMemList




    def mutVarMemList(self):

        localctx = BKOOLParser.MutVarMemListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_mutVarMemList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.mutVarMem()
            self.state = 479
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 475
                self.match(BKOOLParser.COMMA)
                self.state = 476
                self.mutVarMem()
                self.state = 481
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MutVarMemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def EQUAL_SIGN(self):
            return self.getToken(BKOOLParser.EQUAL_SIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_mutVarMem




    def mutVarMem(self):

        localctx = BKOOLParser.MutVarMemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_mutVarMem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.idlist()
            self.state = 485
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EQUAL_SIGN:
                self.state = 483
                self.match(BKOOLParser.EQUAL_SIGN)
                self.state = 484
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsmstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asmlhs(self):
            return self.getTypedRuleContext(BKOOLParser.AsmlhsContext,0)


        def ASSIGN_OP(self):
            return self.getToken(BKOOLParser.ASSIGN_OP, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_asmstmt




    def asmstmt(self):

        localctx = BKOOLParser.AsmstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_asmstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self.asmlhs()
            self.state = 488
            self.match(BKOOLParser.ASSIGN_OP)
            self.state = 489
            self.expr()
            self.state = 490
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsmlhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def expr9(self):
            return self.getTypedRuleContext(BKOOLParser.Expr9Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def expr8(self):
            return self.getTypedRuleContext(BKOOLParser.Expr8Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_asmlhs




    def asmlhs(self):

        localctx = BKOOLParser.AsmlhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_asmlhs)
        try:
            self.state = 498
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 492
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 493
                self.expr9(0)
                self.state = 494
                self.match(BKOOLParser.DOT)
                self.state = 495
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 497
                self.expr8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
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

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmtContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_ifstmt




    def ifstmt(self):

        localctx = BKOOLParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_ifstmt)
        try:
            self.state = 512
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 500
                self.match(BKOOLParser.IF)
                self.state = 501
                self.expr()
                self.state = 502
                self.match(BKOOLParser.THEN)
                self.state = 503
                self.stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 505
                self.match(BKOOLParser.IF)
                self.state = 506
                self.expr()
                self.state = 507
                self.match(BKOOLParser.THEN)
                self.state = 508
                self.stmt()
                self.state = 509
                self.match(BKOOLParser.ELSE)
                self.state = 510
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ASSIGN_OP(self):
            return self.getToken(BKOOLParser.ASSIGN_OP, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_forstmt




    def forstmt(self):

        localctx = BKOOLParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_forstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.match(BKOOLParser.FOR)
            self.state = 515
            self.match(BKOOLParser.ID)
            self.state = 516
            self.match(BKOOLParser.ASSIGN_OP)
            self.state = 517
            self.expr()
            self.state = 518
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 519
            self.expr()
            self.state = 520
            self.match(BKOOLParser.DO)
            self.state = 521
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_breakstmt




    def breakstmt(self):

        localctx = BKOOLParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.match(BKOOLParser.BREAK)
            self.state = 524
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKOOLParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_contstmt




    def contstmt(self):

        localctx = BKOOLParser.ContstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_contstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            self.match(BKOOLParser.CONTINUE)
            self.state = 527
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_retstmt




    def retstmt(self):

        localctx = BKOOLParser.RetstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_retstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
            self.match(BKOOLParser.RETURN)
            self.state = 530
            self.expr()
            self.state = 531
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodivkstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(BKOOLParser.Expr9Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def arglist(self):
            return self.getTypedRuleContext(BKOOLParser.ArglistContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_methodivkstmt




    def methodivkstmt(self):

        localctx = BKOOLParser.MethodivkstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_methodivkstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self.expr9(0)
            self.state = 534
            self.match(BKOOLParser.DOT)
            self.state = 535
            self.match(BKOOLParser.ID)
            self.state = 536
            self.match(BKOOLParser.LB)
            self.state = 537
            self.arglist()
            self.state = 538
            self.match(BKOOLParser.RB)
            self.state = 539
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimiTypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_primiTyp




    def primiTyp(self):

        localctx = BKOOLParser.PrimiTypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_primiTyp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING))) != 0)):
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


    class ClassTypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_classTyp




    def classTyp(self):

        localctx = BKOOLParser.ClassTypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_classTyp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 543
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypContext(ParserRuleContext):
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

        def primiTyp(self):
            return self.getTypedRuleContext(BKOOLParser.PrimiTypContext,0)


        def classTyp(self):
            return self.getTypedRuleContext(BKOOLParser.ClassTypContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_arrayTyp




    def arrayTyp(self):

        localctx = BKOOLParser.ArrayTypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_arrayTyp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING]:
                self.state = 545
                self.primiTyp()
                pass
            elif token in [BKOOLParser.ID]:
                self.state = 546
                self.classTyp()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 549
            self.match(BKOOLParser.LSB)
            self.state = 550
            self.match(BKOOLParser.INTLIT)
            self.state = 551
            self.match(BKOOLParser.RSB)
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
        self._predicates[32] = self.expr2_sempred
        self._predicates[33] = self.expr3_sempred
        self._predicates[34] = self.expr4_sempred
        self._predicates[35] = self.expr5_sempred
        self._predicates[39] = self.expr9_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr5_sempred(self, localctx:Expr5Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr9_sempred(self, localctx:Expr9Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




