import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_stuff(self):
        """ Test Valid Lowercase Keywords """
        self.assertTrue(TestLexer.test(
            r"""
"He ask me: \"Where is John?\""
""",
            r"He ask me: \"Where is John?\",<EOF>",
            101
        ))

    def test_2_valid_keywords(self):
        """ Test Valid Keywords """
        self.assertTrue(TestLexer.test(
            """ boolean
int float
void string
if else then
new break continue to downto
for return true
false class extends static
final
nil this
""",

            "boolean,int,float,void,string,if,else,then,new,break,continue,to,downto,for,return,true,false,class,extends,static,final,nil,this,<EOF>",
            102
        ))

    def test_3_valid_specific_characters(self):
        """ Test Specific Characters """
        self.assertTrue(TestLexer.test(
            """
+ - * / := <= >= <> = < >
( ) [ ] ; , : , .
""",

            "+,-,*,/,:=,<=,>=,<,>,=,<,>,(,),[,],;,,,:,,,.,<EOF>",
            103
        ))

    def test_4_line_comment(self):
        """ Test Line Comment """
        self.assertTrue(TestLexer.test(
            """
# This is a line comment
""",

            "<EOF>",
            104
        ))

    def test_5_block_comment(self):
        """ Test Block Comment """
        self.assertTrue(TestLexer.test(
            """
/* Comment with multiple lines
    Hello comments
*/
""",

            "<EOF>",
            105
        ))

    def test_6_block_comment(self):
        """ Test Block Comment """
        self.assertTrue(TestLexer.test(
            """
/* This is a block comment */
/*
    Comment multiple lines
*/
""",

            "<EOF>",
            106
        ))

    def test_7_mix_comment(self):
        """ Test Mix Comment """
        self.assertTrue(TestLexer.test(
            """
/* This is a block comment */
# This is a line comment
/* Comment with multiple lines
    Hello comments
*/
/*
    Comment multiple lines
*/
/* nest comments /*
block 
comment
    # inline comment
*/
# inline comment /* block 
comment */
*/
""",

            "comment,*,/,*,/,<EOF>",
            107
        ))

    def test_8_int_lit(self):
        """ Test Integer Literal """
        self.assertTrue(TestLexer.test(
            r"""
0 1 2 3 4 123 123456789
""",

            "0,1,2,3,4,123,123456789,<EOF>",
            108
        ))

    def test_9_float_lit(self):
        """ Test Float Literal """
        self.assertTrue(TestLexer.test(
            r"""
9.0 12e8 1. 0.33E-3 128e+42
""",

            "9.0,12e8,1.,0.33E-3,128e+42,<EOF>",
            109
        ))

    def test_10_string_lit(self):
        """ Test String Literal """
        self.assertTrue(TestLexer.test(
            r"""
""      "A"     
"Mulitiple Characters"
""",

            ',A,Mulitiple Characters,<EOF>',
            110
        ))

    def test_11_id(self):
        """ Test Identifiers """
        self.assertTrue(TestLexer.test(
            r"""
a abc a123 a_ a_bc a_bc123 a_123 a_123bc a_bc_123
_ _abc _123 _abc123 _abc_123 _123_abc
__ ____ ____123____
abc ABC aBC Abc _ABC __ABc __123ABc
h98f394__VWT_b5_VT_YGU87udhf__T_
""",

            "a,abc,a123,a_,a_bc,a_bc123,a_123,a_123bc,a_bc_123,_,_abc,_123,_abc123,_abc_123,_123_abc,__,____,____123____,abc,ABC,aBC,Abc,_ABC,__ABc,__123ABc,h98f394__VWT_b5_VT_YGU87udhf__T_,<EOF>",
            111
        ))

    def test_12_invalid_id(self):
        """ Test Invalid Identifiers """
        self.assertTrue(TestLexer.test(
            r"""
123abc 123_abc 00000123_123abc
""",

            "123,abc,123,_abc,00000123,_123abc,<EOF>",
            112
        ))

    def test_13_invalid_comment(self):
        """ Test Invalid Comments """
        self.assertTrue(TestLexer.test(
            r"""
multiple lines
/ block comment missing **/
/* comment without close
 comment not correct close */
""",

            "multiple,lines,/,block,comment,missing,*,*,/,<EOF>",
            113
        ))

    def test_14_invalid_float(self):
        """ Test Invalid Float Literal """
        self.assertTrue(TestLexer.test(
            """
e-12 e+12 . 1e 12e 12.05e .05e ee e01 .12 143e
""",

            "e,-,12,e,+,12,.,1,e,12,e,12.05,e,.,05,e,ee,e01,.,12,143,e,<EOF>",
            114
        ))

    def test_15_arr_lit(self):
        """ Test Array Literal """
        self.assertTrue(TestLexer.test(
            """
int[5] a;
{1, 2, 3}
{2.3, 4.2, 102e3}
""",

            "int,[,5,],a,;,{,1,,,2,,,3,},{,2.3,,,4.2,,,102e3,},<EOF>",
            115
        ))

    def test_16_unclose_without_endline(self):
        """ Test Unclose String without endline """
        self.assertTrue(TestLexer.test(
            """  " hello lexer """,

            "Unclosed String:  hello lexer ",
            116
        ))

    def test_17_unclose_with_endline(self):
        """ Test Unclose String with endline """
        self.assertTrue(TestLexer.test(
            r"""
" abcxyz
""",

            r"""Unclosed String:  abcxyz""",
            117
        ))

    def test_18_escape(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.test(
            r"""
" abc \n xyz "
" abc \\n xyz "
""",

            r''' abc \n xyz , abc \\n xyz ,<EOF>''',
            118
        ))

    def test_19_escape(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.test(
            r"""
" hello lexer \t "     asdf 
""",

            r' hello lexer \t ,asdf,<EOF>',
            119
        ))

    def test_20_escape(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.test(
            r"""
"Backspace  \b"
""",

            r'Backspace  \b,<EOF>',
            120
        ))

    def test_21_escape(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.test(
            r"""
"Formfeed   \f"
""",

            r'Formfeed   \f,<EOF>',
            121
        ))

    def test_22_escape(self):
        """ Test Escape """
        self.assertTrue(TestLexer.test(
            r"""
"Return     \r"
""",

            r'''Return     \r,<EOF>''',
            122
        ))

    def test_23_escape(self):
        """ Test Escape """
        self.assertTrue(TestLexer.test(
            r"""
"Newline    \n"
""",

            r'''Newline    \n,<EOF>''',
            123
        ))

    def test_24_unclose_multi_lines(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.test(
            r"""
"Newline
    multiple lines
"           """,

            r'''Unclosed String: Newline''',
            124
        ))

    def test_25_escape(self):
        """ Test Escape """
        self.assertTrue(TestLexer.test(
            r"""
"Tab        \t"
""",

            r'Tab        \t,<EOF>',
            125
        ))

    def test_26_escape(self):
        """ Test Escape """
        self.assertTrue(TestLexer.test(
            r"""
"Backslash  \\ "
""",

            r"Backslash  \\ ,<EOF>",
            126
        ))

    def test_27_illegal(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.test(
            r"""
Illegal: "\a"
""",

            r'''Illegal,:,Illegal Escape In String: \a''',
            127
        ))

    def test_28_illegal(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.test(
            r"""
" Hi Hi \c \d "
""",

            "Illegal Escape In String:  Hi Hi \c",
            128
        ))

    def test_29_illegal(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.test(
            r"""
" Hi Hi \m\n\c\s\d\\f "
""",

            "Illegal Escape In String:  Hi Hi \m",
            129
        ))

    def test_30_nevermind(self):
        """ Test Nevermind :) """
        self.assertTrue(TestLexer.test(
            r"""
" asdf ` asdf"
""",

            " asdf ` asdf,<EOF>",
            130
        ))

    def test_31_err_str(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            r"""
" abc \7 xyz "
""",

            r"Illegal Escape In String:  abc \7",
            131
        ))

    def test_32_escape_singlequote(self):
        """ Test Escape """
        self.assertTrue(TestLexer.test(
            r"""
" abc \' xyz "
""",

            r"Illegal Escape In String:  abc \'",
            132
        ))

    def test_33_escape_doublequote(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.test(
            r"""
" abc \" xyz " ghi
""",

            r" abc \" xyz ,ghi,<EOF>",
            133
        ))

    def test_34_illegal(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            r"""
"abc" 123 __123 "abc xyz"
" abc\m "
""",

            "abc,123,__123,abc xyz,Illegal Escape In String:  abc\m",
            134
        ))

    def test_35_err_tok(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            """
!== != &
""",

            "!=,=,!=,Error Token &",
            135
        ))

    def test_36_err_tok(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            """
^ % $ # ... \
""",

            "^,%,Error Token $",
            136
        ))

    def test_37_err_tok(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            r"""
a := a & 1
""",

            "a,:=,a,Error Token &",
            137
        ))

    def test_38_err_tok(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            r"""
xyz
$a = 5
""",

            "xyz,Error Token $",
            138
        ))

    def test_39_err_tok(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            r"""
int a = a|b;
""",

            "int,a,=,a,Error Token |",
            139
        ))

    def test_40_num_leading_0(self):
        """ Test Number leading 0 """
        self.assertTrue(TestLexer.test(
            r"""
1234 0000001234 0000043123
""",

            "1234,0000001234,0000043123,<EOF>",
            140
        ))

    def test_41_num_leading_0(self):
        """ Test Real Leading 0 """
        self.assertTrue(TestLexer.test(
            r"""
00001.1111000000
0e-4
000000001e-40000
""",

            "00001.1111000000,0e-4,000000001e-40000,<EOF>",
            141
        ))

    def test_42_illegal(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            r"""
"abc - xyz"
"abc \ xyz"
""",

            "abc - xyz,Illegal Escape In String: abc \ ",
            142
        ))

    def test_43_illegal(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            r"""
"abc - xyz"
"abc \yyz"
""",

            "abc - xyz,Illegal Escape In String: abc \y",
            143
        ))

    def test_44_escape_backsplash_spacing(self):
        """ Test Escape """
        self.assertTrue(TestLexer.test(
            r"""
"abc \\ xyz"
""",

            r"abc \\ xyz,<EOF>",
            144
        ))

    def test_45_escape_backsplash_trim(self):
        """ Test Escape """
        self.assertTrue(TestLexer.test(
            r"""
"\\"
""",

            r'''\\,<EOF>''',
            145
        ))

    def test_46_escape_backsplash_tail_spacing(self):
        """ Test Escape """
        self.assertTrue(TestLexer.test(
            r"""
"\\ "
""",

            r"\\ ,<EOF>",
            146
        ))

    def test_47_unclose_use_escape(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.test(
            r"""
"\"
""",

            r"""Unclosed String: \"""",
            147
        ))

    def test_48_escape(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.test(
            r"""
"\""
""",

            r"""\",<EOF>""",
            148
        ))

    def test_49_unclose_with_invalid_close(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.test(
            """
s = "string 
"
a = 4
g = 9
""",

            '''s,=,Unclosed String: string ''',
            149
        ))

    def test_50_complex(self):
        """ Test Complex Function """
        self.assertTrue(TestLexer.test(
            r"""
float a, b, c;
boolean x, y, z;
int g, h, y;
void nty() {
    readLine();
    # This is readLine()
    fs := readStdin();

    for (a < b)
        for i := 4 downto -5 do h := 6;
        if i > 6 then return 0;
    return 1;
}
    /*
        =======================================
        Comment here
        =======================================
    */
""",

            r"float,a,,,b,,,c,;,boolean,x,,,y,,,z,;,int,g,,,h,,,y,;,void,nty,(,),{,readLine,(,),;,fs,:=,readStdin,(,),;,for,(,a,<,b,),for,i,:=,4,downto,-,5,do,h,:=,6,;,if,i,>,6,then,return,0,;,return,1,;,},<EOF>",
            150
        ))

    def test_51_complex(self):
        """ Test Complex Function """
        self.assertTrue(TestLexer.test(
            r"""
int foo();
    while false{
        hard_work();
			if true then break;
		}
""",

            r"int,foo,(,),;,while,false,{,hard_work,(,),;,if,true,then,break,;,},<EOF>",
            151
        ))

    def test_52_unclose_eof(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.test(
            r"""
s = "abc""",

            r"s,=,Unclosed String: abc",
            152
        ))

    def test_53_unclose_newline(self):
        """ Test Unclosed """
        self.assertTrue(TestLexer.test(
            r"""
s = "abc                   ;
a = "xyz"
""",

            r"""s,=,Unclosed String: abc                   ;""",
            153
        ))

    def test_54_complex(self):
        """ Test Complex Function """
        self.assertTrue(TestLexer.test(
            r"""
procedure foo();
begin
    while 1<2<3<4<5 do ok();
end
""",

            r"procedure,foo,(,),;,begin,while,1,<,2,<,3,<,4,<,5,do,ok,(,),;,end,<EOF>",
            154
        ))

    def test_55_complex(self):
        """ Test Complex Function """
        self.assertTrue(TestLexer.test(
            r"""
procedure foo();
begin
    with a: string do ok();
end
""",

            r"procedure,foo,(,),;,begin,with,a,:,string,do,ok,(,),;,end,<EOF>",
            155
        ))

    def test_56_complex(self):
        """ Test Complex Function """
        self.assertTrue(TestLexer.test(
            r"""
procedure foo();
begin
    with a,b,c,d:string; f:integer do ok();
end
""",

            r"procedure,foo,(,),;,begin,with,a,,,b,,,c,,,d,:,string,;,f,:,integer,do,ok,(,),;,end,<EOF>",
            156
        ))

    def test_57_complex(self):
        """ Test Complex Function """
        self.assertTrue(TestLexer.test(
            r"""
procedure foo();
var a: real;
begin
    for i := 1 to 10 do begin
        for j := i downto 1 do
            if (i + j) mod 2 = 1 then continue break;
    end
end
""",

            r"procedure,foo,(,),;,var,a,:,real,;,begin,for,i,:=,1,to,10,do,begin,for,j,:=,i,downto,1,do,if,(,i,+,j,),mod,2,=,1,then,continue,break,;,end,end,<EOF>",
            157
        ))

    def test_58_complex(self):
        """ Test Complex Function """
        self.assertTrue(TestLexer.test(
            r"""
procedure foo();
begin
    a := a[d < y(5 > 3) + 3 * n(12)] := 5[3] := 3[2] := b;
end
""",

            r"procedure,foo,(,),;,begin,a,:=,a,[,d,<,y,(,5,>,3,),+,3,*,n,(,12,),],:=,5,[,3,],:=,3,[,2,],:=,b,;,end,<EOF>",
            158
        ))

    def test_59_complex(self):
        """ Test Complex Function """
        self.assertTrue(TestLexer.test(
            r"""
procedure foo();
begin
    s = "asdfghjklwertyuio  xcvbnm,dfghjkl;567"
    t = " dfghjk\n\t\rsdfghjkl\bsdfghjklfgh    "
    y = "dfghjkl 


    ";
end
""",

            r"""procedure,foo,(,),;,begin,s,=,asdfghjklwertyuio  xcvbnm,dfghjkl;567,t,=, dfghjk\n\t\rsdfghjkl\bsdfghjklfgh    ,y,=,Unclosed String: dfghjkl """,
            159
        ))

    def test_60_complex(self):
        """ Test Complex Function """
        self.assertTrue(TestLexer.test(
            r"""
procedure foo();
begin
    s = "asdfghjklwertyuio  xcvbnm,dfghjkl;567"
    t = " dfghjk\n\t\rsdfghjkl\bsdfghjklfgh    "
    y = "dfghjkl 


    ";
    begin end
    ok();
    break;
end
""",

            r"""procedure,foo,(,),;,begin,s,=,asdfghjklwertyuio  xcvbnm,dfghjkl;567,t,=, dfghjk\n\t\rsdfghjkl\bsdfghjklfgh    ,y,=,Unclosed String: dfghjkl """,
            160
        ))

    def test_61_float_lit(self):
        """ Test Float Number """
        self.assertTrue(TestLexer.test(
            r"""
12.
12.e05
12.e-05
12.05e05
12.05e-05
12.05
.05
.05e05
.05e-05
""",

            r"12.,12.e05,12.e-05,12.05e05,12.05e-05,12.05,.,05,.,05e05,.,05e-05,<EOF>",
            161
        ))

    def test_62_er_tok(self):
        """ Test */* """
        self.assertTrue(TestLexer.test(
            r"""
*/*123*/*
""",

            "*,*,<EOF>",
            162
        ))

    def test_63_err_tok(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            r"""
\\ // / \
""",

            "\,\,/,/,/,\,<EOF>",
            163
        ))

    def test_64_err_tok(self):
        """ Test Error Token @ """
        self.assertTrue(TestLexer.test(
            r"""
@1
""",

            r"Error Token @",
            164
        ))

    def test_65_err_tok(self):
        """ Test String @ """
        self.assertTrue(TestLexer.test(
            r"""
"@1"
""",

            "@1,<EOF>",
            165
        ))

    def test_66_escape(self):
        """ Test ' " """
        self.assertTrue(TestLexer.test(
            r"""
"\"\"\" \' \' "
""",

            r"Illegal Escape In String: \"\"\" \'",
            166
        ))

    def test_67_err_tok(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            r"""
%%%%%%
""",

            r"%,%,%,%,%,%,<EOF>",
            167
        ))

    def test_68_escape(self):
        """ Test \t """
        self.assertTrue(TestLexer.test(
            r"""
"\t\t\t\t\t\t\t\t"
""",

            r"\t\t\t\t\t\t\t\t,<EOF>",
            168
        ))

    def test_69_escape(self):
        """ Test \n  """
        self.assertTrue(TestLexer.test(
            r"""
"\n\n\n\n\n\n\n\n\n"
""",

            r"\n\n\n\n\n\n\n\n\n,<EOF>",
            169
        ))

    def test_70_escape(self):
        """ Test \r """
        self.assertTrue(TestLexer.test(
            r"""
\r\r\r\r\r\r\r\r\r\
""",

            """\,r,\,r,\,r,\,r,\,r,\,r,\,r,\,r,\,r,\,<EOF>""",
            170
        ))

    def test_71_err_tok(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            r"""
\x\y\z "\."
""",

            r"""\,x,\,y,\,z,Illegal Escape In String: \.""",
            171
        ))

    def test_72_auto_gen(self):
        """ Test Automatically Generated Code """
        self.assertTrue(TestLexer.test(
            """
# [,<>,( k6301 with begin,],true
+ - integer N0699 + > then L09e7 >= real > >= , ] <> * eb142 > integer / while boolean procedure false
/* false procedure Z2262,do,G9a7c end e46e2,+,break*/
""",

            "+,-,integer,N0699,+,>,then,L09e7,>=,real,>,>=,,,],<,>,*,eb142,>,integer,/,while,boolean,procedure,false,<EOF>",
            172
        ))

    def test_73_auto_gen(self):
        """ Test Automatically Generated Code """
        self.assertTrue(TestLexer.test(
            """
# :=,+,> Wcb78 ; false,else,>=
and real ] p5c22 ) array break w1ca2 array mod while , var div to + D989c := - function downto <= + ,
/* for false hb039,string,N6d32 not ua0fa,while,var*/
""",

            "and,real,],p5c22,),array,break,w1ca2,array,mod,while,,,var,div,to,+,D989c,:=,-,function,downto,<=,+,,,<EOF>",
            173
        ))

    def test_74_auto_gen(self):
        """ Test Automatically Generated Code """
        self.assertTrue(TestLexer.test(
            """
# (,true,[ acb40 mod for,),with
= boolean .. p104c ] function do z71ae of < begin if break with of procedure b4169 break - of = = function div
/* <= : a41aa,while,m8bcd .. E8869,,,string*/
""",

            "=,boolean,.,.,p104c,],function,do,z71ae,of,<,begin,if,break,with,of,procedure,b4169,break,-,of,=,=,function,div,<EOF>",
            174
        ))

    def test_75_auto_gen(self):
        """ Test Automatically Generated Code """
        self.assertTrue(TestLexer.test(
            """
# or,(,procedure d7bab true and,,,>=
do >= div nae0b ) else := W12e2 ( for / > if false <= <= pdb8e := + := <> .. to /
/* div > b8286,function,u0f83 .. Iaffa,,,**/
""",

            "do,>=,div,nae0b,),else,:=,W12e2,(,for,/,>,if,false,<=,<=,pdb8e,:=,+,:=,<,>,.,.,to,/,<EOF>",
            175
        ))

    def test_76_auto_gen(self):
        """ Test Automatically Generated Code """
        self.assertTrue(TestLexer.test(
            """
# string,array,break Vbb79 break <>,(,<>
: .. do n1afd then - of Be562 ] end * > .. string * + W0977 var function else or mod if not
/* boolean real M89a9,do,yc501 , x38af,(,/*/
""",

            ":,.,.,do,n1afd,then,-,of,Be562,],end,*,>,.,.,string,*,+,W0977,var,function,else,or,mod,if,not,<EOF>",
            176
        ))

    def test_77_auto_gen(self):
        """ Test Automatically Generated Code """
        self.assertTrue(TestLexer.test(
            """
# /,<=,>= af9f4 , ,,and,mod
- [ string O902e boolean , and y680b string + > , else <> else = a5cbe := return end var boolean [ +
/* <= string Z1f1f,return,s847c with Xa8a2,continue,integer*/
""",

            "-,[,string,O902e,boolean,,,and,y680b,string,+,>,,,else,<,>,else,=,a5cbe,:=,return,end,var,boolean,[,+,<EOF>",
            177
        ))

    def test_78_auto_gen(self):
        """ Test Automatically Generated Code """
        self.assertTrue(TestLexer.test(
            """
# and,:=,false C34d9 = else,<,..
do var [ oa6ec - - .. vc463 var <= , var end ) - [ nedb5 var * - <= * * then
/* / >= Q0dab,mod,qc5bc [ l4ebc,or,string*/
""",

            "do,var,[,oa6ec,-,-,.,.,vc463,var,<=,,,var,end,),-,[,nedb5,var,*,-,<=,*,*,then,<EOF>",
            178
        ))

    def test_79_auto_gen(self):
        """ Test Automatically Generated Code """
        self.assertTrue(TestLexer.test(
            """
# ),-,return Rb4ac true >=,,,not
procedure , with Wd12f boolean >= [ b308a array ) ) or * for , >= n5d7e , , or <= , + <
/* := to Dd5f9,<>,l8df4 - ha663,>=,[*/
""",

            "procedure,,,with,Wd12f,boolean,>=,[,b308a,array,),),or,*,for,,,>=,n5d7e,,,,,or,<=,,,+,<,<EOF>",
            179
        ))

    def test_80_auto_gen(self):
        """ Test Automatically Generated Code """
        self.assertTrue(TestLexer.test(
            """
# >=,<=,for of8ae * :=,then,>=
- + false P4366 ; * , l84bc , > : array procedure [ / while Va93a boolean and integer function - , false
/* function , Wbffd,),y6349 else w7e53,(,)*/
""",

            "-,+,false,P4366,;,*,,,l84bc,,,>,:,array,procedure,[,/,while,Va93a,boolean,and,integer,function,-,,,false,<EOF>",
            180
        ))

    def test_81_auto_gen(self):
        """ Test Automatically Generated Code """
        self.assertTrue(TestLexer.test(
            """
# or,,,>= Y3137 := :,/,then
: * do b3084 function .. array X35a7 real <= .. continue < function continue := Zc3a0 if else <> of then function and
/* begin not Eea5a,then,D1682 and S7555,=,continue*/
""",

            ":,*,do,b3084,function,.,.,array,X35a7,real,<=,.,.,continue,<,function,continue,:=,Zc3a0,if,else,<,>,of,then,function,and,<EOF>",
            181
        ))

    def test_82_auto_gen(self):
        """ Test Automatically Generated Code """
        self.assertTrue(TestLexer.test(
            """
# downto,-,= kf07d string :,real,string
, return not C4462 <> function true n69bd mod with var then < and continue and M615c <= > [ - ; - string
/* real < u5368,:,Z36b0 string dcbf1,;,<>*/
""",

            ",,return,not,C4462,<,>,function,true,n69bd,mod,with,var,then,<,and,continue,and,M615c,<=,>,[,-,;,-,string,<EOF>",
            182
        ))

    def test_83_auto_gen(self):
        """ Test Automatically Generated Code """
        self.assertTrue(TestLexer.test(
            """
# and,<=,return v415f ( div,and,or
+ , or b328b = <= ) G39be : then else break / * = [ Qd057 ] var break * >= do >
/* end , b60f1,>=,dd28e , dd3ab,string,of*/
""",

            "+,,,or,b328b,=,<=,),G39be,:,then,else,break,/,*,=,[,Qd057,],var,break,*,>=,do,>,<EOF>",
            183
        ))

    def test_84_auto_gen(self):
        """ Test Automatically Generated Code """
        self.assertTrue(TestLexer.test(
            """
# then,return,< e0352 : ,,of,>=
return > array Qbfb5 , function var M274c if <= ; function or <= to = x4045 procedure to <> ] ( else *
/* false of Bcdfa,<=,J490b begin J6626,<=,break*/
""",

            "return,>,array,Qbfb5,,,function,var,M274c,if,<=,;,function,or,<=,to,=,x4045,procedure,to,<,>,],(,else,*,<EOF>",
            184
        ))

    def test_85_auto_gen(self):
        """ Test Automatically Generated Code """
        self.assertTrue(TestLexer.test(
            """
# ],],* ae0bc not mod,return,,
function < + Qefbe and ; of o366c false array else < > and downto for J4981 : <> return = for then ..
/* of break h80bb,or,bfa18 ) W6bd3,real,<*/
""",

            "function,<,+,Qefbe,and,;,of,o366c,false,array,else,<,>,and,downto,for,J4981,:,<,>,return,=,for,then,.,.,<EOF>",
            185
        ))

    def test_86_auto_gen(self):
        """ Test Automatically Generated Code """
        self.assertTrue(TestLexer.test(
            """
# <>,while,] jb8be true for,,,<=
else and * x68ae .. continue end c1976 to boolean := or function , * , Y0db2 and <= of else ) mod :
/* else for j5904,true,weadc , e6f92,..,;*/
""",

            "else,and,*,x68ae,.,.,continue,end,c1976,to,boolean,:=,or,function,,,*,,,Y0db2,and,<=,of,else,),mod,:,<EOF>",
            186
        ))

    def test_87_auto_gen(self):
        """ Test Automatically Generated Code """
        self.assertTrue(TestLexer.test(
            """
# :,..,<= fef8b / div,=,continue
return ) then lb1e7 true mod , Ve4b7 , := true do begin or >= >= v8b5e := for <> >= or ) [
/* continue ) p0698,*,Oc0d5 .. c9970,,,downto*/
""",

            "return,),then,lb1e7,true,mod,,,Ve4b7,,,:=,true,do,begin,or,>=,>=,v8b5e,:=,for,<,>,>=,or,),[,<EOF>",
            187
        ))

    def test_88_auto_gen(self):
        """ Test Automatically Generated Code """
        self.assertTrue(TestLexer.test(
            """
# <=,var,> B2bb9 else real,boolean,return
and false then edaa6 integer , break P278e if <> [ * / function while div d74f0 > not <> , ] begin /
/* ; continue Feecf,false,Hc361 <> mf34e,else,or*/
""",

            "and,false,then,edaa6,integer,,,break,P278e,if,<,>,[,*,/,function,while,div,d74f0,>,not,<,>,,,],begin,/,<EOF>",
            188
        ))

    def test_89_auto_gen(self):
        """ Test Automatically Generated Code """
        self.assertTrue(TestLexer.test(
            """
# begin,),] lc648 ; not,(,/
, + var Cd03e else to do xd695 ( string of ; end : ] .. f5179 >= + + [ = ; <=
/* or := d3d6a,begin,I6a5a not Cf2e7,/,<=*/
""",

            ",,+,var,Cd03e,else,to,do,xd695,(,string,of,;,end,:,],.,.,f5179,>=,+,+,[,=,;,<=,<EOF>",
            189
        ))

    def test_90_auto_gen(self):
        """ Test Automatically Generated Code """
        self.assertTrue(TestLexer.test(
            """
# (,while,: H050f end return,+,[
, / or M3ff3 while / for y848d while downto - + , ] ) >= Hdcb8 false / for > not and (
/* ( [ bc9ca,],B1ebd ; w28cd,procedure,if*/
""",

            ",,/,or,M3ff3,while,/,for,y848d,while,downto,-,+,,,],),>=,Hdcb8,false,/,for,>,not,and,(,<EOF>",
            190
        ))

    def test_91_auto_gen(self):
        """ Test Automatically Generated Code """
        self.assertTrue(TestLexer.test(
            """
# var,+,, M6af4 , with,=,-
to >= ( Q51ca : ] to Ie94f for , integer ; , for return if Bbfd7 + real <> if do downto :
/* * / e4686,end,rf588 > R8121,-,,*/
""",

            "to,>=,(,Q51ca,:,],to,Ie94f,for,,,integer,;,,,for,return,if,Bbfd7,+,real,<,>,if,do,downto,:,<EOF>",
            191
        ))

    def test_92_illegal_char_in_string(self):
        """ Test Illegal Character in String """
        self.assertTrue(TestLexer.test(
            r"""
    " abc \\ xyz "
""",

            r" abc \\ xyz ,<EOF>",
            192
        ))

    def test_93_illegal_char_in_string(self):
        """ Test Illegal Character in String """
        self.assertTrue(TestLexer.test(
            """
    " abc "  xyz "
""",

            " abc ,xyz,Unclosed String: ",
            193
        ))

    def test_94_illegal_char_in_string(self):
        """ Test Illegal Character in String """
        self.assertTrue(TestLexer.test(
            """
    " abc \r  xyz "
""",

            "Unclosed String:  abc ",
            194
        ))

    def test_95_legal_char_in_string(self):
        """ Test Legal Character in String """
        self.assertTrue(TestLexer.test(
            """
    " abc \f  xyz "
""",

            " abc   xyz ,<EOF>",
            195
        ))

    def test_96_illegal_char_in_string(self):
        """ Test Illegal Character in String """
        self.assertTrue(TestLexer.test(
            """
    " abc \n  xyz "
""",

            "Unclosed String:  abc ",
            196
        ))

    def test_97_legal_char_in_string(self):
        """ Test Legal Character in String """
        self.assertTrue(TestLexer.test(
            """
    " abc \t  xyz "
""",

            " abc 	  xyz ,<EOF>",
            197
        ))

    def test_98_legal_char_in_string(self):
        """ Test Legal Character in String """
        self.assertTrue(TestLexer.test(
            """
    " abc \b  xyz "
""",

            " abc   xyz ,<EOF>",
            198
        ))

    def test_99_illegal_char_in_string(self):
        """ Test Illegal Character in String """
        self.assertTrue(TestLexer.test(
            """
    " abc \k  xyz "
""",

            "Illegal Escape In String:  abc \k",
            199
        ))

    def test_100_uncomplete_comment(self):
        """ Test Uncomplete Comment """
        self.assertTrue(TestLexer.test(
            r"""
/*=====================
Comment here
====================={{{{{{}}}}}}}}}}}
""",
            r"/,*,==,==,==,==,==,==,==,==,==,==,=,Comment,here,==,==,==,==,==,==,==,==,==,==,=,{,{,{,{,{,{,},},},},},},},},},},},<EOF>",
            200
        ))