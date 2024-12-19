import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifier1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
    def test_identifier2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abcass","abcass,<EOF>",102))
    def test_identifier3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc ass","abc,ass,<EOF>",103))
    def test_identifier4(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abcass__","abcass__,<EOF>",104))
    def test_identifier5(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abcass","abcass,<EOF>",105))
    def test_identifier6(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("float a()","float,a,(,),<EOF>",106))
    def test_identifier7(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("a[5]","a,[,5,],<EOF>",107))
    def test_identifier8(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("a+b*c","a,+,b,*,c,<EOF>",108))
    def test_identifier9(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("a^abc","a,^,abc,<EOF>",109))
    def test_identifier10(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("void main()","void,main,(,),<EOF>",110))

    def test_integer1(self):
        self.assertTrue(TestLexer.test("1a1","1,a1,<EOF>",111))
    def test_integer2(self):
        self.assertTrue(TestLexer.test("1 + 2*4","1,+,2,*,4,<EOF>",112))
    def test_integer3(self):
        self.assertTrue(TestLexer.test("1-2||*2","1,-,2,||,*,2,<EOF>",113))
    def test_integer4(self):
        self.assertTrue(TestLexer.test("int aAC =  4 ;","int,aAC,=,4,;,<EOF>",114))
    def test_integer5(self):
        self.assertTrue(TestLexer.test("0 1 2 3","0,1,2,3,<EOF>",115))  
    def test_integer6(self):
        self.assertTrue(TestLexer.test("34a","34,a,<EOF>",116))
    def test_integer7(self):
        self.assertTrue(TestLexer.test("1a12dsf1","1,a12dsf1,<EOF>",117))
    def test_integer8(self):
        self.assertTrue(TestLexer.test("1 . .9","1,.,.,9,<EOF>",118))
    def test_integer9(self):
        self.assertTrue(TestLexer.test("float[5] a ;","float,[,5,],a,;,<EOF>",119))
    def test_integer10(self):
        self.assertTrue(TestLexer.test("1 2","1,2,<EOF>",120)) 

    def test_float1(self):
        self.assertTrue(TestLexer.test("1.1e4","1.1e4,<EOF>",121))
    def test_float2(self):
        self.assertTrue(TestLexer.test("1. 2. 3a. .4 .5","1.,2.,3,a,.,.,4,.,5,<EOF>",122))
    def test_float3(self):
        self.assertTrue(TestLexer.test("12e8 0.3E-1 12e+43","12e8,0.3E-1,12e+43,<EOF>",123))
    def test_float4(self):
        self.assertTrue(TestLexer.test("143e","143,e,<EOF>",124))
    def test_float5(self):
        self.assertTrue(TestLexer.test("1.0e-30.e-5","1.0e-30,.,e,-,5,<EOF>",125))
    def test_float6(self):
        self.assertTrue(TestLexer.test("as3.1","as3,.,1,<EOF>",126))
    def test_float7(self):
        self.assertTrue(TestLexer.test("7.","7.,<EOF>",127))
    def test_float8(self):
        self.assertTrue(TestLexer.test("12e+42","12e+42,<EOF>",128))
    def test_float9(self):
        self.assertTrue(TestLexer.test("3.12  1e ","3.12,1,e,<EOF>",129))
    def test_float10(self):
        self.assertTrue(TestLexer.test("1.0e-3.e-51.0e-3.e-5","1.0e-3,.,e,-,51.0e-3,.,e,-,5,<EOF>",130))  
# test boolean
    def test_boolean1(self):
        self.assertTrue(TestLexer.test("true","true,<EOF>",131))
    def test_boolean2(self):
        self.assertTrue(TestLexer.test("false","false,<EOF>",132))
    def test_boolean3(self):
        self.assertTrue(TestLexer.test("true1","true1,<EOF>",133))
    def test_boolean4(self):
        self.assertTrue(TestLexer.test("0false","0,false,<EOF>",134))
    def test_boolean5(self):
        self.assertTrue(TestLexer.test("true1false","true1false,<EOF>",135))
    def test_boolean6(self):
        self.assertTrue(TestLexer.test("True","True,<EOF>",136))
    def test_boolean7(self):
        self.assertTrue(TestLexer.test("False","False,<EOF>",137))
    def test_boolean8(self):
        self.assertTrue(TestLexer.test("1true","1,true,<EOF>",138))
    def test_boolean9(self):
        self.assertTrue(TestLexer.test("0false","0,false,<EOF>",139))
    def test_boolean10(self):
        self.assertTrue(TestLexer.test("True3False","True3False,<EOF>",140))
# test string
    def test_string1(self):
        self.assertTrue(TestLexer.test("\"abc ?:)(0) flag{hElpmE_ppL} \"","abc ?:)(0) flag{hElpmE_ppL} ,<EOF>",141))
    def test_string2(self):
        self.assertTrue(TestLexer.test("\"abc\" 'abc'","abc,Error Token '",142))
    def test_string3(self):
        self.assertTrue(TestLexer.test("\"abc 'def'\"","abc 'def',<EOF>",143))
    def test_string4(self):
        self.assertTrue(TestLexer.test("\"abc \"def\"\"","abc \"def\",<EOF>",144))
    def test_string5(self):
        self.assertTrue(TestLexer.test("\"abc \\\"def\\\"\"","abc \\\"def\\\",<EOF>",145))
    
    def test_string6(self):
        self.assertTrue(TestLexer.test("\"abc ?:)(0) flag{hElpmE_ppL} \n \r \"","Unclosed String: abc ?:)(0) flag{hElpmE_ppL} ",146))
    def test_string7(self):
        self.assertTrue(TestLexer.test("\"ASD\" 'AEc'","ASD,Error Token '",147))
    def test_string8(self):
        self.assertTrue(TestLexer.test("\"XCc 'XCc'\"","XCc 'XCc',<EOF>",148))
    def test_string9(self):
        self.assertTrue(TestLexer.test("\"c \1 \"cc\"\"","c \"cc\",<EOF>",149))
    def test_string10(self):
        self.assertTrue(TestLexer.test("\"a \\\"def\\\"\"","a \\\"def\\\",<EOF>",150))
# test Character Set
    def test_characterSet1(self):
        self.assertTrue(TestLexer.test(" \n \r \f \t", "<EOF>",151 ))
    def test_characterSet2(self):
        self.assertTrue(TestLexer.test("kh s", "kh,s,<EOF>",152))
    def test_characterSet3(self):
        self.assertTrue(TestLexer.test("P\n_Ki\fllM\re}","P,_Ki,llM,e,},<EOF>",153))
    def test_characterSet4(self):
        self.assertTrue(TestLexer.test("\ta\n\t\t\t\t\t\t\n","a,<EOF>",154))
    def test_characterSet5(self):
        self.assertTrue(TestLexer.test("a\ta\ta\ta\t}","a,a,a,a,},<EOF>",155)) 
    def test_characterSet6(self):
        self.assertTrue(TestLexer.test("\n \f \b \n \r \f \t", "Error Token ",156 ))
    def test_characterSet7(self):
        self.assertTrue(TestLexer.test("12 sd s", "12,sd,s,<EOF>",157))
    def test_characterSet8(self):
        self.assertTrue(TestLexer.test("\n","<EOF>",158))
    def test_characterSet9(self):
        self.assertTrue(TestLexer.test("\na\na\na\t","a,a,a,<EOF>",159))
    def test_characterSet10(self):
        self.assertTrue(TestLexer.test("\t","<EOF>",160))  
# test comments
    def test_comment1(self):
        self.assertTrue(TestLexer.test("# DT's DAT","<EOF>",161))
    def test_comment2(self):
        self.assertTrue(TestLexer.test("# DAT\n# DAT\n THANH","THANH,<EOF>",162))  
    def test_comment3(self):
        self.assertTrue(TestLexer.test("/* block*/","<EOF>",163))
    def test_comment4(self):
        self.assertTrue(TestLexer.test("/* DU THANH DAT # DAT */DAT\n#cmt","DAT,<EOF>",164))
    def test_comment5(self):
        self.assertTrue(TestLexer.test(" /* a */","<EOF>",165)) 
    def test_comment6(self):
        self.assertTrue(TestLexer.test("#\n #\n# d a","<EOF>",166))
    def test_comment7(self):
        self.assertTrue(TestLexer.test("# abc\n\t# def\n aa","aa,<EOF>",167))  
    def test_comment8(self):
        self.assertTrue(TestLexer.test("/* ^~^ */","<EOF>",168))
    def test_comment9(self):
        self.assertTrue(TestLexer.test("/* ~~~ */aa\n#~~~~~~/* ","aa,<EOF>",169))
    def test_comment10(self):
        self.assertTrue(TestLexer.test("/* ~~~~~~~~~~~ */ ","<EOF>",170))    
# test operator
    def test_operator1(self):
        self.assertTrue(TestLexer.test("=","=,<EOF>",171))
    def test_operator2(self):
        self.assertTrue(TestLexer.test("==","==,<EOF>",172))
    def test_operator3(self):
        self.assertTrue(TestLexer.test("!=","!=,<EOF>",173))
    def test_operator4(self):
        self.assertTrue(TestLexer.test("===","==,=,<EOF>",174))
    def test_operator5(self):
        self.assertTrue(TestLexer.test("!==","!=,=,<EOF>",175))
    def test_operator6(self):
        self.assertTrue(TestLexer.test("+=","+,=,<EOF>",176))
    def test_operator7(self):
        self.assertTrue(TestLexer.test("<><+>++====>=>>=>","<,>,<,+,>,+,+,==,==,>=,>,>=,>,<EOF>",177))
    def test_operator8(self):
        self.assertTrue(TestLexer.test("||&&!=!!=<>>>=>&&%#dfasjdf ","||,&&,!=,!,!=,<,>,>,>=,>,&&,%,<EOF>",178))
    def test_operator9(self):
        self.assertTrue(TestLexer.test("&&==&&==&&==&&==","&&,==,&&,==,&&,==,&&,==,<EOF>",179))
    def test_operator10(self):
        self.assertTrue(TestLexer.test("%&&***/\\\n\\^%<>++==---+<+>\\","%,&&,*,*,*,/,\,\,^,%,<,>,+,+,==,-,-,-,+,<,+,>,\,<EOF>",180))
# test separator
    def test_separator1(self):
        self.assertTrue(TestLexer.test(",,",",,,,<EOF>",181))
    def test_separator2(self):
        self.assertTrue(TestLexer.test("{}{[]][][}{}","{,},{,[,],],[,],[,},{,},<EOF>",182))
    def test_separator3(self):
        self.assertTrue(TestLexer.test(":}{[,];;[}{)",":,},{,[,,,],;,;,[,},{,),<EOF>",183))
    def test_separator4(self):
        self.assertTrue(TestLexer.test("[]}{[,][][}()","[,],},{,[,,,],[,],[,},(,),<EOF>",184))
    def test_separator5(self):
        self.assertTrue(TestLexer.test(";:,,",";,:,,,,,<EOF>",185))
    def test_separator6(self):
        self.assertTrue(TestLexer.test(".,::;{[}]}",".,,,:,:,;,{,[,},],},<EOF>",186))
    def test_separator7(self):
        self.assertTrue(TestLexer.test(".,::;..,.,",".,,,:,:,;,.,.,,,.,,,<EOF>",187))
    def test_separator8(self):
        self.assertTrue(TestLexer.test("{}][]{}[}[[]][]]}","{,},],[,],{,},[,},[,[,],],[,],],},<EOF>",188))
    def test_separator9(self):
        self.assertTrue(TestLexer.test(":[{]]}",":,[,{,],],},<EOF>",189))
    def test_separator10(self):
        self.assertTrue(TestLexer.test(":{[,][][}]",":,{,[,,,],[,],[,},],<EOF>",190))
# test keyword
    def test_keyword1(self):
        self.assertTrue(TestLexer.test("if\tcontinue;break{class}","if,continue,;,break,{,class,},<EOF>",191))
    def test_keyword2(self):
        self.assertTrue(TestLexer.test("while(static)[final]\fto\rdownto","while,(,static,),[,final,],to,downto,<EOF>",192))
    def test_keyword3(self):
        self.assertTrue(TestLexer.test("for","for,<EOF>",193))
    # def test_keyword4(self):
    #     self.assertTrue(TestLexer.test("continue","continue,<EOF>",194))    
    # def test_keyword5(self):
    #     self.assertTrue(TestLexer.test("break","break,<EOF>",195))
    # def test_keyword6(self):
    #     self.assertTrue(TestLexer.test("return","return,<EOF>",196))
    # def test_keyword7(self):
    #     self.assertTrue(TestLexer.test("class","class,<EOF>",197))
    # def test_keyword8 (self):
    #     self.assertTrue(TestLexer.test("static","static,<EOF>",198))
    # def test_keyword9 (self):
    #     self.assertTrue(TestLexer.test("final","final,<EOF>",199))
    # def test_keyword10 (self):
    #     self.assertTrue(TestLexer.test("downto","downto,<EOF>",200)) 
# test Error:
    def test_error_token1(self):
        self.assertTrue(TestLexer.test("s2+123e2 downto to 213e93 ?","s2,+,123e2,downto,to,213e93,Error Token ?",194)) 
    def test_error_token2(self):
        self.assertTrue(TestLexer.test("/* # comment \t\n\t\r ? ~ & $ */ $$$","Error Token $",195)) 
    def test_unclose_string1(self):
        self.assertTrue(TestLexer.test(" \"  newline \n ? ~ & $ */ $$$","Unclosed String:   newline ",196)) 
    def test_unclose_string2(self):
        self.assertTrue(TestLexer.test(" \" carriage return \r ? ~ & $ */ $$$","Unclosed String:  carriage return ",197))
    def test_unclose_string3(self):
        self.assertTrue(TestLexer.test("\" EOF ","Unclosed String:  EOF ",198))  
    def test_illegal_esc1(self):
        self.assertTrue(TestLexer.test("\"  Hi Hi \c \d \a \b \y \" ","Illegal Escape In String:   Hi Hi \c",199)) 
    def test_illegal_esc2(self):
        self.assertTrue(TestLexer.test("\"  Hi Hi \\ \1 \b \y \" ","Illegal Escape In String:   Hi Hi \ ",200)) 
    # def test_illegal_esc3(self):
    #     self.assertTrue(TestLexer.test(""" "He asked me: \"Where is John?\"" ""","",208)) 

