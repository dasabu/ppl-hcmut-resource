import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_01(self):
        self.assertTrue(TestLexer.test("bAc bCa","bAc,bCa,<EOF>",101))

    def test_02(self):
        self.assertTrue(TestLexer.test("ab12","ab12,<EOF>",102))

    def test_03(self):
        self.assertTrue(TestLexer.test("Var x1X;", "Var,x1X,;,<EOF>",103))

    def test_04(self):
        self.assertTrue(TestLexer.test("altershpere_SV12Exp;", "altershpere_SV12Exp,;,<EOF>",104))

    def test_05(self):
        self.assertTrue(TestLexer.test("string&", "string,Error Token &",105))

    def test_06(self):
        self.assertTrue(TestLexer.test("0x2F93_46B5_B", "0x2F9346B5B,<EOF>",106))

    def test_07(self):
        self.assertTrue(TestLexer.test("a \ b", "a,Error Token \\",107))

    def test_08(self):
        self.assertTrue(TestLexer.test("h032he809 890", "h032he809,890,<EOF>",108))

    def test_09(self):
        self.assertTrue(TestLexer.test("+ -  * / % ! && || == = != < > <= >= ==. +. :: New", "+,-,*,/,%,!,&&,||,==,=,!=,<,>,<=,>=,==.,+.,::,New,<EOF>",109))

    def test_10(self):
        self.assertTrue(TestLexer.test(""" "ABC: \\" ""","Illegal Escape In String: ABC: \\\"",110))

    def test_11(self):
        self.assertTrue(TestLexer.test(""" "abc \t xyz" ""","Unclosed String: abc ",111))

    def test_12(self):
        self.assertTrue(TestLexer.test(""" "abc \\t xyz" ""","abc \\t xyz,<EOF>",112))

    def test_13(self):
        self.assertTrue(TestLexer.test("""##""","Error Token #",113))

    def test_14(self):
        self.assertTrue(TestLexer.test("0b01","0b0,1,<EOF>",114))

    def test_15(self):
        self.assertTrue(TestLexer.test("0X_123","0,X_123,<EOF>",115))

    def test_16(self):
        self.assertTrue(TestLexer.test("123_4__56","1234,__56,<EOF>",116))

    def test_17(self):
        self.assertTrue(TestLexer.test("0999","0,999,<EOF>",117))

    def test_18(self):
        self.assertTrue(TestLexer.test("0x1_23","0x123,<EOF>",118))

    def test_19(self):
        self.assertTrue(TestLexer.test("0x12_3_","0x123,_,<EOF>",119))

    def test_20(self):
        self.assertTrue(TestLexer.test(".e3",".e3,<EOF>",120))

    def test_21(self):
        self.assertTrue(TestLexer.test("0.","0.,<EOF>",121))

    def test_22(self):
        self.assertTrue(TestLexer.test("09.E-99","0,9.E-99,<EOF>",122))

    def test_23(self):
        self.assertTrue(TestLexer.test("0_9.","0,_9,.,<EOF>",123))

    def test_24(self):
        self.assertTrue(TestLexer.test("12e4","12e4,<EOF>",124))

    def test_25(self):
        self.assertTrue(TestLexer.test("12.2E-6","12.2E-6,<EOF>",125))

    def test_26(self):
        self.assertTrue(TestLexer.test("a + b","a,+,b,<EOF>",126))

    def test_27(self):
        self.assertTrue(TestLexer.test(""" "ABC: \\\\" ""","ABC: \\\\,<EOF>",127))

    def test_28(self):
        self.assertTrue(TestLexer.test(""" "'" ""","Unclosed String: \'\" ",128))

    def test_29(self):
        self.assertTrue(TestLexer.test(""" "He asked me '"Where is John?'"" ""","He asked me \'\"Where is John?\'\",<EOF>",129))

    def test_30(self):
        self.assertTrue(TestLexer.test(""" "This is how we write comment ## hello ## bye" ""","This is how we write comment ## hello ## bye,<EOF>",130))

    def test_31(self):
        self.assertTrue(TestLexer.test(""" "abc\ as" ""","Illegal Escape In String: abc\\ ",131))

    def test_32(self):
        self.assertTrue(TestLexer.test("Break Continue Return","Break,Continue,Return,<EOF>",132))

    def test_33(self):
        self.assertTrue(TestLexer.test("If Elseif For Class Self Hello ( ) [ ] { }","If,Elseif,For,Class,Self,Hello,(,),[,],{,},<EOF>",133))

    def test_34(self):
        self.assertTrue(TestLexer.test(""" "Hello ##My## World" ""","Hello ##My## World,<EOF>",134))

    def test_35(self):
        self.assertTrue(TestLexer.test(""" "Hello World## " ## ""","Hello World## ,Error Token #",135))

    def test_36(self):
        self.assertTrue(TestLexer.test("1.01","1.01,<EOF>",136))

    def test_37(self):
        self.assertTrue(TestLexer.test("1.1e00","1.1e00,<EOF>",137))

    def test_38(self):
        self.assertTrue(TestLexer.test("001","00,1,<EOF>",138))

    def test_39(self):
        self.assertTrue(TestLexer.test(""" "abc\\h def"  ""","Illegal Escape In String: abc\\h",139))

    def test_40(self):
        self.assertTrue(TestLexer.test(""" "she \'\" ""","Unclosed String: she \'\" ",140))

    def test_41(self):
        self.assertTrue(TestLexer.test("0x000000","0x0,00,00,0,<EOF>",141))

    def test_42(self):
        self.assertTrue(TestLexer.test("0b0101110","0b0,101110,<EOF>",142))

    def test_43(self):
        self.assertTrue(TestLexer.test("000123","00,0123,<EOF>",143))

    def test_44(self):
        self.assertTrue(TestLexer.test("0x0 0X0 0b0 0B0 00 0 0C0","0x0,0X0,0b0,0B0,00,0,0,C0,<EOF>",144))

    def test_45(self):
        self.assertTrue(TestLexer.test(""" "He's John, he say "Hello" to me" ""","He's John, he say ,Hello, to me,<EOF>",145))

    def test_46(self):
        self.assertTrue(TestLexer.test(""" "He's John, he say '"Hello'" to me" ""","He's John, he say \'\"Hello\'\" to me,<EOF>",146))

    def test_47(self):
        self.assertTrue(TestLexer.test("_","_,<EOF>",147))

    def test_48(self):
        self.assertTrue(TestLexer.test(""" "n-V2"" """, "n-V2,Unclosed String:  ",148))
    
    def test_49(self):
        self.assertTrue(TestLexer.test("0311thy","0311,thy,<EOF>",149))

    def test_50(self):
        self.assertTrue(TestLexer.test("$0311thy","$0311thy,<EOF>",150))

    def test_51(self):
        self.assertTrue(TestLexer.test("1_20 1_2_0 1_02 1_0_2 012 0_12 120_","120,120,102,102,012,0,_12,120,_,<EOF>",151))

    def test_52(self):
        self.assertTrue(TestLexer.test(r""" "Hello \' there" """,r"""Hello \' there,<EOF>""",152))

    def test_53(self):
        self.assertTrue(TestLexer.test(""" "My string\nYour string " ""","Unclosed String: My string",153))

    def test_54(self):
        self.assertTrue(TestLexer.test(r""" "This is another \n \r \t string" """,r"""This is another \n \r \t string,<EOF>""",154))

    def test_55(self):
        self.assertTrue(TestLexer.test("{{[]};,;}","{,{,[,],},;,,,;,},<EOF>",155))

    def test_56(self):
        self.assertTrue(TestLexer.test(""" "abvnf\ofnvjg" ""","Illegal Escape In String: abvnf\o",156))

    def test_57(self):
        self.assertTrue(TestLexer.test(""" "abcdxyz123456""","Unclosed String: abcdxyz123456",157))

    def test_58(self):
        self.assertTrue(TestLexer.test("## this is comment ## 0x012_3","0x0,123,<EOF>",158))

    def test_59(self):
        self.assertTrue(TestLexer.test("### ## #####","Error Token #",159))

    def test_60(self):
        self.assertTrue(TestLexer.test(""" "### ## #####" ""","### ## #####,<EOF>",160))

    def test_61(self):
        self.assertTrue(TestLexer.test("abc@ca","abc,Error Token @",161))

    def test_62(self):
        self.assertTrue(TestLexer.test("0x12AEC09F","0x12AEC09F,<EOF>",162))

    def test_63(self):
        self.assertTrue(TestLexer.test("0123_7965","01237,965,<EOF>",163))

    def test_64(self):
        self.assertTrue(TestLexer.test("True False","True,False,<EOF>",164))

    def test_65(self):
        self.assertTrue(TestLexer.test("Int Array ARRAY Class ClAss","Int,Array,ARRAY,Class,ClAss,<EOF>",165))

    def test_66(self):
        self.assertTrue(TestLexer.test(""". Continue<= ::""",""".,Continue,<=,::,<EOF>""",166))

    def test_67(self):
        self.assertTrue(TestLexer.test("""|| ==>= ||>= >=<= ||>= :::: ||== ==## zAR62M6uezmzTqDcWLR2 ##> ##:: ||<= ||== ||<= ::== ==""","""||,==,>=,||,>=,>=,<=,||,>=,::,::,||,==,==,>,Error Token #""",167))

    def test_68(self):
        self.assertTrue(TestLexer.test("""== :::: #### >=""","""==,::,::,>=,<EOF>""",168))

    def test_69(self):
        self.assertTrue(TestLexer.test("""Class %Class KSCxqaxYSJInt oj15rQfFpR<= <=>= >=== Self5FGl_coSS$ <=## X17d$gapeR& ||< <=:: :::: Var== taaeKWlRA_## ||Float Class== kOHXVHUtTL>= <=:: <=|| >u1TBz40kgr ##""","""Class,%,Class,KSCxqaxYSJInt,oj15rQfFpR,<=,<=,>=,>=,==,Self5FGl_coSS,Error Token $""",169))

    def test_70(self):
        self.assertTrue(TestLexer.test("""## ##- Main""","""-,Main,<EOF>""",170))

    def test_71(self):
        self.assertTrue(TestLexer.test("""< By|| <=>= >=& ==|| .|| Continue! ::|| !## ::% <""","""<,By,||,<=,>=,>=,Error Token &""",171))

    def test_72(self):
        self.assertTrue(TestLexer.test(""">= ##:: ||== ==== BreakIn ##>= <=""",""">=,>=,<=,<EOF>""",172))

    def test_73(self):
        self.assertTrue(TestLexer.test("""|| <=Self ##RinCPQhvs8 >=/ >=42d7XW6_Ix />= <=! <=|| <=JzELj7JIj3 ||## ||New >=LpOq8468f1 ==In ==## ::>= ||""","""||,<=,Self,||,New,>=,LpOq8468f1,==,In,==,Error Token #""",173))

    def test_74(self):
        self.assertTrue(TestLexer.test("""## .>= ==## #### Return## ||## |||| lweNtndVAV== ==String 7kzIG58TDX|| ==""","""Return,||,||,lweNtndVAV,==,==,String,7,kzIG58TDX,||,==,<EOF>""",174))

    def test_75(self):
        self.assertTrue(TestLexer.test("""/ ||:: /Val +Program >=* i2FGA20EnU== ##== By:: ##""","""/,||,::,/,Val,+,Program,>=,*,i2FGA20EnU,==,<EOF>""",175))

    def test_76(self):
        self.assertTrue(TestLexer.test("""## 2rDnLulZwmForeach ==## >=<= &== ==== <=>= ##>= #### |||| 5cSkUAUw$I== :::: >=<= ==* ::= ##If :::: ==<= ==>= +""",""">=,<=,Error Token &""",176))

    def test_77(self):
        self.assertTrue(TestLexer.test("""Main ::Var ||""","""Main,::,Var,||,<EOF>""",177))

    def test_78(self):
        self.assertTrue(TestLexer.test("""|| ##""","""||,Error Token #""",178))

    def test_79(self):
        self.assertTrue(TestLexer.test("""|| :::: <=""","""||,::,::,<=,<EOF>""",179))

    def test_80(self):
        self.assertTrue(TestLexer.test(""">= ##|| ##Val ==""",""">=,Val,==,<EOF>""",180))

    def test_81(self):
        self.assertTrue(TestLexer.test("""|| >* ==## ##|| %|| >=>= +""","""||,>,*,==,||,%,||,>=,>=,+,<EOF>""",181))

    def test_82(self):
        self.assertTrue(TestLexer.test(""":: .## |||| <=== $Zz5W5a7kA:: ==>= <=== Return>= ==By >=""","""::,.,Error Token #""",182))

    def test_83(self):
        self.assertTrue(TestLexer.test("""|| ::""","""||,::,<EOF>""",183))

    def test_84(self):
        self.assertTrue(TestLexer.test("""> IZkYv4kleb>= -""",""">,IZkYv4kleb,>=,-,<EOF>""",184))

    def test_85(self):
        self.assertTrue(TestLexer.test("""Destructor <=YKyWy$UBlC ::/ ##|| ##|| 6wyOLmG4$YIn ::## ##|| ::+ Val<= Null! ||== >=""","""Destructor,<=,YKyWy,$UBlC,::,/,||,6,wyOLmG4,$YIn,::,||,::,+,Val,<=,Null,!,||,==,>=,<EOF>""",185))

    def test_86(self):
        self.assertTrue(TestLexer.test("""== :== ::: G0MeRGf9oG<= |||| ::Vlfa1107Yi >=! >=|| Val5c6wGSe9n3 <=## +lr_shKhBM5 <=. Poi_5ya3A0. >=mh24zsvSuQ <=""","""==,:,==,::,:,G0MeRGf9oG,<=,||,||,::,Vlfa1107Yi,>=,!,>=,||,Val5c6wGSe9n3,<=,Error Token #""",186))

    def test_87(self):
        self.assertTrue(TestLexer.test(""":: %<= #### Continue>= <>= ElseElseif >=/ ||BvlhigP0OE eropuVPlZr""","""::,%,<=,Continue,>=,<,>=,ElseElseif,>=,/,||,BvlhigP0OE,eropuVPlZr,<EOF>""",187))

    def test_88(self):
        self.assertTrue(TestLexer.test("""8VX_IX15d1 <=|| <String Float|| adYz1S5KsYNull ||## <=## #### <=|| ::Destructor <=:: ==mOc2RMEEYs :::: Int:: ##""","""8,VX_IX15d1,<=,||,<,String,Float,||,adYz1S5KsYNull,||,<=,||,::,Destructor,<=,::,==,mOc2RMEEYs,::,::,Int,::,Error Token #""",188))

    def test_89(self):
        self.assertTrue(TestLexer.test("""|| ||Class S1$I4$2oMR|| >=* ::>= >=== If## ||>= ::== >|| Programh7KeKU2RaU >=<= ##:: -Boolean ClassNew <=>= >=hDn$1rE3M4 Val""","""||,||,Class,S1,$I4,$2oMR,||,>=,*,::,>=,>=,==,If,::,-,Boolean,ClassNew,<=,>=,>=,hDn,$1rE3M4,Val,<EOF>""",189))

    def test_90(self):
        self.assertTrue(TestLexer.test("""* ##= ::== ||>= ##|| ::SivGBVBBJ4 ||:: /:: ##== >=Class <=:: <=:: ||## IB3azeKxgC|| ==>= <=## <=:: ::|| Constructor|| ||""","""*,||,::,SivGBVBBJ4,||,::,/,::,IB3azeKxgC,||,==,>=,<=,Error Token #""",190))

    def test_91(self):
        self.assertTrue(TestLexer.test(""". Continue<= ::""",""".,Continue,<=,::,<EOF>""",191))

    def test_92(self):
        self.assertTrue(TestLexer.test("""== ##iBOeDdHmo9 ||""","""==,Error Token #""",192))

    def test_93(self):
        self.assertTrue(TestLexer.test("""## <=<= VnhFTEyJmw""","""Error Token #""",193))

    def test_94(self):
        self.assertTrue(TestLexer.test("""Self <=:: ::<= ==: ==|| ::>= /<= +""","""Self,<=,::,::,<=,==,:,==,||,::,>=,/,<=,+,<EOF>""",194))

    def test_95(self):
        self.assertTrue(TestLexer.test("""== :::: #### >=""","""==,::,::,>=,<EOF>""",195))

    def test_96(self):
        self.assertTrue(TestLexer.test("""+ String>= ##:: !:: <=== 82fHxTEUHkTR45gM_$OK Array<= >=! ==## ##== &% ##j5Z$7iodbQ ||""","""+,String,>=,j5Z,$7iodbQ,||,<EOF>""",196))

    def test_97(self):
        self.assertTrue(TestLexer.test("""If ::Destructor 3bYuQSDOkj:: UNGbuy9MeX## ==>= ##<= >=== >|| >=<= <=== .MGuX1pdzHB By""","""If,::,Destructor,3,bYuQSDOkj,::,UNGbuy9MeX,<=,>=,==,>,||,>=,<=,<=,==,.,MGuX1pdzHB,By,<EOF>""",197))

    def test_98(self):
        self.assertTrue(TestLexer.test("$$A","Error Token $",198))

    def test_99(self):
        self.assertTrue(TestLexer.test("$","Error Token $",199))

    def test_100(self):
        self.assertTrue(TestLexer.test("$A","$A,<EOF>",200))

    
