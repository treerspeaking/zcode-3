# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\28")
        buf.write("\u019c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\3\2\3\2\5\2r\n\2\3")
        buf.write("\3\6\3u\n\3\r\3\16\3v\3\3\3\3\7\3{\n\3\f\3\16\3~\13\3")
        buf.write("\5\3\u0080\n\3\3\3\3\3\5\3\u0084\n\3\3\3\6\3\u0087\n\3")
        buf.write("\r\3\16\3\u0088\5\3\u008b\n\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\5\4\u0094\n\4\3\4\7\4\u0097\n\4\f\4\16\4\u009a\13")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3%\3&\3")
        buf.write("&\3\'\3\'\3\'\3(\3(\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3")
        buf.write("-\3.\3.\3.\3.\3.\3.\3.\3.\3.\5.\u0149\n.\3/\5/\u014c\n")
        buf.write("/\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\62\7\62\u015e\n\62\f\62\16\62\u0161")
        buf.write("\13\62\3\62\3\62\3\63\3\63\7\63\u0167\n\63\f\63\16\63")
        buf.write("\u016a\13\63\3\64\6\64\u016d\n\64\r\64\16\64\u016e\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u017a\n")
        buf.write("\65\3\65\7\65\u017d\n\65\f\65\16\65\u0180\13\65\3\65\3")
        buf.write("\65\3\65\5\65\u0185\n\65\3\65\3\65\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\5\66\u0190\n\66\3\66\7\66\u0193\n\66\f")
        buf.write("\66\16\66\u0196\13\66\3\66\3\66\3\67\3\67\3\67\2\28\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8\3\2\r\3\2")
        buf.write("\62;\4\2GGgg\4\2--//\3\2$$\t\2))^^ddhhppttvv\7\2\f\f\17")
        buf.write("\17$$))^^\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\5\2")
        buf.write("\n\13\16\16\"\"\b\2))ddhhppttvv\2\u01b5\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\3q\3\2\2\2\5t\3\2\2\2\7\u008c")
        buf.write("\3\2\2\2\t\u009e\3\2\2\2\13\u00a3\3\2\2\2\r\u00a9\3\2")
        buf.write("\2\2\17\u00b0\3\2\2\2\21\u00b5\3\2\2\2\23\u00bc\3\2\2")
        buf.write("\2\25\u00c3\3\2\2\2\27\u00c7\3\2\2\2\31\u00cf\3\2\2\2")
        buf.write("\33\u00d4\3\2\2\2\35\u00d8\3\2\2\2\37\u00de\3\2\2\2!\u00e1")
        buf.write("\3\2\2\2#\u00e7\3\2\2\2%\u00f0\3\2\2\2\'\u00f3\3\2\2\2")
        buf.write(")\u00f8\3\2\2\2+\u00fd\3\2\2\2-\u0103\3\2\2\2/\u0107\3")
        buf.write("\2\2\2\61\u0109\3\2\2\2\63\u010b\3\2\2\2\65\u010d\3\2")
        buf.write("\2\2\67\u010f\3\2\2\29\u0111\3\2\2\2;\u0115\3\2\2\2=\u0119")
        buf.write("\3\2\2\2?\u011c\3\2\2\2A\u011f\3\2\2\2C\u0121\3\2\2\2")
        buf.write("E\u0124\3\2\2\2G\u0127\3\2\2\2I\u0129\3\2\2\2K\u012c\3")
        buf.write("\2\2\2M\u012e\3\2\2\2O\u0131\3\2\2\2Q\u0135\3\2\2\2S\u0137")
        buf.write("\3\2\2\2U\u0139\3\2\2\2W\u013b\3\2\2\2Y\u013d\3\2\2\2")
        buf.write("[\u0148\3\2\2\2]\u014b\3\2\2\2_\u0150\3\2\2\2a\u0153\3")
        buf.write("\2\2\2c\u0159\3\2\2\2e\u0164\3\2\2\2g\u016c\3\2\2\2i\u0172")
        buf.write("\3\2\2\2k\u0188\3\2\2\2m\u0199\3\2\2\2or\5\t\5\2pr\5\13")
        buf.write("\6\2qo\3\2\2\2qp\3\2\2\2r\4\3\2\2\2su\t\2\2\2ts\3\2\2")
        buf.write("\2uv\3\2\2\2vt\3\2\2\2vw\3\2\2\2w\177\3\2\2\2x|\7\60\2")
        buf.write("\2y{\t\2\2\2zy\3\2\2\2{~\3\2\2\2|z\3\2\2\2|}\3\2\2\2}")
        buf.write("\u0080\3\2\2\2~|\3\2\2\2\177x\3\2\2\2\177\u0080\3\2\2")
        buf.write("\2\u0080\u008a\3\2\2\2\u0081\u0083\t\3\2\2\u0082\u0084")
        buf.write("\t\4\2\2\u0083\u0082\3\2\2\2\u0083\u0084\3\2\2\2\u0084")
        buf.write("\u0086\3\2\2\2\u0085\u0087\t\2\2\2\u0086\u0085\3\2\2\2")
        buf.write("\u0087\u0088\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3")
        buf.write("\2\2\2\u0089\u008b\3\2\2\2\u008a\u0081\3\2\2\2\u008a\u008b")
        buf.write("\3\2\2\2\u008b\6\3\2\2\2\u008c\u0098\t\5\2\2\u008d\u008e")
        buf.write("\7^\2\2\u008e\u0097\t\6\2\2\u008f\u0090\7)\2\2\u0090\u0094")
        buf.write("\6\4\2\2\u0091\u0092\7)\2\2\u0092\u0094\7$\2\2\u0093\u008f")
        buf.write("\3\2\2\2\u0093\u0091\3\2\2\2\u0094\u0097\3\2\2\2\u0095")
        buf.write("\u0097\n\7\2\2\u0096\u008d\3\2\2\2\u0096\u0093\3\2\2\2")
        buf.write("\u0096\u0095\3\2\2\2\u0097\u009a\3\2\2\2\u0098\u0096\3")
        buf.write("\2\2\2\u0098\u0099\3\2\2\2\u0099\u009b\3\2\2\2\u009a\u0098")
        buf.write("\3\2\2\2\u009b\u009c\t\5\2\2\u009c\u009d\b\4\2\2\u009d")
        buf.write("\b\3\2\2\2\u009e\u009f\7v\2\2\u009f\u00a0\7t\2\2\u00a0")
        buf.write("\u00a1\7w\2\2\u00a1\u00a2\7g\2\2\u00a2\n\3\2\2\2\u00a3")
        buf.write("\u00a4\7h\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6\7n\2\2\u00a6")
        buf.write("\u00a7\7u\2\2\u00a7\u00a8\7g\2\2\u00a8\f\3\2\2\2\u00a9")
        buf.write("\u00aa\7p\2\2\u00aa\u00ab\7w\2\2\u00ab\u00ac\7o\2\2\u00ac")
        buf.write("\u00ad\7d\2\2\u00ad\u00ae\7g\2\2\u00ae\u00af\7t\2\2\u00af")
        buf.write("\16\3\2\2\2\u00b0\u00b1\7d\2\2\u00b1\u00b2\7q\2\2\u00b2")
        buf.write("\u00b3\7q\2\2\u00b3\u00b4\7n\2\2\u00b4\20\3\2\2\2\u00b5")
        buf.write("\u00b6\7u\2\2\u00b6\u00b7\7v\2\2\u00b7\u00b8\7t\2\2\u00b8")
        buf.write("\u00b9\7k\2\2\u00b9\u00ba\7p\2\2\u00ba\u00bb\7i\2\2\u00bb")
        buf.write("\22\3\2\2\2\u00bc\u00bd\7t\2\2\u00bd\u00be\7g\2\2\u00be")
        buf.write("\u00bf\7v\2\2\u00bf\u00c0\7w\2\2\u00c0\u00c1\7t\2\2\u00c1")
        buf.write("\u00c2\7p\2\2\u00c2\24\3\2\2\2\u00c3\u00c4\7x\2\2\u00c4")
        buf.write("\u00c5\7c\2\2\u00c5\u00c6\7t\2\2\u00c6\26\3\2\2\2\u00c7")
        buf.write("\u00c8\7f\2\2\u00c8\u00c9\7{\2\2\u00c9\u00ca\7p\2\2\u00ca")
        buf.write("\u00cb\7c\2\2\u00cb\u00cc\7o\2\2\u00cc\u00cd\7k\2\2\u00cd")
        buf.write("\u00ce\7e\2\2\u00ce\30\3\2\2\2\u00cf\u00d0\7h\2\2\u00d0")
        buf.write("\u00d1\7w\2\2\u00d1\u00d2\7p\2\2\u00d2\u00d3\7e\2\2\u00d3")
        buf.write("\32\3\2\2\2\u00d4\u00d5\7h\2\2\u00d5\u00d6\7q\2\2\u00d6")
        buf.write("\u00d7\7t\2\2\u00d7\34\3\2\2\2\u00d8\u00d9\7w\2\2\u00d9")
        buf.write("\u00da\7p\2\2\u00da\u00db\7v\2\2\u00db\u00dc\7k\2\2\u00dc")
        buf.write("\u00dd\7n\2\2\u00dd\36\3\2\2\2\u00de\u00df\7d\2\2\u00df")
        buf.write("\u00e0\7{\2\2\u00e0 \3\2\2\2\u00e1\u00e2\7d\2\2\u00e2")
        buf.write("\u00e3\7t\2\2\u00e3\u00e4\7g\2\2\u00e4\u00e5\7c\2\2\u00e5")
        buf.write("\u00e6\7m\2\2\u00e6\"\3\2\2\2\u00e7\u00e8\7e\2\2\u00e8")
        buf.write("\u00e9\7q\2\2\u00e9\u00ea\7p\2\2\u00ea\u00eb\7v\2\2\u00eb")
        buf.write("\u00ec\7k\2\2\u00ec\u00ed\7p\2\2\u00ed\u00ee\7w\2\2\u00ee")
        buf.write("\u00ef\7g\2\2\u00ef$\3\2\2\2\u00f0\u00f1\7k\2\2\u00f1")
        buf.write("\u00f2\7h\2\2\u00f2&\3\2\2\2\u00f3\u00f4\7g\2\2\u00f4")
        buf.write("\u00f5\7n\2\2\u00f5\u00f6\7u\2\2\u00f6\u00f7\7g\2\2\u00f7")
        buf.write("(\3\2\2\2\u00f8\u00f9\7g\2\2\u00f9\u00fa\7n\2\2\u00fa")
        buf.write("\u00fb\7k\2\2\u00fb\u00fc\7h\2\2\u00fc*\3\2\2\2\u00fd")
        buf.write("\u00fe\7d\2\2\u00fe\u00ff\7g\2\2\u00ff\u0100\7i\2\2\u0100")
        buf.write("\u0101\7k\2\2\u0101\u0102\7p\2\2\u0102,\3\2\2\2\u0103")
        buf.write("\u0104\7g\2\2\u0104\u0105\7p\2\2\u0105\u0106\7f\2\2\u0106")
        buf.write(".\3\2\2\2\u0107\u0108\7-\2\2\u0108\60\3\2\2\2\u0109\u010a")
        buf.write("\7/\2\2\u010a\62\3\2\2\2\u010b\u010c\7,\2\2\u010c\64\3")
        buf.write("\2\2\2\u010d\u010e\7\61\2\2\u010e\66\3\2\2\2\u010f\u0110")
        buf.write("\7\'\2\2\u01108\3\2\2\2\u0111\u0112\7p\2\2\u0112\u0113")
        buf.write("\7q\2\2\u0113\u0114\7v\2\2\u0114:\3\2\2\2\u0115\u0116")
        buf.write("\7c\2\2\u0116\u0117\7p\2\2\u0117\u0118\7f\2\2\u0118<\3")
        buf.write("\2\2\2\u0119\u011a\7q\2\2\u011a\u011b\7t\2\2\u011b>\3")
        buf.write("\2\2\2\u011c\u011d\7>\2\2\u011d\u011e\7/\2\2\u011e@\3")
        buf.write("\2\2\2\u011f\u0120\7?\2\2\u0120B\3\2\2\2\u0121\u0122\7")
        buf.write("?\2\2\u0122\u0123\7?\2\2\u0123D\3\2\2\2\u0124\u0125\7")
        buf.write("#\2\2\u0125\u0126\7?\2\2\u0126F\3\2\2\2\u0127\u0128\7")
        buf.write(">\2\2\u0128H\3\2\2\2\u0129\u012a\7>\2\2\u012a\u012b\7")
        buf.write("?\2\2\u012bJ\3\2\2\2\u012c\u012d\7@\2\2\u012dL\3\2\2\2")
        buf.write("\u012e\u012f\7@\2\2\u012f\u0130\7?\2\2\u0130N\3\2\2\2")
        buf.write("\u0131\u0132\7\60\2\2\u0132\u0133\7\60\2\2\u0133\u0134")
        buf.write("\7\60\2\2\u0134P\3\2\2\2\u0135\u0136\7]\2\2\u0136R\3\2")
        buf.write("\2\2\u0137\u0138\7_\2\2\u0138T\3\2\2\2\u0139\u013a\7*")
        buf.write("\2\2\u013aV\3\2\2\2\u013b\u013c\7+\2\2\u013cX\3\2\2\2")
        buf.write("\u013d\u013e\7.\2\2\u013eZ\3\2\2\2\u013f\u0140\5]/\2\u0140")
        buf.write("\u0141\b.\3\2\u0141\u0149\3\2\2\2\u0142\u0143\5_\60\2")
        buf.write("\u0143\u0144\b.\4\2\u0144\u0149\3\2\2\2\u0145\u0146\5")
        buf.write("a\61\2\u0146\u0147\b.\5\2\u0147\u0149\3\2\2\2\u0148\u013f")
        buf.write("\3\2\2\2\u0148\u0142\3\2\2\2\u0148\u0145\3\2\2\2\u0149")
        buf.write("\\\3\2\2\2\u014a\u014c\7\17\2\2\u014b\u014a\3\2\2\2\u014b")
        buf.write("\u014c\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014e\7\f\2\2")
        buf.write("\u014e\u014f\b/\6\2\u014f^\3\2\2\2\u0150\u0151\7\17\2")
        buf.write("\2\u0151\u0152\b\60\7\2\u0152`\3\2\2\2\u0153\u0154\7\17")
        buf.write("\2\2\u0154\u0155\7\17\2\2\u0155\u0156\7\f\2\2\u0156\u0157")
        buf.write("\3\2\2\2\u0157\u0158\b\61\b\2\u0158b\3\2\2\2\u0159\u015a")
        buf.write("\7%\2\2\u015a\u015b\7%\2\2\u015b\u015f\3\2\2\2\u015c\u015e")
        buf.write("\n\b\2\2\u015d\u015c\3\2\2\2\u015e\u0161\3\2\2\2\u015f")
        buf.write("\u015d\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0162\3\2\2\2")
        buf.write("\u0161\u015f\3\2\2\2\u0162\u0163\b\62\t\2\u0163d\3\2\2")
        buf.write("\2\u0164\u0168\t\t\2\2\u0165\u0167\t\n\2\2\u0166\u0165")
        buf.write("\3\2\2\2\u0167\u016a\3\2\2\2\u0168\u0166\3\2\2\2\u0168")
        buf.write("\u0169\3\2\2\2\u0169f\3\2\2\2\u016a\u0168\3\2\2\2\u016b")
        buf.write("\u016d\t\13\2\2\u016c\u016b\3\2\2\2\u016d\u016e\3\2\2")
        buf.write("\2\u016e\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0170")
        buf.write("\3\2\2\2\u0170\u0171\b\64\t\2\u0171h\3\2\2\2\u0172\u017e")
        buf.write("\t\5\2\2\u0173\u0174\7^\2\2\u0174\u017d\t\6\2\2\u0175")
        buf.write("\u0176\7)\2\2\u0176\u017a\6\65\3\2\u0177\u0178\7)\2\2")
        buf.write("\u0178\u017a\7$\2\2\u0179\u0175\3\2\2\2\u0179\u0177\3")
        buf.write("\2\2\2\u017a\u017d\3\2\2\2\u017b\u017d\n\7\2\2\u017c\u0173")
        buf.write("\3\2\2\2\u017c\u0179\3\2\2\2\u017c\u017b\3\2\2\2\u017d")
        buf.write("\u0180\3\2\2\2\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2")
        buf.write("\u017f\u0184\3\2\2\2\u0180\u017e\3\2\2\2\u0181\u0182\7")
        buf.write("^\2\2\u0182\u0185\n\f\2\2\u0183\u0185\7^\2\2\u0184\u0181")
        buf.write("\3\2\2\2\u0184\u0183\3\2\2\2\u0185\u0186\3\2\2\2\u0186")
        buf.write("\u0187\b\65\n\2\u0187j\3\2\2\2\u0188\u0194\t\5\2\2\u0189")
        buf.write("\u018a\7^\2\2\u018a\u0193\t\6\2\2\u018b\u018c\7)\2\2\u018c")
        buf.write("\u0190\6\66\4\2\u018d\u018e\7)\2\2\u018e\u0190\7$\2\2")
        buf.write("\u018f\u018b\3\2\2\2\u018f\u018d\3\2\2\2\u0190\u0193\3")
        buf.write("\2\2\2\u0191\u0193\n\7\2\2\u0192\u0189\3\2\2\2\u0192\u018f")
        buf.write("\3\2\2\2\u0192\u0191\3\2\2\2\u0193\u0196\3\2\2\2\u0194")
        buf.write("\u0192\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0197\3\2\2\2")
        buf.write("\u0196\u0194\3\2\2\2\u0197\u0198\b\66\13\2\u0198l\3\2")
        buf.write("\2\2\u0199\u019a\13\2\2\2\u019a\u019b\b\67\f\2\u019bn")
        buf.write("\3\2\2\2\31\2qv|\177\u0083\u0088\u008a\u0093\u0096\u0098")
        buf.write("\u0148\u014b\u015f\u0168\u016e\u0179\u017c\u017e\u0184")
        buf.write("\u018f\u0192\u0194\r\3\4\2\3.\3\3.\4\3.\5\3/\6\3\60\7")
        buf.write("\3\61\b\b\2\2\3\65\t\3\66\n\3\67\13")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOL_LIT = 1
    NUM_LIT = 2
    STR_LIT = 3
    TRUE = 4
    FALSE = 5
    NUM = 6
    BOOL = 7
    STR = 8
    RETURN = 9
    VAR = 10
    DYNAMIC = 11
    FUNC = 12
    FOR = 13
    UNTIL = 14
    BY = 15
    BREAK = 16
    CONTINUE = 17
    IF = 18
    ELSE = 19
    ELIF = 20
    BEGIN = 21
    END = 22
    PLUS = 23
    MINUS = 24
    MULTIPLY = 25
    DIVIDE = 26
    MODULO = 27
    NOT = 28
    AND = 29
    OR = 30
    ASSIGN = 31
    EQUAL = 32
    DEQUAL = 33
    NOT_EQUAL = 34
    LESS = 35
    LESS_EQUAL = 36
    GREATER = 37
    GREATER_EQUAL = 38
    CONCAT = 39
    LSB = 40
    RSB = 41
    LRB = 42
    RRB = 43
    COMMA = 44
    NEWLINE = 45
    NL1 = 46
    NL2 = 47
    NL3 = 48
    COMMENT_LINE = 49
    IDENTIFIER = 50
    WS = 51
    ILLEGAL_ESCAPE = 52
    UNCLOSE_STRING = 53
    ERROR_CHAR = 54

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'+'", "'-'", "'*'", "'/'", "'%'", "'not'", "'and'", 
            "'or'", "'<-'", "'='", "'=='", "'!='", "'<'", "'<='", "'>'", 
            "'>='", "'...'", "'['", "']'", "'('", "')'", "','", "'\r'", 
            "'\r\r\n'" ]

    symbolicNames = [ "<INVALID>",
            "BOOL_LIT", "NUM_LIT", "STR_LIT", "TRUE", "FALSE", "NUM", "BOOL", 
            "STR", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", 
            "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "PLUS", 
            "MINUS", "MULTIPLY", "DIVIDE", "MODULO", "NOT", "AND", "OR", 
            "ASSIGN", "EQUAL", "DEQUAL", "NOT_EQUAL", "LESS", "LESS_EQUAL", 
            "GREATER", "GREATER_EQUAL", "CONCAT", "LSB", "RSB", "LRB", "RRB", 
            "COMMA", "NEWLINE", "NL1", "NL2", "NL3", "COMMENT_LINE", "IDENTIFIER", 
            "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "BOOL_LIT", "NUM_LIT", "STR_LIT", "TRUE", "FALSE", "NUM", 
                  "BOOL", "STR", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", 
                  "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", 
                  "BEGIN", "END", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", 
                  "MODULO", "NOT", "AND", "OR", "ASSIGN", "EQUAL", "DEQUAL", 
                  "NOT_EQUAL", "LESS", "LESS_EQUAL", "GREATER", "GREATER_EQUAL", 
                  "CONCAT", "LSB", "RSB", "LRB", "RRB", "COMMA", "NEWLINE", 
                  "NL1", "NL2", "NL3", "COMMENT_LINE", "IDENTIFIER", "WS", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[2] = self.STR_LIT_action 
            actions[44] = self.NEWLINE_action 
            actions[45] = self.NL1_action 
            actions[46] = self.NL2_action 
            actions[47] = self.NL3_action 
            actions[51] = self.ILLEGAL_ESCAPE_action 
            actions[52] = self.UNCLOSE_STRING_action 
            actions[53] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STR_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            if self.text == '\r\n':  
                self.text = '\n'
              
     

        if actionIndex == 2:
            self.text = '\n'
     

        if actionIndex == 3:
            self.text = '\n'
     

    def NL1_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

              if self.text == '\r\n':  
                self.text = '\n'
              
     

    def NL2_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            self.text = '\n'
     

    def NL3_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            self.text = '\n'
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
            raise IllegalEscape(self.text[1:])
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:
            raise UncloseString(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 9:
            raise ErrorToken(self.text)
     

    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[2] = self.STR_LIT_sempred
            preds[51] = self.ILLEGAL_ESCAPE_sempred
            preds[52] = self.UNCLOSE_STRING_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def STR_LIT_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self._input.LA(1)!=ord("\"")
         

    def ILLEGAL_ESCAPE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 1:
                return self._input.LA(1)!=ord("\"")
         

    def UNCLOSE_STRING_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 2:
                return self._input.LA(1)!=ord("\"")
         


