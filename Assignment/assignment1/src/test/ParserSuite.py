import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    # def test_wrong_miss_close(self):
    #     """Miss ) int main( {}"""
    #     input = """int main() {
    #         int a = 1+1*2/3;
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,1000))
    
    def testParser1(self):
        input = """class test{
            final float a, b = 1e9, c = 2E-9, d, e = 123.0, f = 6.;
            static final int k = 3124;
            final static string name = "Le Duy Anh";
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1))

    def testParser2(self):
        input = """class Main {
            int x, y, z;
            boolean a,b,c = true, d,e,f = false, k,j,m;
            static float m,n;
            static string a,b,c = 21, o,i,w = 12;
            static int _l = 8, q, r;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 2))
    
    def testParser3(self):
        input = """class main {
            final int x, y;
        }"""
        expect = "Error on line 2 col 26: ;"
        self.assertTrue(TestParser.test(input, expect, 3))
    
    def testParser4(self):
        input = """ class _main_ {
            ;
        }
        """
        expect = "Error on line 2 col 12: ;"
        self.assertTrue(TestParser.test(input, expect, 4))
        
    def testParser5(self):
        input = """ class __main__ {
            int x, 9x = 10;
        }
        """
        expect = "Error on line 2 col 19: 9"
        self.assertTrue(TestParser.test(input, expect, 5))
    
    def testParser6(self):
        input = """class test {
            final int x = 1 + 1 / 2 * 3 - 5 % 8 \ 1;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 6))
    
    def testParser7(self):
        input = """class test {
            int[5] a, b = {1,2,3,4,5,6,6,7}, xyz__;
            final string[10] x = {true, true, false};
            static string[12] _da;
            static final float[100] keke = {0};
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 7))
        
    def testParser8(self):
        input = """class test {
            static final int x = (1 + 2 * 3 / 4);
            final float y = x.bar_(1,2,3);
            static string str = arr.foo(1);
            final static boolean a = this.api;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 8))
    
    def testParser9(self):
        input = """class test {
            static final int[4] x = x.foo();
            final float y = x.bar_(1,2,3);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 9))
    
    def testParser10(self):
        input = """class empty_method {
            
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 10))
        
    def testParser11(self):
        input = """ class smallest{
            string x = "Hi!";
            int a, b, c = 10;
            final float c, d = 1e9, e,f = 1E-9;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 11))
        
    def testParser12(self):
        input = """ class inner_class_test {
            class inner_class {
            }
        }
        """
        expect = "Error on line 2 col 12: class"
        self.assertTrue(TestParser.test(input, expect, 12))
    
    def testParser13(self):
        input = """ class test_comment {
            /* This is a block comment
            so # has no meaning here */
            
            # This is a line comment so /* or */ has no meaning here
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 13))
        
    def testParser14(self):
        input = """class testingConstructor {
            testingConstructor(){
                int x, y;
                final float x = 10, y,z = 100, t,f,g = 1;
            }        
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 14))
        
    def testParser15(self):
        input = """class testingConstructor {
            testingConstructor(int x,y ; boolean a; string h; float g,h,j){
                static int x;
            }       
        }
        """
        expect = "Error on line 3 col 16: static"
        self.assertTrue(TestParser.test(input, expect, 15))
        
    def testParser16(self):
        input = """class testingConstructor {
            testingConstructor(int x,y ; boolean a; string h; float g,h,j){
                # testing line comment 
                
                /* testing block comment 
                bkool by da
                */
            }       
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 16))
    
    def testParser17(self):
        input = """class testingConstructor {
            testingConstructor(int x,y ; boolean a; string h; float g,h,j){
            }       
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 17))
    
    
    def testParser18(self):
        """ testing_EQUAL-OP_is_not_allowed_in_block_statement """
        """ only_assignment_statement_is_allowed """
        input = """class testingConstructor {
            testingConstructor(int x,y ; boolean a; string h; float g,h,j){
                this.x = 1+1;
            } 
        }
        """
        expect = "Error on line 3 col 23: ="
        self.assertTrue(TestParser.test(input, expect, 18))
    
    def testParser19(self):
        input = """class testing_method {
            int getVal(int x){
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 19))
    
    def testParser20(self):
        input = """class testing_method {
            int getVal(int x){
                this.x := this.foo(1 + 2 * 3 / 4);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 20))
        
    def testParser21(self):
        """ no_return_statement_in_constructor """
        input = """class testing_constructor{
            /* i dont know wut to write here
            # so i wont silent
            */
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 21))
    
    def testParser22(self):
        """ no_return_statement_in_constructor """
        input = """class testing_constructor{
            /* 
            ********
            */
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 22))
        
    def testParser23(self):
        input = """class testing_constructor{
            # this is a comment
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 23))
    
    
    def testParser24(self):
        input = """class Point{
            int x, y;
            Point(int x, y){
                this.x := x;
                this.y := y;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 24))
        
    def testParser25(self):
        input = """class Point{
            int x, y;
            Point(int x, y){
                this.x := x;
                this.y := y;
            }
            int getX(){
                return this.x;
            }
            int getY(){
                return this.y;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 25))
        
    def testParser26(self):
        input = """class testIfStmt{
            static boolean check = true;
            void doSomething(){
                if check then io.printOnConsole("expr is good");
                else io.printOnConsole("expr is not good");
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 26))
        
    def testParser27(self):
        input = """class testIfStmt{
            static boolean check = true;
            Keke doSomething(){
                if check then {}
                else {}
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 27))
        
    def testParser28(self):
        input = """class testIfStmt{
            static boolean check = true;
            Keke doSomething(){
                if check then {
                    io.printOnConsole(check);
                }
                else {
                    io.printOnConsole(!check);
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 28))   
    
    def testParser29(self):
        input = """class testNestedIfStmt{
            static boolean[2] flag;
            testNestedIfStmt(){
                flag[0] := true;
                flag[1] := false;
            }
            float test_nested_if_statement(){
                if flag[0] == true then {
                    if flag[1] == true then {
                        io.consoleLog("both is good!");
                    }
                    else {
                        io.consoleLog("just the first one");
                        flag[1] := !(flag[1]);
                    }
                }
                else {
                    if flag[1] == true then {
                        io.consoleLog("just the second one");
                        flag[0] := !!flag[1];
                    }
                    else io.consoleLog("both is not good");
                }
            }   
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 29))     
        
    def testParser30(self):
        input = """class findMax{
            final static int a = 10;
            static final float b = 20;
            final string c = "Duy Anh";
            void printOnConsole(float value){
                io.print(value);
                this.max := value;
                this.minArray[0] := -value;
            }
            static void FunctionForNothing(string da, DA){
                if (a > b) then {
                    if (a > c) then {
                        if (b > c) then {
                            x.printOnConsole(1,2,3);
                        }
                        else x.printOnConsole("largest is a and smallest is b");
                    }
                    else {
                        final string danh = "DA";
                        danh := "Le Duy Anh";
                        if (a == !x) then x.callSomeFunctionHere();
                        if b then {
                            this.minusArray[1] := this.foo(a,b);
                            this.print("heeh");
                        }
                        else {
                            this.doSomethingHere();
                            DA.print("notSoWise");
                        }
                    }
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 30))   
        
        # khong goi function truc tiep bang ten function ma chi co the goi = this.functionName
        # Error x[3].func()
        # Loi cho eprx cho if (b > c && c > a) : because of precedence
        
    def testParser31(self):
        input = """class for_test1{
            void main(){
                for i := 1 to 100 do {
                    io.writeIntLn(i);
                    Intarray[i] := i + 1;
                }
            } }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 31))   
    
    def testParser32(self):
        input = """class for_test2{
            void main(){
                for i := 1 to (1 + 2 - 3 == 3 - 2 + 1 && 1 * 2 / 3 \ 4) do io.consoleLog(123);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 32)) 
        
    def testParser33(self):
        input = """class nested_for_method{
            void nested(int x, y; float e){
                for i := 1 to this.getLength(x) do 
                    for j := i + 1 to this.getLength(x) - 1 do{
                        arr[i] := i + j;
                    }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 33))
    
    def testParser34(self):
        input = """class nested_for_method{
            void nested(int x, y; float e){
                for i := 1 to this.getLength(x) do 
                    for j := i + 1 to this.getLength(x) - 1 do {
                        for k := i + j to this.something[9] do io.consoleWrite("hello");
                    }
                for x := 1 + 2 - 3 * 4 / 5 to true || false do {}
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 34))
    
    
    def testParser35(self):
        input = """class mixed_for_if_method{
            void mid_if_for(int x, y; float e; string f; boolean k; Point x, y, z){
                if (x % 2 == 0) then {
                    for i := 1 to (x * x / 2) do {
                        # I dont know I dont know, nguoi ta noi hanh phuc se chang bao lau
                        /* Tim mot noi tinh yeu dua loi
                        Buon lam chi thoi da het roi
                        */ 
                        System.out.println("Nonsense function");
                        if i == 1 then this.consoleLog(i);
                        i := i * j * this.foo();
                    }
                    x := (1 + 1 * this.foo());
                for j := 10 to (i + i / 2) do {
                    j := j + 1 - 2 + 3;
                    if (i == j) then {
                        x.printf("What does the fox say");
                        i := j * 2 / 3;
                    }
                }
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 35))
    
    def testParser36(self):
        input = """class mixed_for_if_method2{
            void mix_if_for_method2(){
                if i != this.getLength(this.j) then {
                    for j := 0 to i - 1 do this.print();
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 36))
    
    def testParser37(self):
        input = """class mixed_for_if_method3{
            void mix_if_for_method3(){
                if i != this.getLength(this.j) then 
                    for j := 0 to i - 1 do this.print();
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 37))
    
    def testParser38(self):
        input = """class mixed_for_if_method4{
            void mix_if_for_method4(){
                for i := 1 to this.size do {
                    j := i * i;
                    if j == this.sqrt(i) then j.printTrue();
                    else j.printFalse();
                }
                if j == i then {
                    for i := j downto j == 0 do {}
                }
                else {}
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 38))
    
    def testParser39(self):
        input = """class mixed_for_if_method5{
            int main(){
                for x := this.getLength(this.foo(1,this.arr[2],this.x)) downto this.getLength(this.foo(1,this.arr[2],this.x)) do {}
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 39))
    
    def testParser40(self):
        input = """class mixed_for_if_method6{
            int main(){
                for x := this.getLength(this.foo(1,this.arr[2],this.x)) downto this.getLength(this.foo(1,this.arr[2],this.x)) do {\
                    if (x % 2 == 0) then {}
                    else {}
                    i := this.setX(this.x);
                }
                if (x == 0) then {}
                else {
                    i := x + 1 / 2 * (3 && 4) || 5;
                    for x := true downto x == true do {}
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 40))
    
    def testParser41(self):
        input = """class Random_Test {
            string Random_method() {
                final int x = 10, y, z, t = 10;
                static float x;
            } 
        }
        """
        expect = "Error on line 4 col 16: static"
        self.assertTrue(TestParser.test(input, expect, 41))
    
    def testParser42(self):
        input = """class final_attribute_test {
            string Random_method() {
                final int x = 10, y, z, t = 10;
                float a = 10, b, c;
                final boolean x,y,z;
            } 
        }
        """
        expect = "Error on line 5 col 35: ;"
        self.assertTrue(TestParser.test(input, expect, 42))
        
    def testParser43(self):
        input = """class Random_Test {
            string Random_method() {
                final int x = 10, y, z, t = 10;
                float a, a1 = 10, b, c;
                final boolean x,y,z;
            } 
        }
        """
        expect = "Error on line 5 col 35: ;"
        self.assertTrue(TestParser.test(input, expect, 43))
    
    def testParser44(self):
        input = """class Random_Test {
            string Random_method() {
                final int x = 10, y, z, t = 10;
                float a, a1 = 10, b, c;
                final boolean x,y,z;
            } 
        }
        """
        expect = "Error on line 5 col 35: ;"
        self.assertTrue(TestParser.test(input, expect, 44))
    
    def testParser45(self):
        input = """class Random_Test {
            string Random_method() {
                final int x = 10, y, z, t = 10;
                float a, a1 = 10, b, c;
                final boolean x,y,z;
            } 
        }
        """
        expect = "Error on line 5 col 35: ;"
        self.assertTrue(TestParser.test(input, expect, 45))
        
    def testParser46(self):
        input = """class Exp{}
        class IntLit extends Exp{}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 46))
    
    def testParser47(self):
        input = """class Exp{}
        class IntLit extends Exp{}
        class FloatLit{}
        class BinExp extends Exp{
            void _mAiN_(){
                self.left := this.separated("exp");
                for i := 0 to this.sizeExp do {
                    self.right := i * this.seperated("expresso");
                    if (self.right % 3 == 0) then {}
                    if (self.right(1,2e9,l[1+2*3], true, this.funcfoobar) % 3 == 1) then {
                        # I_dont_know_wut_to_*&*@()bfshjfbjhsdbhjf_do_here
                        self.middle := this.hehe;
                    }
                    else {
                        for x2 := 1 downto da.pi(this.func("DuyAnh")) do {}
                    }
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 47))
    
    def testParser48(self):
        input = """class test_return_stmt{
            final int a,b,c = 10, x,y = 100;
            int retSthIdontknow(int a,b,c){
                if (a == b) then {
                    return 1;
                }
                if (b != c) then return 0;
                else return -1;
            }
            
            void main(){
                boolean x = this.retSthIdontknow(this.x, this.foo(1), this.z[3]);
                float r, s;
                r := s * s / x;
                final string s = "PPL";
                for x := 1 downto -1 do{
                    if (r == x) then return r.getVal();
                }
                if (r != s) then {
                    if (r + 1 && 2 * 3 / 4 \ this.getVal()) then return a;
                    else {
                        r := this.getVal(1e9, "Duy Anh");
                        return this.r;
                    }
                }
                else {
                    x := (this.x + this.y[1+1/2]);
                    return x * this.l[3];
                }
                return (1+1 * 2);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 48))
    
    def testParser49(self):
        input = """class Random_Test {
            int main(){
                return 0;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 49))
        
    #! Hmmmmmm something wrong with this testcase... return statement cannot exist in any constructor
    def testParser50(self): 
        input = """class Random_Test {
            constructorTesting(Student x){
                if (x.name == "Duy Anh") then return "Le " ^ x.name;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 50))
    
    def testParser51(self): 
        input = """class testParser{
            /* Choi can, choi co, choi ke
            Khong bang mot phut choi em ca doi
            */
            void doNothing(){
                return x.l[3];
            }
        }
        class MaIn_mAiN___{
            void mAiNNNN(){
                return testParser.doNothing(this.foo());
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 51))
    
    def testParser52(self):
        input = """ class test_break_statement {
            int breakstmt_checking_method(int f){
                # Le Duy Anh 
                /* Echo of 
                Computer Science
                Engineering 
                #### nonsense line ####
                */
                break;
                # I dont know what is this for =)))
            }
        }
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 52))
        
    def testParser53(self):
        input = """ class test_break_statement {
            int breakstmt_checking_method_2(int ele){
                for i:= 0 to arr.size() do {
                    cursor := arr[i];
                    if arr[i] == ele / this.atom() then break;
                    else break;
                    if arr[i] != ele * this.foo(l[this.size() / 2]) then {
                        break;
                    }
                    else {
                        cursor := arr[i] * ele;
                        if (cursor == arr[i-1*this.atom()]) then {
                            boolean x, y;
                            x := 10;
                            if (x % 2 == 0) then return x;
                            else {
                                break;
                            }
                        }
                    }
                }
            }
        }
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 53))

    def testParser54(self):
        input = """ class test_break_statement {
            void test_for_with_break(){
                for eXp := 1 downto arrOfSthing[x.a] do {
                    break;
                }
                if eXp == 1 then {
                    for i := this.getValFromIndex(arr[this.x * arr[3]]) downto true == false do break;
                }
            }
        }
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 54))
    
    def testParser55(self):
        input = """ class test_break_statement {
            void test_for_with_break(){
                for eXp := 1 downto arrOfSthing[x.a] do { break; }
                if eXp == 1 then {
                    for i := this.getValFromIndex(arr[this.x * arr[3]]) downto true == false do break;
                }
            }
        }
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 55))
        
    def testParser56(self):
        input = """ class bReAk {
            break;
        }
        """    
        expect = "Error on line 2 col 12: break"
        self.assertTrue(TestParser.test(input, expect, 56))
        
    def testParser57(self):
        input = """ class test_continue_statement {
            boolean contstmt_testing(){
                continue;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 57))
    
    def testParser58(self):
        input = """ class test_continue_statement {
            void contstmt_testing_2(){
                for i := this.arr.getSize() downto (1-1+2-2*0/2-1) do {
                    if this.arr[i] % 2 == 0 then break;
                    else continue;
                }
                for i := 0 to this.arr.getSize(this) do {
                    if !this.isPrime(this.arr[i]) then continue;
                    else break;
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 58))
    
    def testParser59(self):
        input = """ class test_continue_statement {
            Student contstmt_testing_3(){
                {
                    continue;
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 59))
    
    def testParser60(self):
        input = """ class test_continue_statement {
            static float contstmt_testing_3(int ele){
                if ele == 4 then {
                    continue;
                }
                if ele == 3 then continue;
                if ele == 2 then {
                    i := 1;
                    if (i + 1 == ele) then break;
                    else continue;
                }
                if ele == 1 then {
                    for i := this.size(this.arr.isBalance()) downto this.minSize(this, 3, random.str()) do
                        continue;
                }
                else {
                    continue;
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 60))

    def testParser61(self):
        input = """ class test_continue_statement {
            final static float flagNum = 1;
            static void print(Point point){
                for i := 1 to point.getDistance(this, otherPoint) do continue; 
                if (point.getEuclideDistance(this) == this.flagNum) then return (true != false);
                else continue;
                break;
            }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 61))
        
    def testParser62(self):
        input = """ class test_continue_statement {
            static Person test(){
                {}
                { continue; }
                { break; }
                { return this.isSuccess.arr[this.getAtomElement]; }
                {}
            }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 62))
    
    def testParser63(self):
        input = """ class Shape{}
            class Circle extends Shape{
                static void _MaiN_(){
                    Shape s; 
                    s := new Circle(); 
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 63))
    
    def testParser64(self):
        input = """ class Shape {
            boolean type;
            boolean retType(){
                return this.type;
            }
            static void create(){
                if (this.getType()) then return new Circle(5);
                else return new Rectangle(1,2);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 64))
        
    def testParser65(self):
        input = """ class Shape {
            boolean type;
            boolean retType(){
                return this.type;
            }
            static void create(){
                if (this.getType()) then return new Circle(5,this.arrayOfShape[0]);
                else return new Rectangle(1,2,this);
            }
        }
        class Main{
            void _main_(){
                Circle c;
                c := Shape.create(true);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 65))
    
    def testParser66(self):
        input = """ class Shape {
            boolean type;
            boolean retType(){
                return this.type;
            }
            static void create(){
                if (this.getType()) then return new Circle(5,this.arrayOfShape[0]);
                else return new Rectangle();
            }
        }
        class Main{
            void _main_(){
                Rectangle r;
                r := new Rectangle(Shape.create(false, "HCN", 1,2), this);
                r.printArea();
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 66))
        
        
    def testParser67(self):
        input = """ class test_ret_with_new{
            void main(){
                Shape s = new Circle();
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 67))
    
    def testParser68(self):
        input = """ class test_ret_with_new_2{
            void main(){
                final Shape s = new Circle();
                final Shape s;
            }
        }
        """
        expect = "Error on line 4 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 68))
    
    def testParser69(self):
        input = """ class test_ret_with_new_2{
            ArrayOfShape test_create_new_array(){
                Shape[5] shape = {1,2,3};
                return shape[3];
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 69))
        
    def testParser70(self):
        input = """ class Shape{}
        class test_create_object{
            Shape c, _c_, C__ = new Circle(), RrR, ___r = new Rectangle(), s, sH;
            static Shape shapeeeee;
            final static Shape Sh = new Square();
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 70)) 
        
    def testParser71(self):
        input = """ class Shape{}
        class test_create_object{
            final Shape ssss;
        }
        """
        expect = "Error on line 3 col 28: ;"
        self.assertTrue(TestParser.test(input, expect, 71))
    
    def testParser72(self):
        input = """ class Shape{}
        class test_create_object{
            final Shape sHSh = new;
        }
        """
        expect = "Error on line 3 col 34: ;"
        self.assertTrue(TestParser.test(input, expect, 72))
    
    # Testcase Distribution on BKEL:
    # 1-5: class only
    # 6-15: mutable  attribute
    # 16-25: immutable attribute
    # 26-40: method with empty body
    # 41-50: method with local declaration    
    # 51-70: method with assignment
    # 71-80: method with if and assignment
    # 81-85: method with for
    # 86-90: method with break, continue and return
    # 91-100: mix
    
    
    def testParser73(self):
        input = """class Shape {
            float length,width;
            float getArea() {} 
            Shape(float length,width){
                this.length := length;
                this.width := width; 
            }
        }
        class Rectangle extends Shape {
            float getArea(){
                return this.length * this.width;
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 73))
    
    def testParser74(self):
        input = """
            class Example1 {
                int factorial(int n){
                    if n == 0 then return 1; 
                    else return n * this.factorial(n - 1); 
                }
                void main(){ 
                    int x;
                    x := io.readInt();
                    io.writeIntLn(this.factorial(x));
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 74))
    
    def testParser75(self):
        input = """ 
        class assignment_statement_test{
            int foo(){
                a[3+x.foo(2)] := a[b[2]] +3;
                x.b[2] := x.m()[3];
                a[x+b.foo(2)+3] := a[b[2]+6]+3;
                t.y[0] := r.len()[10];
                a[3+x] := a[b[f+y[2]-h[t[5+j]] * 4]] + 3;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 75))
    
    def testParser76(self):
        input = """ 
        class associative_operator_test{
            int foo(){
                a := b + 2 + n + 5 - g - 9;
                a := b + 2 + n && 4 + 5 - g || 2 - 9;
                a := b / 2 * n / 4 && 5 % l || 2 * 9 / 4 % 2;
                a := b ^ c ;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 76))
    
    def testParser77(self):
        input = """ 
        class precedence_operator_test{
            int foo(){
                a := b && c && !d || e && !f && (g || !k);
                a :=  F * G % 5 + (I || L && N + Y || Q * !P) && 6 * 5 + O %  (5 % T) ;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 77))
    
    def testParser78(self):
        input = """class array_wrong_syntax_test_1{
            void main(){
                int[5] arr;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 78))
    
    def testParser79(self):
        input = """class array_wrong_syntax_test_2{
            void main(){
                int[6] a;b;c;
            }
        }
        """
        expect = "Error on line 3 col 26: ;"
        self.assertTrue(TestParser.test(input,expect, 79))
    
    def testParser80(self):
        """ Test Empty Program """
        input = """"""
        expect = "Error on line 1 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 80))
    
    def testParser81(self):
        """ Mixed method """
        input = """ class someMethodWillbeDeclhere{
            int getVal(int x; float y; Point a,b,c){
                this.a[3] := this.callFoo(this.x[this.sqrt(9)]);
                if (x == this.x) then return new Point(1,2,3);
                if (x == this.x[x.foo() * 2 + 1]) then {
                    if this.str[this.str[3]] then return this.x.foo(2);
                    else {
                        break;
                    }
                    if x == 3 * 3 + 1 then continue;
                }
                else break;
            }
            int setVal(){
                for i := 1 to this.foo() do continue;
                for i := this.fooCalling(this.x[this.getVal(this.x[3])]) downto this.valueOfEle() do {
                    continue;
                }
                if check then break;
                else return false && !true;
            }
        }
        class Empty{ 
            # nothing in this class
            /* it is just used for 
            inherited for its subclasses \t\n */
        }
        class Main extends Empty{
            void main(){
                for i := this.foo(x.callExp(670 * true)) downto 1e9 do {
                    this.x[i] := this.y.callingMethod(x.foo());
                    if this.x == 0 then {
                        this.x := this.y.getSomething();
                        return 0;
                    }
                    else return "ramdom_string";
            }
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 81))
    
    def testParser82(self):
        input = """
            class test {
                int foo() {
                    this.foo();
                        this.foo();
                            this.foo();
                                this.foo();
                            this.foo();
                        this.foo();
                    this.foo();
                this.foo();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 82))

    def testParser83(self):
        input = """
        class test {
            int foo() {
                return continue;
            }
        }
        """
        expect = "Error on line 4 col 23: continue"
        self.assertTrue(TestParser.test(input, expect, 83))
    
    def testParser84(self):
        input = """
        class test {
            int foo() {
                a [(1 + 2 * 3 - 4 / 5 && 6 && -7)*(1+2+3)-(4+5*6/abc && (123))] := a[(((-5)))];
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 84))
    
    def testParser85(self):
        input = """
        class String1 {
            string a = "Le Duy";
            string getString(){
                return this.a;
            }
        }
        class String2 {
            string b = "Anh";
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 85))
    
    def testParser86(self):
        input = """
        class Test{
            void main(){
                int[-5] a;
            }
        }
        """
        expect = "Error on line 4 col 20: -"
        self.assertTrue(TestParser.test(input, expect, 86))
    
    def testParser87(self):
        input = """
        class Test{
            void main(){
                int[-5] a;
            }
        }
        """
        expect = "Error on line 4 col 20: -"
        self.assertTrue(TestParser.test(input, expect, 87)) 

    def testParser88(self):
        input = """
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 88))
    
    def testParser89(self):
        input = """
        class test {
            void main(int a,b){
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 89))
        
    def testParser90(self):
        """ Test Complex """
        input = """
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 90))
    
    def testParser91(self):
        input = """class test {
        int foo() {
            a := b[3] := foo(3)[5] := 5;
        }
        }
        """
        expect = "Error on line 3 col 22: :="
        self.assertTrue(TestParser.test(input, expect, 91))
    
    def testParser92(self):
        input = """
        class WAP {
            void func(int a,b,c,d) {
                if a == b + c then
                    for d := 0 to 10 do
                        c := c + 1 / 3 % d;
                else
                    for d := 0 to 10 do
                        c := c - 1 * 2018E+10;
            }
            void func2(string e, f) {
                return e ^ f ^ "Duy Anh";
            }
            boolean func3(boolean g, h) {
                h := false;
                return g == true;
            }
        }
        class WAP2 {
            int width = 0;
            int length = 0;
            WAP2() {
                WAP pg1 = new WAP();
            }
            static int func() {
                return "";
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 92))
    
    def testParser93(self):
        input = """
        class WAP {
            WAP(int a, b, c; string d; boolean e) {
                a := 0;
                b := 0;
                for a := 5 to 10 do
                    for b := 15 downto 1 do
                        for c := 0 downto -10 do
                            if c == 0 then
                                if d == "" then
                                    if e == false then
                                        d := d ^ "abc";
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 93))
    
    def testParser94(self):
        input = """
        class WAP {
            int a,b,c=9,d ;
            static int[6] k,d = {1,2,true,false},c, f = 10.e5;
            final static int m = 3,n = 9;
            static int foo(float c,d; boolean g; int c){
                A a = new X();
                B b = new X(2,3)[x.foo(m)];
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 94))
    
    def testParser95(self):
        input = """
        class ABC {
            B b = new X(!a, -b+a, c || a && m)[m+n];
            static int foo(float m,n; B b){}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 95))
    
    def testParser96(self):
        input = """
        class foo {
            Ab[5] n = this.Geometry(x.foo(5)[4]*(!m) + (s >= m || m+-n));
            H function(A a,b,c; H n){
                int m = h;
                #B b, h = 40, k, d = {3,true,false,5.e5,5.8e+12};
                int a;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 96))
    
    def testParser97(self):
        input = """
        class foo {
            int cam(){
            }
            foo(){{}{}}
            int[5] b[5];
        }
        """
        expect = "Error on line 6 col 20: ["
        self.assertTrue(TestParser.test(input,expect, 97))
    
    def testParser98(self):
        input = """
        class WAP {
            WAP(int a, b, c; string d; boolean e) {
                a := 0;
                b := 0;
                for a := 5 to 10 do
                    for b := 5 to 10 do
                        break;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 98))

    def testParser99(self):
        input = """
        class WAP {
            void func(int a,b) {
                a.a()[5] := 5;
                return a == b % 2;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 99))
    
    def testParser100(self):
        input = """
        class WAP {
            static int a = 0;
            boolean[10000] a, b;
            bool a = true;
            string func(int a, b, float c) {
                return 0;
            }
        }
        """
        expect = "Error on line 6 col 34: float"
        self.assertTrue(TestParser.test(input, expect, 100))
    
    def testParser101(self):
        input = """
        class Test {
            int main(){
                int x = 10;
                final boolean f = true;
                for i := 1 to x do {
                    if (i % 2 == 0) then this.c();
                }
                final int x = i;
                boolean a = 1;
                this.l[1] := x;
                return x;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1000))