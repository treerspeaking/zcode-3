# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\38")
        buf.write("\u01dd\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\3\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3\177\n\3\3\4\3\4")
        buf.write("\5\4\u0083\n\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u008b\n\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\5\5\u0092\n\5\5\5\u0094\n\5\3\6\3\6")
        buf.write("\3\6\5\6\u0099\n\6\3\7\3\7\3\7\5\7\u009e\n\7\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\5\t\u00a7\n\t\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\5\r\u00b7\n\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\5\20\u00c6\n\20\3\21\3\21\3\21\3\21\3\22\3")
        buf.write("\22\3\22\3\23\3\23\3\23\3\23\3\23\5\23\u00d4\n\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\5\24\u00db\n\24\3\25\3\25\3\25\3")
        buf.write("\25\3\25\5\25\u00e2\n\25\3\26\3\26\3\26\3\26\3\26\5\26")
        buf.write("\u00e9\n\26\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u00f1\n")
        buf.write("\27\f\27\16\27\u00f4\13\27\3\30\3\30\3\30\3\30\3\30\3")
        buf.write("\30\7\30\u00fc\n\30\f\30\16\30\u00ff\13\30\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\7\31\u0107\n\31\f\31\16\31\u010a\13")
        buf.write("\31\3\32\3\32\3\32\5\32\u010f\n\32\3\33\3\33\3\33\5\33")
        buf.write("\u0114\n\33\3\34\3\34\5\34\u0118\n\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\5\34\u011f\n\34\3\35\3\35\3\35\3\35\3\35\5\35")
        buf.write("\u0126\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\5\36\u0132\n\36\3\37\3\37\5\37\u0136\n\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3#\3#\5#\u0146")
        buf.write("\n#\3#\3#\3#\3#\5#\u014c\n#\3#\3#\3#\3#\3#\5#\u0153\n")
        buf.write("#\3#\3#\3$\3$\3%\3%\3%\3%\3&\3&\3&\5&\u0160\n&\3\'\3\'")
        buf.write("\3\'\3\'\5\'\u0166\n\'\3(\3(\3(\3(\3(\5(\u016d\n(\3)\3")
        buf.write(")\3)\3)\3)\3)\5)\u0175\n)\5)\u0177\n)\3)\3)\3*\3*\5*\u017d")
        buf.write("\n*\3+\3+\3+\3+\5+\u0183\n+\3,\3,\3,\3,\3,\5,\u018a\n")
        buf.write(",\3-\3-\3-\3-\3-\3.\3.\3.\3/\3/\5/\u0196\n/\3\60\3\60")
        buf.write("\3\60\5\60\u019b\n\60\3\60\3\60\3\60\3\61\3\61\3\61\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u01b7")
        buf.write("\n\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\65")
        buf.write("\3\65\3\66\3\66\3\67\3\67\3\67\3\67\5\67\u01ca\n\67\3")
        buf.write("8\38\38\38\38\58\u01d1\n8\39\39\39\39\39\3:\3:\3:\3:\3")
        buf.write(":\3:\2\5,.\60;\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnpr\2")
        buf.write("\b\3\2\"(\3\2\37 \3\2\31\32\3\2\33\35\4\2\b\n\r\r\3\2")
        buf.write("\b\n\2\u01db\2t\3\2\2\2\4~\3\2\2\2\6\u0082\3\2\2\2\b\u0093")
        buf.write("\3\2\2\2\n\u0098\3\2\2\2\f\u009d\3\2\2\2\16\u009f\3\2")
        buf.write("\2\2\20\u00a6\3\2\2\2\22\u00a8\3\2\2\2\24\u00aa\3\2\2")
        buf.write("\2\26\u00af\3\2\2\2\30\u00b6\3\2\2\2\32\u00b8\3\2\2\2")
        buf.write("\34\u00bd\3\2\2\2\36\u00c5\3\2\2\2 \u00c7\3\2\2\2\"\u00cb")
        buf.write("\3\2\2\2$\u00d3\3\2\2\2&\u00da\3\2\2\2(\u00e1\3\2\2\2")
        buf.write("*\u00e8\3\2\2\2,\u00ea\3\2\2\2.\u00f5\3\2\2\2\60\u0100")
        buf.write("\3\2\2\2\62\u010e\3\2\2\2\64\u0113\3\2\2\2\66\u011e\3")
        buf.write("\2\2\28\u0125\3\2\2\2:\u0131\3\2\2\2<\u0135\3\2\2\2>\u013b")
        buf.write("\3\2\2\2@\u013d\3\2\2\2B\u013f\3\2\2\2D\u0152\3\2\2\2")
        buf.write("F\u0156\3\2\2\2H\u0158\3\2\2\2J\u015c\3\2\2\2L\u0165\3")
        buf.write("\2\2\2N\u016c\3\2\2\2P\u016e\3\2\2\2R\u017c\3\2\2\2T\u0182")
        buf.write("\3\2\2\2V\u0189\3\2\2\2X\u018b\3\2\2\2Z\u0190\3\2\2\2")
        buf.write("\\\u0195\3\2\2\2^\u019a\3\2\2\2`\u019f\3\2\2\2b\u01a2")
        buf.write("\3\2\2\2d\u01b6\3\2\2\2f\u01b8\3\2\2\2h\u01c1\3\2\2\2")
        buf.write("j\u01c3\3\2\2\2l\u01c9\3\2\2\2n\u01d0\3\2\2\2p\u01d2\3")
        buf.write("\2\2\2r\u01d7\3\2\2\2tu\5\n\6\2uv\5\6\4\2vw\5\4\3\2w\3")
        buf.write("\3\2\2\2xy\5\6\4\2yz\5\4\3\2z\177\3\2\2\2{|\5\n\6\2|}")
        buf.write("\7\2\2\3}\177\3\2\2\2~x\3\2\2\2~{\3\2\2\2\177\5\3\2\2")
        buf.write("\2\u0080\u0083\5D#\2\u0081\u0083\5P)\2\u0082\u0080\3\2")
        buf.write("\2\2\u0082\u0081\3\2\2\2\u0083\7\3\2\2\2\u0084\u008b\5")
        buf.write("p9\2\u0085\u008b\5j\66\2\u0086\u008b\5h\65\2\u0087\u008b")
        buf.write("\5Z.\2\u0088\u008b\5^\60\2\u0089\u008b\5X-\2\u008a\u0084")
        buf.write("\3\2\2\2\u008a\u0085\3\2\2\2\u008a\u0086\3\2\2\2\u008a")
        buf.write("\u0087\3\2\2\2\u008a\u0088\3\2\2\2\u008a\u0089\3\2\2\2")
        buf.write("\u008b\u008c\3\2\2\2\u008c\u008d\5\16\b\2\u008d\u0094")
        buf.write("\3\2\2\2\u008e\u0092\5b\62\2\u008f\u0092\5f\64\2\u0090")
        buf.write("\u0092\5D#\2\u0091\u008e\3\2\2\2\u0091\u008f\3\2\2\2\u0091")
        buf.write("\u0090\3\2\2\2\u0092\u0094\3\2\2\2\u0093\u008a\3\2\2\2")
        buf.write("\u0093\u0091\3\2\2\2\u0094\t\3\2\2\2\u0095\u0096\7/\2")
        buf.write("\2\u0096\u0099\5\f\7\2\u0097\u0099\3\2\2\2\u0098\u0095")
        buf.write("\3\2\2\2\u0098\u0097\3\2\2\2\u0099\13\3\2\2\2\u009a\u009b")
        buf.write("\7/\2\2\u009b\u009e\5\f\7\2\u009c\u009e\3\2\2\2\u009d")
        buf.write("\u009a\3\2\2\2\u009d\u009c\3\2\2\2\u009e\r\3\2\2\2\u009f")
        buf.write("\u00a0\7/\2\2\u00a0\u00a1\5\20\t\2\u00a1\17\3\2\2\2\u00a2")
        buf.write("\u00a3\5\16\b\2\u00a3\u00a4\5\20\t\2\u00a4\u00a7\3\2\2")
        buf.write("\2\u00a5\u00a7\3\2\2\2\u00a6\u00a2\3\2\2\2\u00a6\u00a5")
        buf.write("\3\2\2\2\u00a7\21\3\2\2\2\u00a8\u00a9\7\64\2\2\u00a9\23")
        buf.write("\3\2\2\2\u00aa\u00ab\7\64\2\2\u00ab\u00ac\7*\2\2\u00ac")
        buf.write("\u00ad\5\26\f\2\u00ad\u00ae\7+\2\2\u00ae\25\3\2\2\2\u00af")
        buf.write("\u00b0\7\4\2\2\u00b0\u00b1\5\30\r\2\u00b1\27\3\2\2\2\u00b2")
        buf.write("\u00b3\7.\2\2\u00b3\u00b4\7\4\2\2\u00b4\u00b7\5\30\r\2")
        buf.write("\u00b5\u00b7\3\2\2\2\u00b6\u00b2\3\2\2\2\u00b6\u00b5\3")
        buf.write("\2\2\2\u00b7\31\3\2\2\2\u00b8\u00b9\7\64\2\2\u00b9\u00ba")
        buf.write("\7*\2\2\u00ba\u00bb\5\34\17\2\u00bb\u00bc\7+\2\2\u00bc")
        buf.write("\33\3\2\2\2\u00bd\u00be\5(\25\2\u00be\u00bf\5\36\20\2")
        buf.write("\u00bf\35\3\2\2\2\u00c0\u00c1\7.\2\2\u00c1\u00c2\5(\25")
        buf.write("\2\u00c2\u00c3\5\36\20\2\u00c3\u00c6\3\2\2\2\u00c4\u00c6")
        buf.write("\3\2\2\2\u00c5\u00c0\3\2\2\2\u00c5\u00c4\3\2\2\2\u00c6")
        buf.write("\37\3\2\2\2\u00c7\u00c8\7*\2\2\u00c8\u00c9\5\"\22\2\u00c9")
        buf.write("\u00ca\7+\2\2\u00ca!\3\2\2\2\u00cb\u00cc\5&\24\2\u00cc")
        buf.write("\u00cd\5$\23\2\u00cd#\3\2\2\2\u00ce\u00cf\7.\2\2\u00cf")
        buf.write("\u00d0\5&\24\2\u00d0\u00d1\5$\23\2\u00d1\u00d4\3\2\2\2")
        buf.write("\u00d2\u00d4\3\2\2\2\u00d3\u00ce\3\2\2\2\u00d3\u00d2\3")
        buf.write("\2\2\2\u00d4%\3\2\2\2\u00d5\u00db\5 \21\2\u00d6\u00db")
        buf.write("\7\4\2\2\u00d7\u00db\7\5\2\2\u00d8\u00db\7\3\2\2\u00d9")
        buf.write("\u00db\5(\25\2\u00da\u00d5\3\2\2\2\u00da\u00d6\3\2\2\2")
        buf.write("\u00da\u00d7\3\2\2\2\u00da\u00d8\3\2\2\2\u00da\u00d9\3")
        buf.write("\2\2\2\u00db\'\3\2\2\2\u00dc\u00dd\5*\26\2\u00dd\u00de")
        buf.write("\7)\2\2\u00de\u00df\5*\26\2\u00df\u00e2\3\2\2\2\u00e0")
        buf.write("\u00e2\5*\26\2\u00e1\u00dc\3\2\2\2\u00e1\u00e0\3\2\2\2")
        buf.write("\u00e2)\3\2\2\2\u00e3\u00e4\5,\27\2\u00e4\u00e5\t\2\2")
        buf.write("\2\u00e5\u00e6\5,\27\2\u00e6\u00e9\3\2\2\2\u00e7\u00e9")
        buf.write("\5,\27\2\u00e8\u00e3\3\2\2\2\u00e8\u00e7\3\2\2\2\u00e9")
        buf.write("+\3\2\2\2\u00ea\u00eb\b\27\1\2\u00eb\u00ec\5.\30\2\u00ec")
        buf.write("\u00f2\3\2\2\2\u00ed\u00ee\f\4\2\2\u00ee\u00ef\t\3\2\2")
        buf.write("\u00ef\u00f1\5.\30\2\u00f0\u00ed\3\2\2\2\u00f1\u00f4\3")
        buf.write("\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3-")
        buf.write("\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f5\u00f6\b\30\1\2\u00f6")
        buf.write("\u00f7\5\60\31\2\u00f7\u00fd\3\2\2\2\u00f8\u00f9\f\4\2")
        buf.write("\2\u00f9\u00fa\t\4\2\2\u00fa\u00fc\5\60\31\2\u00fb\u00f8")
        buf.write("\3\2\2\2\u00fc\u00ff\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd")
        buf.write("\u00fe\3\2\2\2\u00fe/\3\2\2\2\u00ff\u00fd\3\2\2\2\u0100")
        buf.write("\u0101\b\31\1\2\u0101\u0102\5\62\32\2\u0102\u0108\3\2")
        buf.write("\2\2\u0103\u0104\f\4\2\2\u0104\u0105\t\5\2\2\u0105\u0107")
        buf.write("\5\62\32\2\u0106\u0103\3\2\2\2\u0107\u010a\3\2\2\2\u0108")
        buf.write("\u0106\3\2\2\2\u0108\u0109\3\2\2\2\u0109\61\3\2\2\2\u010a")
        buf.write("\u0108\3\2\2\2\u010b\u010c\7\36\2\2\u010c\u010f\5\62\32")
        buf.write("\2\u010d\u010f\5\64\33\2\u010e\u010b\3\2\2\2\u010e\u010d")
        buf.write("\3\2\2\2\u010f\63\3\2\2\2\u0110\u0111\7\32\2\2\u0111\u0114")
        buf.write("\5\64\33\2\u0112\u0114\5\66\34\2\u0113\u0110\3\2\2\2\u0113")
        buf.write("\u0112\3\2\2\2\u0114\65\3\2\2\2\u0115\u0118\7\64\2\2\u0116")
        buf.write("\u0118\5r:\2\u0117\u0115\3\2\2\2\u0117\u0116\3\2\2\2\u0118")
        buf.write("\u0119\3\2\2\2\u0119\u011a\7*\2\2\u011a\u011b\58\35\2")
        buf.write("\u011b\u011c\7+\2\2\u011c\u011f\3\2\2\2\u011d\u011f\5")
        buf.write(":\36\2\u011e\u0117\3\2\2\2\u011e\u011d\3\2\2\2\u011f\67")
        buf.write("\3\2\2\2\u0120\u0121\5(\25\2\u0121\u0122\7.\2\2\u0122")
        buf.write("\u0123\58\35\2\u0123\u0126\3\2\2\2\u0124\u0126\5(\25\2")
        buf.write("\u0125\u0120\3\2\2\2\u0125\u0124\3\2\2\2\u01269\3\2\2")
        buf.write("\2\u0127\u0132\7\5\2\2\u0128\u0132\7\4\2\2\u0129\u0132")
        buf.write("\7\3\2\2\u012a\u0132\7\64\2\2\u012b\u0132\5 \21\2\u012c")
        buf.write("\u0132\5r:\2\u012d\u012e\7,\2\2\u012e\u012f\5(\25\2\u012f")
        buf.write("\u0130\7-\2\2\u0130\u0132\3\2\2\2\u0131\u0127\3\2\2\2")
        buf.write("\u0131\u0128\3\2\2\2\u0131\u0129\3\2\2\2\u0131\u012a\3")
        buf.write("\2\2\2\u0131\u012b\3\2\2\2\u0131\u012c\3\2\2\2\u0131\u012d")
        buf.write("\3\2\2\2\u0132;\3\2\2\2\u0133\u0136\7\64\2\2\u0134\u0136")
        buf.write("\5r:\2\u0135\u0133\3\2\2\2\u0135\u0134\3\2\2\2\u0136\u0137")
        buf.write("\3\2\2\2\u0137\u0138\7*\2\2\u0138\u0139\58\35\2\u0139")
        buf.write("\u013a\7+\2\2\u013a=\3\2\2\2\u013b\u013c\t\6\2\2\u013c")
        buf.write("?\3\2\2\2\u013d\u013e\t\7\2\2\u013eA\3\2\2\2\u013f\u0140")
        buf.write("\7\f\2\2\u0140C\3\2\2\2\u0141\u0142\5> \2\u0142\u0145")
        buf.write("\5\22\n\2\u0143\u0144\7!\2\2\u0144\u0146\5(\25\2\u0145")
        buf.write("\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0153\3\2\2\2")
        buf.write("\u0147\u0148\5@!\2\u0148\u014b\5\24\13\2\u0149\u014a\7")
        buf.write("!\2\2\u014a\u014c\5(\25\2\u014b\u0149\3\2\2\2\u014b\u014c")
        buf.write("\3\2\2\2\u014c\u0153\3\2\2\2\u014d\u014e\5B\"\2\u014e")
        buf.write("\u014f\5\22\n\2\u014f\u0150\7!\2\2\u0150\u0151\5(\25\2")
        buf.write("\u0151\u0153\3\2\2\2\u0152\u0141\3\2\2\2\u0152\u0147\3")
        buf.write("\2\2\2\u0152\u014d\3\2\2\2\u0153\u0154\3\2\2\2\u0154\u0155")
        buf.write("\5\16\b\2\u0155E\3\2\2\2\u0156\u0157\t\7\2\2\u0157G\3")
        buf.write("\2\2\2\u0158\u0159\7,\2\2\u0159\u015a\5L\'\2\u015a\u015b")
        buf.write("\7-\2\2\u015bI\3\2\2\2\u015c\u015f\5F$\2\u015d\u0160\5")
        buf.write("\22\n\2\u015e\u0160\5\24\13\2\u015f\u015d\3\2\2\2\u015f")
        buf.write("\u015e\3\2\2\2\u0160K\3\2\2\2\u0161\u0162\5J&\2\u0162")
        buf.write("\u0163\5N(\2\u0163\u0166\3\2\2\2\u0164\u0166\3\2\2\2\u0165")
        buf.write("\u0161\3\2\2\2\u0165\u0164\3\2\2\2\u0166M\3\2\2\2\u0167")
        buf.write("\u0168\7.\2\2\u0168\u0169\5J&\2\u0169\u016a\5N(\2\u016a")
        buf.write("\u016d\3\2\2\2\u016b\u016d\3\2\2\2\u016c\u0167\3\2\2\2")
        buf.write("\u016c\u016b\3\2\2\2\u016dO\3\2\2\2\u016e\u016f\7\16\2")
        buf.write("\2\u016f\u0170\7\64\2\2\u0170\u0176\5H%\2\u0171\u0174")
        buf.write("\5\n\6\2\u0172\u0175\5Z.\2\u0173\u0175\5X-\2\u0174\u0172")
        buf.write("\3\2\2\2\u0174\u0173\3\2\2\2\u0175\u0177\3\2\2\2\u0176")
        buf.write("\u0171\3\2\2\2\u0176\u0177\3\2\2\2\u0177\u0178\3\2\2\2")
        buf.write("\u0178\u0179\5\16\b\2\u0179Q\3\2\2\2\u017a\u017d\5D#\2")
        buf.write("\u017b\u017d\5\b\5\2\u017c\u017a\3\2\2\2\u017c\u017b\3")
        buf.write("\2\2\2\u017dS\3\2\2\2\u017e\u017f\5R*\2\u017f\u0180\5")
        buf.write("V,\2\u0180\u0183\3\2\2\2\u0181\u0183\3\2\2\2\u0182\u017e")
        buf.write("\3\2\2\2\u0182\u0181\3\2\2\2\u0183U\3\2\2\2\u0184\u0185")
        buf.write("\5\n\6\2\u0185\u0186\5R*\2\u0186\u0187\5V,\2\u0187\u018a")
        buf.write("\3\2\2\2\u0188\u018a\3\2\2\2\u0189\u0184\3\2\2\2\u0189")
        buf.write("\u0188\3\2\2\2\u018aW\3\2\2\2\u018b\u018c\7\27\2\2\u018c")
        buf.write("\u018d\5\16\b\2\u018d\u018e\5T+\2\u018e\u018f\7\30\2\2")
        buf.write("\u018fY\3\2\2\2\u0190\u0191\7\13\2\2\u0191\u0192\5\\/")
        buf.write("\2\u0192[\3\2\2\2\u0193\u0196\5(\25\2\u0194\u0196\3\2")
        buf.write("\2\2\u0195\u0193\3\2\2\2\u0195\u0194\3\2\2\2\u0196]\3")
        buf.write("\2\2\2\u0197\u019b\5\22\n\2\u0198\u019b\5\32\16\2\u0199")
        buf.write("\u019b\5<\37\2\u019a\u0197\3\2\2\2\u019a\u0198\3\2\2\2")
        buf.write("\u019a\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019d\7")
        buf.write("!\2\2\u019d\u019e\5(\25\2\u019e_\3\2\2\2\u019f\u01a0\5")
        buf.write("\n\6\2\u01a0\u01a1\5\b\5\2\u01a1a\3\2\2\2\u01a2\u01a3")
        buf.write("\7\24\2\2\u01a3\u01a4\7,\2\2\u01a4\u01a5\5(\25\2\u01a5")
        buf.write("\u01a6\7-\2\2\u01a6\u01a7\5`\61\2\u01a7\u01a8\5d\63\2")
        buf.write("\u01a8c\3\2\2\2\u01a9\u01aa\5\n\6\2\u01aa\u01ab\7\26\2")
        buf.write("\2\u01ab\u01ac\7,\2\2\u01ac\u01ad\5(\25\2\u01ad\u01ae")
        buf.write("\7-\2\2\u01ae\u01af\5`\61\2\u01af\u01b0\5d\63\2\u01b0")
        buf.write("\u01b7\3\2\2\2\u01b1\u01b2\5\n\6\2\u01b2\u01b3\7\25\2")
        buf.write("\2\u01b3\u01b4\5`\61\2\u01b4\u01b7\3\2\2\2\u01b5\u01b7")
        buf.write("\3\2\2\2\u01b6\u01a9\3\2\2\2\u01b6\u01b1\3\2\2\2\u01b6")
        buf.write("\u01b5\3\2\2\2\u01b7e\3\2\2\2\u01b8\u01b9\7\17\2\2\u01b9")
        buf.write("\u01ba\7\64\2\2\u01ba\u01bb\7\20\2\2\u01bb\u01bc\5(\25")
        buf.write("\2\u01bc\u01bd\7\21\2\2\u01bd\u01be\5(\25\2\u01be\u01bf")
        buf.write("\5\n\6\2\u01bf\u01c0\5\b\5\2\u01c0g\3\2\2\2\u01c1\u01c2")
        buf.write("\7\22\2\2\u01c2i\3\2\2\2\u01c3\u01c4\7\23\2\2\u01c4k\3")
        buf.write("\2\2\2\u01c5\u01c6\5(\25\2\u01c6\u01c7\5n8\2\u01c7\u01ca")
        buf.write("\3\2\2\2\u01c8\u01ca\3\2\2\2\u01c9\u01c5\3\2\2\2\u01c9")
        buf.write("\u01c8\3\2\2\2\u01cam\3\2\2\2\u01cb\u01cc\7.\2\2\u01cc")
        buf.write("\u01cd\5(\25\2\u01cd\u01ce\5n8\2\u01ce\u01d1\3\2\2\2\u01cf")
        buf.write("\u01d1\3\2\2\2\u01d0\u01cb\3\2\2\2\u01d0\u01cf\3\2\2\2")
        buf.write("\u01d1o\3\2\2\2\u01d2\u01d3\7\64\2\2\u01d3\u01d4\7,\2")
        buf.write("\2\u01d4\u01d5\5l\67\2\u01d5\u01d6\7-\2\2\u01d6q\3\2\2")
        buf.write("\2\u01d7\u01d8\7\64\2\2\u01d8\u01d9\7,\2\2\u01d9\u01da")
        buf.write("\5l\67\2\u01da\u01db\7-\2\2\u01dbs\3\2\2\2*~\u0082\u008a")
        buf.write("\u0091\u0093\u0098\u009d\u00a6\u00b6\u00c5\u00d3\u00da")
        buf.write("\u00e1\u00e8\u00f2\u00fd\u0108\u010e\u0113\u0117\u011e")
        buf.write("\u0125\u0131\u0135\u0145\u014b\u0152\u015f\u0165\u016c")
        buf.write("\u0174\u0176\u017c\u0182\u0189\u0195\u019a\u01b6\u01c9")
        buf.write("\u01d0")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'true'", "'false'", "'number'", "'bool'", "'string'", 
                     "'return'", "'var'", "'dynamic'", "'func'", "'for'", 
                     "'until'", "'by'", "'break'", "'continue'", "'if'", 
                     "'else'", "'elif'", "'begin'", "'end'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'not'", "'and'", "'or'", "'<-'", 
                     "'='", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'...'", "'['", "']'", "'('", "')'", "','", "<INVALID>", 
                     "<INVALID>", "'\r'", "'\r\r\n'" ]

    symbolicNames = [ "<INVALID>", "BOOL_LIT", "NUM_LIT", "STR_LIT", "TRUE", 
                      "FALSE", "NUM", "BOOL", "STR", "RETURN", "VAR", "DYNAMIC", 
                      "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
                      "IF", "ELSE", "ELIF", "BEGIN", "END", "PLUS", "MINUS", 
                      "MULTIPLY", "DIVIDE", "MODULO", "NOT", "AND", "OR", 
                      "ASSIGN", "EQUAL", "DEQUAL", "NOT_EQUAL", "LESS", 
                      "LESS_EQUAL", "GREATER", "GREATER_EQUAL", "CONCAT", 
                      "LSB", "RSB", "LRB", "RRB", "COMMA", "NEWLINE", "NL1", 
                      "NL2", "NL3", "COMMENT_LINE", "IDENTIFIER", "WS", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_program_tail = 1
    RULE_decl = 2
    RULE_stmt = 3
    RULE_nullable_newline_list = 4
    RULE_nullable_newline_list_tail = 5
    RULE_newline_list = 6
    RULE_newline_list_tail = 7
    RULE_id_single = 8
    RULE_decl_array = 9
    RULE_decl_array_list = 10
    RULE_decl_array_list_tail = 11
    RULE_ass_array = 12
    RULE_ass_array_list = 13
    RULE_ass_array_list_tail = 14
    RULE_arr = 15
    RULE_array_list = 16
    RULE_array_list_tail = 17
    RULE_arr_content = 18
    RULE_expr = 19
    RULE_expr1 = 20
    RULE_expr2 = 21
    RULE_expr3 = 22
    RULE_expr4 = 23
    RULE_expr5 = 24
    RULE_expr6 = 25
    RULE_expr7 = 26
    RULE_index_op = 27
    RULE_expr8 = 28
    RULE_index_expr = 29
    RULE_decl_typ_no_var = 30
    RULE_decl_typ_arr = 31
    RULE_var = 32
    RULE_var_decl = 33
    RULE_param_decl_typ = 34
    RULE_param_decl = 35
    RULE_param_decl_content = 36
    RULE_param_decl_list = 37
    RULE_param_decl_list_tail = 38
    RULE_func_decl = 39
    RULE_body_content = 40
    RULE_body_list = 41
    RULE_body_list_tail = 42
    RULE_block_stmt = 43
    RULE_ret_stmt = 44
    RULE_ret_stmt_tail = 45
    RULE_ass_stmt = 46
    RULE_if_stmt_content = 47
    RULE_if_stmt = 48
    RULE_if_stmt_tail = 49
    RULE_for_stmt = 50
    RULE_break_stmt = 51
    RULE_cont_stmt = 52
    RULE_arg_list = 53
    RULE_arg_list_tail = 54
    RULE_func_call_stmt = 55
    RULE_func_call_expr = 56

    ruleNames =  [ "program", "program_tail", "decl", "stmt", "nullable_newline_list", 
                   "nullable_newline_list_tail", "newline_list", "newline_list_tail", 
                   "id_single", "decl_array", "decl_array_list", "decl_array_list_tail", 
                   "ass_array", "ass_array_list", "ass_array_list_tail", 
                   "arr", "array_list", "array_list_tail", "arr_content", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "index_op", "expr8", "index_expr", 
                   "decl_typ_no_var", "decl_typ_arr", "var", "var_decl", 
                   "param_decl_typ", "param_decl", "param_decl_content", 
                   "param_decl_list", "param_decl_list_tail", "func_decl", 
                   "body_content", "body_list", "body_list_tail", "block_stmt", 
                   "ret_stmt", "ret_stmt_tail", "ass_stmt", "if_stmt_content", 
                   "if_stmt", "if_stmt_tail", "for_stmt", "break_stmt", 
                   "cont_stmt", "arg_list", "arg_list_tail", "func_call_stmt", 
                   "func_call_expr" ]

    EOF = Token.EOF
    BOOL_LIT=1
    NUM_LIT=2
    STR_LIT=3
    TRUE=4
    FALSE=5
    NUM=6
    BOOL=7
    STR=8
    RETURN=9
    VAR=10
    DYNAMIC=11
    FUNC=12
    FOR=13
    UNTIL=14
    BY=15
    BREAK=16
    CONTINUE=17
    IF=18
    ELSE=19
    ELIF=20
    BEGIN=21
    END=22
    PLUS=23
    MINUS=24
    MULTIPLY=25
    DIVIDE=26
    MODULO=27
    NOT=28
    AND=29
    OR=30
    ASSIGN=31
    EQUAL=32
    DEQUAL=33
    NOT_EQUAL=34
    LESS=35
    LESS_EQUAL=36
    GREATER=37
    GREATER_EQUAL=38
    CONCAT=39
    LSB=40
    RSB=41
    LRB=42
    RRB=43
    COMMA=44
    NEWLINE=45
    NL1=46
    NL2=47
    NL3=48
    COMMENT_LINE=49
    IDENTIFIER=50
    WS=51
    ILLEGAL_ESCAPE=52
    UNCLOSE_STRING=53
    ERROR_CHAR=54

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

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def program_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Program_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.nullable_newline_list()
            self.state = 115
            self.decl()
            self.state = 116
            self.program_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Program_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def program_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Program_tailContext,0)


        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram_tail" ):
                return visitor.visitProgram_tail(self)
            else:
                return visitor.visitChildren(self)




    def program_tail(self):

        localctx = ZCodeParser.Program_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program_tail)
        try:
            self.state = 124
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM, ZCodeParser.BOOL, ZCodeParser.STR, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.decl()
                self.state = 119
                self.program_tail()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.nullable_newline_list()
                self.state = 122
                self.match(ZCodeParser.EOF)
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


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Var_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Func_declContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM, ZCodeParser.BOOL, ZCodeParser.STR, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.var_decl()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.func_decl()
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

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def func_call_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Func_call_stmtContext,0)


        def cont_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Cont_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Break_stmtContext,0)


        def ret_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Ret_stmtContext,0)


        def ass_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Ass_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.For_stmtContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Var_declContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stmt)
        try:
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 130
                    self.func_call_stmt()
                    pass

                elif la_ == 2:
                    self.state = 131
                    self.cont_stmt()
                    pass

                elif la_ == 3:
                    self.state = 132
                    self.break_stmt()
                    pass

                elif la_ == 4:
                    self.state = 133
                    self.ret_stmt()
                    pass

                elif la_ == 5:
                    self.state = 134
                    self.ass_stmt()
                    pass

                elif la_ == 6:
                    self.state = 135
                    self.block_stmt()
                    pass


                self.state = 138
                self.newline_list()
                pass
            elif token in [ZCodeParser.NUM, ZCodeParser.BOOL, ZCodeParser.STR, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.IF]:
                    self.state = 140
                    self.if_stmt()
                    pass
                elif token in [ZCodeParser.FOR]:
                    self.state = 141
                    self.for_stmt()
                    pass
                elif token in [ZCodeParser.NUM, ZCodeParser.BOOL, ZCodeParser.STR, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                    self.state = 142
                    self.var_decl()
                    pass
                else:
                    raise NoViableAltException(self)

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


    class Nullable_newline_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def nullable_newline_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nullable_newline_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullable_newline_list" ):
                return visitor.visitNullable_newline_list(self)
            else:
                return visitor.visitChildren(self)




    def nullable_newline_list(self):

        localctx = ZCodeParser.Nullable_newline_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_nullable_newline_list)
        try:
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.match(ZCodeParser.NEWLINE)
                self.state = 148
                self.nullable_newline_list_tail()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.NUM, ZCodeParser.BOOL, ZCodeParser.STR, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.ELSE, ZCodeParser.ELIF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
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


    class Nullable_newline_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def nullable_newline_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nullable_newline_list_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullable_newline_list_tail" ):
                return visitor.visitNullable_newline_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def nullable_newline_list_tail(self):

        localctx = ZCodeParser.Nullable_newline_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_nullable_newline_list_tail)
        try:
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.match(ZCodeParser.NEWLINE)
                self.state = 153
                self.nullable_newline_list_tail()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.NUM, ZCodeParser.BOOL, ZCodeParser.STR, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.ELSE, ZCodeParser.ELIF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
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


    class Newline_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def newline_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newline_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewline_list" ):
                return visitor.visitNewline_list(self)
            else:
                return visitor.visitChildren(self)




    def newline_list(self):

        localctx = ZCodeParser.Newline_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_newline_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(ZCodeParser.NEWLINE)
            self.state = 158
            self.newline_list_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Newline_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def newline_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newline_list_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewline_list_tail" ):
                return visitor.visitNewline_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def newline_list_tail(self):

        localctx = ZCodeParser.Newline_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_newline_list_tail)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.newline_list()
                self.state = 161
                self.newline_list_tail()
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


    class Id_singleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_id_single

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_single" ):
                return visitor.visitId_single(self)
            else:
                return visitor.visitChildren(self)




    def id_single(self):

        localctx = ZCodeParser.Id_singleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_id_single)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(ZCodeParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def decl_array_list(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_array_listContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_decl_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_array" ):
                return visitor.visitDecl_array(self)
            else:
                return visitor.visitChildren(self)




    def decl_array(self):

        localctx = ZCodeParser.Decl_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_decl_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 169
            self.match(ZCodeParser.LSB)
            self.state = 170
            self.decl_array_list()
            self.state = 171
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_array_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_LIT(self):
            return self.getToken(ZCodeParser.NUM_LIT, 0)

        def decl_array_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_array_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl_array_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_array_list" ):
                return visitor.visitDecl_array_list(self)
            else:
                return visitor.visitChildren(self)




    def decl_array_list(self):

        localctx = ZCodeParser.Decl_array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_decl_array_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(ZCodeParser.NUM_LIT)
            self.state = 174
            self.decl_array_list_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_array_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def NUM_LIT(self):
            return self.getToken(ZCodeParser.NUM_LIT, 0)

        def decl_array_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_array_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl_array_list_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_array_list_tail" ):
                return visitor.visitDecl_array_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def decl_array_list_tail(self):

        localctx = ZCodeParser.Decl_array_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_decl_array_list_tail)
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.match(ZCodeParser.COMMA)
                self.state = 177
                self.match(ZCodeParser.NUM_LIT)
                self.state = 178
                self.decl_array_list_tail()
                pass
            elif token in [ZCodeParser.RSB]:
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


    class Ass_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def ass_array_list(self):
            return self.getTypedRuleContext(ZCodeParser.Ass_array_listContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ass_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAss_array" ):
                return visitor.visitAss_array(self)
            else:
                return visitor.visitChildren(self)




    def ass_array(self):

        localctx = ZCodeParser.Ass_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ass_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 183
            self.match(ZCodeParser.LSB)
            self.state = 184
            self.ass_array_list()
            self.state = 185
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ass_array_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def ass_array_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Ass_array_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ass_array_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAss_array_list" ):
                return visitor.visitAss_array_list(self)
            else:
                return visitor.visitChildren(self)




    def ass_array_list(self):

        localctx = ZCodeParser.Ass_array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_ass_array_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.expr()
            self.state = 188
            self.ass_array_list_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ass_array_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def ass_array_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Ass_array_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ass_array_list_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAss_array_list_tail" ):
                return visitor.visitAss_array_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def ass_array_list_tail(self):

        localctx = ZCodeParser.Ass_array_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ass_array_list_tail)
        try:
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.match(ZCodeParser.COMMA)
                self.state = 191
                self.expr()
                self.state = 192
                self.ass_array_list_tail()
                pass
            elif token in [ZCodeParser.RSB]:
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


    class ArrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def array_list(self):
            return self.getTypedRuleContext(ZCodeParser.Array_listContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr" ):
                return visitor.visitArr(self)
            else:
                return visitor.visitChildren(self)




    def arr(self):

        localctx = ZCodeParser.ArrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(ZCodeParser.LSB)
            self.state = 198
            self.array_list()
            self.state = 199
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arr_content(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_contentContext,0)


        def array_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Array_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list" ):
                return visitor.visitArray_list(self)
            else:
                return visitor.visitChildren(self)




    def array_list(self):

        localctx = ZCodeParser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_array_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.arr_content()
            self.state = 202
            self.array_list_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def arr_content(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_contentContext,0)


        def array_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Array_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_list_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list_tail" ):
                return visitor.visitArray_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def array_list_tail(self):

        localctx = ZCodeParser.Array_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_array_list_tail)
        try:
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.match(ZCodeParser.COMMA)
                self.state = 205
                self.arr_content()
                self.state = 206
                self.array_list_tail()
                pass
            elif token in [ZCodeParser.RSB]:
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


    class Arr_contentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arr(self):
            return self.getTypedRuleContext(ZCodeParser.ArrContext,0)


        def NUM_LIT(self):
            return self.getToken(ZCodeParser.NUM_LIT, 0)

        def STR_LIT(self):
            return self.getToken(ZCodeParser.STR_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(ZCodeParser.BOOL_LIT, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arr_content

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_content" ):
                return visitor.visitArr_content(self)
            else:
                return visitor.visitChildren(self)




    def arr_content(self):

        localctx = ZCodeParser.Arr_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arr_content)
        try:
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.arr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.match(ZCodeParser.NUM_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 213
                self.match(ZCodeParser.STR_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 214
                self.match(ZCodeParser.BOOL_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 215
                self.expr()
                pass


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
                return self.getTypedRuleContexts(ZCodeParser.Expr1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr1Context,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr)
        try:
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.expr1()
                self.state = 219
                self.match(ZCodeParser.CONCAT)
                self.state = 220
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
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
                return self.getTypedRuleContexts(ZCodeParser.Expr2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr2Context,i)


        def EQUAL(self):
            return self.getToken(ZCodeParser.EQUAL, 0)

        def DEQUAL(self):
            return self.getToken(ZCodeParser.DEQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(ZCodeParser.NOT_EQUAL, 0)

        def LESS(self):
            return self.getToken(ZCodeParser.LESS, 0)

        def GREATER(self):
            return self.getToken(ZCodeParser.GREATER, 0)

        def LESS_EQUAL(self):
            return self.getToken(ZCodeParser.LESS_EQUAL, 0)

        def GREATER_EQUAL(self):
            return self.getToken(ZCodeParser.GREATER_EQUAL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = ZCodeParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.expr2(0)
                self.state = 226
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL) | (1 << ZCodeParser.DEQUAL) | (1 << ZCodeParser.NOT_EQUAL) | (1 << ZCodeParser.LESS) | (1 << ZCodeParser.LESS_EQUAL) | (1 << ZCodeParser.GREATER) | (1 << ZCodeParser.GREATER_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 227
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
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
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(ZCodeParser.Expr2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 240
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 235
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 236
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 237
                    self.expr3(0) 
                self.state = 242
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def PLUS(self):
            return self.getToken(ZCodeParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 251
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 246
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 247
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 248
                    self.expr4(0) 
                self.state = 253
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def MULTIPLY(self):
            return self.getToken(ZCodeParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(ZCodeParser.DIVIDE, 0)

        def MODULO(self):
            return self.getToken(ZCodeParser.MODULO, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 262
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 257
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 258
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MULTIPLY) | (1 << ZCodeParser.DIVIDE) | (1 << ZCodeParser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 259
                    self.expr5() 
                self.state = 264
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expr5)
        try:
            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.match(ZCodeParser.NOT)
                self.state = 266
                self.expr5()
                pass
            elif token in [ZCodeParser.BOOL_LIT, ZCodeParser.NUM_LIT, ZCodeParser.STR_LIT, ZCodeParser.MINUS, ZCodeParser.LSB, ZCodeParser.LRB, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.expr6()
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


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = ZCodeParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expr6)
        try:
            self.state = 273
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.match(ZCodeParser.MINUS)
                self.state = 271
                self.expr6()
                pass
            elif token in [ZCodeParser.BOOL_LIT, ZCodeParser.NUM_LIT, ZCodeParser.STR_LIT, ZCodeParser.LSB, ZCodeParser.LRB, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
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

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def index_op(self):
            return self.getTypedRuleContext(ZCodeParser.Index_opContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def func_call_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Func_call_exprContext,0)


        def expr8(self):
            return self.getTypedRuleContext(ZCodeParser.Expr8Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = ZCodeParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expr7)
        try:
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 275
                    self.match(ZCodeParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 276
                    self.func_call_expr()
                    pass


                self.state = 279
                self.match(ZCodeParser.LSB)
                self.state = 280
                self.index_op()
                self.state = 281
                self.match(ZCodeParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.expr8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def index_op(self):
            return self.getTypedRuleContext(ZCodeParser.Index_opContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_op" ):
                return visitor.visitIndex_op(self)
            else:
                return visitor.visitChildren(self)




    def index_op(self):

        localctx = ZCodeParser.Index_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_index_op)
        try:
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.expr()
                self.state = 287
                self.match(ZCodeParser.COMMA)
                self.state = 288
                self.index_op()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.expr()
                pass


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

        def STR_LIT(self):
            return self.getToken(ZCodeParser.STR_LIT, 0)

        def NUM_LIT(self):
            return self.getToken(ZCodeParser.NUM_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(ZCodeParser.BOOL_LIT, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def arr(self):
            return self.getTypedRuleContext(ZCodeParser.ArrContext,0)


        def func_call_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Func_call_exprContext,0)


        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = ZCodeParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expr8)
        try:
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.match(ZCodeParser.STR_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.match(ZCodeParser.NUM_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 295
                self.match(ZCodeParser.BOOL_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 296
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 297
                self.arr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 298
                self.func_call_expr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 299
                self.match(ZCodeParser.LRB)
                self.state = 300
                self.expr()
                self.state = 301
                self.match(ZCodeParser.RRB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def index_op(self):
            return self.getTypedRuleContext(ZCodeParser.Index_opContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def func_call_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Func_call_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expr" ):
                return visitor.visitIndex_expr(self)
            else:
                return visitor.visitChildren(self)




    def index_expr(self):

        localctx = ZCodeParser.Index_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_index_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 305
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 306
                self.func_call_expr()
                pass


            self.state = 309
            self.match(ZCodeParser.LSB)
            self.state = 310
            self.index_op()
            self.state = 311
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_typ_no_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def NUM(self):
            return self.getToken(ZCodeParser.NUM, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STR(self):
            return self.getToken(ZCodeParser.STR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_decl_typ_no_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_typ_no_var" ):
                return visitor.visitDecl_typ_no_var(self)
            else:
                return visitor.visitChildren(self)




    def decl_typ_no_var(self):

        localctx = ZCodeParser.Decl_typ_no_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_decl_typ_no_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUM) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STR) | (1 << ZCodeParser.DYNAMIC))) != 0)):
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


    class Decl_typ_arrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(ZCodeParser.NUM, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STR(self):
            return self.getToken(ZCodeParser.STR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_decl_typ_arr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_typ_arr" ):
                return visitor.visitDecl_typ_arr(self)
            else:
                return visitor.visitChildren(self)




    def decl_typ_arr(self):

        localctx = ZCodeParser.Decl_typ_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_decl_typ_arr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUM) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STR))) != 0)):
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


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = ZCodeParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(ZCodeParser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def decl_typ_no_var(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_typ_no_varContext,0)


        def id_single(self):
            return self.getTypedRuleContext(ZCodeParser.Id_singleContext,0)


        def decl_typ_arr(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_typ_arrContext,0)


        def decl_array(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_arrayContext,0)


        def var(self):
            return self.getTypedRuleContext(ZCodeParser.VarContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = ZCodeParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 319
                self.decl_typ_no_var()
                self.state = 320
                self.id_single()
                self.state = 323
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.ASSIGN:
                    self.state = 321
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 322
                    self.expr()


                pass

            elif la_ == 2:
                self.state = 325
                self.decl_typ_arr()
                self.state = 326
                self.decl_array()
                self.state = 329
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.ASSIGN:
                    self.state = 327
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 328
                    self.expr()


                pass

            elif la_ == 3:
                self.state = 331
                self.var()
                self.state = 332
                self.id_single()
                self.state = 333
                self.match(ZCodeParser.ASSIGN)
                self.state = 334
                self.expr()
                pass


            self.state = 338
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_decl_typContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(ZCodeParser.NUM, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STR(self):
            return self.getToken(ZCodeParser.STR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_param_decl_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_decl_typ" ):
                return visitor.visitParam_decl_typ(self)
            else:
                return visitor.visitChildren(self)




    def param_decl_typ(self):

        localctx = ZCodeParser.Param_decl_typContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_param_decl_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUM) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STR))) != 0)):
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


    class Param_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def param_decl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Param_decl_listContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_param_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_decl" ):
                return visitor.visitParam_decl(self)
            else:
                return visitor.visitChildren(self)




    def param_decl(self):

        localctx = ZCodeParser.Param_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_param_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(ZCodeParser.LRB)
            self.state = 343
            self.param_decl_list()
            self.state = 344
            self.match(ZCodeParser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_decl_contentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_decl_typ(self):
            return self.getTypedRuleContext(ZCodeParser.Param_decl_typContext,0)


        def id_single(self):
            return self.getTypedRuleContext(ZCodeParser.Id_singleContext,0)


        def decl_array(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_arrayContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_decl_content

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_decl_content" ):
                return visitor.visitParam_decl_content(self)
            else:
                return visitor.visitChildren(self)




    def param_decl_content(self):

        localctx = ZCodeParser.Param_decl_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_param_decl_content)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.param_decl_typ()
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 347
                self.id_single()
                pass

            elif la_ == 2:
                self.state = 348
                self.decl_array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_decl_content(self):
            return self.getTypedRuleContext(ZCodeParser.Param_decl_contentContext,0)


        def param_decl_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Param_decl_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_decl_list" ):
                return visitor.visitParam_decl_list(self)
            else:
                return visitor.visitChildren(self)




    def param_decl_list(self):

        localctx = ZCodeParser.Param_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_param_decl_list)
        try:
            self.state = 355
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM, ZCodeParser.BOOL, ZCodeParser.STR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.param_decl_content()
                self.state = 352
                self.param_decl_list_tail()
                pass
            elif token in [ZCodeParser.RRB]:
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


    class Param_decl_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def param_decl_content(self):
            return self.getTypedRuleContext(ZCodeParser.Param_decl_contentContext,0)


        def param_decl_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Param_decl_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_decl_list_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_decl_list_tail" ):
                return visitor.visitParam_decl_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def param_decl_list_tail(self):

        localctx = ZCodeParser.Param_decl_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_param_decl_list_tail)
        try:
            self.state = 362
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.match(ZCodeParser.COMMA)
                self.state = 358
                self.param_decl_content()
                self.state = 359
                self.param_decl_list_tail()
                pass
            elif token in [ZCodeParser.RRB]:
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


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def param_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Param_declContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def ret_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Ret_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = ZCodeParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(ZCodeParser.FUNC)
            self.state = 365
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 366
            self.param_decl()
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 367
                self.nullable_newline_list()
                self.state = 370
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.RETURN]:
                    self.state = 368
                    self.ret_stmt()
                    pass
                elif token in [ZCodeParser.BEGIN]:
                    self.state = 369
                    self.block_stmt()
                    pass
                else:
                    raise NoViableAltException(self)



            self.state = 374
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_contentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Var_declContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_body_content

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_content" ):
                return visitor.visitBody_content(self)
            else:
                return visitor.visitChildren(self)




    def body_content(self):

        localctx = ZCodeParser.Body_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_body_content)
        try:
            self.state = 378
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body_content(self):
            return self.getTypedRuleContext(ZCodeParser.Body_contentContext,0)


        def body_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Body_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_body_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_list" ):
                return visitor.visitBody_list(self)
            else:
                return visitor.visitChildren(self)




    def body_list(self):

        localctx = ZCodeParser.Body_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_body_list)
        try:
            self.state = 384
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM, ZCodeParser.BOOL, ZCodeParser.STR, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.body_content()
                self.state = 381
                self.body_list_tail()
                pass
            elif token in [ZCodeParser.END]:
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


    class Body_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def body_content(self):
            return self.getTypedRuleContext(ZCodeParser.Body_contentContext,0)


        def body_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Body_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_body_list_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_list_tail" ):
                return visitor.visitBody_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def body_list_tail(self):

        localctx = ZCodeParser.Body_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_body_list_tail)
        try:
            self.state = 391
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM, ZCodeParser.BOOL, ZCodeParser.STR, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.NEWLINE, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 386
                self.nullable_newline_list()
                self.state = 387
                self.body_content()
                self.state = 388
                self.body_list_tail()
                pass
            elif token in [ZCodeParser.END]:
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


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def body_list(self):
            return self.getTypedRuleContext(ZCodeParser.Body_listContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = ZCodeParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(ZCodeParser.BEGIN)
            self.state = 394
            self.newline_list()
            self.state = 395
            self.body_list()
            self.state = 396
            self.match(ZCodeParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ret_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def ret_stmt_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Ret_stmt_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ret_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRet_stmt" ):
                return visitor.visitRet_stmt(self)
            else:
                return visitor.visitChildren(self)




    def ret_stmt(self):

        localctx = ZCodeParser.Ret_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_ret_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.match(ZCodeParser.RETURN)
            self.state = 399
            self.ret_stmt_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ret_stmt_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ret_stmt_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRet_stmt_tail" ):
                return visitor.visitRet_stmt_tail(self)
            else:
                return visitor.visitChildren(self)




    def ret_stmt_tail(self):

        localctx = ZCodeParser.Ret_stmt_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_ret_stmt_tail)
        try:
            self.state = 403
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOL_LIT, ZCodeParser.NUM_LIT, ZCodeParser.STR_LIT, ZCodeParser.MINUS, ZCodeParser.NOT, ZCodeParser.LSB, ZCodeParser.LRB, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.expr()
                pass
            elif token in [ZCodeParser.NEWLINE]:
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


    class Ass_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def id_single(self):
            return self.getTypedRuleContext(ZCodeParser.Id_singleContext,0)


        def ass_array(self):
            return self.getTypedRuleContext(ZCodeParser.Ass_arrayContext,0)


        def index_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Index_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ass_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAss_stmt" ):
                return visitor.visitAss_stmt(self)
            else:
                return visitor.visitChildren(self)




    def ass_stmt(self):

        localctx = ZCodeParser.Ass_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_ass_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 405
                self.id_single()
                pass

            elif la_ == 2:
                self.state = 406
                self.ass_array()
                pass

            elif la_ == 3:
                self.state = 407
                self.index_expr()
                pass


            self.state = 410
            self.match(ZCodeParser.ASSIGN)
            self.state = 411
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmt_contentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_stmt_content

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt_content" ):
                return visitor.visitIf_stmt_content(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt_content(self):

        localctx = ZCodeParser.If_stmt_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_if_stmt_content)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.nullable_newline_list()
            self.state = 414
            self.stmt()
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
            return self.getToken(ZCodeParser.IF, 0)

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def if_stmt_content(self):
            return self.getTypedRuleContext(ZCodeParser.If_stmt_contentContext,0)


        def if_stmt_tail(self):
            return self.getTypedRuleContext(ZCodeParser.If_stmt_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = ZCodeParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(ZCodeParser.IF)
            self.state = 417
            self.match(ZCodeParser.LRB)
            self.state = 418
            self.expr()
            self.state = 419
            self.match(ZCodeParser.RRB)
            self.state = 420
            self.if_stmt_content()
            self.state = 421
            self.if_stmt_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmt_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def if_stmt_content(self):
            return self.getTypedRuleContext(ZCodeParser.If_stmt_contentContext,0)


        def if_stmt_tail(self):
            return self.getTypedRuleContext(ZCodeParser.If_stmt_tailContext,0)


        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_if_stmt_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt_tail" ):
                return visitor.visitIf_stmt_tail(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt_tail(self):

        localctx = ZCodeParser.If_stmt_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_if_stmt_tail)
        try:
            self.state = 436
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 423
                self.nullable_newline_list()
                self.state = 424
                self.match(ZCodeParser.ELIF)
                self.state = 425
                self.match(ZCodeParser.LRB)
                self.state = 426
                self.expr()
                self.state = 427
                self.match(ZCodeParser.RRB)
                self.state = 428
                self.if_stmt_content()
                self.state = 429
                self.if_stmt_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 431
                self.nullable_newline_list()
                self.state = 432
                self.match(ZCodeParser.ELSE)
                self.state = 433
                self.if_stmt_content()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

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
            return self.getToken(ZCodeParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = ZCodeParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.match(ZCodeParser.FOR)
            self.state = 439
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 440
            self.match(ZCodeParser.UNTIL)
            self.state = 441
            self.expr()
            self.state = 442
            self.match(ZCodeParser.BY)
            self.state = 443
            self.expr()
            self.state = 444
            self.nullable_newline_list()
            self.state = 445
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
            return self.getToken(ZCodeParser.BREAK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = ZCodeParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.match(ZCodeParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cont_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_cont_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCont_stmt" ):
                return visitor.visitCont_stmt(self)
            else:
                return visitor.visitChildren(self)




    def cont_stmt(self):

        localctx = ZCodeParser.Cont_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_cont_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.match(ZCodeParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def arg_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Arg_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arg_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg_list" ):
                return visitor.visitArg_list(self)
            else:
                return visitor.visitChildren(self)




    def arg_list(self):

        localctx = ZCodeParser.Arg_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_arg_list)
        try:
            self.state = 455
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOL_LIT, ZCodeParser.NUM_LIT, ZCodeParser.STR_LIT, ZCodeParser.MINUS, ZCodeParser.NOT, ZCodeParser.LSB, ZCodeParser.LRB, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 451
                self.expr()
                self.state = 452
                self.arg_list_tail()
                pass
            elif token in [ZCodeParser.RRB]:
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


    class Arg_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def arg_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Arg_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arg_list_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg_list_tail" ):
                return visitor.visitArg_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def arg_list_tail(self):

        localctx = ZCodeParser.Arg_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_arg_list_tail)
        try:
            self.state = 462
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.match(ZCodeParser.COMMA)
                self.state = 458
                self.expr()
                self.state = 459
                self.arg_list_tail()
                pass
            elif token in [ZCodeParser.RRB]:
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


    class Func_call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def arg_list(self):
            return self.getTypedRuleContext(ZCodeParser.Arg_listContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_stmt" ):
                return visitor.visitFunc_call_stmt(self)
            else:
                return visitor.visitChildren(self)




    def func_call_stmt(self):

        localctx = ZCodeParser.Func_call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_func_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 465
            self.match(ZCodeParser.LRB)
            self.state = 466
            self.arg_list()
            self.state = 467
            self.match(ZCodeParser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def arg_list(self):
            return self.getTypedRuleContext(ZCodeParser.Arg_listContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_expr" ):
                return visitor.visitFunc_call_expr(self)
            else:
                return visitor.visitChildren(self)




    def func_call_expr(self):

        localctx = ZCodeParser.Func_call_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_func_call_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 470
            self.match(ZCodeParser.LRB)
            self.state = 471
            self.arg_list()
            self.state = 472
            self.match(ZCodeParser.RRB)
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
        self._predicates[21] = self.expr2_sempred
        self._predicates[22] = self.expr3_sempred
        self._predicates[23] = self.expr4_sempred
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
         




