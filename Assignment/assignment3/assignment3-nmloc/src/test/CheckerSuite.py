import unittest
from TestUtils import TestChecker
from AST import *
from main.bkool.checker.StaticError import Class

from main.bkool.utils.AST import *


class CheckerSuite(unittest.TestCase):
    def test_1(self):
        input = "class a extends b {}"
        expect = "Undeclared Class: b"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_2(self):
        input = "class a {} class a {}"
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_3(self):
        input = """
        class Ex
        {
            int my1Var;
            static float my1Var;
        }"""
        expect = "Redeclared Attribute: my1Var"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_4(self):
        input = """
        class Ex
        {
            final int x = 10.0;
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(x),IntType,FloatLit(10.0))"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_5(self):
        input = """
        class Ex
        {
            void foo()
            {
                continue;
            }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_6(self):
        input = """
        class Ex
        {
            final int x = x;
        }
        """
        expect = "Illegal Constant Expression: Id(x)"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_7(self):
        input = Program(
            [
                ClassDecl(
                    Id("Ex"),
                    [
                        AttributeDecl(
                            Instance(),
                            VarDecl(
                                Id("x"),
                                ArrayType(3, IntType()),
                                ArrayLiteral(
                                    [IntLiteral(2), FloatLiteral(1.2), NullLiteral()]
                                ),
                            ),
                        )
                    ],
                )
            ]
        )
        expect = "Illegal Array Literal: [IntLit(2),FloatLit(1.2),NullLiteral()]"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_8(self):
        input = """
        class a {}
        class b extends a {}
        class a {}
        """
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_9(self):
        input = """
        class ABC
        {
            int x;
            float y;
            static string z;
        }
        class XYZ extends ABC
        {
            float x;
            int y;
            final int[3] z = {1,2,3};
        }
        """
        expect = "Illegal Constant Expression: [IntLit(1),IntLit(2),IntLit(3)]"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_10(self):
        input = """
        class ABC
        {
            int[3] a = {1,2,3};
            final int[3] b = {1,2,3e6};
        }
        """
        expect = "Illegal Array Literal: [IntLit(1),IntLit(2),FloatLit(3000000.0)]"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_11(self):
        input = """
        class ABC
        {
            final float[3] a = {1,2,4};
        }
        """
        expect = "Illegal Constant Expression: [IntLit(1),IntLit(2),IntLit(4)]"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_12(self):
        input = """
        class ABC {
            int test() {
                for i := 0 to 5 do {
                    for j := 0 to 5 do {
                        break;
                    }
                    break;
                }
                break;
            }
        }
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_13(self):
        input = """
        class ABC {
            final float x = 1 + 2.2;
            final float y = 1 + 2;
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(y),FloatType,BinaryOp(+,IntLit(1),IntLit(2)))"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_14(self):
        input = """
        class ABC {
            static int x = 5;
        }
        class XYZ extends ABC {
            float x = 7.7;
            int x = 7.7;
        }
        """
        expect = "Redeclared Attribute: x"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_15(self):
        input = """
        class X
        {
            float x = 5 + 2 + 4.4 + 6 + 7;
            final int y = 1 + a;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_16(self):
        input = "class a extends b {}"
        expect = "Undeclared Class: b"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_17(self):
        input = """
        class X
        {
            int[5] x = {1,2,3,4,5};
            float x = 7.7;
        }
        """
        expect = "Redeclared Attribute: x"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_18(self):
        input = Program(
            [
                ClassDecl(
                    Id("Ex"),
                    [
                        AttributeDecl(Static(), VarDecl(Id("a"), IntType())),
                        AttributeDecl(
                            Instance(),
                            ConstDecl(
                                Id("x"), IntType(), FieldAccess(Id("Ex"), Id("a"))
                            ),
                        ),
                    ],
                )
            ]
        )
        expect = "Illegal Constant Expression: FieldAccess(Id(Ex),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_19(self):
        input = """
        class Test
        {
            int x;
            int y;
            int z;
            final int u = 5;
            final int v = 5 + u;
            void run(int x; int y; float z) {
                continue;
            }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_20(self):
        input = """
        class ABC {
            void count(int a; int b; A a) {}
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_21(self):
        input = """
        class A {
            int x = 5;
        }
        class B extends A {
            int x = 6;
            int y = 7;
        }
        class C extends B {
            int z = 8;
            final float u = 10 + e;
        }
        """
        expect = "Undeclared Identifier: e"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_22(self):
        input = """
        class ABC {
            int x = 5;
            final int y = 7;
            final static int z = 9;
        }
        class XYZ extends ABC {
            int x = 6 + y;
        }
        class U extends XYZ {
            final int x = x;
        }
        """
        expect = "Illegal Constant Expression: Id(x)"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_23(self):
        input = """
        class A
        {
            int x = 5;
            static int u = 10;
        }
        class B
        {
            A y = new A();
            float z1 = y.x +5.5;
            float z2 = y.x + 5;
            final float u = A.u + 10;
        }
        """
        expect = "Illegal Constant Expression: BinaryOp(+,FieldAccess(Id(A),Id(u)),IntLit(10))"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_24(self):
        input = """
        class A
        {
            int x = 6;
        }
        class B extends A
        {
            final float y = -(2 + 3);
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(y),FloatType,UnaryOp(-,BinaryOp(+,IntLit(2),IntLit(3))))"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_25(self):
        input = """
        class A
        {
            int x = 6;
        }
        class B extends A
        {
            final int y = -(2 + x);
        }
        """
        expect = "Illegal Constant Expression: UnaryOp(-,BinaryOp(+,IntLit(2),Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_26(self):
        input = """
        class A
        {
            int x = 6;
        }
        class B extends A
        {
            final int y = (2 + x + 7 + 9);
        }
        """
        expect = "Illegal Constant Expression: BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(2),Id(x)),IntLit(7)),IntLit(9))"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_27(self):
        input = """
        class A
        {
            int x = 6;
        }
        class B extends A
        {
            final int y = -(2 + x + 7 + -9);
        }
        """
        expect = "Illegal Constant Expression: UnaryOp(-,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(2),Id(x)),IntLit(7)),UnaryOp(-,IntLit(9))))"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_28(self):
        input = """
        class A {
            int math(int a; int b; float c) {
                float a;
            }
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_29(self):
        input = """
        class A {
            int func(int a; int b) {
                int c = 5;
                int i;
                if 4 == 5 then {
                    for i := 0 to 100 do {continue;}
                    return 5.5;
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(FloatLit(5.5))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_30(self):
        input = """
        class ABC {
            int test() {
                int i, j;
                for i := 0 to 5 do {
                    for j := 0 to 5 do {
                        break;
                    }
                    break;
                }
                break;
            }
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_31(self):
        input = Program(
            [
                ClassDecl(
                    Id("A"),
                    [
                        AttributeDecl(
                            Instance(), VarDecl(Id("a"), ArrayType(5, IntType()))
                        ),
                        AttributeDecl(
                            Instance(),
                            VarDecl(
                                Id("x"),
                                FloatType(),
                                BinaryOp(
                                    "+",
                                    ArrayCell(Id("a"), IntLiteral(0)),
                                    IntLiteral(6),
                                ),
                            ),
                        ),
                        AttributeDecl(
                            Instance(),
                            VarDecl(
                                Id("x"),
                                FloatType(),
                                BinaryOp(
                                    "+",
                                    ArrayCell(Id("a"), FloatLiteral(0.5)),
                                    IntLiteral(7),
                                ),
                            ),
                        ),
                    ],
                )
            ]
        )
        expect = "Redeclared Attribute: x"
        self.assertTrue(TestChecker.test(input, expect, 430))
        
    def test_32(self):
        input = """
        class A 
        {
            int[5] a;
            float x = a[0] + 6;
            int y = a[0.5] + 7;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),FloatLit(0.5))"
        self.assertTrue(TestChecker.test(input, expect, 431))
        
    def test_33(self):
        input = "class a extends b {}"
        expect = "Undeclared Class: b"
        self.assertTrue(TestChecker.test(input, expect, 432))
        
    def test_34(self):
        input = "class a extends b {}"
        expect = "Undeclared Class: b"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_35(self):
        input = "class a {} class a {}"
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_36(self):
        input = """
        class Ex
        {
            int my1Var;
            static float my1Var;
        }"""
        expect = "Redeclared Attribute: my1Var"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_37(self):
        input = """
        class Ex
        {
            final int x = 10.0;
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(x),IntType,FloatLit(10.0))"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_38(self):
        input = """
        class Ex
        {
            void foo()
            {
                continue;
            }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_39(self):
        input = """
        class Ex
        {
            final int x = x;
        }
        """
        expect = "Illegal Constant Expression: Id(x)"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_40(self):
        input = Program(
            [
                ClassDecl(
                    Id("Ex"),
                    [
                        AttributeDecl(
                            Instance(),
                            VarDecl(
                                Id("x"),
                                ArrayType(3, IntType()),
                                ArrayLiteral(
                                    [IntLiteral(2), FloatLiteral(1.2), NullLiteral()]
                                ),
                            ),
                        )
                    ],
                )
            ]
        )
        expect = "Illegal Array Literal: [IntLit(2),FloatLit(1.2),NullLiteral()]"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_41(self):
        input = """
        class a {}
        class b extends a {}
        class a {}
        """
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_42(self):
        input = """
        class ABC
        {
            int x;
            float y;
            static string z;
        }
        class XYZ extends ABC
        {
            float x;
            int y;
            final int[3] z = {1,2,3};
        }
        """
        expect = "Illegal Constant Expression: [IntLit(1),IntLit(2),IntLit(3)]"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_43(self):
        input = """
        class ABC
        {
            int[3] a = {1,2,3};
            final int[3] b = {1,2,3e6};
        }
        """
        expect = "Illegal Array Literal: [IntLit(1),IntLit(2),FloatLit(3000000.0)]"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_44(self):
        input = """
        class ABC
        {
            final float[3] a = {1,2,4};
        }
        """
        expect = "Illegal Constant Expression: [IntLit(1),IntLit(2),IntLit(4)]"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_45(self):
        input = """
        class ABC {
            int test() {
                for i := 0 to 5 do {
                    for j := 0 to 5 do {
                        break;
                    }
                    break;
                }
                break;
            }
        }
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_46(self):
        input = """
        class ABC {
            final float x = 1 + 2.2;
            final float y = 1 + 2;
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(y),FloatType,BinaryOp(+,IntLit(1),IntLit(2)))"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_47(self):
        input = """
        class ABC {
            static int x = 5;
        }
        class XYZ extends ABC {
            float x = 7.7;
            int x = 7.7;
        }
        """
        expect = "Redeclared Attribute: x"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_48(self):
        input = """
        class X
        {
            float x = 5 + 2 + 4.4 + 6 + 7;
            final int y = 1 + a;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_49(self):
        input = "class a extends b {}"
        expect = "Undeclared Class: b"
        self.assertTrue(TestChecker.test(input, expect, 448))
        
    def test_50(self):
        input = """
        class X
        {
            int[5] x = {1,2,3,4,5};
            float x = 7.7;
        }
        """
        expect = "Redeclared Attribute: x"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_51(self):
        input = Program(
            [
                ClassDecl(
                    Id("Ex"),
                    [
                        AttributeDecl(Static(), VarDecl(Id("a"), IntType())),
                        AttributeDecl(
                            Instance(),
                            ConstDecl(
                                Id("x"), IntType(), FieldAccess(Id("Ex"), Id("a"))
                            ),
                        ),
                    ],
                )
            ]
        )
        expect = "Illegal Constant Expression: FieldAccess(Id(Ex),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_52(self):
        input = """
        class Test
        {
            int x;
            int y;
            int z;
            final int u = 5;
            final int v = 5 + u;
            void run(int x; int y; float z) {
                continue;
            }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_53(self):
        input = """
        class ABC {
            void count(int a; int b; A a) {}
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_54(self):
        input = """
        class A {
            int x = 5;
        }
        class B extends A {
            int x = 6;
            int y = 7;
        }
        class C extends B {
            int z = 8;
            final float u = 10 + e;
        }
        """
        expect = "Undeclared Identifier: e"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_55(self):
        input = """
        class ABC {
            int x = 5;
            final int y = 7;
            final static int z = 9;
        }
        class XYZ extends ABC {
            int x = 6 + y;
        }
        class U extends XYZ {
            final int x = x;
        }
        """
        expect = "Illegal Constant Expression: Id(x)"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_56(self):
        input = """
        class A
        {
            int x = 5;
            static int u = 10;
        }
        class B
        {
            A y = new A();
            float z1 = y.x +5.5;
            float z2 = y.x + 5;
            final float u = A.u + 10;
        }
        """
        expect = "Illegal Constant Expression: BinaryOp(+,FieldAccess(Id(A),Id(u)),IntLit(10))"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_57(self):
        input = """
        class A
        {
            int x = 6;
        }
        class B extends A
        {
            final float y = -(2 + 3);
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(y),FloatType,UnaryOp(-,BinaryOp(+,IntLit(2),IntLit(3))))"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_58(self):
        input = """
        class A
        {
            int x = 6;
        }
        class B extends A
        {
            final int y = -(2 + x);
        }
        """
        expect = "Illegal Constant Expression: UnaryOp(-,BinaryOp(+,IntLit(2),Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_59(self):
        input = """
        class A
        {
            int x = 6;
        }
        class B extends A
        {
            final int y = (2 + x + 7 + 9);
        }
        """
        expect = "Illegal Constant Expression: BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(2),Id(x)),IntLit(7)),IntLit(9))"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_60(self):
        input = """
        class A
        {
            int x = 6;
        }
        class B extends A
        {
            final int y = -(2 + x + 7 + -9);
        }
        """
        expect = "Illegal Constant Expression: UnaryOp(-,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(2),Id(x)),IntLit(7)),UnaryOp(-,IntLit(9))))"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_61(self):
        input = """
        class A {
            int math(int a; int b; float c) {
                float a;
            }
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_62(self):
        input = """
        class A {
            int func(int a; int b) {
                int c = 5;
                int i;
                if 4 == 5 then {
                    for i := 0 to 100 do {continue;}
                    return 5.5;
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(FloatLit(5.5))"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_63(self):
        input = """
        class ABC {
            int test() {
                int i, j;
                for i := 0 to 5 do {
                    for j := 0 to 5 do {
                        break;
                    }
                    break;
                }
                break;
            }
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_64(self):
        input = Program(
            [
                ClassDecl(
                    Id("A"),
                    [
                        AttributeDecl(
                            Instance(), VarDecl(Id("a"), ArrayType(5, IntType()))
                        ),
                        AttributeDecl(
                            Instance(),
                            VarDecl(
                                Id("x"),
                                FloatType(),
                                BinaryOp(
                                    "+",
                                    ArrayCell(Id("a"), IntLiteral(0)),
                                    IntLiteral(6),
                                ),
                            ),
                        ),
                        AttributeDecl(
                            Instance(),
                            VarDecl(
                                Id("x"),
                                FloatType(),
                                BinaryOp(
                                    "+",
                                    ArrayCell(Id("a"), FloatLiteral(0.5)),
                                    IntLiteral(7),
                                ),
                            ),
                        ),
                    ],
                )
            ]
        )
        expect = "Redeclared Attribute: x"
        self.assertTrue(TestChecker.test(input, expect, 463))
        
    def test_65(self):
        input = """
        class A 
        {
            int[5] a;
            float x = a[0] + 6;
            int y = a[0.5] + 7;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),FloatLit(0.5))"
        self.assertTrue(TestChecker.test(input, expect, 464))
        
    def test_66(self):
        input = "class a extends b {}"
        expect = "Undeclared Class: b"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_67(self):
        input = "class a extends b {}"
        expect = "Undeclared Class: b"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_68(self):
        input = "class a {} class a {}"
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_69(self):
        input = """
        class Ex
        {
            int my1Var;
            static float my1Var;
        }"""
        expect = "Redeclared Attribute: my1Var"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_70(self):
        input = """
        class Ex
        {
            final int x = 10.0;
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(x),IntType,FloatLit(10.0))"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_71(self):
        input = """
        class Ex
        {
            void foo()
            {
                continue;
            }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_72(self):
        input = """
        class Ex
        {
            final int x = x;
        }
        """
        expect = "Illegal Constant Expression: Id(x)"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_73(self):
        input = Program(
            [
                ClassDecl(
                    Id("Ex"),
                    [
                        AttributeDecl(
                            Instance(),
                            VarDecl(
                                Id("x"),
                                ArrayType(3, IntType()),
                                ArrayLiteral(
                                    [IntLiteral(2), FloatLiteral(1.2), NullLiteral()]
                                ),
                            ),
                        )
                    ],
                )
            ]
        )
        expect = "Illegal Array Literal: [IntLit(2),FloatLit(1.2),NullLiteral()]"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_74(self):
        input = """
        class a {}
        class b extends a {}
        class a {}
        """
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_75(self):
        input = """
        class ABC
        {
            int x;
            float y;
            static string z;
        }
        class XYZ extends ABC
        {
            float x;
            int y;
            final int[3] z = {1,2,3};
        }
        """
        expect = "Illegal Constant Expression: [IntLit(1),IntLit(2),IntLit(3)]"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_76(self):
        input = """
        class ABC
        {
            int[3] a = {1,2,3};
            final int[3] b = {1,2,3e6};
        }
        """
        expect = "Illegal Array Literal: [IntLit(1),IntLit(2),FloatLit(3000000.0)]"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_77(self):
        input = """
        class ABC
        {
            final float[3] a = {1,2,4};
        }
        """
        expect = "Illegal Constant Expression: [IntLit(1),IntLit(2),IntLit(4)]"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_78(self):
        input = """
        class ABC {
            int test() {
                for i := 0 to 5 do {
                    for j := 0 to 5 do {
                        break;
                    }
                    break;
                }
                break;
            }
        }
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_79(self):
        input = """
        class ABC {
            final float x = 1 + 2.2;
            final float y = 1 + 2;
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(y),FloatType,BinaryOp(+,IntLit(1),IntLit(2)))"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_80(self):
        input = """
        class ABC {
            static int x = 5;
        }
        class XYZ extends ABC {
            float x = 7.7;
            int x = 7.7;
        }
        """
        expect = "Redeclared Attribute: x"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_81(self):
        input = """
        class X
        {
            float x = 5 + 2 + 4.4 + 6 + 7;
            final int y = 1 + a;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_82(self):
        input = "class a extends b {}"
        expect = "Undeclared Class: b"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_83(self):
        input = """
        class X
        {
            int[5] x = {1,2,3,4,5};
            float x = 7.7;
        }
        """
        expect = "Redeclared Attribute: x"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_84(self):
        input = Program(
            [
                ClassDecl(
                    Id("Ex"),
                    [
                        AttributeDecl(Static(), VarDecl(Id("a"), IntType())),
                        AttributeDecl(
                            Instance(),
                            ConstDecl(
                                Id("x"), IntType(), FieldAccess(Id("Ex"), Id("a"))
                            ),
                        ),
                    ],
                )
            ]
        )
        expect = "Illegal Constant Expression: FieldAccess(Id(Ex),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_85(self):
        input = """
        class Test
        {
            int x;
            int y;
            int z;
            final int u = 5;
            final int v = 5 + u;
            void run(int x; int y; float z) {
                continue;
            }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_86(self):
        input = """
        class ABC {
            void count(int a; int b; A a) {}
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_87(self):
        input = """
        class A {
            int x = 5;
        }
        class B extends A {
            int x = 6;
            int y = 7;
        }
        class C extends B {
            int z = 8;
            final float u = 10 + e;
        }
        """
        expect = "Undeclared Identifier: e"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_88(self):
        input = """
        class ABC {
            int x = 5;
            final int y = 7;
            final static int z = 9;
        }
        class XYZ extends ABC {
            int x = 6 + y;
        }
        class U extends XYZ {
            final int x = x;
        }
        """
        expect = "Illegal Constant Expression: Id(x)"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_89(self):
        input = """
        class A
        {
            int x = 5;
            static int u = 10;
        }
        class B
        {
            A y = new A();
            float z1 = y.x +5.5;
            float z2 = y.x + 5;
            final float u = A.u + 10;
        }
        """
        expect = "Illegal Constant Expression: BinaryOp(+,FieldAccess(Id(A),Id(u)),IntLit(10))"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_90(self):
        input = """
        class A
        {
            int x = 6;
        }
        class B extends A
        {
            final float y = -(2 + 3);
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(y),FloatType,UnaryOp(-,BinaryOp(+,IntLit(2),IntLit(3))))"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_91(self):
        input = """
        class A
        {
            int x = 6;
        }
        class B extends A
        {
            final int y = -(2 + x);
        }
        """
        expect = "Illegal Constant Expression: UnaryOp(-,BinaryOp(+,IntLit(2),Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_92(self):
        input = """
        class A
        {
            int x = 6;
        }
        class B extends A
        {
            final int y = (2 + x + 7 + 9);
        }
        """
        expect = "Illegal Constant Expression: BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(2),Id(x)),IntLit(7)),IntLit(9))"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_93(self):
        input = """
        class A
        {
            int x = 6;
        }
        class B extends A
        {
            final int y = -(2 + x + 7 + -9);
        }
        """
        expect = "Illegal Constant Expression: UnaryOp(-,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(2),Id(x)),IntLit(7)),UnaryOp(-,IntLit(9))))"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_94(self):
        input = """
        class A {
            int math(int a; int b; float c) {
                float a;
            }
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_95(self):
        input = """
        class A {
            int func(int a; int b) {
                int c = 5;
                int i;
                if 4 == 5 then {
                    for i := 0 to 100 do {continue;}
                    return 5.5;
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(FloatLit(5.5))"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_96(self):
        input = """
        class ABC {
            int test() {
                int i, j;
                for i := 0 to 5 do {
                    for j := 0 to 5 do {
                        break;
                    }
                    break;
                }
                break;
            }
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_97(self):
        input = Program(
            [
                ClassDecl(
                    Id("A"),
                    [
                        AttributeDecl(
                            Instance(), VarDecl(Id("a"), ArrayType(5, IntType()))
                        ),
                        AttributeDecl(
                            Instance(),
                            VarDecl(
                                Id("x"),
                                FloatType(),
                                BinaryOp(
                                    "+",
                                    ArrayCell(Id("a"), IntLiteral(0)),
                                    IntLiteral(6),
                                ),
                            ),
                        ),
                        AttributeDecl(
                            Instance(),
                            VarDecl(
                                Id("x"),
                                FloatType(),
                                BinaryOp(
                                    "+",
                                    ArrayCell(Id("a"), FloatLiteral(0.5)),
                                    IntLiteral(7),
                                ),
                            ),
                        ),
                    ],
                )
            ]
        )
        expect = "Redeclared Attribute: x"
        self.assertTrue(TestChecker.test(input, expect, 496))
        
    def test_98(self):
        input = """
        class A 
        {
            int[5] a;
            float x = a[0] + 6;
            int y = a[0.5] + 7;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),FloatLit(0.5))"
        self.assertTrue(TestChecker.test(input, expect, 497))
        
    def test_99(self):
        input = "class a extends b {}"
        expect = "Undeclared Class: b"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_100(self):
        input = "class a extends b {}"
        expect = "Undeclared Class: b"
        self.assertTrue(TestChecker.test(input, expect, 499))