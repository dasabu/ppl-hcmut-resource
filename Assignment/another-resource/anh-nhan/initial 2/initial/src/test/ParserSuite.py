import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_01(self):
        input = """
            class Shape {
                int getNumOfShape() {
                    a := "Mai Thy";
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_02(self):
        input = """
            class Shape {
                int a, b=1;
                void getNumOfShape() {
                    a := "Mai Thy";
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_03(self):
        input = """
            class Shape {
                a getNumOfShape() {
                    a := "Mai Thy";
                }
                void main(){}
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_04(self):
        input = """
            class Shape {
                int b;
                string a = 5, b, c = 19;
                a getNumOfShape() {
                    a := "Mai Thy";
                }
                void main(){}
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))

    def test_05(self):
        input = """
            class Shape {
                int b;
                string a = 5, b, c = 19;
                a getNumOfShape() {
                    a := "Mai Thy";
                }
                void main(){}
                string a = 5, b, c = 19;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))

    def test_06(self):
        input = """
            class Shape {
                int b;
                string a = 5, b, c = 19;
                a getNumOfShape() {
                    a := "Mai Thy";
                }
                void main(){
                    int b = "thy";
                    b := 12;
                    return;
                }
                string a = 5, b, c = 19;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))

    def test_07(self):
        input = """
            class Shape {
                int b;
                string a = 5, b, c = 19;
                a getNumOfShape() {
                    a := "Mai Thy";
                }
                void main(){
                    int b;
                    b:=c;
                    float c;
                }
                string a = 5, b, c = 19;
            }
        """
        expect = "Error on line 11 col 20: float"
        self.assertTrue(TestParser.test(input,expect,207))

    def test_08(self):
        input = """
            class Shape {
                int b;
                string a = 5, b, c = 19;
                a getNumOfShape() {
                    a := "Mai Thy";
                }
                void main(){
                    int b;
                    b:=c;
                    
                }
                string a = 5, b, c = 19;
            }
            float a;
        """
        expect = "Error on line 15 col 12: float"
        self.assertTrue(TestParser.test(input,expect,208))

    def test_09(self):
        input = """
            class Shape {
                int b;
                string a = 5, b, c = 19;
                a getNumOfShape() {
                    a := "Mai Thy";
                }
                void main(){
                    int b;
                    b:=c;
                    
                }
                string a = 5, b, c = 19;
            }
            float test(int a, b, c; float d){

            }
        """
        expect = "Error on line 15 col 12: float"
        self.assertTrue(TestParser.test(input,expect,209))

    def test_10(self):
        input = """
            class Shape {
                int b;
                string a = 5, b, c = 19;
                a getNumOfShape() {
                    a := "Mai Thy";
                }
                void main(){
                    int b;
                    b:=c;
                    
                }
                string a = 5, b, c = 19;
                float test(int a, b, c; float d){}
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))

    def test_11(self):
        input = """
            class Shape {
                int b;
                string a = 5, b, c = 19;
                a getNumOfShape() {
                    a := "Mai Thy";
                }
                void main(){
                    int b;
                    b:=c;
                    
                }
                string a = 5, b, c = 19;
                float test(int a, b, c; float d; r){}
            }

        """
        expect = "Error on line 14 col 50: )"
        self.assertTrue(TestParser.test(input,expect,211))

    def test_12(self):
        input = """
            class Shape {
                int b;
                string a = 5, b, c = 19;
                a getNumOfShape() {
                    a := "Mai Thy";
                }
                void main(){
                    int b;
                    b:=c;
                    
                }
                string a = 5, b, c = 19;
                float test(int a, b, c; float d; string){}
            }

        """
        expect = "Error on line 14 col 55: )"
        self.assertTrue(TestParser.test(input,expect,212))

    def test_13(self):
        input = """
            class Shape {
                int b;
                string a = 5, b, c = 19;
                a getNumOfShape() {
                    a := "Mai Thy";
                }
                void main(){
                    int b;
                    b:=c;
                    
                }
                string a = 5, b, c = 19;
                float test(int a, b, c; float d; string thy; thy thy, thy, thy){}
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))

    def test_14(self):
        input = """
            class Shape {
                int b;
                string a = 5, b, c = 19;
                a getNumOfShape() {
                    a := "Mai Thy";
                }
                void main(){
                    int b;
                    b:=c;
                    
                }
                string a = 5, b, c = 19;
                float test(int a, b, c; float d; string thy; thy thy, thy, thy; int[4] thinh, thinh; thy[3] thy){}
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))

    def test_15(self):
        input = """
            class Shape {
                int b;
                string a = 5, b, c = 19;
                a getNumOfShape() {
                    a := "Mai Thy";
                }
                void main(){
                    int b;
                    b:=c;
                    
                }
                string a = 5, b, c = 19;
                float test(int a, b, c; float d; string thy; thy thy, thy, thy){
                    thy := thy + thy;
                }
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))

    def test_16(self):
        input = """
            class Shape {
                int b;
                a thy, thy = 19;
                string a = 5, b, c = 19;
                a getNumOfShape() {
                    a := "Mai Thy";
                }
                void main(){
                    int b;
                    b:=c;
                    
                }
                string a = 5, b, c = 19;
                a:=12;
                float test(int a, b, c; float d; string thy; thy thy, thy, thy){}
            }

        """
        expect = "Error on line 15 col 17: :="
        self.assertTrue(TestParser.test(input,expect,216))

    def test_17(self):
        input = """
            class Shape {
                int b;
                a thy, thy = 19;
                string a = 5, b, c = 19;
                a getNumOfShape() {
                    Student Student = new Student();

                    a := b + c;
                    thy := (ngoc/quang)-dopo;
                    x := (a[1]).hello;
                    y := a.b().c.d();
                    z := new Y().Hello();
                }
                void main(){
                    int b;
                    b:=c;
                    
                }
                string a = 5, b, c = 19;
                float test(int a, b, c; float d; string thy; thy thy, thy, thy){}
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))

    def test_18(self):
        input = """
            class Shape {
                int b;
                a thy, thy = 19;
                string a = 5, b, c = 19;
                a getNumOfShape() {
                    Student Student = new Student();

                    a := b + c;
                    thy := (ngoc/quang)-dopo;
                    x := (a[1]).hello;
                    y := a.b().c.d();
                    z := new Y().Hello();
                }
                Student Student = new Student();
                void main(){
                    if a[5] >= (X.hello) then{
                            a := b && c;
                    }
                    else{
                        for i:= 10 to 1000 do{
                            x := x - 1;
                        }
                    }

                    if 12 then a:=b;
                    if a == c then 
                        for hehe := 10 downto 1 do
                            x := x - 2;
                }
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))

    def test_19(self):
        input = """
            class Shape {
                int b;
                a thy, thy = 19;
                string a = 5, b, c = 19;
                a getNumOfShape() {
                    Student Student = new Student();

                    a := b + c;
                    thy := (ngoc/quang)-dopo;
                    x := (a[1]).hello;
                    y := a.b().c.d();
                    z := new Y().Hello();
                }
                Student Student = new Student();
                void main(){
                    if a[5] >= (X.hello) then{
                            a := b && c;
                    }
                    else{
                        for lehoe := a to 900-2+a[4] do{
                                x := x - 1;
                                if(a == b) then {
                                    break;
                                }
                                else{
                                    return;
                                }
                        }
                            continue;
                            if a.b[5] != 9 then
                                return a.c[9];
                    }
                }
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))

    def test_20(self):
        input = """
            class Shape {
                int b;
                string a = 5, b, c = 19;
                a getNumOfShape() {
                    a := "Mai Thy";
                }
                void main(){
                    int b;
                    b:=c;
                    
                }
                string a = 5, b, c = 19;
                float test(int a, b, c; float d; string thy; thy thy, thy, thy){
                    thy := thy + thy;
                    if a then {
                        bool[3] i, x = {1, 2, 3};
                    }
                }
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))

    def test_21(self):
        input = """
            class Shape {
                int b;
                string a = 5, b, c = 19;
                a getNumOfShape(int b = 9) {
                    a := "Mai Thy";
                }
            }

        """
        expect = "Error on line 5 col 38: ="
        self.assertTrue(TestParser.test(input,expect,221))

    def test_22(self):
        input = """
            class Shape extends Hhh {
                he he(){
                    a.c().c();
                    (a[10]).c.b();
                }
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))

    def test_23(self):
        input = """
            class Shape extends Hhh {
                int b(){
                    return (a[b[3]]).c();
                }
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))

    def test_24(self):
        input = """
            class Shape extends Hhh {
                int b(){
                    int a = (!b).c(), b, c = 10;
                    bool hel = (2-(b/2)+-12)[5];
                    X := (2-3).hello;
                    return (a[b[3]]).c();
                }
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))

    def test_25(self):
        input = """
            class Shape extends Hhh {
                int b(){
                    a.hello();
                    b.hi;
                }
            }

        """
        expect = "Error on line 5 col 24: ;"
        self.assertTrue(TestParser.test(input,expect,225))

    def test_26(self):
        input = """
            class Shape extends Hhh {
                int b(){
                    a.b[3] := 12 && 4 - 15 + (12--a);
                    a.b() := 12;
                }
            }

        """
        expect = "Error on line 5 col 26: :="
        self.assertTrue(TestParser.test(input,expect,226))

    def test_27(self):
        input = """
            class Shape extends Hhh {
                int b(){
                    a.b[3] := 12 && 4 - 15 + (12--a);
                    a.b(12+3, !b, new X()).bruh := 12;
                    a.c := 19;
                }
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))

    def test_28(self):
        input = """
            class Shape extends Hhh {
                int b(){
                    a.b[3] := 12 && 4 - 15 + (12--a);
                    a.b(12+3, !b, new X()).bruh := 12;
                    a.c := 19;
                }
                a b = new b(x, (100/4)-2, new c(Hello,1));
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))

    def test_29(self):
        input = """
            class Shape extends Hhh {
                int b(){
                    a.b[3] := 12 && 4 - 15 + (12--a);
                    a.b(12+3, !b, new X()).bruh := 12;
                    a.c := 19;
                }
                Hhh(){}
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,229))

    def test_30(self):
        input = """
            class Shape extends Hhh {
                int b(){
                    a.b[3] := 12 && 4 - 15 + (12--a);
                    a.b(12+3, !b, new X()).bruh := 12;
                    a.c := 19;
                }
                Hhh(int a, b){}
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))

    def test_31(self):
        input = """
            class Shape extends Hhh {
                int b(){
                    a.b[3] := 12 && 4 - 15 + (12--a);
                    a.b(12+3, !b, new X()).bruh := 12;
                    a.c := 19;
                }
                Hhh(int a, b){
                    (aimabiet.jztr[5]).a := 12;
                    (a.b[9-2+-12]).b();
                    /* comment cho vui ne */
                    ## a = b; cai nay sai ne 
                    x := "hello hihi \\t alo";
                }
                
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))

    def test_32(self):
        input = """
            class Shape extends Hhh {
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))

    def test_33(self):
        input = """
            class Shape extends Hhh {
                void test(){
                    a := 12;
                    a.b().e[5] := 19;
                    new X().b().e[3] := 20;
                    c := 21;
                    ((a+b).c[5]).d := {2, 3, {12, 1}};
                }
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))

    def test_34(self):
        input = """
            class Shape extends Hhh {
                ## comment nay thi dung ne 
                int x, y, b = 12.34E-33;
                test(){
                    a := 12;
                    /* tham hoa bat dau
                    a.b().e[5] = 19;
                    New X().b().e[3] = 20;
                    b::$c = 21;
                    */
                }
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))

    def test_35(self):
        input = """
            class Shape extends Hhh {
                ## comment nay thi dung ne 
                int x, y, b = 12.34E-33;
                test(){
                    t2 := !(2+9) - !1234 + - ab + "hello \\t haha" / 1000;
                }
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))

    def test_36(self):
        input = """
            class Shape extends Hhh {
                ## comment nay thi dung ne 
                int x, y, b = 12.34E-33;
                test(){
                    t2 := !(2+9) - !1234 + - ab + "hello \\t haha" / 1000;
                }
            }

            class newname{
                test(){
                    a := new Y(25, new C(new B()), 13+12-(19-7)) % 12;
                    a1 := new Y().b().e.c()[5];
                    a2 := (9+15 / (--29 + 3))[6];
                }
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))

    def test_37(self):
        input = """
            class Shape extends Hhh {
                ## comment nay thi dung ne 
                int x, y, b = 12.34E-33;
                test(){
                    a := !b;
                    b := ---c;
                    d := e + ---f;
                    g := !---h;                
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))

    def test_38(self):
        input = """
            class Shape extends Hhh {
                ## comment nay thi dung ne 
                int x, y, b = 12.34E-33;
                test(){
                    t2 := !(2+9) - !1234 + - ab + "hello \\t haha" / 1000;
                }
                void main(){
                    int b, c= 0;
                    for i:= 1 to 10 do
                        this.print("hehe");
                    break;
                }
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))

    def test_39(self):
        input = """
            class newname{
                test(){
                    for i:= 10 downto a[9] do
                        for e := 1 to 18 do
                            if a == b then
                                this.hello(a, b, new X());
                            else return;
                }
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))

    def test_40(self):
        input = """
            class newname{
                test(){
                    if a then {
                        else i:=10;
                    }
                }
            }

        """
        expect = "Error on line 5 col 24: else"
        self.assertTrue(TestParser.test(input,expect,240))

    def test_41(self):
        input = """
            class newname{
                test(){
                    if a then {
                        if b then {}
                        else i:=10;
                        if c then {}
                    }
                }
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))

    def test_42(self):
        input = """
            class newname{
                test(){
                    if ((a[5]).b()[4] == !True) then {
                        return a;
                    }
                    else{
                        this.Donothing();
                    }
                }
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))

    def test_43(self):
        input = """
            class newname{
                test(){
                    if a then {
                        a := {1, 3, };
                    }
                }
            }

        """
        expect = "Error on line 5 col 36: }"
        self.assertTrue(TestParser.test(input,expect,243))

    def test_44(self):
        input = """
            class newname{
                test(){
                    if a then {
                        id[4][4] b = 12; 
                    }
                }
            }

        """
        expect = "Error on line 5 col 29: ["
        self.assertTrue(TestParser.test(input,expect,244))

    def test_45(self):
        input = """
            class newname{
                test(){
                    if a then {
                        int[0] h;
                    }
                }
            }

        """
        expect = "Error on line 5 col 28: 0"
        self.assertTrue(TestParser.test(input,expect,245))

    def test_46(self):
        input = """
            class 12newname{
                test(){
                    if a then {
                        int[0] h;
                    }
                }
            }

        """
        expect = "Error on line 2 col 18: 12"
        self.assertTrue(TestParser.test(input,expect,246))

    def test_47(self):
        input = """
            class _newname{
                test(){
                    if a then {
                        int[0] h;
                    }
                }
            }

        """
        expect = "Error on line 5 col 28: 0"
        self.assertTrue(TestParser.test(input,expect,247))

    def test_48(self):
        input = """
            class newname{
                test(){
                    class B{

                    }
                }
            }

        """
        expect = "Error on line 4 col 20: class"
        self.assertTrue(TestParser.test(input,expect,248))

    def test_49(self):
        input = """
            class newname{
                void test(){
                    void main(){

                    }
                }
            }

        """
        expect = "Error on line 4 col 20: void"
        self.assertTrue(TestParser.test(input,expect,249))

    def test_50(self):
        input = """
            class Shape {
                test(){
                }
                class Hoa extends shape{

                }
            }

        """
        expect = "Error on line 5 col 16: class"
        self.assertTrue(TestParser.test(input,expect,250))

    ##------------ clone part ------------------
    def test_51(self):
        input = """
            class Shape {
                test(){
                }
                class Hoa extends shape{

                }
            }

        """
        expect = "Error on line 5 col 16: class"
        self.assertTrue(TestParser.test(input,expect,251))

    def test_52(self):
        input = """
            class Shape {
                test(){
                }
                class Hoa extends shape{

                }
            }

        """
        expect = "Error on line 5 col 16: class"
        self.assertTrue(TestParser.test(input,expect,252))

    def test_53(self):
        input = """
            class Shape {
                test(){
                }
                class Hoa extends shape{

                }
            }

        """
        expect = "Error on line 5 col 16: class"
        self.assertTrue(TestParser.test(input,expect,253))

    def test_54(self):
        input = """
            class Shape {
                test(){
                }
                class Hoa extends shape{

                }
            }

        """
        expect = "Error on line 5 col 16: class"
        self.assertTrue(TestParser.test(input,expect,254))

    def test_55(self):
        input = """
            class Shape {
                test(){
                }
                class Hoa extends shape{

                }
            }

        """
        expect = "Error on line 5 col 16: class"
        self.assertTrue(TestParser.test(input,expect,255))

