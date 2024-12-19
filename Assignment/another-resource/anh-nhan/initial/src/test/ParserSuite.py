import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_01(self):
        input = """
            Class Shape {
                $getNumOfShape() {
                    a = "Mai Thy";
                }
                Val abc:Int=1;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_02(self):
        """ var outsize class """
        input = """
            Class Shape {
                $getNumOfShape() {
                    a = "Mai Thy";
                }
            }
            Val abc:Int=1;
        """
        expect = "Error on line 7 col 12: Val"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_03(self):
        """ method outsize class """
        input = """
            Class Shape {
                $getNumOfShape() {
                    a = "Mai Thy";
                }
            }
            Hello(a,b,c: Int; b: Float){

            }
        """
        expect = "Error on line 7 col 12: Hello"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_04(self):
        """ method outsize class """
        input = """
            Class Shape {
                $getNumOfShape() {
                    a = "Mai Thy";
                }
                
                Hello(a,b,c: Int; b: Float){
                    {
                        a = b + c;
                    }
                }
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))

    def test_05(self):
        input = """
            Class Shape {
                $getNumOfShape() {
                    a = "Mai Thy";
                }
                
                Hello(a,b,c: Int; b: Float; c: MaiThy; e: Array[Array[Float, 2], 4]){
                    {
                        a = b + c;

                    }
                }
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))

    def test_06(self):
        input = """
            Class Shape {
                $getNumOfShape() {
                    a = "Mai Thy";
                }
                Var $Student : Student = New Student();
                Hello(a,b,c: Int; b: Float; c: MaiThy; e: Array[Array[Boolean, 2], 4]){
                    {
                        a = b + c;
                        thy = (ngoc/quang)-dopo;
                        x = (a[1]).hello;
                        y = a.b().c.d();
                        z = New Y().Hello();
                        Var Student : Student = New Student();
                        Var $Student : Student = New Student();
                    }
                }

            }

        """
        expect = "Error on line 15 col 28: $Student"
        self.assertTrue(TestParser.test(input,expect,206))

    def test_07(self):
        """ test if and for stmt """
        input = """
            Class Shape {
                $getNumOfShape() {
                    a = "Mai Thy";
                }
                Var $Student : Student = New Student();
                Hello(a,b,c: Int; b: Float; c: MaiThy; e: Array[Array[Boolean, 2], 4]){
                    {
                        If(a[5] >= (X::$hello)){
                            a = b && c;
                        }
                        Elseif(a < b){
                            Foreach(lehoe In a .. b[9+2] By 5-9+1){
                                x = x - 1;
                            }
                        }
                        Elseif(c > d){

                        }
                        Else{

                        }
                    }
                }

            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))

    def test_08(self):
        """ break, continue, return """
        input = """
            Class Shape {
                $getNumOfShape() {
                    a = "Mai Thy";
                }
                Var $Student : Student = New Student();
                Hello(a,b,c: Int; b: Float; c: MaiThy; e: Array[Array[Boolean, 2], 4]){
                    {
                        If(a[5] >= (X::$hello)){
                            a = b && c;
                        }
                        Elseif(a < b){
                            Foreach(lehoe In a .. b[9+2] By 5-9+1){
                                x = x - 1;
                                If(a == b){
                                    Break;
                                }
                                Else{
                                    Return;
                                }
                            }
                            Continue;
                            If(a.b[5] != 9){
                                Return a.c[9];
                            }
                        }
                    }
                }
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))

    def test_09(self):
        """ var and const decl """
        input = """
            Class Shape {
                $getNumOfShape() {
                    a = "Mai Thy";
                }
                Var $Student : Student = New Student();
                Var $a, b, $c, d: Int = 1,2,3,4;

                Hello(a,b,c: Int; b: Float; c: MaiThy; e: Array[Array[Boolean, 2], 4]){
                    {
                        Var hello : Array[Boolean, 3];
                        Val length : Int = 1, 2;
                    }
                }
            }

        """
        expect = "Error on line 12 col 44: ,"
        self.assertTrue(TestParser.test(input,expect,209))
    
    def test_10(self):
        """ var and const decl """
        input = """
            Class Shape {
                $getNumOfShape() {
                    a = "Mai Thy";
                }
                Var $Student : Student = New Student();
                Var $a, b, $c, d: Int = 1,2,3,4;

                Hello(a,b,c: Int; b: Float; c: MaiThy; e: Array[Array[Boolean, 2], 4]){
                    {
                        Var hello : Array[Boolean, 3];
                        Val length, width : Int = 1;
                    }
                }
            }

        """
        expect = "Error on line 12 col 51: ;"
        self.assertTrue(TestParser.test(input,expect,210))

    def test_11(self):
        """ class name is key word"""
        input = """
            Class Shape {
                Int(){
                }
            }

        """
        expect = "Error on line 3 col 16: Int"
        self.assertTrue(TestParser.test(input,expect,211))

    def test_12(self):
        """ class name is key word"""
        input = """
            Class Rectangle: Shape {
                getArea() {
                    a = Array(
                            Array(
                                Array(1,2),
                                Array(2,3)
                            ),
                            Array (
                                Array(1,2),
                                Array(2,3)
                            )
                        );
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))

    def test_13(self):
        """ $ID in param list of method"""
        input = """
            Class Shape {
                Hi(a, b, s: baby; x, $y: Int){
                }
            }

        """
        expect = "Error on line 3 col 37: $y"
        self.assertTrue(TestParser.test(input,expect,213))

    def test_14(self):
        """ $ID in param list of method"""
        input = """
            Class $Shape {
                Hi(a, b, s: baby; x, $y: Int){
                }
            }

        """
        expect = "Error on line 2 col 18: $Shape"
        self.assertTrue(TestParser.test(input,expect,214))

    def test_15(self):
        """ multi dimen arr"""
        input = """
            Class Shape {
                Hi(a, b, s: baby; x, y: Int){
                }
                Var $hi: Array[Array[Int,2],2] = Array(Array(15-9, Array(2,3,12)), Array(0,1));
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))

    def test_16(self):
        """ multi dimen arr"""
        input = """
            Class Shape {
                Hi(a, b, s: baby; x, y: Int){
                }
                Var $hi: Array[Array[Int,2],2] = "Hello this is \\f some nmice \\t string hehe";
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))

    def test_17(self):
        """ 6.8 """
        input = """
            Class Shape {
                Hi(a, b, s: baby; x, y: Int){
                }
                Val Babe = (!b).c();
                Var hel = (2-(b/2)+-12)[5][9];
                Var X = (2-3)::$hello;
            }

        """
        expect = "Error on line 5 col 25: ="
        self.assertTrue(TestParser.test(input,expect,217))

    def test_18(self):
        """ 6.8 """
        input = """
            Class Shape {
                Hi(a, b, s: baby; x, y: Int){
                    a::$baby();
                    a::$hello;
                }
            }

        """
        expect = "Error on line 5 col 29: ;"
        self.assertTrue(TestParser.test(input,expect,218))

    def test_19(self):
        """ 6.2 """
        input = """
            Class Shape {
                Hi(a, b, s: baby; x, y: Int){
                    a.b[3] = 12 && 4 - 15 + (12--a);
                    a.b() = 12;
                }
            }

        """
        expect = "Error on line 5 col 26: ="
        self.assertTrue(TestParser.test(input,expect,219))

    def test_20(self):
        """ 6.2 """
        input = """
            Class Shape {
                Hi(a, b, s: baby; x, y: Int){
                    a.b[3] = 12 && 4 - 15 + (12--a);
                    a.b(12+3, !b, New X()).bruh = 12;
                    a::$c = 19;
                }
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))

    def test_21(self):
        """ 5.8 """
        input = """
            Class Shape {
                Hi(a, b, s: baby; x, y: Int){
                    a.b[3] = 12 && 4 - 15 + (12--a);
                    a.b(12+3, !b, New X()).bruh = 12;
                    a::$c = 19;
                }
                Var a: b = New b(x, (100/4)-2, New c(Hello,1));
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))

    def test_22(self):
        """ 2.3 """
        input = """
            Class Shape {
                Hi(a, b, s: baby; x, y: Int){
                    a.b[3] = 12 && 4 - 15 + (12--a);
                    a.b(12+3, !b, New X()).bruh = 12;
                    a::$c = 19;
                }
                Constructor(a, b, c: Int; e,f: Bay){
                }
                Destructor(){
                }
                Var a: b = New b(x, (100/4)-2, New c(Hello,1));
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))

    def test_23(self):
        """ 2.3 """
        input = """
            Class Shape {
                Constructor(a, b, c: Int; e,f: Bay){
                }
                Destructor(a: Int){
                }
            }

        """
        expect = "Error on line 5 col 27: a"
        self.assertTrue(TestParser.test(input,expect,223))

    def test_24(self):
        """ 6.2 """
        input = """
            Class Shape {
                Constructor(a, b, c: Int; e,f: Bay){
                }
                Destructor(){
                }
            }
            Class Circle : Shape {
                Var a, $b, c : Conheo = 10, 20, 49;
                Test(){
                    (aimabiet.jztr[5]).a = 12;
                    (a.b[9-2+-12]).b();
                    ## comment cho vui ne ##
                    ## var a = b; cai nay sai ne ##
                    Val x : String = "hello hihi \\t alo";
                }
            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))
#------------------------------------------------------------------
    def test_25(self):
        """ 2.1 """
        input = """
            Class Nothing{

            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))

    def test_26(self):
        """ 2.1 """
        input = """
            Class Shape {
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))

    def test_27(self):
        """ 6.2 """
        input = """
            Class Shape {
                Var $b, c, $d : Huhu = a.b() + b.x, 12, 01_23;
                Test(){
                    a = 12;
                    $c = 16;
                    a.b().e[5] = 19;
                    New X().b().e[3] = 20;
                    b::$c = 21;
                    ((a+b).c[5]).d = Array(Array(15-9, Array(2,3,12)), Array(0,1));
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))

    def test_28(self):
        """ 2.1 """
        input = """
            Class program {
                Var $x, y : $type = 1,2;
            }
        """
        expect = "Error on line 3 col 28: $type"
        self.assertTrue(TestParser.test(input,expect,228))

    def test_29(self):
        """ 3.2 """
        input = """
            Class Shape {
                ## comment nay thi dung ne ##
                Var x, y : b = 12, 0;
                test(){
                    a = 12;
                    $c = 16;
                    ## tham hoa bat dau
                    a.b().e[5] = 19;
                    New X().b().e[3] = 20;
                    b::$c = 21;
                }##
            }
        """
        expect = "Error on line 14 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,229))

    def test_30(self):
        """ 3.2 """
        input = """
            Class Shape {
                ## comment nay thi dung ne ##
                Var x, y : b = 12, 0;
                test(){
                    a = 12;
                    $c = 16;
                    ## tham hoa bat dau
                    a.b().e[5] = 19;
                    New X().b().e[3] = 20;
                    b::$c = 21;
                    ##
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))
##---------------------------------------------------------------------------------
    def test_31(self):
        """ 3.2 """
        input = """
            Class Shape {
                Var x, y : b = 12, 0;
                test(){
                    a = 12;
                    $c = 16;
                }
                test(a,b : Int; c : Float){
                    t2 = !(2+9) - !123_4 + - 0X0 + "hello \\t haha" / 1000;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))

    def test_32(self):
        """ exp """
        input = """
            Class Shape {
                Var x, y : b = 12, 0;
                test(){
                    t1 = (12+3)%x - 9 +. (New X(New y(), (a/b)).haha().hihi - hihi::$ok); 
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))

    def test_33(self):
        """ exp """
        input = """
            Class Shape {
                Var x, y : b = 12, 0;
                test(){
                    d1 = a +. b;
                    d2 = a ==. b;
                    d3 = !(a<=b);
                    d4 = c*d%x;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))

    def test_34(self):
        """ array exp"""
        input = """
            Class Shape {
                Var x, y : b = 12, 0;
                Val $e : Array[Array[Array[Int, 3],4],5];
                Var $x : Array[String, 2] = "hello";
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))
#------------------------------------------------------------------------
    def test_35(self):
        """ array type"""
        input = """
            Class Shape {
                test(){
                    e = a[b*c];
                    e1 = a[e[2]][4];
                    e2 = a[4][5][c[b[9]]];
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))

    def test_36(self):
        """ array type"""
        input = """
            Class Shape {
                Var x, y : b = 12, 0;
                test(){
                    a = New Y(25, New C(New B()), 13+12-(19-7)) % 12;
                    a1 = New Y().b().e.c()[5];
                    a2 = (9+15 / (--29 + 3))[6];
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))

    def test_37(self):
        """ literal """
        input = """
            Class Shape {
                test(){
                    b = 2;
                    c = True;
                    d = False;
                    e = f;
                    a = tRue;
                    g = 90_3.E+9;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))

    def test_38(self):
        """ exp """
        input = """
            Class Shape {
                test(){
                    a = !b;
                    b = ---c;
                    d = e + ---f;
                    g = !---h;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))

    def test_39(self):
        input = """
            Class Program {
                main() {
                    Val a : Int;
                    Foreach (i In 1 .. 100 By 1)
                    {
                        Self.printf("enter the number:");
                        If (self == 0) {
                            Break;
                        }
                    }
                    Return 0;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))

    def test_40(self):
        """ for stmt """
        input = """
            Class Shape {
                test(){
                    Foreach (i In a--b .. (e/f).b()[5] By 12){
                        Foreach(j In 1 .. 4 By a){
                            a = 9;
                            c = !(c==b);
                        }
                        Continue;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))

#------------------------------------------------------------------------------
    def test_41(self):
        """ for stmt """
        input = """
            Class Shape {
                test(){
                    If(12 <= 3){
                        a.haha();
                        Else{

                        }
                    }
                }
            }
        """
        expect = "Error on line 6 col 24: Else"
        self.assertTrue(TestParser.test(input,expect,241))

    def test_42(self):
        """ if stmt """
        input = """
            Class Shape {
                test(){
                    Foreach (i In a--b .. (e/f).b()[5] By 12){
                        a::$b();
                        Var a, b, c : b = a::$b, b.c, c[5];
                        a.b();
                        a.b;
                    }
                }
            }
        """
        expect = "Error on line 8 col 27: ;"
        self.assertTrue(TestParser.test(input,expect,242))

    def test_43(self):
        """ if stmt """
        input = """
            Class Shape {
                test(){
                    If (a == 2){
                    }
                    If (b == 10){
                    }
                    Else{
                        If(12 != 2){
                        }
                        Else{
                        }
                        Elseif{
                        }
                    }
                }
            }
        """
        expect = "Error on line 13 col 24: Elseif"
        self.assertTrue(TestParser.test(input,expect,243))

    def test_44(self):
        """ if stmt """
        input = """
            Class Shape {
                test(){
                    If ((a[5]).b()[4] == !True){
                        Return a;
                    }
                    Else{
                        Self.Donothing();
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))

#---------------------------------------------------------------------
    def test_45(self):
        input = """
            Class Shape {
                test(){
                    b = Array();
                    c = Array(1,);
                }
            }
        """
        expect = "Error on line 5 col 32: )"
        self.assertTrue(TestParser.test(input,expect,245))

    def test_46(self):
        input = """
            Class Shape {
                test(){
                    Self.Foo();
                    (1+1).X = 12;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))

    def test_47(self):
        input = """
            Class Shape {
                test(){
                    a.foo();
                    a::$foo();
                    a.$foo();
                }
            }
        """
        expect = "Error on line 6 col 22: $foo"
        self.assertTrue(TestParser.test(input,expect,247))

    def test_48(self):
        input = """
            Class Shape {
                test(){
                    Var b : Array[Array[Int, 9], 12_95.2E19];
                }
            }
        """
        expect = "Error on line 4 col 49: 1295.2E19"
        self.assertTrue(TestParser.test(input,expect,248))

    def test_49(self):
        input = """
            Class Shape {
                test(){
                    Var b : Array[Array[Int, 9], 0X12_A9BF];
                    Var b : Array[Array[Int, 9], 0B0];
                    Var b : Array[Array[Int, 9], 0];
                }
            }
        """
        expect = "Error on line 5 col 49: 0B0"
        self.assertTrue(TestParser.test(input,expect,249))

    def test_50(self):
        input = """
            Class Shape {
                test(){
                    Var b : Array[Array[Int, 9],-1];
                }
            }
        """
        expect = "Error on line 4 col 48: -"
        self.assertTrue(TestParser.test(input,expect,250))

#-----------------------------------------------------------------------
    def test_51(self):
        """ Class in class """
        input = """
            Class Shape {
                test(){
                }
                Class Hoa : Shape {

                }
            }
        """
        expect = "Error on line 5 col 16: Class"
        self.assertTrue(TestParser.test(input,expect,251))

    def test_52(self):
        """ Func in Func """
        input = """
            Class Shape {
                test(){
                    hello(a,b,c : Int; d: Float){

                    }
                }
            }
        """
        expect = "Error on line 4 col 25: ("
        self.assertTrue(TestParser.test(input,expect,252))

    def test_53(self):
        """ Class in func """
        input = """
            Class Shape {
                test(){
                    Var b : Array[Array[Int, 9],12];
                    Class _Shape_mini{

                    }
                }
            }
        """
        expect = "Error on line 5 col 20: Class"
        self.assertTrue(TestParser.test(input,expect,253))

    def test_54(self):
        """ wrong class name"""
        input = """
            Class 12Shape {
                test(){
                    Var b : Array[Array[Int, 9],-1];
                }
            }
        """
        expect = "Error on line 2 col 18: 12"
        self.assertTrue(TestParser.test(input,expect,254))

    def test_55(self):
        input = """
            Class Shape {
                test(){
                    Var a : Int = 0B0;
                    If (a == 0x0){
                        Foreach (i In i .. j){
                            If (i - j == 12){
                                a = a + 2;
                                Return;
                            }
                            Else{
                                Continue;
                            }
                        }
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))

#-----------------------------------------------------------------------------
    def test_56(self):
        input = """
            Class Shape {
                test(){
                    Var b : = 1, 2;
                }
            }
        """
        expect = "Error on line 4 col 28: ="
        self.assertTrue(TestParser.test(input,expect,256))

    def test_57(self):
        input = """
            Class Dog{
                Val sound = "Gawu";
            }
        """
        expect = "Error on line 3 col 26: ="
        self.assertTrue(TestParser.test(input,expect,257))

    def test_58(self):
        """ Func name """
        input = """
            Class Shape {
                _(){
                }
                test(){
                    _.b(a, b+c, 12);
                }
                12X(){
                }
            }
        """
        expect = "Error on line 8 col 16: 12"
        self.assertTrue(TestParser.test(input,expect,258))

    def test_59(self):
        """ Main func """
        input = """
            Class Shape {
                Main(){
                    ;
                }
            }
        """
        expect = "Error on line 4 col 20: ;"
        self.assertTrue(TestParser.test(input,expect,259))

    def test_60(self):
        """ cmt in string """
        input = """
            Class Shape {
                test(){
                    Var i : String = "This is how we comment ## try it";
                };
            }
        """
        expect = "Error on line 5 col 17: ;"
        self.assertTrue(TestParser.test(input,expect,260))

    def test_61(self):
        """ var name is keyword """
        input = """
            Class _Shape {
                test(){
                    Val _Var : Array[Array[Int, 9],1];
                    Val Var : Array[Array[Int, 9],-1];
                }
            }
        """
        expect = "Error on line 5 col 24: Var"
        self.assertTrue(TestParser.test(input,expect,261))

#--------------------------------------------------------------------------
    def test_62(self):
        input = """
            Class Shape {
                test(){
                    Var b : Int = 1, 2;
                }
            }
        """
        expect = "Error on line 4 col 35: ,"
        self.assertTrue(TestParser.test(input,expect,262))

    def test_63(self):
        input = """
            Class Shape {
                test(){
                    Var b, c : = 1, 2;
                }
            }
        """
        expect = "Error on line 4 col 31: ="
        self.assertTrue(TestParser.test(input,expect,263))

    def test_64(self):
        input = """
            Class Shape {
                test(){
                    ## Class Heo {
                    }
                    ##
                    a = (12/12_0_9_3 + 0XAF_BE) --(a[5] + b[9][New X().Y().id]);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))

    def test_65(self):
        input = """
            Class Shape {
                test(){
                    Break;
                    Continue;
                    Return;
                    Return Main;
                    Return Int;
                }
            }
        """
        expect = "Error on line 8 col 27: Int"
        self.assertTrue(TestParser.test(input,expect,265))

#------------------------------------------------------------------
    def test_66(self):
        input = """
            Class Shape {
                test(){
                    a = true + True && False;
                    a = true + "True ## && ## False";
                    b = !False;
                    c = true + (True && False);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))

    def test_67(self):
        input = """
            Class Shape {
                Count_Xgiaithua_(x:Int){
                    If (x <= 0){
                        Return "Error";
                    }
                    Var GT : Int = 1;
                    Foreach(i In 1 .. x By 1){
                        GT = GT * i;
                    }
                    Return GT;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267))

    def test_68(self):
        input = """
            Class Shape {
                Tinhtong_khoang(start, end: Int){
                    If (start < end){
                        Return "Bye";
                    }
                    Elseif(start == end){
                        Return start;
                    }
                    Else{
                        Var a: Int = 0;
                        Foreach(i In start .. end By 1){
                            a = a + i;
                        }
                        Return a;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,268))

    def test_69(self):
        input = """
            Class Shape {
                demsophantu_duong(start, end: Int; arr: Array[Float, 12]){
                    Var count : Int = 0;
                    Foreach(i In start .. end By 1){
                        If(arr[i] >= 0){
                            count = count + 1;
                        }
                        Return count;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,269))

    def test_70(self):
        input = """
            Class Shape {
                Var x, y: Float;
                TinhS(x, y: Float){
                    Return x*y;
                }
                TinhC(x, y: Float){
                    Return 2*(x+y);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))

#-------------------------------------------------------------------------
    def test_71(self):
        input = """
            Class DongVat{
                Var moitruongsong: moitruong;
                Var thucan: loaithucan;
                Keu(){
                    Self.keu();
                }
            }
            Class ConHeo : DongVat{
                Constructor(){
                    moitruongsong = "Ba Ria";
                    thucan: "an hai";
                }
                Destructor(){
                    Self.nhayvaolo();
                }
                Keu(){
                    Return "lehoe";
                }
            }
        """
        expect = "Error on line 12 col 26: :"
        self.assertTrue(TestParser.test(input,expect,271))

    def test_72(self):
        input = """
            Class Shape {
                Var chuvi, dientich : Float;
            }
            Class Hinhchunhat : Shape{
                TinhS(){
                    Return x*y;
                }
            }
            Class Hinhvuong : Hinhchunhat{

            }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,272))

    def test_73(self):
        input = """
            Class VatNuoi{
                Var giatien : Int;
                Choan(){
                    chunhan.nauan();
                    chunhan.choan();
                }
                Chamsoc(){
                    chunhan.choditam();
                    chunhan.datdidao();
                }
            }
            Class conmeo: VatNuoi{
                Anhai(){
                    self.an();
                    self.ngu(cangay);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))

    def test_74(self):
        input = """
            Class Banhkem{
                Var giatien: Int;
                Tanggia(){
                    giatien = giatien + 10;
                }
                Lambanh(){
                    bot = botmi;
                    kem = kembo;
                    tho.quaybot(bot);
                    tho.trangtri(kem);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,274))

    def test_75(self):
        input = """
            Class Banhtrangtron{
                Val Topping : Array[String, 5] = Array("Tom", "Hanh", "Muoi ot", "Sa te", "Toi phi");
                Var Banhtrang: Banhtrang;
                Tron(){
                    chuquan.laybanhtrang();
                    chuquan.botopping(Topping);
                    chuquan.baogia();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,275))

#---------------------------------------------------------------------
    def test_76(self):
        input = """
            Class Test{
                test(){
                    a = ("Self").strlength();
                    b = (True).ascii;
                    c = 90_45.E0;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,276))

    def test_77(self):
        input = """
            Class Test{
                test(){
                    d = Hello.b("Self").hello;
                    Hello.b("Self").hello();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,277))

    def test_78(self):
        input = """
            Class test{
                d = Hello.b("Self").hello;
                Hello.b("Self").hello();
            }
        """
        expect = "Error on line 3 col 18: ="
        self.assertTrue(TestParser.test(input,expect,278))

    def test_79(self):
        input = """
            Class Test{
                test(){
                    a1 = ("Int").strlength;
                    a2 = Int.strlength;
                }
            }
        """
        expect = "Error on line 5 col 25: Int"
        self.assertTrue(TestParser.test(input,expect,279))

    def test_80(self):
        input = """
            Class Test{
                test(){
                    a1 = ("Float" + True).strlength;
                    a2 = Float.strlength;
                }
            }
        """
        expect = "Error on line 5 col 25: Float"
        self.assertTrue(TestParser.test(input,expect,280))

    def test_81(self):
        input = """
            Class Banhchuoi{
                Val $botbanh :bot;
                Var chuoi: chuoixiem = chuoi && chuoingon;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))

#-------------------------------------------------------------------------
    def test_82(self):
        input = """
            Class Banhchuoi{
                test(){
                    a1 = True && False;
                    a2 = True || False;
                    a3 = "&@" - "## ##";
                    a4 = "True" == 2;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))

    def test_83(self):
        input = """
            Class Banhchuoi{
                test(){
                    b = Array(2, "13", "hello \\t", Array(2,3,4));
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283))

    def test_84(self):
        input = """
            Class Banhchuoi{
                test(){
                    If(Banhchuoi.Ngon == True){
                        Self.tratien();
                    }
                    Else{
                        Self.Anquit();
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,284))

    def test_85(self):
        input = """
            Class Banhchuoi{
                test(){
                    hehe = "This is a tring" + "This is another string";
                    b = 0e000;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,285))

#----------------------------------------------------------------------

    def test_86(self):
        input = """
            Class Banhchuoi{
                test(){
                    hesay = "hello i'm lehoe";
                    shesay = "who iz the hoehoe";
                    hesayagain = "It\'s me";
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,286))

    def test_87(self):
        input = """
            Class Banhchuoi{
                test(){
                    _e12 = 0x0;
                    _ = hello * 2 - !baby;
                    sth = sth - sthth + sththth;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))

    def test_88(self):
        input = """
            Class Banhchuoi{
                test(){
                    spamming = spaming1 - spamming2[3][spamming[4]];
                    spam = Self.Spamminghere();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))

    def test_89(self):
        input = """
            Class Banhchuoi{
                test(){
                    ## i just want some error $%#() ##
                    spam = a.Self;
                }
            }
        """
        expect = "Error on line 5 col 29: Self"
        self.assertTrue(TestParser.test(input,expect,289))

    def test_90(self):
        input = """
            Class Banhchuoi{
                test(){
                    a = Self + Self.next;
                    b.c(Self);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,290))

#-------------------------------------------------------------------------
    def test_91(self):
        input = """
            Class Banhchuoi{
                test(){
                    a = 12_23_4_455_6789;
                    b = 90_234.E12;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))

    def test_92(self):
        input = """
            Class Banhchuoi{
                test(){
                    a = Boolean.spam();
                    ## this is an error##
                }
            }
        """
        expect = "Error on line 4 col 24: Boolean"
        self.assertTrue(TestParser.test(input,expect,292))

    def test_93(self):
        input = """
            Class Banhchuoi{
                test(){
                    lazy = sleepy + tired + boring;
                    spamming_here_ = " hehe he's cool; haha 242 @Q$# ";
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,293))

    def test_94(self):
        input = """
            Class Banhchuoi{
                test(){
                    trying = iwannafilldiz;
                    hihi = haha + hehe;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,294))

    def test_95(self):
        input = """
            Class Banhchuoi{
                test(){
                    Foreach(i In 1 .. 20){
                        Self.Spam();
                        Return "ahihi"+True;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))

#----------------------------------------------------------------------

    def test_96(self):
        input = """
            Class Banhchuoi{
                test(){
                    a5 = countdowning;
                    Var a: Int = tired;
                    Var b: Tired = a;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,296))

    def test_97(self):
        input = """
            Class Banhchuoi{
                test(){
                    only4last = trytrytry;
                    messagetoPPL = "I wanna an tet";
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))

    def test_98(self):
        input = """
            Class Banhchuoi{
                test(){
                    someid::$method();
                    someid::$method().hello;
                }
            }
        """
        expect = "Error on line 5 col 43: ;"
        self.assertTrue(TestParser.test(input,expect,298))

    def test_99(self):
        input = """
            Class Banhchuoi{
                test(){
                    Self.colen(Self).hello("self");
                    Var a : Int = Self + 4;
                    X = a::$hello.haha();
                    a[9][12] = hello;
                    b = Self + Self;
                }
                Var x, $y : Int = 2, 3;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))

    def test_100(self):
        input = """
            Class Banhchuoi{
                test(){
                    Self.colen(Self)[12];
                }
            }
        """
        expect = "Error on line 4 col 40: ;"
        self.assertTrue(TestParser.test(input,expect,300))

##########################################################################