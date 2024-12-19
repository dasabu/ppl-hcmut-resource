import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test0(self):
        input_text = """class Test {
            int a = "addmaximum",b = 0001.18;
            static Test2 abc;
            Test2 abcc(Test2 a,a){
                Test2 an;
                for i := 1 to 100 do 
                {
                    io.writeIntLn(i);
                    Intarray[i] := i + 1;
                }
            }
            void aneue,onichann= 1213;
        }
        """
        expect = "Redeclared Parameter: a"
        # Neu muon check class truoc check param thi sao
        self.assertTrue(TestChecker.test(input_text, expect, 300)) 

    def test1(self):
        input_text = """class Test {
            int a = "addmaximum",b = 0001.18;
            static Test2 abc;
        }
        class Test {
            int a = "addmaximum",b = 0001.18;
            Test abc;
            void aneue,onichann= 1213;
        }"""
        expect = "Redeclared Class: Test"
        # Neu muon check class truoc check param thi sao
        self.assertTrue(TestChecker.test(input_text, expect, 301)) 

    def test_2(self):
        input = """
            class a {
                int a;
                static float bb;
                final int c = 1;
                void main(int i;float j; string k){
                    int[5] a;
                    return 5;
                }
            }
            """
        expect = "Type Mismatch In Statement: Return(IntLiteral(5))"
        self.assertTrue(TestChecker.test(input, expect, 302))

    def test_3(self):
        input = """
            class A{
                static void d(string a) {
                    int a, c, d;
                }
            }
            """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 303))

    def test4(self):
        input = """
            class A{
                static void d(string o) {
                    int a, c, d;
                    break;
                }
                
            }
            """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 304))
    
    def test_5(self):
        input = """
            class a {
                int a;
                static float b;
                final int b = 1;
            }
            """

        expect = "Redeclared Constant: b"
        self.assertTrue(TestChecker.test(input, expect, 305))

    def test_6(self):
        input = """
            class a {
                int a;
                static float b;
                final int c = 1;
                void c(){
                }
            }
            """

        expect = "Redeclared Method: c"
        self.assertTrue(TestChecker.test(input, expect, 306))

    def test_7(self):
        input = """
            class a {
                int a;
                static float b;
                final int c = 1;
                void tinh(int d,d){
                
                }
            }
            """

        expect = "Redeclared Parameter: d"
        self.assertTrue(TestChecker.test(input, expect, 307))

    def test_8(self):
        input = """
            class a {
                int a;
                static float b;
                final int c = 1;
                void tinh(int d,e; string f; boolean e){
                
                }
            }
            """

        expect = "Redeclared Parameter: e"
        self.assertTrue(TestChecker.test(input, expect, 308))

    def test_9(self):
        input = """
            class a {
                int a;
                static float b;
                final int c = 1;
                void main(int d,e; string f){
                    float e;
                
                }
            }
            """

        expect = "Redeclared Variable: e"
        self.assertTrue(TestChecker.test(input, expect, 309))

    def test_10(self):
        input = """
            class a {
                int a;
                static float b;
                final int c = 1;
                void mainc(){
                    float e;
                    string f = "Str";
                }
                int mainc(){
                }
            }
            """

        expect = "Redeclared Method: mainc"
        self.assertTrue(TestChecker.test(input, expect, 310))

    def test_11(self):
        input = """
            class a {
                int a;
                static float b;
                final int c = 1;
                void mainc(){
                    string e;
                    string f = "Str";
                    int e;
                }
            }
            """

        expect = "Redeclared Variable: e"
        self.assertTrue(TestChecker.test(input, expect, 311))

    def test_12(self):
        input = """
            class a extends b {
                int a;
                static float b;
                final int c = 1;
                void main(){
                }
            }
            """

        expect = "Undeclared Class: b"
        self.assertTrue(TestChecker.test(input, expect, 312))

    def test_13(self):
        input = """
            class a extends b {
                int a;
                static float b;
                final int c = 1;
                void main(){
                    aa := 1;
                }
            }
            class b{
            }
            """

        expect = "Undeclared Identifier: aa"
        self.assertTrue(TestChecker.test(input, expect, 313))
    def test_14(self):
        input = """
            class a {
                final static int r=4;
                int main(){
                    int[4] t;
                    t := {1,2,"r"};
                }
            }                
            """

        expect = """Illegal Array Literal: [IntLiteral(1),IntLiteral(2),StringLiteral("r")]"""
        self.assertTrue(TestChecker.test(input, expect, 314))

    def test_15(self):
        input = """class A {
            final int x;
            B foo(B b, a) {
                b.a := new A();
            }
        }
        class B {
            A a;
            A foo(A a, b) {
                C c1;
            }
        }
        class D {}"""
        expect = """Illegal Constant Expression: None"""
        self.assertTrue(TestChecker.test(input, expect, 315))
    
    def test_16(self):
        input = """class A {
            int a;
            int a;
        }"""
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,316))

    def test_17(self):
        input = """class A {
            int a;
            final int a = "ngoductri";
        }"""
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,317))

    def test_18(self):
        input = """class A {
            int a;
            void a() {}
        }"""
        expect = "Redeclared Method: a"
        self.assertTrue(TestChecker.test(input,expect,318))

    def test_19(self):
        input = """class A {
            int a;
            void foo(int b) {
                float b;
            }
        }"""
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,319))

    def test_20(self):
        input = """class A {
            int a;
            void foo(int b, b) {
                float b;
            }
        }"""
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input,expect,320))
    
    def test_21(self):
        input = """class A {
            int a;
            void foo(int b, a) {
                float c;
                final float a = 25.12;
            }
        }"""
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input,expect,321))

    def test_22(self):
        input = """class A {
            int a;
            void foo(int b, a) {}
        }
        class A {}"""
        expect = "Redeclared Class: A"
        self.assertTrue(TestChecker.test(input,expect,322))

    def test_23(self):
        input = """class A {
            int a;
            void foo(int b, a) {
                float c;
            }
            int foo() {}
        }"""
        expect = "Redeclared Method: foo"
        self.assertTrue(TestChecker.test(input,expect,323))

    def test_24(self):
        input = """class A {
            A a;
            void foo(B b, a) {
                float c;
            }
            #int foo() {}
        }"""
        expect = "Undeclared Class: B"
        self.assertTrue(TestChecker.test(input,expect,324))

    def test_25(self):
        input = """class A {
            A a;
            void foo(B b, a) {
                float c;
            }
            int foo() {}
        }"""
        expect = "Undeclared Class: B"
        self.assertTrue(TestChecker.test(input,expect,325))

    def test_326(self):
        input = """class A {
            A a;
            void foo(B b, a) {
                float c;
            }
        }
        class B {
            A a;
            void foo(A a, b) {
                C c;
            }
        }"""
        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input,expect,326))

    def test_327(self):
        input = """class A {
            A a;
            B foo(B b, a) {
                float c;
            }
        }
        class B {
            A a;
            D foo(A a, b) {
                C c;
            }
        }"""
        expect = "Undeclared Class: D"
        self.assertTrue(TestChecker.test(input,expect,327))

    def test_328(self):
        input = """class A {
            A a;
            B foo(B b, a) {
                float c;
                B.foo(5, 6);
            }
        }
        class B {
            A a;
            A foo(A a, b) {
                final int c = 69;
                C c1;
            }
        }"""
        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input,expect,328))

    def test_29(self):
        input = """class A {
            A a;
            B foo(B b, a) {
                float c;
                B.hihi(5, 6);
            }
        }
        class B {
            A a;
            A foo(A a, b) {
                final int c = 69;
                C c1;
            }
        }"""
        expect = "Undeclared Method: hihi"
        self.assertTrue(TestChecker.test(input,expect,329))

    def test_30(self):
        input = """class A {
            A a;
            B foo(B b, a) {
                float c;
                B.hihi();
            }
        }
        class B {
            A a;
            A foo(A a, b) {
                C c1;
            }
            int[3] hihi() {}
        }"""
        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input,expect,330))
    
    def test_31(self):
        input = """class A {
            A a;
            B foo(B b, a) {
                float c;
                B.hihi();
            }
        }
        class B {
            A a;
            A foo(A a, b) {
                C c1;
            }
            int[3] hihi() {}
        }"""
        expect = "Type Mismatch In Statement: Call(Id(B),Id(hihi),[])"
        self.assertTrue(TestChecker.test(input,expect,331))

    def test_32(self):
        input = """class A {
            A a;
            B foo(B b, a) {
                float c;
                B.hihi();
                c := { 1, "12"};
            }
        }
        class B {
            A a;
            A foo(A a, b) {
                C c1;
            }
            static void hihi() {}
        }"""
        expect = """Illegal Array Literal: [IntLit(1),StringLit("12")]"""
        self.assertTrue(TestChecker.test(input,expect,332))

    def test_33(self):
        input = """class A {
            A a;
            B foo(B b, a) {
                string[3] c;
                B.hihi();
                c := { "ngoductri", "12", "sana"};
            }
        }
        class B {
            A a;
            A foo(A a, b) {
                C c1;
            }
            int[3] hihi() {}
        }"""
        expect = """Undeclared Class: C"""
        self.assertTrue(TestChecker.test(input,expect,333))

    def test_34(self):
        input = """class A {
            A a;
            B foo(B b, a) {
                float c;
                B.hihi();
                c := { "ngoductri", "12", "sana", 1};
            }
        }
        class B {
            A a;
            A foo(A a, b) {
                C c1;
            }
            int[3] hihi() {}
        }"""
        expect = """Illegal Array Literal: [StringLit("ngoductri"),StringLit("12"),StringLit("sana"),IntLit(1)]"""
        self.assertTrue(TestChecker.test(input,expect,334))
    
    def test_35(self):
        input = """class A {
            A a;
            B foo(B b, a) {
                float c;
                B.hihi();
            }
        }
        class B {
            A a;
            A foo(A a, b) {
                C c1;
                C.foo(6, 9);
                B.haha();
            }
            int[3] hihi() {}
        }
        class C extends A {}"""
        expect = """Undeclared Method: haha"""
        self.assertTrue(TestChecker.test(input,expect,335))

    def test_36(self):
        input = """class A extends B {
            int main() {
                C.foo();
                return A.x;
            }
        }
        class B {
            static int x;
        }
        class C {
            int foo() {}
        }"""
        expect = """['A', 'B', 'C']"""
        self.assertTrue(TestChecker.test(input,expect,336))

    def test_37(self):
        input = """class A {
            A a;
            B foo(B b, a) {
                D c;
                B.hihi();
                c := new D();
            }
        }
        class B {
            A a;
            A foo(A a, b) {
                C c1;
            }
            int[3] hihi() {}
        }
        class D {}"""
        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input,expect,337))

    def test_38(self):
        input = """class A {
            A a;
            B foo(B b, a) {
                float c;
                B.hihi();
                return B.foo;
            }
        }
        class B {
            A a;
            A foo(A a, b) {
                C c1;
            }
            int[3] hihi() {}
        }"""
        expect = "Undeclared Attribute: foo"
        self.assertTrue(TestChecker.test(input,expect,338))

    def test_39(self):
        input = """class A {
            B foo(B b, a) {
                float c;
                B.hihi();
                for i := 1 to 10 do {
                    B.foo(6, 9);
                    break;
                }
            }
        }
        class B {
            A a;
            A foo(A a, b) {
                C c;
            }
            int[3] hihi() {}
        }"""
        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input,expect,339))

    def test40(self):
        input = """class A {
            B foo(B b, a) {
                float c;
                B.hihi();
                for i := 1 to 10 do {
                    B.foo(6, 9);
                    {
                        break;
                    }
                }
            }
        }
        class B {
            A a;
            A foo(A a, b) {
                C c;
            }
            int[3] hihi() {}
        }"""
        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input,expect,340))

    def test_41(self):
        input = """class A {
            B foo(B b, a) {
                for i := 1 to 10 do {
                    B.foo(6, 9);
                    {
                        break;
                    }
                }
                continue;
            }
        }
        class B {
            A foo(A a, b) {
                C c;
            }
            int[3] hihi() {}
        }"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,341))

    def test_42(self):
        input = """class A {
            B foo(B b, a) {
                for i := 1 to 10 do {
                    for j := 1 to 10 do {
                        break;
                    }
                    {
                        break;
                    }
                }
                continue;
            }
        }
        class B {}"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,342))

    def test_43(self):
        input = """class A {
            A a;
            B foo(B b, a) {
                b.a := new A();
            }
        }
        class B {
            A a;
            A foo(A a, b) {
                C c1;
            }
            int[3] hihi() {}
        }
        class D {}"""
        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input,expect,343))

    def test_44(self):
        input = """class A {
            B foo(B b, a) {
                B.a := new A();
            }
        }
        class B {
            A a;
            A foo(A a, b) {
                C c1;
            }
            int[3] hihi() {}
        }
        class D {}"""
        expect = "Illegal Member Access: FieldAccess(Id(B),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,344))

    def test_45(self):
        input = """class A {
            final int x;
            B foo(B b, a) {
                b.a := new A();
            }
        }
        class B {
            A a;
            A foo(A a, b) {
                C c1;
            }
        }
        class D {}"""
        expect = "Illegal Constant Expression: None"
        self.assertTrue(TestChecker.test(input,expect,345))

    def test_46(self):
        input = """class A {
            int a;
            final int x = 1 + 2;
            B foo(B b, a) {
                b.a := new A();
            }
        }
        class B {
            A a;
            A foo(A a, b) {
                C c1;
            }
        }
        class D {}"""
        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input,expect,346))

    def test_47(self):
        input = """class A {
            static int a;
            final int x = A.a + 1;
            B foo(B b, a) {
                b.a := new A();
            }
        }
        class B {
            A a;
            A foo(A a, b) {
                C c1;
            }
        }
        class D {}"""
        expect = "Illegal Constant Expression: BinaryOp(+,FieldAccess(Id(A),Id(a)),IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,347))

