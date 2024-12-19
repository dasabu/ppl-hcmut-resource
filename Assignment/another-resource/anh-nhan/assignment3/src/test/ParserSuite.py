import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_1_attr_decl(self):
        """ Test Attribute Declare 1 line 1 var """
        input = r"""
class test {
	static void main() {
		int a;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_2_attr_decl(self):
        """ Test Attribute Declare 1 line n var """
        input = r"""
class test {
	void main() {
	float a,b,c;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_3_attr_decl(self):
        """ Test Attribute Declare n line """
        input = r"""
class test {
	int a, b, c;
	float x, y;
	string z = "abc";
	static boolean d = "true";
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_4_attr_decl(self):
        """ Test Array Declare """
        input = r"""
class test {
	void main() {
		int[5] a;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_5_attr_decl(self):
        """ Test Array with Assignment Expression """
        input = r"""
class test {
	void main() {
		a[0] := 5;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_6_attr_decl(self):
        """ Test Attribute Declare """
        input = r"""
class test {
	void main() {
		iNt a;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_7_func_decl(self):
        """ Test Function Declare """
        input = r"""
class test {
	void main() {
		float a;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_8_func_decl(self):
        """ Test Function Declare with Parameter List """
        input = r"""
class test {
	void foo(int a,b;float c) {
	string _str_,o,c;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_9_func_decl(self):
        """ Test Function Declare """
        input = r"""
class test {
	int foo(){
		int a,b;
		float c,d;
		string e,f;
		boolean k,h;
		return a;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_10_attr_func_decl(self):
        """ Test Function and Attribute Declare """
        input = r"""
class test {
	void foo() {
		int x;
		float y;
		string[1000] str;
	}
	int x;
	float y;
	string[1000] str;
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_11_assign(self):
        """ Test Assign Statment """
        input = r"""
class test {
	int foo() {
		this.aPI := 3.14;
		value := x.foo(5);
		l[3] := value * 2;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_12_assign(self):
        """ Test Assign Statment """
        input = r"""
class test {
	int foo() {
		a[3+x.foo(2)] := a[b[2]] +3;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_13_assign(self):
        """ Test Assign Statment """
        input = r"""
class test {
	int foo(){
		x.b[2] := x.m()[3];
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_14_assign(self):
        """ Test Assign Statment """
        input = r"""
class test {
	void main() {
		s := r*r*this.myAPI;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_15_assign(self):
        """ Test Assign Statment """
        input = r"""
class test {
	int foo(){
    a[3+x] := a[b[f+y[2]-h[t[5+j]] * 4]] + 3;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_16_assoc(self):
        """ Test Associative """
        input = r"""
class test {
	int foo(){
    a := b + 2 + n + 5 - g - 9;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_17_assoc(self):
        """ Test Associative """
        input = r"""
class test {
	int foo(){
    a := b + 2 + n && 4 + 5 - g || 2 - 9;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_18_assoc(self):
        """ Test Associative """
        input = r"""
class test {
	int foo(){
    a := b / 2 * n / 4 && 5 % g || 2 * 9 / 4 % 2;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_19_precedence(self):
        """ Test Precedence """
        input = r"""
class test {
	int foo(){
    a := b && c && !d || e && !f && (g || !k);
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_20_precedence(self):
        """ Test Precedence """
        input = r"""
class test {
	int foo(){
    a :=  F * G % 5 + (I || L && N + Y || Q * !P) && 6 * 5 + O %  (5 % T) ;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_21_assoc(self):
        """ Test Associative """
        input = r"""
class test {
	int foo(){
    a := b ^ c ;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_22_arr_value_type(self):
        """ Test Array Value Type """
        input = r"""
class test {
	int foo() {
		int[3] a = {5, 6, true};
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_23_arr_value_type(self):
        """ Test Array Value Type """
        input = r"""
class test {
		int[3] a = {5, 6, true};
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_24_stmt(self):
        """ Test Return Statement """
        input = r"""
class Rectangle extends Shape {
	float getArea(){
		return this.length*this.width;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_25_keyword(self):
        """ Test True False Keywords """
        input = r"""
class Shape {
	static final int numOfShape = 0;
	final int immuAttribute = 0;
	float length,width;
	static int getNumOfShape() {
		return numOfShape;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_26_if(self):
        """ Test If Statement in Class """
        input = r"""
class test {
    if a == 1 then break;
}
"""
        expect = r"Error on line 3 col 4: if"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_27_if(self):
        """ Test If Statement """
        input = r"""
class test {
	int foo() {
    if a == 1 then break;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_28_if(self):
        """ Test If Statement """
        input = r"""
class test {
	int foo() {
    if a == 1 then
        a := 5;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_29_if(self):
        """ Test If Statement """
        input = r"""
class test {
	int foo() {
		if true then continue;
		else break;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_30_if(self):
        """ Test If Statement """
        input = r"""
class test {
	int a;
	int foo() {
		if a == 1 then a := 1; else a := 2;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_31_if(self):
        """ Test If Statement """
        input = r"""
class test {
	int foo() {
		if a == 1 then
        if b > 3 then
            c := 5;
        else 
            d := 1;
    else
        e := 0;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_32_if(self):
        """ Test If Statement """
        input = r"""
class test {
	int foo() {
		if a == 1 then continue;
        if b > 3 then c := 5;
        else d := 1;
        if e < 4 then break;
     else
        if h > 5 then c :=1; else c :=2;
        g := 5;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_33_for(self):
        """ Test for Statment """
        input = r"""
class test {
	int foo() {
		for i := 1 to 100 do {
		return z;
		Intarray[5] := i + 1;
		}
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_34_for(self):
        """ Test for Statement """
        input = r"""
class test {
	int foo() {
		for x := 5 downto 2 do
		break;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_35_for(self):
        """ Test For Statment """
        input = r"""
class test {
	int foo() {
		for i := 1 to 10 do continue;
        for j := i downto 1 do
            if (i + j) % 2 == 1 then break;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_36_comment(self):
        """ Test Comment Line in Block """
        input = """
class test{
	void main() {
    # Line Comment
    /* Block Comment */
	}
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_37_comment(self):
        """ Test Comment Block in Line """
        input = """
class test{
	void main() {
		# Line Comment { Block Comment }
		# Line Comment /* Block Comment */
	}
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_38_method_invo(self):
        """ Test Method Invocation """
        input = r"""
class test {
	int gh() {
		this.foo();
		this.abc();
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_39_complex(self):
        """ Test Complex Code """
        input = r"""
class test {
	int foo() {
		float a, b, c;
		boolean x, y, z;
    int g, h, y;
    this.foo1();
    /* This is foo()*/
    this.foo2();

    for x := a to b
		do break;
    return 1;
    /*
        =======================================
        Comment here
        =======================================
    */
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_40_complex(self):
        """ Test Success Code Statment """
        input = r"""
class test {
	float a;
	int foo() {
		for i := 1 to 10 do this.sth();
			for j := i downto 1 do
				if (i + j) % 2 == 1 then break;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_41_err_delc(self):
        """ Test Missing ; """
        input = r"""
int a
"""
        expect = r"Error on line 2 col 0: int"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_42_err_delc(self):
        """ Test Missing ; """
        input = r"""
int a"""
        expect = r"Error on line 2 col 0: int"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_43_err_delc(self):
        """ Test Error : """
        input = r"""
int a;;
"""
        expect = r"Error on line 2 col 0: int"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_44_err_delc(self):
        """ Test Error Type """
        input = r"""
a;
"""
        expect = r"Error on line 2 col 0: a"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_45_err_delc(self):
        """ Test Missing type """
        input = r"""
string a = "em sap be dau roi thay oi;
"""
        expect = r"Error on line 2 col 0: string"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_46_err_delc(self):
        """ Test Missing type """
        input = r"""
class test {
	toi kiet suc lam roi;
}
"""
        expect = r"Error on line 3 col 10: suc"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_47_err_delc(self):
        """ Test Wrong Syntax Var Declare """
        input = r"""
class test {
	int foo() {
		ai do lam on cuu t voi!!!!;
	}
}
"""
        expect = r"Error on line 4 col 5: do"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_48_err_delc(self):
        """ Test Wrong Syntax Var Declare """
        input = r"""
a : integer
"""
        expect = r"Error on line 2 col 0: a"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_49_err_delc(self):
        """ Test Wrong Syntax Var Declare """
        input = r"""
string a = "Mr Phung turned me into a fuckin PPL monster!!!"
"""
        expect = r"Error on line 2 col 0: string"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_50_luv_chipupu(self):
        """ Test Love Chipu """
        input = r"""
					class test {
									int foo() {									this.CHIPU();
			this.CHIPU();		this.CHIPU();					this.CHIPU();		this.CHIPU();
	this.CHIPU();						this.CHIPU();this.CHIPU();						this.CHIPU();
this.CHIPU();										this.CHIPU();											this.CHIPU();
		this.CHIPU();																							this.CHIPU();
				this.CHIPU();																			this.CHIPU();				
						this.CHIPU();															this.CHIPU();
								this.CHIPU();											this.CHIPU();
										this.CHIPU();							this.CHIPU();
												this.CHIPU();			this.CHIPU();
													this.CHIPU();this.CHIPU();
																this.CHIPU();
						}
					}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_51_complex(self):
        """ Test Random Error Code """
        input = r"""
class test {
int a;
float b;
string z;
float nml () {
    # This is PPL god
    for i:= traithang to bede do this.hahaha();
        for i := 4 downto -5 do h := 6;
    return 1;
}
    /*
        =======================================
        Comment here
        =======================================*/
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_52_complex(self):
        """ Test Random Error Code """
        input = r"""
class test {
int a;
float b;
string z;
float nml () {
    # This is PPL god
    for i:= traithang to bede do this.hahaha();
        for i := 4 downto -5 do h := 6;
    return 1;
}
    /*
        =======================================
        Comment here
        =======================================*/
int a;
float b;
string z;
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_53_complex(self):
        """ Test Random Error Code """
        input = r"""
class test {
int a;
float b;
string z;
float nml () {
    # This is PPL god
    for i:= traithang to bede do this.hahaha();
        for i := 4 downto -5 do h := 6;
    return 1;
}
    /*
        =======================================
        Comment here
        =======================================*/
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_54_complex(self):
        """ Test Random Error Code """
        input = r"""
class test {
int a;
float b;
string z;
float nml () {
    # This is PPL god
    for i:= traithang to bede do this.hahaha();
        for i := 4 downto -5 do h := 6;
    return 1;
}
    /*
        =======================================
        Comment here
        =======================================*/
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_55_complex(self):
        """ Test Random Error Code """
        input = r"""
class test {
int a;
float b;
string z;
float nml () {
    # This is PPL god
    for i:= traithang to bede do this.hahaha()
        for i := 4 downto -5 do h := 6;
    return 1;
}
    /*
        =======================================
        Comment here
        =======================================*/
}
"""
        expect = r"Error on line 9 col 8: for"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_56_complex(self):
        """ Test Random Error Code """
        input = r"""
class test {
int a;
float b;
string z;
float nml () {
    # This is PPL god
    for i:= traithang to bede do this.hahaha();
        for i := 4; downto -5 do h := 6
    return 1;
}
    /*
        =======================================
        Comment here
        =======================================*/
}
"""
        expect = r"Error on line 9 col 18: ;"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_57_complex(self):
        """ Test Random Error Code """
        input = r"""
class test {
int a;
float b;
string z;
float nml () {
    # This is PPL god
    for i:= traithang; to bede do this.hahaha();
        for i := 4 downto -5 do h := 6;
    return 1;
}
    /*
        =======================================
        Comment here
        =======================================*/
}
"""
        expect = r"Error on line 8 col 21: ;"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_58_complex(self):
        """ Test Random Error Code """
        input = r"""
class test {
int a;
float b;
string z;
float nml () {
    # This is PPL god
    for i:= traithang to bede do this.hahaha();
        for i := 4 downto -5 do h := 6;
    return 1
}
    /*
        =======================================
        Comment here
        =======================================*/
}
"""
        expect = r"Error on line 11 col 0: }"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_59_complex(self):
        """ Test Random Error Code """
        input = r"""
class test {
int a;
float b;
string z;
float nml () {
    # This is PPL god
    for i:= traithang to bede do this.hahaha();
        for i = 4 downto -5 do h := 6;
    return 1;
}
    /*
        =======================================
        Comment here
        =======================================*/
}
"""
        expect = r"Error on line 9 col 14: ="
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_60_complex(self):
        """ Test Random Error Code """
        input = r"""
class test {
int a;
float b;
string z;
float nml ) {
    # This is PPL god
    for i:= traithang to bede do this.hahaha();
        for i := 4 downto -5 do h := 6;
    return 1;
}
    /*
        =======================================
        Comment here
        =======================================*/
}
"""
        expect = r"Error on line 6 col 10: )"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_61_complex(self):
        """ Test Random Error Code """
        input = r"""
class test {
int a;
float b;
string z;
float nml () {
	int foo() {}
    # This is PPL god
    for i:= traithang to bede do this.hahaha();
        for i := 4 downto -5 do h := 6;
    return 1;
}
    /*
        =======================================
        Comment here
        =======================================*/
}
"""
        expect = r"Error on line 7 col 8: ("
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_62_complex(self):
        """ Test Random Error Code """
        input = r"""
class test {
int a;
float b;
string z;
float nml () {
    # This is PPL god
    for i:= traithang to bede do this.hahaha();
        for i := 4 downto -5 do h := 6;
    return 1;
}
    /*
        =======================================
        Comment here
        =======================================*/
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_63_complex(self):
        """ Test Random Error Code """
        input = r"""
class test {
int a;
float b;
string z;
float nml () {
    # This is PPL god
    for i:= traithang to bede do this.hahaha();
        for i := 4 downto -5 do h := 6;
    return 1;
}
    /*
        =======================================
        Comment here
        =======================================*/
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_64_compound(self):
        """ Test Compound Stmt in Compound Stmt """
        input = r"""
class test {
	int foo() {
		this.isCkChipu();
			this.isCkChipu();
				this.isCkChipu();
					this.isCkChipu();
				this.isCkChipu();
			this.isCkChipu();
		this.isCkChipu();
	this.isCkChipu();
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_65_stmt(self):
        """ Test Stmt """
        input = r"""
class test {
	int foo() {
		a := 5;
		if a ==b then this.abc; else this.hihihi;
		break;
		continue;
		return a;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_66_return_break(self):
        """ Test return break """
        input = r"""
class test {
	int foo() {
		return break;
	}
}
"""
        expect = r"Error on line 4 col 9: break"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_67_return_continue(self):
        """ Test return continue """
        input = r"""
class test {
	int foo() {
		return continue;
	}
}
"""
        expect = r"Error on line 4 col 9: continue"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_68_expr_in_para(self):
        """ Test expression in Function Declare """
        input = r"""
class test {
	int foo(int a := 5 + 6 - 7 * 8 / 9 % 10 && a) {
	}
}
"""
        expect = r"Error on line 3 col 15: :="
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_69_expr_in_para(self):
        """ Test expression in Function Declare  """
        input = r"""
class test {
	void foo(int a := 5 + 6 - 7 * 8 / 9 % 10 && a) {
	}
}
"""
        expect = r"Error on line 3 col 16: :="
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_70_example1c(self):
        """ Test Example 1"""
        input = r"""
class Example1 {
	int factorial(int n){
		if n == 0 then return 1; else return n * this.factorial(n - 1);
	}
	int a;
	void main(){
		int x;
		x := io.readInt();
		io.writeIntLn(this.factorial(x));
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_71_err_delc(self):
        """ Test Array Declare Error  """
        input = r"""
class test {
	int[6] := {1};
}
"""
        expect = r"Error on line 3 col 8: :="
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_72_err_delc(self):
        """ Test Array Declare Error  """
        input = r"""
class test {
	int[6] a,b; c;
}
"""
        expect = r"Error on line 3 col 14: ;"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_73_err_delc(self):
        """ Test Array Declare Error  """
        input = r"""
class test {
	void[6] b;
}
"""
        expect = r"Error on line 3 col 5: ["
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_74_empty_program(self):
        """ Test Empty Program """
        input = r""""""
        expect = r"Error on line 1 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_75_idx_exp(self):
        """ Test Index Expression with or else """
        input = r"""
class test {
	int foo() {
		a [(1 + 2 * 3 - 4 / 5 && 6 && -7)*(1+2+3)-(4+5*6/abc && (123))] := a[(((-5)))];
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_76_idx_exp(self):
        """ Test Index Expression """
        input = r"""
class test {
	int foo() {
		a [(1 + 2 * 3 - 4 / 5 && 6 || 7)*(1+2+3)-(4+5*6/abc && !(123))] := a[(((-5)))];
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_77_err_delc(self):
        """ Test Negative index Array Declare """
        input = r"""
class test {
	int[-5] a;
}
"""
        expect = r"Error on line 3 col 5: -"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_78_assign(self):
        """ Test Assignment Stmt """
        input = r"""
class test {
	int foo() {
    a := b[3] := foo(3)[5] := 5;
	}
}
"""
        expect = r"Error on line 4 col 14: :="
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_79_assign(self):
        """ Test Assignment Stmt """
        input = r"""
class test {
	int foo() {
    a := b[3] := foo(3) := 5;
	}
}
"""
        expect = r"Error on line 4 col 14: :="
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_80_assign(self):
        """ Test Assignment Stmt """
        input = r"""
class test {
	int foo() {
    a := b+5 := 5;
	}
}
"""
        expect = r"Error on line 4 col 13: :="
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_81_err_for(self):
        """ Test Wrong Syntax For Statement """
        input = r"""
class test {
	int foo() {
		for i := 1 to 10+5-4*e+x do break;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_82_err_for(self):
        """ Test Wrong Syntax For Statement """
        input = r"""
class test {
	int foo() {
		for i := 10+5-4*e+x downto 1 do break;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_83_err_for(self):
        """ Test Wrong Syntax For Statement """
        input = r"""
class test {
	int foo() {
		for i := 1 to 5e2 do fibonacci();
	}
}
"""
        expect = r"Error on line 4 col 32: ("
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_84_err_delc(self):
        """ Test Wrong Syntax Declare """
        input = r"""
class test {
	break;
}
"""
        expect = r"Error on line 3 col 1: break"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_85_err_delc(self):
        """ Test Wrong Syntax Declare """
        input = r"""
class test {
	int foo() {
		break
	}
}
"""
        expect = r"Error on line 5 col 1: }"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_86_err_delc(self):
        """ Test Wrong Syntax Declare """
        input = r"""
class test {
	int foo() {
		int a = 5
	}
}
"""
        expect = r"Error on line 5 col 1: }"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_87_err_delc(self):
        """ Test Wrong Syntax Declare """
        input = r"""
class test {
	int foo() {
		int ;
	}
}
"""
        expect = r"Error on line 4 col 6: ;"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_88_Example_2(self):
        """ Test Example 2 """
        input = r"""
class Shape {
	float length,width;
	float getArea() {}
	Shape(float length,width){
		this.length := length;
		this.width := width;
	}
}
class Rectangle extends Shape {
	float getArea(){
		return this.length*this.width;
	}
}
class Triangle extends Shape {
	float getArea(){
		return this.length*this.width / 2;
	}
}
class Example2 {
	void main(){
		Shape s;
		s := new Rectangle(3,4);
		io.writeFloatLn(s.getArea());
		s := new Triangle(3,4);
		io.writeFloatLn(s.getArea());
	}
}

"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_89_complex(self):
        """ Test Complex """
        input = r"""
class String1 {
	string a = "I love U!!!!!";
	string getString(){
		return this.a;
	}
}
class String2 {
	string b = " Chi Pu";
	string getString(){
		return this.b;
	}
}
class Example {
	void main(){
		String1 str1;
		String2 str2;
		string result;
		result := str1.getString ^ str2.getString;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_90_complex(self):
        """ Test Complex """
        input = r"""
class person {
    string name;
    int id;
    void getdetails(){}
}
class Example {
	void main() {
		person p1;
		p1.getdetails();
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_91_complex(self):
        """ Test Complex """
        input = r"""
class Animal {
	void move(){}
	void eat(){}
	void label() {
		System.out.println("Animal's data:");
	}
}
class Bird extends Animal {

	void move() {
		 System.out.println("Moves by flying.");
     }
	void eat() {
		 System.out.println("Eats birdfood.");
	}	 
}

class Fish extends Animal {
		 void move() {
			 System.out.println("Moves by swimming.");
	     }
		 void eat() {
			 System.out.println("Eats seafood.");
		 }
}
class TestBird {
	void main() {
		Animal myBird;
		myBird := new Bird();

		myBird.label();
		myBird.move();
		myBird.eat();
	}
}

class TestFish {
	void main() {
		Animal myFish;
		myFish := new Fish();

		myFish.label();
		myFish.move();
		myFish.eat();
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_92_err_delc(self):
        """ Test Wrong Syntax Declare """
        input = r"""
class test {
	int foo(int a){
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_93_err_delc(self):
        """ Test Wrong Syntax Declare """
        input = r"""
class test {
	int foo(int a){
		a :=5 ;
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_94_err_delc(self):
        """ Test Wrong Syntax Declare """
        input = r"""
class test {
	void main(int a,b){
	}
}
"""
        expect = r"Error on line 3 col 11: int"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_95_err_delc(self):
        """ Test Wrong Syntax Function Declare """
        input = r"""
class test {
	void main(){
	}
	void main(){
	}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_96_err_delc(self):
        """ Test Wrong Syntax Function Declare """
        input = r"""
class test {
	int main(){
	}
}
"""
        expect = r"Error on line 3 col 5: main"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_97_err_delc(self):
        """ Test Wrong Syntax Function Declare """
        input = r"""
class test() {
	int foo() {

	}
}
"""
        expect = r"Error on line 2 col 10: ("
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_98_err_delc(self):
        """ Test Error If Stmt """
        input = r"""
class test {
	int foo(){
    a = 1;
	}
}
"""
        expect = r"Error on line 4 col 6: ="
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_99_err_stmt(self):
        """ Test Error If Stmt """
        input = r"""
class test {
	int foo(){
    if a == 1 :
        break;
	}
}
"""
        expect = r"Error on line 4 col 14: :"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_100_err_if(self):
        """ Test Error If Stmt """
        input = r"""
class test {
	int foo(){
    if a == 1 {
        break;
    }
	}
}
"""
        expect = r"Error on line 4 col 14: {"
        self.assertTrue(TestParser.test(input, expect, 300))