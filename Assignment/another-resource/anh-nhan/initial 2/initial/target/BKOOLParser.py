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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u021d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u008e\n\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\5\5\u009a\n\5\3\6\3\6\5\6\u009e")
        buf.write("\n\6\3\7\3\7\3\7\3\7\5\7\u00a4\n\7\3\b\3\b\5\b\u00a8\n")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\5\n\u00b4\n")
        buf.write("\n\3\13\3\13\3\13\3\13\5\13\u00ba\n\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\5\f\u00c2\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r")
        buf.write("\u00cb\n\r\3\16\3\16\3\16\5\16\u00d0\n\16\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\5\20\u00dc\n\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\5\21\u00e3\n\21\3\22\3\22\3")
        buf.write("\22\3\23\3\23\3\23\3\23\5\23\u00ec\n\23\3\24\3\24\5\24")
        buf.write("\u00f0\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\27\3\27\5\27\u0100\n\27\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\32\3\32\5\32\u010b\n\32\3")
        buf.write("\33\3\33\5\33\u010f\n\33\3\34\3\34\3\34\3\34\5\34\u0115")
        buf.write("\n\34\3\35\3\35\3\35\3\35\5\35\u011b\n\35\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\5\36\u0125\n\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \5 \u0132\n \3!\3!\3")
        buf.write("!\3!\3!\5!\u0139\n!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\5")
        buf.write("$\u0145\n$\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'")
        buf.write("\3\'\3(\3(\3(\3)\3)\5)\u015b\n)\3)\3)\3*\3*\3*\3+\3+\3")
        buf.write("+\3+\3+\3+\3+\3,\3,\3,\3,\3,\5,\u016e\n,\3-\3-\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\5.\u017b\n.\3/\3/\3/\3/\3/\3/\3/\3")
        buf.write("/\3/\7/\u0186\n/\f/\16/\u0189\13/\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\7\60\u0194\n\60\f\60\16\60\u0197")
        buf.write("\13\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\61\7\61\u01a8\n\61\f\61\16\61")
        buf.write("\u01ab\13\61\3\62\3\62\3\62\3\62\3\62\3\62\7\62\u01b3")
        buf.write("\n\62\f\62\16\62\u01b6\13\62\3\63\3\63\3\63\5\63\u01bb")
        buf.write("\n\63\3\64\3\64\3\64\3\64\3\64\5\64\u01c2\n\64\3\65\3")
        buf.write("\65\3\65\3\65\3\65\3\65\5\65\u01ca\n\65\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\7\66\u01d2\n\66\f\66\16\66\u01d5\13\66")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u01dd\n\67\38\38\5")
        buf.write("8\u01e1\n8\39\39\39\39\39\39\39\59\u01ea\n9\3:\3:\5:\u01ee")
        buf.write("\n:\3;\3;\3;\3;\3;\5;\u01f5\n;\3<\3<\3<\3<\3<\3<\5<\u01fd")
        buf.write("\n<\3=\3=\3>\3>\3>\3>\3>\3?\3?\3?\3?\3?\5?\u020b\n?\3")
        buf.write("@\3@\3A\3A\3B\3B\3B\3B\3B\3B\5B\u0217\nB\3C\3C\3C\3C\3")
        buf.write("C\2\7\\^`bjD\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz")
        buf.write("|~\u0080\u0082\u0084\2\5\3\2\22\23\3\2),\3\2\f\20\2\u0221")
        buf.write("\2\u0086\3\2\2\2\4\u008d\3\2\2\2\6\u008f\3\2\2\2\b\u0099")
        buf.write("\3\2\2\2\n\u009d\3\2\2\2\f\u00a3\3\2\2\2\16\u00a7\3\2")
        buf.write("\2\2\20\u00a9\3\2\2\2\22\u00b3\3\2\2\2\24\u00b9\3\2\2")
        buf.write("\2\26\u00c1\3\2\2\2\30\u00ca\3\2\2\2\32\u00cf\3\2\2\2")
        buf.write("\34\u00d1\3\2\2\2\36\u00db\3\2\2\2 \u00e2\3\2\2\2\"\u00e4")
        buf.write("\3\2\2\2$\u00eb\3\2\2\2&\u00ef\3\2\2\2(\u00f1\3\2\2\2")
        buf.write("*\u00f7\3\2\2\2,\u00ff\3\2\2\2.\u0101\3\2\2\2\60\u0105")
        buf.write("\3\2\2\2\62\u010a\3\2\2\2\64\u010e\3\2\2\2\66\u0114\3")
        buf.write("\2\2\28\u011a\3\2\2\2:\u0124\3\2\2\2<\u0126\3\2\2\2>\u0131")
        buf.write("\3\2\2\2@\u0138\3\2\2\2B\u013a\3\2\2\2D\u013d\3\2\2\2")
        buf.write("F\u0144\3\2\2\2H\u0146\3\2\2\2J\u0149\3\2\2\2L\u0152\3")
        buf.write("\2\2\2N\u0155\3\2\2\2P\u0158\3\2\2\2R\u015e\3\2\2\2T\u0161")
        buf.write("\3\2\2\2V\u016d\3\2\2\2X\u016f\3\2\2\2Z\u017a\3\2\2\2")
        buf.write("\\\u017c\3\2\2\2^\u018a\3\2\2\2`\u0198\3\2\2\2b\u01ac")
        buf.write("\3\2\2\2d\u01ba\3\2\2\2f\u01c1\3\2\2\2h\u01c9\3\2\2\2")
        buf.write("j\u01cb\3\2\2\2l\u01dc\3\2\2\2n\u01e0\3\2\2\2p\u01e9\3")
        buf.write("\2\2\2r\u01ed\3\2\2\2t\u01f4\3\2\2\2v\u01fc\3\2\2\2x\u01fe")
        buf.write("\3\2\2\2z\u0200\3\2\2\2|\u020a\3\2\2\2~\u020c\3\2\2\2")
        buf.write("\u0080\u020e\3\2\2\2\u0082\u0216\3\2\2\2\u0084\u0218\3")
        buf.write("\2\2\2\u0086\u0087\5\4\3\2\u0087\u0088\7\2\2\3\u0088\3")
        buf.write("\3\2\2\2\u0089\u008a\5\6\4\2\u008a\u008b\5\4\3\2\u008b")
        buf.write("\u008e\3\2\2\2\u008c\u008e\5\6\4\2\u008d\u0089\3\2\2\2")
        buf.write("\u008d\u008c\3\2\2\2\u008e\5\3\2\2\2\u008f\u0090\7\27")
        buf.write("\2\2\u0090\u0091\79\2\2\u0091\u0092\5\b\5\2\u0092\u0093")
        buf.write("\7\67\2\2\u0093\u0094\5\n\6\2\u0094\u0095\78\2\2\u0095")
        buf.write("\7\3\2\2\2\u0096\u0097\7\13\2\2\u0097\u009a\79\2\2\u0098")
        buf.write("\u009a\3\2\2\2\u0099\u0096\3\2\2\2\u0099\u0098\3\2\2\2")
        buf.write("\u009a\t\3\2\2\2\u009b\u009e\5\f\7\2\u009c\u009e\3\2\2")
        buf.write("\2\u009d\u009b\3\2\2\2\u009d\u009c\3\2\2\2\u009e\13\3")
        buf.write("\2\2\2\u009f\u00a0\5\16\b\2\u00a0\u00a1\5\f\7\2\u00a1")
        buf.write("\u00a4\3\2\2\2\u00a2\u00a4\5\16\b\2\u00a3\u009f\3\2\2")
        buf.write("\2\u00a3\u00a2\3\2\2\2\u00a4\r\3\2\2\2\u00a5\u00a8\5\20")
        buf.write("\t\2\u00a6\u00a8\5\32\16\2\u00a7\u00a5\3\2\2\2\u00a7\u00a6")
        buf.write("\3\2\2\2\u00a8\17\3\2\2\2\u00a9\u00aa\5\30\r\2\u00aa\u00ab")
        buf.write("\5\26\f\2\u00ab\u00ac\5\22\n\2\u00ac\u00ad\7\65\2\2\u00ad")
        buf.write("\21\3\2\2\2\u00ae\u00af\5\24\13\2\u00af\u00b0\7\64\2\2")
        buf.write("\u00b0\u00b1\5\22\n\2\u00b1\u00b4\3\2\2\2\u00b2\u00b4")
        buf.write("\5\24\13\2\u00b3\u00ae\3\2\2\2\u00b3\u00b2\3\2\2\2\u00b4")
        buf.write("\23\3\2\2\2\u00b5\u00ba\79\2\2\u00b6\u00b7\79\2\2\u00b7")
        buf.write("\u00b8\7&\2\2\u00b8\u00ba\5V,\2\u00b9\u00b5\3\2\2\2\u00b9")
        buf.write("\u00b6\3\2\2\2\u00ba\25\3\2\2\2\u00bb\u00c2\7\16\2\2\u00bc")
        buf.write("\u00c2\7\f\2\2\u00bd\u00c2\7\r\2\2\u00be\u00c2\7\17\2")
        buf.write("\2\u00bf\u00c2\5z>\2\u00c0\u00c2\5\u0080A\2\u00c1\u00bb")
        buf.write("\3\2\2\2\u00c1\u00bc\3\2\2\2\u00c1\u00bd\3\2\2\2\u00c1")
        buf.write("\u00be\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c0\3\2\2\2")
        buf.write("\u00c2\27\3\2\2\2\u00c3\u00c4\7\30\2\2\u00c4\u00cb\7\31")
        buf.write("\2\2\u00c5\u00c6\7\31\2\2\u00c6\u00cb\7\30\2\2\u00c7\u00cb")
        buf.write("\7\31\2\2\u00c8\u00cb\7\30\2\2\u00c9\u00cb\3\2\2\2\u00ca")
        buf.write("\u00c3\3\2\2\2\u00ca\u00c5\3\2\2\2\u00ca\u00c7\3\2\2\2")
        buf.write("\u00ca\u00c8\3\2\2\2\u00ca\u00c9\3\2\2\2\u00cb\31\3\2")
        buf.write("\2\2\u00cc\u00d0\5\34\17\2\u00cd\u00d0\5(\25\2\u00ce\u00d0")
        buf.write("\5*\26\2\u00cf\u00cc\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf")
        buf.write("\u00ce\3\2\2\2\u00d0\33\3\2\2\2\u00d1\u00d2\5&\24\2\u00d2")
        buf.write("\u00d3\5,\27\2\u00d3\u00d4\79\2\2\u00d4\u00d5\7/\2\2\u00d5")
        buf.write("\u00d6\5\36\20\2\u00d6\u00d7\7\60\2\2\u00d7\u00d8\5.\30")
        buf.write("\2\u00d8\35\3\2\2\2\u00d9\u00dc\5 \21\2\u00da\u00dc\3")
        buf.write("\2\2\2\u00db\u00d9\3\2\2\2\u00db\u00da\3\2\2\2\u00dc\37")
        buf.write("\3\2\2\2\u00dd\u00de\5\"\22\2\u00de\u00df\7\65\2\2\u00df")
        buf.write("\u00e0\5 \21\2\u00e0\u00e3\3\2\2\2\u00e1\u00e3\5\"\22")
        buf.write("\2\u00e2\u00dd\3\2\2\2\u00e2\u00e1\3\2\2\2\u00e3!\3\2")
        buf.write("\2\2\u00e4\u00e5\5\26\f\2\u00e5\u00e6\5$\23\2\u00e6#\3")
        buf.write("\2\2\2\u00e7\u00e8\79\2\2\u00e8\u00e9\7\64\2\2\u00e9\u00ec")
        buf.write("\5$\23\2\u00ea\u00ec\79\2\2\u00eb\u00e7\3\2\2\2\u00eb")
        buf.write("\u00ea\3\2\2\2\u00ec%\3\2\2\2\u00ed\u00f0\7\31\2\2\u00ee")
        buf.write("\u00f0\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00ee\3\2\2\2")
        buf.write("\u00f0\'\3\2\2\2\u00f1\u00f2\79\2\2\u00f2\u00f3\7/\2\2")
        buf.write("\u00f3\u00f4\5\36\20\2\u00f4\u00f5\7\60\2\2\u00f5\u00f6")
        buf.write("\5.\30\2\u00f6)\3\2\2\2\u00f7\u00f8\7\20\2\2\u00f8\u00f9")
        buf.write("\7\33\2\2\u00f9\u00fa\7/\2\2\u00fa\u00fb\7\60\2\2\u00fb")
        buf.write("\u00fc\5.\30\2\u00fc+\3\2\2\2\u00fd\u0100\5\26\f\2\u00fe")
        buf.write("\u0100\7\20\2\2\u00ff\u00fd\3\2\2\2\u00ff\u00fe\3\2\2")
        buf.write("\2\u0100-\3\2\2\2\u0101\u0102\7\67\2\2\u0102\u0103\5\60")
        buf.write("\31\2\u0103\u0104\78\2\2\u0104/\3\2\2\2\u0105\u0106\5")
        buf.write("\62\32\2\u0106\u0107\5\64\33\2\u0107\61\3\2\2\2\u0108")
        buf.write("\u010b\5\66\34\2\u0109\u010b\3\2\2\2\u010a\u0108\3\2\2")
        buf.write("\2\u010a\u0109\3\2\2\2\u010b\63\3\2\2\2\u010c\u010f\5")
        buf.write("8\35\2\u010d\u010f\3\2\2\2\u010e\u010c\3\2\2\2\u010e\u010d")
        buf.write("\3\2\2\2\u010f\65\3\2\2\2\u0110\u0111\5\20\t\2\u0111\u0112")
        buf.write("\5\66\34\2\u0112\u0115\3\2\2\2\u0113\u0115\5\20\t\2\u0114")
        buf.write("\u0110\3\2\2\2\u0114\u0113\3\2\2\2\u0115\67\3\2\2\2\u0116")
        buf.write("\u0117\5:\36\2\u0117\u0118\58\35\2\u0118\u011b\3\2\2\2")
        buf.write("\u0119\u011b\5:\36\2\u011a\u0116\3\2\2\2\u011a\u0119\3")
        buf.write("\2\2\2\u011b9\3\2\2\2\u011c\u0125\5<\37\2\u011d\u0125")
        buf.write("\5B\"\2\u011e\u0125\5J&\2\u011f\u0125\5L\'\2\u0120\u0125")
        buf.write("\5N(\2\u0121\u0125\5P)\2\u0122\u0125\5R*\2\u0123\u0125")
        buf.write("\5.\30\2\u0124\u011c\3\2\2\2\u0124\u011d\3\2\2\2\u0124")
        buf.write("\u011e\3\2\2\2\u0124\u011f\3\2\2\2\u0124\u0120\3\2\2\2")
        buf.write("\u0124\u0121\3\2\2\2\u0124\u0122\3\2\2\2\u0124\u0123\3")
        buf.write("\2\2\2\u0125;\3\2\2\2\u0126\u0127\5> \2\u0127\u0128\7")
        buf.write("\'\2\2\u0128\u0129\5V,\2\u0129\u012a\7\65\2\2\u012a=\3")
        buf.write("\2\2\2\u012b\u0132\5@!\2\u012c\u012d\5j\66\2\u012d\u012e")
        buf.write("\7\61\2\2\u012e\u012f\5V,\2\u012f\u0130\7\62\2\2\u0130")
        buf.write("\u0132\3\2\2\2\u0131\u012b\3\2\2\2\u0131\u012c\3\2\2\2")
        buf.write("\u0132?\3\2\2\2\u0133\u0139\79\2\2\u0134\u0135\5j\66\2")
        buf.write("\u0135\u0136\7\63\2\2\u0136\u0137\79\2\2\u0137\u0139\3")
        buf.write("\2\2\2\u0138\u0133\3\2\2\2\u0138\u0134\3\2\2\2\u0139A")
        buf.write("\3\2\2\2\u013a\u013b\5D#\2\u013b\u013c\5F$\2\u013cC\3")
        buf.write("\2\2\2\u013d\u013e\7\b\2\2\u013e\u013f\5V,\2\u013f\u0140")
        buf.write("\7\t\2\2\u0140\u0141\5:\36\2\u0141E\3\2\2\2\u0142\u0145")
        buf.write("\5H%\2\u0143\u0145\3\2\2\2\u0144\u0142\3\2\2\2\u0144\u0143")
        buf.write("\3\2\2\2\u0145G\3\2\2\2\u0146\u0147\7\n\2\2\u0147\u0148")
        buf.write("\5:\36\2\u0148I\3\2\2\2\u0149\u014a\7\21\2\2\u014a\u014b")
        buf.write("\5@!\2\u014b\u014c\7\'\2\2\u014c\u014d\5V,\2\u014d\u014e")
        buf.write("\t\2\2\2\u014e\u014f\5V,\2\u014f\u0150\7\24\2\2\u0150")
        buf.write("\u0151\5:\36\2\u0151K\3\2\2\2\u0152\u0153\7\6\2\2\u0153")
        buf.write("\u0154\7\65\2\2\u0154M\3\2\2\2\u0155\u0156\7\7\2\2\u0156")
        buf.write("\u0157\7\65\2\2\u0157O\3\2\2\2\u0158\u015a\7\25\2\2\u0159")
        buf.write("\u015b\5V,\2\u015a\u0159\3\2\2\2\u015a\u015b\3\2\2\2\u015b")
        buf.write("\u015c\3\2\2\2\u015c\u015d\7\65\2\2\u015dQ\3\2\2\2\u015e")
        buf.write("\u015f\5T+\2\u015f\u0160\7\65\2\2\u0160S\3\2\2\2\u0161")
        buf.write("\u0162\5j\66\2\u0162\u0163\7\63\2\2\u0163\u0164\79\2\2")
        buf.write("\u0164\u0165\7/\2\2\u0165\u0166\5r:\2\u0166\u0167\7\60")
        buf.write("\2\2\u0167U\3\2\2\2\u0168\u0169\5Z.\2\u0169\u016a\5X-")
        buf.write("\2\u016a\u016b\5Z.\2\u016b\u016e\3\2\2\2\u016c\u016e\5")
        buf.write("Z.\2\u016d\u0168\3\2\2\2\u016d\u016c\3\2\2\2\u016eW\3")
        buf.write("\2\2\2\u016f\u0170\t\3\2\2\u0170Y\3\2\2\2\u0171\u0172")
        buf.write("\5\\/\2\u0172\u0173\7%\2\2\u0173\u0174\5\\/\2\u0174\u017b")
        buf.write("\3\2\2\2\u0175\u0176\5\\/\2\u0176\u0177\7(\2\2\u0177\u0178")
        buf.write("\5\\/\2\u0178\u017b\3\2\2\2\u0179\u017b\5\\/\2\u017a\u0171")
        buf.write("\3\2\2\2\u017a\u0175\3\2\2\2\u017a\u0179\3\2\2\2\u017b")
        buf.write("[\3\2\2\2\u017c\u017d\b/\1\2\u017d\u017e\5^\60\2\u017e")
        buf.write("\u0187\3\2\2\2\u017f\u0180\f\5\2\2\u0180\u0181\7#\2\2")
        buf.write("\u0181\u0186\5^\60\2\u0182\u0183\f\4\2\2\u0183\u0184\7")
        buf.write("$\2\2\u0184\u0186\5^\60\2\u0185\u017f\3\2\2\2\u0185\u0182")
        buf.write("\3\2\2\2\u0186\u0189\3\2\2\2\u0187\u0185\3\2\2\2\u0187")
        buf.write("\u0188\3\2\2\2\u0188]\3\2\2\2\u0189\u0187\3\2\2\2\u018a")
        buf.write("\u018b\b\60\1\2\u018b\u018c\5`\61\2\u018c\u0195\3\2\2")
        buf.write("\2\u018d\u018e\f\5\2\2\u018e\u018f\7\34\2\2\u018f\u0194")
        buf.write("\5`\61\2\u0190\u0191\f\4\2\2\u0191\u0192\7\35\2\2\u0192")
        buf.write("\u0194\5`\61\2\u0193\u018d\3\2\2\2\u0193\u0190\3\2\2\2")
        buf.write("\u0194\u0197\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0196\3")
        buf.write("\2\2\2\u0196_\3\2\2\2\u0197\u0195\3\2\2\2\u0198\u0199")
        buf.write("\b\61\1\2\u0199\u019a\5b\62\2\u019a\u01a9\3\2\2\2\u019b")
        buf.write("\u019c\f\7\2\2\u019c\u019d\7\36\2\2\u019d\u01a8\5b\62")
        buf.write("\2\u019e\u019f\f\6\2\2\u019f\u01a0\7\37\2\2\u01a0\u01a8")
        buf.write("\5b\62\2\u01a1\u01a2\f\5\2\2\u01a2\u01a3\7!\2\2\u01a3")
        buf.write("\u01a8\5b\62\2\u01a4\u01a5\f\4\2\2\u01a5\u01a6\7 \2\2")
        buf.write("\u01a6\u01a8\5b\62\2\u01a7\u019b\3\2\2\2\u01a7\u019e\3")
        buf.write("\2\2\2\u01a7\u01a1\3\2\2\2\u01a7\u01a4\3\2\2\2\u01a8\u01ab")
        buf.write("\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa")
        buf.write("a\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac\u01ad\b\62\1\2\u01ad")
        buf.write("\u01ae\5d\63\2\u01ae\u01b4\3\2\2\2\u01af\u01b0\f\4\2\2")
        buf.write("\u01b0\u01b1\7-\2\2\u01b1\u01b3\5d\63\2\u01b2\u01af\3")
        buf.write("\2\2\2\u01b3\u01b6\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4\u01b5")
        buf.write("\3\2\2\2\u01b5c\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b7\u01b8")
        buf.write("\7\"\2\2\u01b8\u01bb\5d\63\2\u01b9\u01bb\5f\64\2\u01ba")
        buf.write("\u01b7\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bbe\3\2\2\2\u01bc")
        buf.write("\u01bd\7\35\2\2\u01bd\u01c2\5f\64\2\u01be\u01bf\7\34\2")
        buf.write("\2\u01bf\u01c2\5f\64\2\u01c0\u01c2\5h\65\2\u01c1\u01bc")
        buf.write("\3\2\2\2\u01c1\u01be\3\2\2\2\u01c1\u01c0\3\2\2\2\u01c2")
        buf.write("g\3\2\2\2\u01c3\u01c4\5j\66\2\u01c4\u01c5\7\61\2\2\u01c5")
        buf.write("\u01c6\5V,\2\u01c6\u01c7\7\62\2\2\u01c7\u01ca\3\2\2\2")
        buf.write("\u01c8\u01ca\5j\66\2\u01c9\u01c3\3\2\2\2\u01c9\u01c8\3")
        buf.write("\2\2\2\u01cai\3\2\2\2\u01cb\u01cc\b\66\1\2\u01cc\u01cd")
        buf.write("\5n8\2\u01cd\u01d3\3\2\2\2\u01ce\u01cf\f\4\2\2\u01cf\u01d0")
        buf.write("\7\63\2\2\u01d0\u01d2\5l\67\2\u01d1\u01ce\3\2\2\2\u01d2")
        buf.write("\u01d5\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2")
        buf.write("\u01d4k\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d6\u01dd\79\2\2")
        buf.write("\u01d7\u01d8\79\2\2\u01d8\u01d9\7/\2\2\u01d9\u01da\5r")
        buf.write(":\2\u01da\u01db\7\60\2\2\u01db\u01dd\3\2\2\2\u01dc\u01d6")
        buf.write("\3\2\2\2\u01dc\u01d7\3\2\2\2\u01ddm\3\2\2\2\u01de\u01e1")
        buf.write("\7\32\2\2\u01df\u01e1\5p9\2\u01e0\u01de\3\2\2\2\u01e0")
        buf.write("\u01df\3\2\2\2\u01e1o\3\2\2\2\u01e2\u01e3\7.\2\2\u01e3")
        buf.write("\u01e4\5\u0080A\2\u01e4\u01e5\7/\2\2\u01e5\u01e6\5r:\2")
        buf.write("\u01e6\u01e7\7\60\2\2\u01e7\u01ea\3\2\2\2\u01e8\u01ea")
        buf.write("\5v<\2\u01e9\u01e2\3\2\2\2\u01e9\u01e8\3\2\2\2\u01eaq")
        buf.write("\3\2\2\2\u01eb\u01ee\5t;\2\u01ec\u01ee\3\2\2\2\u01ed\u01eb")
        buf.write("\3\2\2\2\u01ed\u01ec\3\2\2\2\u01ees\3\2\2\2\u01ef\u01f0")
        buf.write("\5V,\2\u01f0\u01f1\7\64\2\2\u01f1\u01f2\5t;\2\u01f2\u01f5")
        buf.write("\3\2\2\2\u01f3\u01f5\5V,\2\u01f4\u01ef\3\2\2\2\u01f4\u01f3")
        buf.write("\3\2\2\2\u01f5u\3\2\2\2\u01f6\u01fd\5\u0082B\2\u01f7\u01fd")
        buf.write("\79\2\2\u01f8\u01f9\7/\2\2\u01f9\u01fa\5V,\2\u01fa\u01fb")
        buf.write("\7\60\2\2\u01fb\u01fd\3\2\2\2\u01fc\u01f6\3\2\2\2\u01fc")
        buf.write("\u01f7\3\2\2\2\u01fc\u01f8\3\2\2\2\u01fdw\3\2\2\2\u01fe")
        buf.write("\u01ff\t\4\2\2\u01ffy\3\2\2\2\u0200\u0201\5|?\2\u0201")
        buf.write("\u0202\7\61\2\2\u0202\u0203\5~@\2\u0203\u0204\7\62\2\2")
        buf.write("\u0204{\3\2\2\2\u0205\u020b\7\16\2\2\u0206\u020b\7\f\2")
        buf.write("\2\u0207\u020b\7\r\2\2\u0208\u020b\7\17\2\2\u0209\u020b")
        buf.write("\5\u0080A\2\u020a\u0205\3\2\2\2\u020a\u0206\3\2\2\2\u020a")
        buf.write("\u0207\3\2\2\2\u020a\u0208\3\2\2\2\u020a\u0209\3\2\2\2")
        buf.write("\u020b}\3\2\2\2\u020c\u020d\7:\2\2\u020d\177\3\2\2\2\u020e")
        buf.write("\u020f\79\2\2\u020f\u0081\3\2\2\2\u0210\u0217\7:\2\2\u0211")
        buf.write("\u0217\7;\2\2\u0212\u0217\7<\2\2\u0213\u0217\7=\2\2\u0214")
        buf.write("\u0217\7@\2\2\u0215\u0217\5\u0084C\2\u0216\u0210\3\2\2")
        buf.write("\2\u0216\u0211\3\2\2\2\u0216\u0212\3\2\2\2\u0216\u0213")
        buf.write("\3\2\2\2\u0216\u0214\3\2\2\2\u0216\u0215\3\2\2\2\u0217")
        buf.write("\u0083\3\2\2\2\u0218\u0219\7\67\2\2\u0219\u021a\5r:\2")
        buf.write("\u021a\u021b\78\2\2\u021b\u0085\3\2\2\2/\u008d\u0099\u009d")
        buf.write("\u00a3\u00a7\u00b3\u00b9\u00c1\u00ca\u00cf\u00db\u00e2")
        buf.write("\u00eb\u00ef\u00ff\u010a\u010e\u0114\u011a\u0124\u0131")
        buf.write("\u0138\u0144\u015a\u016d\u017a\u0185\u0187\u0193\u0195")
        buf.write("\u01a7\u01a9\u01b4\u01ba\u01c1\u01c9\u01d3\u01dc\u01e0")
        buf.write("\u01e9\u01ed\u01f4\u01fc\u020a\u0216")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'break'", "'continue'", "'if'", "'then'", "'else'", 
                     "'extends'", "'float'", "'boolean'", "'int'", "'string'", 
                     "'void'", "'for'", "'to'", "'downto'", "'do'", "'return'", 
                     "'nil'", "'class'", "'final'", "'static'", "'this'", 
                     "'main'", "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", 
                     "'!'", "'&&'", "'||'", "'=='", "'='", "':='", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "'^'", "'new'", "'('", 
                     "')'", "'['", "']'", "'.'", "','", "';'", "':'", "'{'", 
                     "'}'", "<INVALID>", "<INVALID>", "'0'", "<INVALID>", 
                     "<INVALID>", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "WS", "COMMENT", "LINE_COMMENT", "BREAK", 
                      "CONTINUE", "IF", "THEN", "ELSE", "EXTENDS", "FLOAT", 
                      "BOOLEAN", "INT", "STRING", "VOID", "FOR", "TO", "DOWNTO", 
                      "DO", "RETURN", "NIL", "CLASS", "FINAL", "STATIC", 
                      "THIS", "MAIN", "ADD", "SUB", "MUL", "DIV", "INT_DIV", 
                      "MOD", "NOT", "AND", "OR", "EQQ", "EQ", "ASSIGN", 
                      "NOTEQ", "LT", "LTEQ", "GT", "GTEQ", "CONCAT", "NEW", 
                      "LR", "RR", "LS", "RS", "DOT", "COMMA", "SEMI", "COLON", 
                      "LB", "RB", "ID", "INTLIT", "ZEROLIT", "FLOATLIT", 
                      "BOOLEANLIT", "TRUE", "FALSE", "STRING_LIT", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_class_decl = 2
    RULE_superclass = 3
    RULE_memberlist = 4
    RULE_members = 5
    RULE_member = 6
    RULE_variable_decl = 7
    RULE_attribute_list = 8
    RULE_attribute = 9
    RULE_type_name = 10
    RULE_var_prefix = 11
    RULE_method_decl = 12
    RULE_normal_method = 13
    RULE_paramlist = 14
    RULE_params = 15
    RULE_param = 16
    RULE_idlist = 17
    RULE_method_prefix = 18
    RULE_construct_method = 19
    RULE_main_method = 20
    RULE_method_type_name = 21
    RULE_block_stmt = 22
    RULE_block_body = 23
    RULE_var_decl_part = 24
    RULE_stmt_part = 25
    RULE_var_decl_list = 26
    RULE_stmt_list = 27
    RULE_stmt = 28
    RULE_assignment_stmt = 29
    RULE_left_exp = 30
    RULE_scalar_variable = 31
    RULE_if_stmt = 32
    RULE_if_part = 33
    RULE_else_part = 34
    RULE_else_block = 35
    RULE_for_stmt = 36
    RULE_break_stmt = 37
    RULE_continue_stmt = 38
    RULE_return_stmt = 39
    RULE_method_invo_stmt = 40
    RULE_method_invo = 41
    RULE_expr = 42
    RULE_relational = 43
    RULE_exp2 = 44
    RULE_exp3 = 45
    RULE_exp4 = 46
    RULE_exp5 = 47
    RULE_exp6 = 48
    RULE_exp7 = 49
    RULE_exp8 = 50
    RULE_exp9 = 51
    RULE_exp10 = 52
    RULE_tail_part = 53
    RULE_exp13 = 54
    RULE_exp11 = 55
    RULE_exp_list = 56
    RULE_exps = 57
    RULE_exp12 = 58
    RULE_primitive_type = 59
    RULE_array_type = 60
    RULE_element_type = 61
    RULE_size = 62
    RULE_class_type = 63
    RULE_literal = 64
    RULE_indexarr_lit = 65

    ruleNames =  [ "program", "decl", "class_decl", "superclass", "memberlist", 
                   "members", "member", "variable_decl", "attribute_list", 
                   "attribute", "type_name", "var_prefix", "method_decl", 
                   "normal_method", "paramlist", "params", "param", "idlist", 
                   "method_prefix", "construct_method", "main_method", "method_type_name", 
                   "block_stmt", "block_body", "var_decl_part", "stmt_part", 
                   "var_decl_list", "stmt_list", "stmt", "assignment_stmt", 
                   "left_exp", "scalar_variable", "if_stmt", "if_part", 
                   "else_part", "else_block", "for_stmt", "break_stmt", 
                   "continue_stmt", "return_stmt", "method_invo_stmt", "method_invo", 
                   "expr", "relational", "exp2", "exp3", "exp4", "exp5", 
                   "exp6", "exp7", "exp8", "exp9", "exp10", "tail_part", 
                   "exp13", "exp11", "exp_list", "exps", "exp12", "primitive_type", 
                   "array_type", "element_type", "size", "class_type", "literal", 
                   "indexarr_lit" ]

    EOF = Token.EOF
    WS=1
    COMMENT=2
    LINE_COMMENT=3
    BREAK=4
    CONTINUE=5
    IF=6
    THEN=7
    ELSE=8
    EXTENDS=9
    FLOAT=10
    BOOLEAN=11
    INT=12
    STRING=13
    VOID=14
    FOR=15
    TO=16
    DOWNTO=17
    DO=18
    RETURN=19
    NIL=20
    CLASS=21
    FINAL=22
    STATIC=23
    THIS=24
    MAIN=25
    ADD=26
    SUB=27
    MUL=28
    DIV=29
    INT_DIV=30
    MOD=31
    NOT=32
    AND=33
    OR=34
    EQQ=35
    EQ=36
    ASSIGN=37
    NOTEQ=38
    LT=39
    LTEQ=40
    GT=41
    GTEQ=42
    CONCAT=43
    NEW=44
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
    ID=55
    INTLIT=56
    ZEROLIT=57
    FLOATLIT=58
    BOOLEANLIT=59
    TRUE=60
    FALSE=61
    STRING_LIT=62
    UNCLOSE_STRING=63
    ILLEGAL_ESCAPE=64
    ERROR_TOKEN=65

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
            self.state = 132
            self.decl()
            self.state = 133
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
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.class_decl()
                self.state = 136
                self.decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
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
            self.state = 141
            self.match(BKOOLParser.CLASS)
            self.state = 142
            self.match(BKOOLParser.ID)
            self.state = 143
            self.superclass()
            self.state = 144
            self.match(BKOOLParser.LB)
            self.state = 145
            self.memberlist()
            self.state = 146
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
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.EXTENDS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.match(BKOOLParser.EXTENDS)
                self.state = 149
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

        def members(self):
            return self.getTypedRuleContext(BKOOLParser.MembersContext,0)


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
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.FLOAT, BKOOLParser.BOOLEAN, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.FINAL, BKOOLParser.STATIC, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.members()
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


    class MembersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(BKOOLParser.MemberContext,0)


        def members(self):
            return self.getTypedRuleContext(BKOOLParser.MembersContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_members

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMembers" ):
                return visitor.visitMembers(self)
            else:
                return visitor.visitChildren(self)




    def members(self):

        localctx = BKOOLParser.MembersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_members)
        try:
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.member()
                self.state = 158
                self.members()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.member()
                pass


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
        self.enterRule(localctx, 12, self.RULE_member)
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.variable_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
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

        def var_prefix(self):
            return self.getTypedRuleContext(BKOOLParser.Var_prefixContext,0)


        def type_name(self):
            return self.getTypedRuleContext(BKOOLParser.Type_nameContext,0)


        def attribute_list(self):
            return self.getTypedRuleContext(BKOOLParser.Attribute_listContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_variable_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_decl" ):
                return visitor.visitVariable_decl(self)
            else:
                return visitor.visitChildren(self)




    def variable_decl(self):

        localctx = BKOOLParser.Variable_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variable_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.var_prefix()
            self.state = 168
            self.type_name()
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
        self.enterRule(localctx, 16, self.RULE_attribute_list)
        try:
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.attribute()
                self.state = 173
                self.match(BKOOLParser.COMMA)
                self.state = 174
                self.attribute_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
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
        self.enterRule(localctx, 18, self.RULE_attribute)
        try:
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.match(BKOOLParser.ID)
                self.state = 181
                self.match(BKOOLParser.EQ)
                self.state = 182
                self.expr()
                pass


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
        self.enterRule(localctx, 20, self.RULE_type_name)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.match(BKOOLParser.INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.match(BKOOLParser.FLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 187
                self.match(BKOOLParser.BOOLEAN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 188
                self.match(BKOOLParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 189
                self.array_type()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 190
                self.class_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_prefixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_var_prefix

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_prefix" ):
                return visitor.visitVar_prefix(self)
            else:
                return visitor.visitChildren(self)




    def var_prefix(self):

        localctx = BKOOLParser.Var_prefixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_var_prefix)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.match(BKOOLParser.FINAL)
                self.state = 194
                self.match(BKOOLParser.STATIC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.match(BKOOLParser.STATIC)
                self.state = 196
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 197
                self.match(BKOOLParser.STATIC)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 198
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)

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

        def normal_method(self):
            return self.getTypedRuleContext(BKOOLParser.Normal_methodContext,0)


        def construct_method(self):
            return self.getTypedRuleContext(BKOOLParser.Construct_methodContext,0)


        def main_method(self):
            return self.getTypedRuleContext(BKOOLParser.Main_methodContext,0)


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
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.normal_method()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.construct_method()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 204
                self.main_method()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Normal_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_prefix(self):
            return self.getTypedRuleContext(BKOOLParser.Method_prefixContext,0)


        def method_type_name(self):
            return self.getTypedRuleContext(BKOOLParser.Method_type_nameContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LR(self):
            return self.getToken(BKOOLParser.LR, 0)

        def paramlist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamlistContext,0)


        def RR(self):
            return self.getToken(BKOOLParser.RR, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_normal_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormal_method" ):
                return visitor.visitNormal_method(self)
            else:
                return visitor.visitChildren(self)




    def normal_method(self):

        localctx = BKOOLParser.Normal_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_normal_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.method_prefix()
            self.state = 208
            self.method_type_name()
            self.state = 209
            self.match(BKOOLParser.ID)
            self.state = 210
            self.match(BKOOLParser.LR)
            self.state = 211
            self.paramlist()
            self.state = 212
            self.match(BKOOLParser.RR)
            self.state = 213
            self.block_stmt()
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

        def params(self):
            return self.getTypedRuleContext(BKOOLParser.ParamsContext,0)


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
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.FLOAT, BKOOLParser.BOOLEAN, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.params()
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


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def params(self):
            return self.getTypedRuleContext(BKOOLParser.ParamsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = BKOOLParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_params)
        try:
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.param()
                self.state = 220
                self.match(BKOOLParser.SEMI)
                self.state = 221
                self.params()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
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
            self.state = 226
            self.type_name()
            self.state = 227
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
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.match(BKOOLParser.ID)
                self.state = 230
                self.match(BKOOLParser.COMMA)
                self.state = 231
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_prefixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_method_prefix

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_prefix" ):
                return visitor.visitMethod_prefix(self)
            else:
                return visitor.visitChildren(self)




    def method_prefix(self):

        localctx = BKOOLParser.Method_prefixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_method_prefix)
        try:
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.STATIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(BKOOLParser.STATIC)
                pass
            elif token in [BKOOLParser.FLOAT, BKOOLParser.BOOLEAN, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.ID]:
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


    class Construct_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LR(self):
            return self.getToken(BKOOLParser.LR, 0)

        def paramlist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamlistContext,0)


        def RR(self):
            return self.getToken(BKOOLParser.RR, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_construct_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstruct_method" ):
                return visitor.visitConstruct_method(self)
            else:
                return visitor.visitChildren(self)




    def construct_method(self):

        localctx = BKOOLParser.Construct_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_construct_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(BKOOLParser.ID)
            self.state = 240
            self.match(BKOOLParser.LR)
            self.state = 241
            self.paramlist()
            self.state = 242
            self.match(BKOOLParser.RR)
            self.state = 243
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def MAIN(self):
            return self.getToken(BKOOLParser.MAIN, 0)

        def LR(self):
            return self.getToken(BKOOLParser.LR, 0)

        def RR(self):
            return self.getToken(BKOOLParser.RR, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_main_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_method" ):
                return visitor.visitMain_method(self)
            else:
                return visitor.visitChildren(self)




    def main_method(self):

        localctx = BKOOLParser.Main_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_main_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(BKOOLParser.VOID)
            self.state = 246
            self.match(BKOOLParser.MAIN)
            self.state = 247
            self.match(BKOOLParser.LR)
            self.state = 248
            self.match(BKOOLParser.RR)
            self.state = 249
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_type_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_name(self):
            return self.getTypedRuleContext(BKOOLParser.Type_nameContext,0)


        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_method_type_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_type_name" ):
                return visitor.visitMethod_type_name(self)
            else:
                return visitor.visitChildren(self)




    def method_type_name(self):

        localctx = BKOOLParser.Method_type_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_method_type_name)
        try:
            self.state = 253
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.FLOAT, BKOOLParser.BOOLEAN, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.type_name()
                pass
            elif token in [BKOOLParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.match(BKOOLParser.VOID)
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
        self.enterRule(localctx, 44, self.RULE_block_stmt)
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

        def var_decl_part(self):
            return self.getTypedRuleContext(BKOOLParser.Var_decl_partContext,0)


        def stmt_part(self):
            return self.getTypedRuleContext(BKOOLParser.Stmt_partContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_block_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_body" ):
                return visitor.visitBlock_body(self)
            else:
                return visitor.visitChildren(self)




    def block_body(self):

        localctx = BKOOLParser.Block_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_block_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.var_decl_part()
            self.state = 260
            self.stmt_part()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl_list(self):
            return self.getTypedRuleContext(BKOOLParser.Var_decl_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_var_decl_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_part" ):
                return visitor.visitVar_decl_part(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_part(self):

        localctx = BKOOLParser.Var_decl_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_var_decl_part)
        try:
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.var_decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_list(self):
            return self.getTypedRuleContext(BKOOLParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_part" ):
                return visitor.visitStmt_part(self)
            else:
                return visitor.visitChildren(self)




    def stmt_part(self):

        localctx = BKOOLParser.Stmt_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_stmt_part)
        try:
            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BREAK, BKOOLParser.CONTINUE, BKOOLParser.IF, BKOOLParser.FOR, BKOOLParser.RETURN, BKOOLParser.THIS, BKOOLParser.NEW, BKOOLParser.LR, BKOOLParser.LB, BKOOLParser.ID, BKOOLParser.INTLIT, BKOOLParser.ZEROLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLEANLIT, BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.stmt_list()
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


    class Var_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Variable_declContext,0)


        def var_decl_list(self):
            return self.getTypedRuleContext(BKOOLParser.Var_decl_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_var_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_list" ):
                return visitor.visitVar_decl_list(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_list(self):

        localctx = BKOOLParser.Var_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_var_decl_list)
        try:
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.variable_decl()
                self.state = 271
                self.var_decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.variable_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def stmt_list(self):
            return self.getTypedRuleContext(BKOOLParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_list(self):

        localctx = BKOOLParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_stmt_list)
        try:
            self.state = 280
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.stmt()
                self.state = 277
                self.stmt_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
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
        self.enterRule(localctx, 56, self.RULE_stmt)
        try:
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.assignment_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 284
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 285
                self.break_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 286
                self.continue_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 287
                self.return_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 288
                self.method_invo_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 289
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

        def left_exp(self):
            return self.getTypedRuleContext(BKOOLParser.Left_expContext,0)


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
        self.enterRule(localctx, 58, self.RULE_assignment_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.left_exp()
            self.state = 293
            self.match(BKOOLParser.ASSIGN)
            self.state = 294
            self.expr()
            self.state = 295
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Left_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_variable(self):
            return self.getTypedRuleContext(BKOOLParser.Scalar_variableContext,0)


        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


        def LS(self):
            return self.getToken(BKOOLParser.LS, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RS(self):
            return self.getToken(BKOOLParser.RS, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_left_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeft_exp" ):
                return visitor.visitLeft_exp(self)
            else:
                return visitor.visitChildren(self)




    def left_exp(self):

        localctx = BKOOLParser.Left_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_left_exp)
        try:
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.scalar_variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.exp10(0)
                self.state = 299
                self.match(BKOOLParser.LS)
                self.state = 300
                self.expr()
                self.state = 301
                self.match(BKOOLParser.RS)
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

        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_scalar_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_variable" ):
                return visitor.visitScalar_variable(self)
            else:
                return visitor.visitChildren(self)




    def scalar_variable(self):

        localctx = BKOOLParser.Scalar_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_scalar_variable)
        try:
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
                self.exp10(0)
                self.state = 307
                self.match(BKOOLParser.DOT)
                self.state = 308
                self.match(BKOOLParser.ID)
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

        def if_part(self):
            return self.getTypedRuleContext(BKOOLParser.If_partContext,0)


        def else_part(self):
            return self.getTypedRuleContext(BKOOLParser.Else_partContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = BKOOLParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.if_part()
            self.state = 313
            self.else_part()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_partContext(ParserRuleContext):
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


        def getRuleIndex(self):
            return BKOOLParser.RULE_if_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_part" ):
                return visitor.visitIf_part(self)
            else:
                return visitor.visitChildren(self)




    def if_part(self):

        localctx = BKOOLParser.If_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_if_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(BKOOLParser.IF)
            self.state = 316
            self.expr()
            self.state = 317
            self.match(BKOOLParser.THEN)
            self.state = 318
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def else_block(self):
            return self.getTypedRuleContext(BKOOLParser.Else_blockContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_else_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_part" ):
                return visitor.visitElse_part(self)
            else:
                return visitor.visitChildren(self)




    def else_part(self):

        localctx = BKOOLParser.Else_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_else_part)
        try:
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.else_block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_else_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_block" ):
                return visitor.visitElse_block(self)
            else:
                return visitor.visitChildren(self)




    def else_block(self):

        localctx = BKOOLParser.Else_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_else_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(BKOOLParser.ELSE)
            self.state = 325
            self.stmt()
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


        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = BKOOLParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(BKOOLParser.FOR)
            self.state = 328
            self.scalar_variable()
            self.state = 329
            self.match(BKOOLParser.ASSIGN)
            self.state = 330
            self.expr()
            self.state = 331
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 332
            self.expr()
            self.state = 333
            self.match(BKOOLParser.DO)
            self.state = 334
            self.stmt()
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
        self.enterRule(localctx, 74, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(BKOOLParser.BREAK)
            self.state = 337
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
        self.enterRule(localctx, 76, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(BKOOLParser.CONTINUE)
            self.state = 340
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
        self.enterRule(localctx, 78, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(BKOOLParser.RETURN)
            self.state = 344
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.LR) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.ZEROLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.BOOLEANLIT) | (1 << BKOOLParser.STRING_LIT))) != 0):
                self.state = 343
                self.expr()


            self.state = 346
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
        self.enterRule(localctx, 80, self.RULE_method_invo_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.method_invo()
            self.state = 349
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

        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


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
            return BKOOLParser.RULE_method_invo

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invo" ):
                return visitor.visitMethod_invo(self)
            else:
                return visitor.visitChildren(self)




    def method_invo(self):

        localctx = BKOOLParser.Method_invoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_method_invo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.exp10(0)
            self.state = 352
            self.match(BKOOLParser.DOT)
            self.state = 353
            self.match(BKOOLParser.ID)
            self.state = 354
            self.match(BKOOLParser.LR)
            self.state = 355
            self.exp_list()
            self.state = 356
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


        def relational(self):
            return self.getTypedRuleContext(BKOOLParser.RelationalContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expr)
        try:
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.exp2()
                self.state = 359
                self.relational()
                self.state = 360
                self.exp2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.exp2()
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
        self.enterRule(localctx, 86, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LT) | (1 << BKOOLParser.LTEQ) | (1 << BKOOLParser.GT) | (1 << BKOOLParser.GTEQ))) != 0)):
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


        def EQQ(self):
            return self.getToken(BKOOLParser.EQQ, 0)

        def NOTEQ(self):
            return self.getToken(BKOOLParser.NOTEQ, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)




    def exp2(self):

        localctx = BKOOLParser.Exp2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_exp2)
        try:
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.exp3(0)
                self.state = 368
                self.match(BKOOLParser.EQQ)
                self.state = 369
                self.exp3(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 371
                self.exp3(0)
                self.state = 372
                self.match(BKOOLParser.NOTEQ)
                self.state = 373
                self.exp3(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 375
                self.exp3(0)
                pass


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
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 389
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 387
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 381
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 382
                        self.match(BKOOLParser.AND)
                        self.state = 383
                        self.exp4(0)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 384
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 385
                        self.match(BKOOLParser.OR)
                        self.state = 386
                        self.exp4(0)
                        pass

             
                self.state = 391
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_exp4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 403
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 401
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 395
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 396
                        self.match(BKOOLParser.ADD)
                        self.state = 397
                        self.exp5(0)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 398
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 399
                        self.match(BKOOLParser.SUB)
                        self.state = 400
                        self.exp5(0)
                        pass

             
                self.state = 405
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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

        def INT_DIV(self):
            return self.getToken(BKOOLParser.INT_DIV, 0)

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
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_exp5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.exp6(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 423
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 421
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                        self.state = 409
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 410
                        self.match(BKOOLParser.MUL)
                        self.state = 411
                        self.exp6(0)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                        self.state = 412
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 413
                        self.match(BKOOLParser.DIV)
                        self.state = 414
                        self.exp6(0)
                        pass

                    elif la_ == 3:
                        localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                        self.state = 415
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 416
                        self.match(BKOOLParser.MOD)
                        self.state = 417
                        self.exp6(0)
                        pass

                    elif la_ == 4:
                        localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                        self.state = 418
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 419
                        self.match(BKOOLParser.INT_DIV)
                        self.state = 420
                        self.exp6(0)
                        pass

             
                self.state = 425
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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

        def exp7(self):
            return self.getTypedRuleContext(BKOOLParser.Exp7Context,0)


        def exp6(self):
            return self.getTypedRuleContext(BKOOLParser.Exp6Context,0)


        def CONCAT(self):
            return self.getToken(BKOOLParser.CONCAT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)



    def exp6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_exp6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self.exp7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 434
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 429
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 430
                    self.match(BKOOLParser.CONCAT)
                    self.state = 431
                    self.exp7() 
                self.state = 436
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

        def exp7(self):
            return self.getTypedRuleContext(BKOOLParser.Exp7Context,0)


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
        self.enterRule(localctx, 98, self.RULE_exp7)
        try:
            self.state = 440
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 437
                self.match(BKOOLParser.NOT)
                self.state = 438
                self.exp7()
                pass
            elif token in [BKOOLParser.THIS, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NEW, BKOOLParser.LR, BKOOLParser.LB, BKOOLParser.ID, BKOOLParser.INTLIT, BKOOLParser.ZEROLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLEANLIT, BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 439
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

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def exp8(self):
            return self.getTypedRuleContext(BKOOLParser.Exp8Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = BKOOLParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_exp8)
        try:
            self.state = 447
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.match(BKOOLParser.SUB)
                self.state = 443
                self.exp8()
                pass
            elif token in [BKOOLParser.ADD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 444
                self.match(BKOOLParser.ADD)
                self.state = 445
                self.exp8()
                pass
            elif token in [BKOOLParser.THIS, BKOOLParser.NEW, BKOOLParser.LR, BKOOLParser.LB, BKOOLParser.ID, BKOOLParser.INTLIT, BKOOLParser.ZEROLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLEANLIT, BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 446
                self.exp9()
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


    class Exp9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


        def LS(self):
            return self.getToken(BKOOLParser.LS, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RS(self):
            return self.getToken(BKOOLParser.RS, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)




    def exp9(self):

        localctx = BKOOLParser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_exp9)
        try:
            self.state = 455
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 449
                self.exp10(0)
                self.state = 450
                self.match(BKOOLParser.LS)
                self.state = 451
                self.expr()
                self.state = 452
                self.match(BKOOLParser.RS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 454
                self.exp10(0)
                pass


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

        def exp13(self):
            return self.getTypedRuleContext(BKOOLParser.Exp13Context,0)


        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def tail_part(self):
            return self.getTypedRuleContext(BKOOLParser.Tail_partContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp10" ):
                return visitor.visitExp10(self)
            else:
                return visitor.visitChildren(self)



    def exp10(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp10Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 104
        self.enterRecursionRule(localctx, 104, self.RULE_exp10, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.exp13()
            self._ctx.stop = self._input.LT(-1)
            self.state = 465
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp10Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp10)
                    self.state = 460
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 461
                    self.match(BKOOLParser.DOT)
                    self.state = 462
                    self.tail_part() 
                self.state = 467
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

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
        self.enterRule(localctx, 106, self.RULE_tail_part)
        try:
            self.state = 474
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 468
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 469
                self.match(BKOOLParser.ID)
                self.state = 470
                self.match(BKOOLParser.LR)
                self.state = 471
                self.exp_list()
                self.state = 472
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

        def exp11(self):
            return self.getTypedRuleContext(BKOOLParser.Exp11Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp13

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp13" ):
                return visitor.visitExp13(self)
            else:
                return visitor.visitChildren(self)




    def exp13(self):

        localctx = BKOOLParser.Exp13Context(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_exp13)
        try:
            self.state = 478
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 476
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.LR, BKOOLParser.LB, BKOOLParser.ID, BKOOLParser.INTLIT, BKOOLParser.ZEROLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLEANLIT, BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 477
                self.exp11()
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


    class Exp11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(BKOOLParser.NEW, 0)

        def class_type(self):
            return self.getTypedRuleContext(BKOOLParser.Class_typeContext,0)


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
        self.enterRule(localctx, 110, self.RULE_exp11)
        try:
            self.state = 487
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 480
                self.match(BKOOLParser.NEW)
                self.state = 481
                self.class_type()
                self.state = 482
                self.match(BKOOLParser.LR)
                self.state = 483
                self.exp_list()
                self.state = 484
                self.match(BKOOLParser.RR)
                pass
            elif token in [BKOOLParser.LR, BKOOLParser.LB, BKOOLParser.ID, BKOOLParser.INTLIT, BKOOLParser.ZEROLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLEANLIT, BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 486
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
        self.enterRule(localctx, 112, self.RULE_exp_list)
        try:
            self.state = 491
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.THIS, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT, BKOOLParser.NEW, BKOOLParser.LR, BKOOLParser.LB, BKOOLParser.ID, BKOOLParser.INTLIT, BKOOLParser.ZEROLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLEANLIT, BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 489
                self.exps()
                pass
            elif token in [BKOOLParser.RR, BKOOLParser.RB]:
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
        self.enterRule(localctx, 114, self.RULE_exps)
        try:
            self.state = 498
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 493
                self.expr()
                self.state = 494
                self.match(BKOOLParser.COMMA)
                self.state = 495
                self.exps()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 497
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
        self.enterRule(localctx, 116, self.RULE_exp12)
        try:
            self.state = 506
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LB, BKOOLParser.INTLIT, BKOOLParser.ZEROLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLEANLIT, BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 500
                self.literal()
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 501
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.LR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 502
                self.match(BKOOLParser.LR)
                self.state = 503
                self.expr()
                self.state = 504
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
        self.enterRule(localctx, 118, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID))) != 0)):
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

        def size(self):
            return self.getTypedRuleContext(BKOOLParser.SizeContext,0)


        def RS(self):
            return self.getToken(BKOOLParser.RS, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = BKOOLParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self.element_type()
            self.state = 511
            self.match(BKOOLParser.LS)
            self.state = 512
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
        self.enterRule(localctx, 122, self.RULE_element_type)
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
        self.enterRule(localctx, 124, self.RULE_size)
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
        self.enterRule(localctx, 126, self.RULE_class_type)
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

        def ZEROLIT(self):
            return self.getToken(BKOOLParser.ZEROLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def BOOLEANLIT(self):
            return self.getToken(BKOOLParser.BOOLEANLIT, 0)

        def STRING_LIT(self):
            return self.getToken(BKOOLParser.STRING_LIT, 0)

        def indexarr_lit(self):
            return self.getTypedRuleContext(BKOOLParser.Indexarr_litContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BKOOLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_literal)
        try:
            self.state = 532
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 526
                self.match(BKOOLParser.INTLIT)
                pass
            elif token in [BKOOLParser.ZEROLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 527
                self.match(BKOOLParser.ZEROLIT)
                pass
            elif token in [BKOOLParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 528
                self.match(BKOOLParser.FLOATLIT)
                pass
            elif token in [BKOOLParser.BOOLEANLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 529
                self.match(BKOOLParser.BOOLEANLIT)
                pass
            elif token in [BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 530
                self.match(BKOOLParser.STRING_LIT)
                pass
            elif token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 6)
                self.state = 531
                self.indexarr_lit()
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


    class Indexarr_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def exp_list(self):
            return self.getTypedRuleContext(BKOOLParser.Exp_listContext,0)


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
        self.enterRule(localctx, 130, self.RULE_indexarr_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            self.match(BKOOLParser.LB)
            self.state = 535
            self.exp_list()
            self.state = 536
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
        self._predicates[45] = self.exp3_sempred
        self._predicates[46] = self.exp4_sempred
        self._predicates[47] = self.exp5_sempred
        self._predicates[48] = self.exp6_sempred
        self._predicates[52] = self.exp10_sempred
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
         

    def exp6_sempred(self, localctx:Exp6Context, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         

    def exp10_sempred(self, localctx:Exp10Context, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         




