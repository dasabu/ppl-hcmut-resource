import unittest
from TestUtils import TestAST
from AST import *

# ~ Test distribution:
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

class ASTGenSuite(unittest.TestCase):
    def test0(self):
        """Simple program: class main {} """
        input = """class main {}"""
        expect = str(Program([ClassDecl(Id("main"),[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test1(self):
        input = """class Shape{
            int main(){
                int x, y;
                final float z, y = 1e9, a = 1.0;
                string abc, xyz = 1;
            }
        }"""
        expect = str(
            Program(
                [ClassDecl(
                    Id("Shape"),
                    [MethodDecl(
                        Instance(),
                        Id("main"),
                        [],
                        IntType(),
                        Block(
                            [
                                VarDecl(Id("x"), IntType(), None),
                                VarDecl(Id("y"), IntType(), None),
                                ConstDecl(Id("z"), FloatType(), FloatLiteral(1e9)),
                                ConstDecl(Id("y"), FloatType(), FloatLiteral(1e9)),
                                ConstDecl(Id("a"), FloatType(), FloatLiteral(1.0)),
                                VarDecl(Id("abc"), StringType(), IntLiteral(1)),
                                VarDecl(Id("xyz"), StringType(), IntLiteral(1))
                            ],
                            [])
                    )]
                )]
            )
        )
        self.assertTrue(TestAST.test(input,expect,301))

    def test2(self):
        input = """
        class test{
            static void support(int f; float a, b, c; boolean x, y) {}
            int main(){}
        }"""
        expect = str(
            Program(
                [ClassDecl(
                    Id("test"),
                    [MethodDecl(
                        Static(),
                        Id("support"),
                        [VarDecl(Id("f"), IntType(), None),
                         VarDecl(Id("a"), FloatType(), None),
                         VarDecl(Id("b"), FloatType(), None),
                         VarDecl(Id("c"), FloatType(), None),
                         VarDecl(Id("x"), BoolType(), None),
                         VarDecl(Id("y"), BoolType(), None)
                         ],
                        VoidType(),
                        Block(
                            [],
                            []
                        )
                    ),
                    MethodDecl(
                        Instance(),
                        Id("main"),
                        [],
                        IntType(),
                        Block(
                            [], 
                            []
                        )
                    )
                    ]
                )]
            )
        )
        self.assertTrue(TestAST.test(input,expect,302))
    
    def test3(self):
        input = """
        class Test extends Test0{
            int x, y = 10, a;
            final boolean f = true;
            final static int g = !f;
            static float main(){
                a := f ^ g;
                f := !g;
            }
            static string b;
            static final int xyz = b;
            int main2(int x){
                
            }
        }
        """
        expect = str(
            Program(
                [ClassDecl(
                    Id("Test"),
                    [
                        AttributeDecl(Instance(), VarDecl(Id("x"), IntType(), IntLiteral(10))),
                        AttributeDecl(Instance(), VarDecl(Id("y"), IntType(), IntLiteral(10))),
                        AttributeDecl(Instance(), VarDecl(Id("a"), IntType(), None)),
                        AttributeDecl(Instance(), ConstDecl(Id("f"), BoolType(), BooleanLiteral(True))),
                        AttributeDecl(Static(), ConstDecl(Id("g"), IntType(), UnaryOp("!", Id("f")))),
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            FloatType(),
                            Block(
                                [], 
                                [Assign(Id("a"), BinaryOp("^", Id("f"), Id("g"))),
                                 Assign(Id("f"), UnaryOp("!", Id("g")))]
                            )
                        ),
                        AttributeDecl(Static(), VarDecl(Id("b"), StringType(), None)),
                        AttributeDecl(Static(), ConstDecl(Id("xyz"), IntType(), Id("b"))),
                        MethodDecl(
                            Instance(),
                            Id("main2"),
                            [VarDecl(Id("x"), IntType(), None)],
                            IntType(),
                            Block(
                                [],
                                []
                            )
                        )
                    ],
                    Id("Test0")
                )]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 303))

    def test4(self):
        input = """
        class test{
            int x = 10, a;
        }
        """
        expect = str(
            Program(
                [ClassDecl(
                    Id("test"),
                    [
                    AttributeDecl(Instance(), VarDecl(Id("x"), IntType(), IntLiteral(10))),
                    AttributeDecl(Instance(), VarDecl(Id("a"), IntType(), None)),
                    ]
                )]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 304))
        
    def test5(self):
        input = """
        class Test5{
            int set(int val){
                int x;
                x := -val;
                return x;
            }
        }
        """
        expect = str(
            Program(
                [ClassDecl(
                    Id("Test5"),
                    [MethodDecl(
                        Instance(),
                        Id("set"),
                        [VarDecl(Id("val"), IntType(), None)],
                        IntType(),
                        Block(
                            [VarDecl(Id("x"), IntType(), None)],
                            [
                                Assign(Id("x"), UnaryOp("-", Id("val"))),
                                Return(Id("x"))
                            ]
                        )
                    )]
                )]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 305))
    
    def test6(self):
        input = """class Test{ 
            void testing(int max){
                int x;
                final int y = x;
                for i := 1 to x do {
                    y := x + i;
                    if y > max then max := y;
                    else continue;
                }
            }
        }
        """
        expect = str(
            Program(
                [ClassDecl(
                    Id("Test"),
                    [MethodDecl(
                        Instance(),
                        Id("testing"),
                        [VarDecl(Id("max"), IntType(), None)],
                        VoidType(),
                        Block(
                            [
                                VarDecl(Id("x"), IntType(), None),
                                ConstDecl(Id("y"), IntType(), Id("x"))
                            ],
                            [
                                For(Id("i"),
                                    IntLiteral(1),
                                    Id("x"),
                                    True,
                                    Block(
                                        [],
                                        [
                                            Assign(Id("y"), BinaryOp("+", Id("x"), Id("i"))),
                                            If(BinaryOp(">", Id("y"), Id("max")), Assign(Id("max"), Id("y")), Continue())
                                        ]
                                    )
                                    )
                            ]
                        )
                    )]
                )]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 306))
    
    def test7(self):
        input = """
        class Main{
            void test(){
                for i := 1 to 10 do {
                    int y;
                    y := i;
                    final int i = -y;
                    break;
                    if max < i then max := i;
                    else continue;
                }
            }
        }
        """
        expect = str(
            Program(
                [ClassDecl(
                    Id("Main"),
                    [MethodDecl(
                        Instance(),
                        Id("test"),
                        [],
                        VoidType(),
                        Block(
                            [],
                            [For(Id("i"), 
                                 IntLiteral(1), 
                                 IntLiteral(10), 
                                 True, 
                                 Block(
                                     [
                                        VarDecl(Id("y"), IntType()),
                                        ConstDecl(Id("i"), IntType(), UnaryOp("-", Id("y")))
                                     ],
                                     [
                                        Assign(Id("y"), Id("i")),
                                        Break(),
                                        If(BinaryOp("<", Id("max"), Id("i")), Assign(Id("max"), Id("i")), Continue())
                                     ]
                                 )
                                 )
                             ]
                        )
                    )]
                )]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 307))
    
    def test8(self):
        input = """
        class Test{
            static void main(){
                int x, y;
                y := 1;
                if y > max then max := i;
                else continue;
                y := i;
                final int x, z = true;
            }
        }
        """
        expect = str(
            Program(
                [ClassDecl(
                    Id("Test"),
                    [MethodDecl(
                        Static(),
                        Id("main"),
                        [],
                        VoidType(),
                        Block(
                            [
                                VarDecl(Id("x"), IntType()),
                                VarDecl(Id("y"), IntType()),
                                ConstDecl(Id("x"), IntType(), BooleanLiteral(True)),
                                ConstDecl(Id("z"), IntType(), BooleanLiteral(True))
                            ], 
                            [
                                Assign(Id("y"), IntLiteral(1)),
                                If(BinaryOp(">", Id("y"), Id("max")), Assign(Id("max"), Id("i")), Continue()),
                                Assign(Id("y"), Id("i"))
                            ]
                        )
                    )]
                )]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 308))
    
    def test9(self):
        input = """
        class Test{
            int x, y = 10, a, b, d = 1 + 2, c;
        }
        """
        expect = str(
            Program(
                [ClassDecl(
                    Id("Test"),
                    [
                        AttributeDecl(
                            Instance(), 
                            VarDecl(Id("x"), IntType() ,IntLiteral(10))
                        ),
                        AttributeDecl(
                            Instance(),
                            VarDecl(Id("y"), IntType(), IntLiteral(10))
                        ),
                        AttributeDecl(
                            Instance(), 
                            VarDecl(Id("a"), IntType(), BinaryOp("+", IntLiteral(1), IntLiteral(2)))
                        ),
                        AttributeDecl(
                            Instance(), 
                            VarDecl(Id("b"), IntType(), BinaryOp("+", IntLiteral(1), IntLiteral(2)))
                        ),
                        AttributeDecl(
                            Instance(), 
                            VarDecl(Id("d"), IntType(), BinaryOp("+", IntLiteral(1), IntLiteral(2)))
                        ),
                        AttributeDecl(
                            Instance(), 
                            VarDecl(Id("c"), IntType(), None)
                        )
                    ]
                )]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 309))
    
    def test10(self):
        input = """
        class AttriTest{
            final int x = 10, a, b = 2.0, d = true;
            static int x, y = 10, z, f;
        }
        """
        expect = str(
            Program(
                [ClassDecl(
                    Id("AttriTest"),
                    [
                        AttributeDecl(
                            Instance(),
                            ConstDecl(Id("x"), IntType(), IntLiteral(10))
                        ),
                        AttributeDecl(
                            Instance(),
                            ConstDecl(Id("a"), IntType(), FloatLiteral(2.0))
                        ),
                        AttributeDecl(
                            Instance(),
                            ConstDecl(Id("b"), IntType(), FloatLiteral(2.0))
                        ),
                        AttributeDecl(
                            Instance(),
                            ConstDecl(Id("d"), IntType(), BooleanLiteral(True))
                        ),
                        AttributeDecl(
                            Static(),
                            VarDecl(Id("x"), IntType(), IntLiteral(10))
                        ),
                        AttributeDecl(
                            Static(),
                            VarDecl(Id("y"), IntType(), IntLiteral(10))
                        ),
                        AttributeDecl(
                            Static(),
                            VarDecl(Id("z"), IntType(), None)
                        ),
                        AttributeDecl(
                            Static(),
                            VarDecl(Id("f"), IntType())
                        )
                    ])
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 310))
    
    def test11(self):
        input = """
        class Example1{
            int factorial(int n){
                if n == 1 then return 1;
                else return n * this.factorial(n-1);
            }
        }
        """
        expect = str(
            Program(
                [ClassDecl(
                    Id("Example1"),
                    [MethodDecl(
                        Instance(),
                        Id("factorial"),
                        [VarDecl(Id("n"), IntType())],
                        IntType(),
                        Block(
                            [],
                            [
                                If(
                                    BinaryOp("==", Id("n"), IntLiteral(1)),
                                    Return(IntLiteral(1)),
                                    Return(
                                        BinaryOp("*",
                                                Id("n"),
                                                CallExpr(
                                                    SelfLiteral(),
                                                    Id("factorial"),
                                                    [
                                                        BinaryOp("-", Id("n"), IntLiteral(1))
                                                    ]
                                                )
                                                )
                                    )
                                )
                            ]
                        )
                    )]
                )]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 311))
    
    def test12(self):
        input = """
        class Shape {
            float length,width;
            float getArea() {
                
            } 
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
        
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Shape"),
                        [
                            AttributeDecl(
                                Instance(), 
                                VarDecl(Id("length"), FloatType())
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("width"), FloatType())
                            ),
                            MethodDecl(
                                Instance(),
                                Id("getArea"),
                                [],
                                FloatType(),
                                Block(
                                    [],
                                    []
                                )
                            ),
                            MethodDecl(
                                Instance(),
                                Id("<init>"),
                                [
                                    VarDecl(Id("length"), FloatType()),
                                    VarDecl(Id("width"), FloatType())
                                ],
                                None,
                                Block(
                                    [],
                                    [
                                        Assign(
                                            FieldAccess(
                                                SelfLiteral(),
                                                Id("length")
                                            ),
                                            Id("length")
                                        ),
                                        Assign(
                                            FieldAccess(
                                                SelfLiteral(),
                                                Id("width")
                                            ),
                                            Id("width")
                                        )
                                    ]
                                )
                            ),
                        ]
                    ),
                    ClassDecl(
                        Id("Rectangle"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("getArea"),
                                [],
                                FloatType(),
                                Block(
                                    [],
                                    [
                                        Return(
                                            BinaryOp(
                                                "*",
                                                FieldAccess(
                                                    SelfLiteral(),
                                                    Id("length")
                                                ),
                                                FieldAccess(
                                                    SelfLiteral(),
                                                    Id("width")
                                                )
                                            )
                                        )
                                    ]
                                )
                            )
                        ],
                        Id("Shape")
                    ),
                    ClassDecl(
                        Id("Triangle"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("getArea"),
                                [],
                                FloatType(),
                                Block(
                                    [],
                                    [
                                        Return(
                                            BinaryOp(
                                                "/",
                                                BinaryOp(
                                                    "*",
                                                    FieldAccess(
                                                        SelfLiteral(),
                                                        Id("length")
                                                    ),
                                                    FieldAccess(
                                                        SelfLiteral(),
                                                        Id("width")
                                                    )
                                                ),
                                                IntLiteral(2)
                                            )
                                        )
                                    ]
                                )
                            )
                        ],
                        Id("Shape")
                    ),
                    ClassDecl(
                        Id("Example2"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("main"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("s"),
                                            ClassType(Id("Shape"))
                                        )
                                    ],
                                    [
                                        Assign(
                                            Id("s"),
                                            NewExpr(
                                                Id("Rectangle"),
                                                [
                                                    IntLiteral(3),
                                                    IntLiteral(4)
                                                ]
                                            )
                                        ),
                                        CallStmt(
                                            Id("io"),
                                            Id("writeFloatLn"),
                                            [
                                                CallExpr(
                                                    Id("s"),
                                                    Id("getArea"),
                                                    []
                                                )
                                            ]
                                        ),
                                        Assign(
                                            Id("s"),
                                            NewExpr(
                                                Id("Triangle"),
                                                [
                                                    IntLiteral(3),
                                                    IntLiteral(4)
                                                ]
                                            )
                                        ),
                                        CallStmt(
                                            Id("io"),
                                            Id("writeFloatLn"),
                                            [
                                                CallExpr(
                                                    Id("s"),
                                                    Id("getArea"),
                                                    []
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 312))
    
    def test13(self):
        input = """
        class ArrayTest {
            final int[5] arr = {1,2,3,4,5};
            static float[1] ar = {1.0,2e2};
            Shape[10] sh;
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("ArrayTest"),
                        [
                            AttributeDecl(
                                Instance(),
                                ConstDecl(
                                    Id("arr"),
                                    ArrayType(5, IntType()),
                                    ArrayLiteral(
                                        [
                                            IntLiteral(1),
                                            IntLiteral(2),
                                            IntLiteral(3),
                                            IntLiteral(4),
                                            IntLiteral(5)
                                        ]
                                    )
                                )
                            ),
                            AttributeDecl(
                                Static(),
                                VarDecl(
                                    Id("ar"),
                                    ArrayType(1, FloatType()),
                                    ArrayLiteral(
                                        [
                                            FloatLiteral(1.0),
                                            FloatLiteral(2e2)
                                        ]
                                    )
                                )
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("sh"),
                                    ArrayType(10, ClassType(Id("Shape"))),
                                    None
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 313))
    
    def test14(self):
        input = """
        class Test{
            Test(Shape n){
                for i := 0 to arr.getLength() do {
                    this.arr[i] := i + arr.getVal(i % 10);
                }
            }
            static void printArr(){
                for i := 0 to (1 + 1 == 2) do {
                    int x = 10, a, b;
                    io.print(this.arr[i % 2]);
                    a := x;
                    if b == nil then b := a;
                    else {
                        final float z = a[3];
                        b := -z;
                    }
                }
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("<init>"),
                                [VarDecl(Id("n"), ClassType(Id("Shape")))],
                                None,
                                Block(
                                    [],
                                    [
                                        For(
                                            Id("i"),
                                            IntLiteral(0),
                                            CallExpr(
                                                Id("arr"),
                                                Id("getLength"),
                                                []
                                            ),
                                            True,
                                            Block(
                                                [],
                                                [
                                                    Assign(
                                                        ArrayCell(
                                                            FieldAccess(
                                                                SelfLiteral(),
                                                                Id("arr")
                                                            ),
                                                            Id("i")
                                                        ),
                                                        BinaryOp(
                                                            "+",
                                                            Id("i"),
                                                            CallExpr(
                                                                Id("arr"),
                                                                Id("getVal"),
                                                                [
                                                                    BinaryOp(
                                                                        "%",
                                                                        Id("i"),
                                                                        IntLiteral(10)
                                                                    )
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    
                                                ]
                                            )
                                        )
                                    ]
                                )
                            ),
                            MethodDecl(
                                Static(),
                                Id("printArr"),
                                [],
                                VoidType(),
                                Block(
                                    [],
                                    [
                                        For(
                                            Id("i"),
                                            IntLiteral(0),
                                            BinaryOp("==", BinaryOp("+", IntLiteral(1), IntLiteral(1)), IntLiteral(2)),
                                            True,
                                            Block(
                                                [
                                                    VarDecl(Id("x"), IntType(), IntLiteral(10)),
                                                    VarDecl(Id("a"), IntType()),
                                                    VarDecl(Id("b"), IntType())
                                                ],
                                                [
                                                    CallStmt(
                                                        Id("io"),
                                                        Id("print"),
                                                        [
                                                            ArrayCell(
                                                                FieldAccess(
                                                                    SelfLiteral(),
                                                                    Id("arr")
                                                                ),
                                                                BinaryOp("%", Id("i"), IntLiteral(2))
                                                            )
                                                        ]
                                                    ),
                                                    Assign(Id("a"), Id("x")),
                                                    If(
                                                        BinaryOp("==", Id("b"), NullLiteral()),
                                                        Assign(Id("b"), Id("a")),
                                                        Block(
                                                            [
                                                                ConstDecl(Id("z"), FloatType(), ArrayCell(Id("a"), IntLiteral(3)))
                                                            ],
                                                            [
                                                                Assign(Id("b"), UnaryOp("-", Id("z")))
                                                            ]
                                                        )
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 314))

    # ! Class only
    def test15(self):
        input = """
        class Test15{
            
        }
        """
        expect = str(Program([ClassDecl(Id("Test15"), [])]))
        self.assertTrue(TestAST.test(input, expect, 315))
    
    def test16(self):
        input = """
        class Test16_1{
            
        }
        class Test16_2 {}
        class Test16_3         {}
        class Test16_4 { # This is line comment }
        class Test16_5 {
            /* This is
            block
            comment */
        }
        """
        expect = str(Program([
                                ClassDecl(Id("Test16"), []),
                                ClassDecl(Id("Test16_2"), []),
                                ClassDecl(Id("Test16_3"), []),
                                ClassDecl(Id("Test16_4"), []),
                                ClassDecl(Id("Test16_5"), [])
                            ]))
    
    def test17(self):
        input = """
        class Test{
            
        }
        class t extends Test {
            
        }
        class ttt extends t {
            # something here i dont know
            
            
            /* hehe
            keke
            */
        }
        class x extends Test {}
        """
        expect = str(
            Program(
                [ClassDecl(Id("Test"), []),
                 ClassDecl(Id("t"), [], Id("Test")),
                 ClassDecl(Id("ttt"), [], Id("t")),
                 ClassDecl(Id("x"), [], Id("Test"))
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 317))
    
    # ! Mutable Attribute 
    def test18(self):
        input = """
        class Test {
            int x, y = 10, z, y;
            static float z = this.x[1 + 2], y;
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("x"), IntType(), IntLiteral(10))
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("y"), IntType(), IntLiteral(10))
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("z"), IntType())
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("y"), IntType())
                            ),
                            AttributeDecl(
                                Static(),
                                VarDecl(
                                    Id("z"),
                                    FloatType(),
                                    ArrayCell(
                                        FieldAccess(
                                            SelfLiteral(),
                                            Id("x")
                                        ),
                                        BinaryOp("+", IntLiteral(1), IntLiteral(2))
                                    )
                                )
                            ),
                            AttributeDecl(
                                Static(),
                                VarDecl(Id("y"), FloatType())
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 318))

    def test19(self):
        input = """
        class Test { }
        class Child extends Test{
            int x, y = this.a(-(1+2), true, "hehe" ^ "hihi"), a;
            static boolean z, t = this.a[3], m = this.a, n;
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        []
                    ),
                    ClassDecl(
                        Id("Child"),
                        [
                            AttributeDecl(
                                Instance(), 
                                VarDecl(
                                    Id("x"),
                                    IntType(),
                                    CallExpr(
                                        SelfLiteral(),
                                        Id("a"),
                                        [
                                            UnaryOp("-", BinaryOp("+", IntLiteral(1), IntLiteral(2))),
                                            BooleanLiteral(True),
                                            BinaryOp("^", StringLiteral("hehe"), StringLiteral("hihi"))
                                        ]
                                    )
                                )
                            ),
                            AttributeDecl(
                                Instance(), 
                                VarDecl(
                                    Id("y"),
                                    IntType(),
                                    CallExpr(
                                        SelfLiteral(),
                                        Id("a"),
                                        [
                                            UnaryOp("-", BinaryOp("+", IntLiteral(1), IntLiteral(2))),
                                            BooleanLiteral(True),
                                            BinaryOp("^", StringLiteral("hehe"), StringLiteral("hihi"))
                                        ]
                                    )
                                )
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("a"), IntType())
                            ),
                            AttributeDecl(
                                Static(),
                                VarDecl(
                                    Id("z"),
                                    BoolType(),
                                    ArrayCell(
                                        FieldAccess(
                                            SelfLiteral(),
                                            Id("a")
                                        ),
                                        IntLiteral(3)
                                    )
                                )
                            ),
                            AttributeDecl(
                                Static(),
                                VarDecl(
                                    Id("t"),
                                    BoolType(),
                                    ArrayCell(
                                        FieldAccess(
                                            SelfLiteral(),
                                            Id("a")
                                        ),
                                        IntLiteral(3)
                                    )
                                )
                            ),
                            AttributeDecl(
                                Static(),
                                VarDecl(
                                    Id("m"),
                                    BoolType(),
                                    FieldAccess(
                                        SelfLiteral(),
                                        Id("a")
                                    )
                                )
                            ),
                            AttributeDecl(
                                Static(),
                                VarDecl(
                                    Id("n"),
                                    BoolType()
                                )
                            )                        
                        ],
                        Id("Test")
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 319))
    
    def test20(self):
        input = """
        class Test{
            static Shape[10] s;
            Shape[2] S = {2, 3.0}, sh, as;
        }
        """ 
        expect = str(
            Program(
                [ClassDecl(
                    Id("Test"),
                    [
                        AttributeDecl(
                            Static(),
                            VarDecl(
                                Id("s"),
                                ArrayType(
                                    10,
                                    ClassType(Id("Shape"))
                                )
                            )
                        ),
                        AttributeDecl(
                            Instance(),
                            VarDecl(
                                Id("S"),
                                ArrayType(
                                    2,
                                    ClassType(Id("Shape"))
                                ),
                                ArrayLiteral(
                                    [IntLiteral(2), FloatLiteral(3.0)]
                                )
                            )
                        ),
                        AttributeDecl(
                            Instance(),
                            VarDecl(
                                Id("sh"),
                                ArrayType(
                                    2,
                                    ClassType(Id("Shape"))
                                )
                            )
                        ),
                        AttributeDecl(
                            Instance(),
                            VarDecl(
                                Id("as"),
                                ArrayType(
                                    2,
                                    ClassType(Id("Shape"))
                                )
                            )
                        )
                    ]
                )]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 320))
    
    # ! Immutable Attribute 
    def test21(self):
        input = """
        class Test {
            final int x, y = 10, z = 2.0, t, w = !false;
            final static float s = ((x + y) * 3) / z;
            static final string a = "PPL", b, c = a ^ "isHard";
        }
        """
        expect = str(
            Program(
                [ClassDecl(
                    Id("Test"),
                    [AttributeDecl(
                        Instance(),
                        ConstDecl(
                            Id("x"),
                            IntType(),
                            IntLiteral(10)
                        )
                    ),
                    AttributeDecl(
                        Instance(),
                        ConstDecl(
                            Id("y"),
                            IntType(),
                            IntLiteral(10)
                        )
                    ),
                    AttributeDecl(
                        Instance(),
                        ConstDecl(
                            Id("z"),
                            IntType(),
                            FloatLiteral(2.0)
                        )
                    ),
                    AttributeDecl(
                        Instance(),
                        ConstDecl(
                            Id("t"),
                            IntType(),
                            UnaryOp("!", BooleanLiteral(False))
                        )
                    ),
                    AttributeDecl(
                        Instance(),
                        ConstDecl(
                            Id("w"),
                            IntType(),
                            UnaryOp("!", BooleanLiteral(False))
                        )
                    ),
                    AttributeDecl(
                        Static(),
                        ConstDecl(
                            Id("s"),
                            FloatType(),
                            BinaryOp("/", BinaryOp("*",BinaryOp("+", Id("x"), Id("y")),IntLiteral(3)), Id("z"))
                        )
                    ),
                    AttributeDecl(
                        Static(),
                        ConstDecl(
                            Id("a"),
                            StringType(),
                            StringLiteral("PPL")
                        )
                    ),
                    AttributeDecl(
                        Static(),
                        ConstDecl(
                            Id("b"),
                            StringType(),
                            BinaryOp("^", Id("a"), StringLiteral("isHard"))
                        )
                    ),
                    AttributeDecl(
                        Static(),
                        ConstDecl(
                            Id("c"),
                            StringType(),
                            BinaryOp("^", Id("a"), StringLiteral("isHard"))
                        )
                    )]
                )]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 321))
    
    def test22(self):
        input = """
        class Test {
            final int x = this.arr[3], y, z = this.getVal(1.0,!false);
            final float a, b = this.arr;
            # static final Shape s = new Shape();
            # final static Shape[10] s = {"Tri", "Rec"};
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            AttributeDecl(
                                Instance(),
                                ConstDecl(
                                    Id("x"),
                                    IntType(),
                                    ArrayCell(
                                        FieldAccess(
                                            SelfLiteral(),
                                            Id("arr")
                                        ),
                                        IntLiteral(3)
                                    )
                                )
                            ),
                            AttributeDecl(
                                Instance(),
                                ConstDecl(
                                    Id("y"),
                                    IntType(),
                                    CallExpr(
                                        SelfLiteral(),
                                        Id("getVal"),
                                        [
                                            FloatLiteral(1.0),
                                            UnaryOp("!", BooleanLiteral(False))
                                        ]
                                    )
                                )
                            ),
                            AttributeDecl(
                                Instance(),
                                ConstDecl(
                                    Id("z"),
                                    IntType(),
                                    CallExpr(
                                        SelfLiteral(),
                                        Id("getVal"),
                                        [
                                            FloatLiteral(1.0),
                                            UnaryOp("!", BooleanLiteral(False))
                                        ]
                                    )
                                )
                            ),
                            AttributeDecl(
                                Instance(),
                                ConstDecl(
                                    Id("a"),
                                    FloatType(),
                                    FieldAccess(
                                        SelfLiteral(),
                                        Id("arr")
                                    )
                                )
                            ),
                            AttributeDecl(
                                Instance(),
                                ConstDecl(
                                    Id("b"),
                                    FloatType(),
                                    FieldAccess(
                                        SelfLiteral(),
                                        Id("arr")
                                    )
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 322))
    
    def test23(self):
        input = """
        class test extends parents{
            static final Shape s = new Shape("Square");
            final static Shape[10] s = {"Tri", "Rec"};
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("test"),
                        [
                            AttributeDecl(
                                Static(),
                                ConstDecl(
                                    Id("s"),
                                    ClassType(Id("Shape")),
                                    NewExpr(
                                        Id("Shape"),
                                        [
                                            StringLiteral("Square")
                                        ]
                                    )
                                )
                            ),
                            AttributeDecl(
                                Static(),
                                ConstDecl(
                                    Id("s"),
                                    ArrayType(
                                        10,
                                        ClassType(Id("Shape"))
                                    ),
                                    ArrayLiteral(
                                        [
                                            StringLiteral("Tri"),
                                            StringLiteral("Rec")
                                        ]
                                    )
                                )
                            )
                        ],
                        Id("parents")
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 323))
    
    # ! Method with empty body 
    def test24(self):
        input = """
        class Person{
            void setName(string s){
                
            }
            string getName(){
                
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Person"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("setName"),
                                [VarDecl(Id("s"), StringType())],
                                VoidType(),
                                Block([], [])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("getName"),
                                [],
                                StringType(),
                                Block([], [])
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 324))
    
    def test25(self):
        input = """
        class Test extends Test{
            static int Method(int a, b; float c; boolean e, g){
                
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Static(),
                                Id("Method"),
                                [
                                    VarDecl(Id("a"), IntType()),
                                    VarDecl(Id("b"), IntType()),
                                    VarDecl(Id("c"), FloatType()),
                                    VarDecl(Id("e"), BoolType()),
                                    VarDecl(Id("g"), BoolType())
                                ],
                                IntType(),
                                Block([], [])
                            )
                        ],
                        Id("Test")
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 325))
    
    # ! Method with local declaration: mutable 
    def test26(self):
        input = """
        class Test { 
            int foo(int a, b; float c, d){
                int x, y, z;
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("foo"),
                                [
                                    VarDecl(Id("a"), IntType()),
                                    VarDecl(Id("b"), IntType()),
                                    VarDecl(Id("c"), FloatType()),
                                    VarDecl(Id("d"), FloatType()),
                                ],
                                IntType(),
                                Block(
                                    [
                                        VarDecl(Id("x"), IntType()),
                                        VarDecl(Id("y"), IntType()),
                                        VarDecl(Id("z"), IntType())
                                    ],
                                    []
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 326))
    
    def test27(self):
        input = """
        class Test { 
            int foo(){
                int x, y, z = 10;
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("foo"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        VarDecl(Id("x"), IntType(), IntLiteral(10)),
                                        VarDecl(Id("y"), IntType(), IntLiteral(10)),
                                        VarDecl(Id("z"), IntType(), IntLiteral(10))
                                    ],
                                    []
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 327))
    
    def test28(self):
        input = """
        class Test { 
            int foo(){
                int x = 10, a, b, c = 1 + 2 * 3;
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("foo"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        VarDecl(Id("x"), IntType(), IntLiteral(10)),
                                        VarDecl(Id("a"), IntType(), BinaryOp("+", IntLiteral(1), BinaryOp("*", IntLiteral(2), IntLiteral(3)))),
                                        VarDecl(Id("b"), IntType(), BinaryOp("+", IntLiteral(1), BinaryOp("*", IntLiteral(2), IntLiteral(3)))),
                                        VarDecl(Id("c"), IntType(), BinaryOp("+", IntLiteral(1), BinaryOp("*", IntLiteral(2), IntLiteral(3)))),
                                    ],
                                    []
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 328))
    
    def test29(self):
        input = """
        class Test { 
            int foo(){
                int x = 10, a, b = 1, c, d, e;
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("foo"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        VarDecl(Id("x"), IntType(), IntLiteral(10)),
                                        VarDecl(Id("a"), IntType(), IntLiteral(1)),
                                        VarDecl(Id("b"), IntType(), IntLiteral(1)),
                                        VarDecl(Id("c"), IntType()),
                                        VarDecl(Id("d"), IntType()),
                                        VarDecl(Id("e"), IntType())
                                    ],
                                    []
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 329))
    
    def test30(self):
        input = """
        class Test { 
            int foo(){
                int x = 10, a = 1, c;
                float y;
                string t = "PPL";
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("foo"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        VarDecl(Id("x"), IntType(), IntLiteral(10)),
                                        VarDecl(Id("a"), IntType(), IntLiteral(1)),
                                        VarDecl(Id("c"), IntType()),
                                        VarDecl(Id("y"), FloatType()),
                                        VarDecl(Id("t"), StringType(), StringLiteral("PPL"))
                                    ],
                                    []
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 330))
    
    def test31(self):
        input = """
        class Test { 
            static void foo(){
                Shape s = new Shape();
                Shape[10] s_arr;
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Static(),
                                Id("foo"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        VarDecl(Id("s"), ClassType(Id("Shape")), NewExpr(Id("Shape"), [])),
                                        VarDecl(Id("s_arr"), ArrayType(10, ClassType(Id("Shape"))))
                                    ],
                                    []
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 331))
    
    # ! Method with local declaration: immutable 
    def test32(self):
        input = """
        class Test{
            Shape bar(){
                final int x = 10;
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("bar"),
                                [],
                                ClassType(Id("Shape")),
                                Block(
                                    [
                                        ConstDecl(Id("x"), IntType(), IntLiteral(10))
                                    ],
                                    []
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 332))
    
    def test33(self):
        input = """
        class Test { 
            void bar(){
                final int x, y = 1, z = 10, e, f = 1 + 1;
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("bar"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        ConstDecl(Id("x"), IntType(), IntLiteral(1)),
                                        ConstDecl(Id("y"), IntType(), IntLiteral(1)),
                                        ConstDecl(Id("z"), IntType(), IntLiteral(10)),
                                        ConstDecl(Id("e"), IntType(), BinaryOp("+", IntLiteral(1), IntLiteral(1))),
                                        ConstDecl(Id("f"), IntType(), BinaryOp("+", IntLiteral(1), IntLiteral(1)))
                                    ],
                                    []
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 333))
    
    def test34(self):
        input = """
        class Test { 
            static void bar(){
                final string x = "PPL", y, z = "DA";
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Static(),
                                Id("bar"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        ConstDecl(Id("x"), StringType(), StringLiteral("PPL")),
                                        ConstDecl(Id("y"), StringType(), StringLiteral("DA")),
                                        ConstDecl(Id("z"), StringType(), StringLiteral("DA"))
                                    ],
                                    []
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 334))
    
    def test35(self):
        input = """
        class Test { 
            void bar(){
                final boolean[3] arr = {1,2,3};
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("bar"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        ConstDecl(Id("arr"), ArrayType(3, BoolType()), ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]))
                                    ],
                                    []
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 335))
    
    def test36(self):
        input = """
        class Test { 
            void bar(){
                final Shape s = new Shape("Circle", 3.14);
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("bar"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        ConstDecl(Id("s"), ClassType(Id("Shape")), NewExpr(Id("Shape"), [StringLiteral("Circle"), FloatLiteral(3.14)])),
                                    ],
                                    []
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 336))
    
    # ! Method with assignment statement 
    def test37(self):
        input = """
            class Test{
                int test(){
                    x := 10;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("test"),
                                [],
                                IntType(),
                                Block(
                                    [],
                                    [Assign(Id("x"), IntLiteral(10))]
                                )
                            )
                        ]
                        
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 337))
    
    def test38(self):
        input = """
            class Test{
                int test(){
                    this.x := 1 + 2;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [MethodDecl(
                            Instance(),
                            Id("test"),
                            [],
                            IntType(),
                            Block(
                                [],
                                [
                                    Assign(
                                        FieldAccess(
                                            SelfLiteral(),
                                            Id("x")
                                        ),
                                        BinaryOp(
                                            "+",
                                            IntLiteral(1),
                                            IntLiteral(2)
                                        )
                                    )
                                ]
                            )
                        )]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 338))
    
    def test39(self):
        input = """
        class Test{
            static void test(){
                this.x[0] := 1;
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Static(),
                                Id("test"),
                                [],
                                VoidType(),
                                Block(
                                    [],
                                    [
                                        Assign(
                                            ArrayCell(
                                                FieldAccess(
                                                    SelfLiteral(),
                                                    Id("x")
                                                ),
                                                IntLiteral(0)
                                            ),
                                            IntLiteral(1)
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 339))
    
    def test40(self):
        input = """
        class Test {
            static float test(string hehe){
                this.x := this.getVal(1, "PPL");
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Static(),
                                Id("test"),
                                [VarDecl(Id("hehe"), StringType())],
                                FloatType(),
                                Block(
                                    [],
                                    [
                                        Assign(
                                            FieldAccess(
                                                SelfLiteral(),
                                                Id("x")
                                            ),
                                            CallExpr(
                                                SelfLiteral(),
                                                Id("getVal"),
                                                [
                                                    IntLiteral(1),
                                                    StringLiteral("PPL")
                                                ]
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 340))
    
    def test41(self):
        input = """
        class Test {
            int foo(){
                l[3] := value * 2;
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("foo"),
                                [],
                                IntType(),
                                Block(
                                    [],
                                    [
                                        Assign(
                                            ArrayCell(
                                                Id("l"),
                                                IntLiteral(3)
                                            ),
                                            BinaryOp(
                                                "*",
                                                Id("value"),
                                                IntLiteral(2)
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 341))
    
    # ! If and Assignment statement 
    def test42(self):
        input = """
        class Test {
            void foo(){
                if this.x == true then {}
            }
        }"""
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("foo"),
                                [],
                                VoidType(),
                                Block(
                                    [],
                                    [
                                        If(
                                            BinaryOp(
                                                '==',
                                                FieldAccess(
                                                    SelfLiteral(),
                                                    Id("x")
                                                ),
                                                BooleanLiteral(True)
                                            ),
                                            Block([],[])
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 342))
    
    def test43(self):
        input = """
        class Test {
            void foo(){
                if this.x == true then {}
                else {}
            }
        }"""
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("foo"),
                                [],
                                VoidType(),
                                Block(
                                    [],
                                    [
                                        If(
                                            BinaryOp(
                                                '==',
                                                FieldAccess(
                                                    SelfLiteral(),
                                                    Id("x")
                                                ),
                                                BooleanLiteral(True)
                                            ),
                                            Block([],[]),
                                            Block([],[])
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 343))
    
    def test44(self):
        input = """
        class Test {
            void foo(){
                if this.x % 2 == 1 then isEven := false;
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("foo"),
                                [],
                                VoidType(),
                                Block(
                                    [],
                                    [
                                        If(
                                            BinaryOp(
                                                '==',
                                                BinaryOp(
                                                    '%',
                                                    FieldAccess(
                                                        SelfLiteral(),
                                                        Id("x")
                                                    ),
                                                    IntLiteral(2)
                                                ),
                                                IntLiteral(1)
                                            ),
                                            Assign(
                                                Id("isEven"),
                                                BooleanLiteral(False)
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 344))
    
    def test45(self):
        input = """
        class Test {
            void foo(){
                if this.x % 2 == 1 then isEven := false;
                else isEven := true;
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("foo"),
                                [],
                                VoidType(),
                                Block(
                                    [],
                                    [
                                        If(
                                            BinaryOp(
                                                '==',
                                                BinaryOp(
                                                    '%',
                                                    FieldAccess(
                                                        SelfLiteral(),
                                                        Id("x")
                                                    ),
                                                    IntLiteral(2)
                                                ),
                                                IntLiteral(1)
                                            ),
                                            Assign(
                                                Id("isEven"),
                                                BooleanLiteral(False)
                                            ),
                                            Assign(
                                                Id("isEven"),
                                                BooleanLiteral(True)
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 345))
    
    def test46(self):
        input = """
        class Test {
            void foo(){
                if this.x % 2 == 1 then {
                    isEven := false;
                }
                else {
                    isEven := true;
                }
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("foo"),
                                [],
                                VoidType(),
                                Block(
                                    [],
                                    [
                                        If(
                                            BinaryOp(
                                                '==',
                                                BinaryOp(
                                                    '%',
                                                    FieldAccess(
                                                        SelfLiteral(),
                                                        Id("x")
                                                    ),
                                                    IntLiteral(2)
                                                ),
                                                IntLiteral(1)
                                            ),
                                            Block(
                                                [],
                                                [
                                                    Assign(
                                                        Id("isEven"),
                                                        BooleanLiteral(False)
                                                    )
                                                ]
                                            ),
                                            Block(
                                                [],
                                                [
                                                    Assign(
                                                        Id("isEven"),
                                                        BooleanLiteral(True)
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 346))
    
    def test47(self):
        input = """
        class Test {
            void bar(){
                if this.x % 2 == 1 then {
                    this.isOdd := true;
                    isEven := false;
                }
                else {
                    isEven := true;
                    this.isOdd := false;
                }
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("bar"),
                                [],
                                VoidType(),
                                Block(
                                    [],
                                    [
                                        If(
                                            BinaryOp(
                                                '==',
                                                BinaryOp(
                                                    '%',
                                                    FieldAccess(
                                                        SelfLiteral(),
                                                        Id("x")
                                                    ),
                                                    IntLiteral(2)
                                                ),
                                                IntLiteral(1)
                                            ),
                                            Block(
                                                [],
                                                [
                                                    Assign(
                                                        FieldAccess(
                                                            SelfLiteral(),
                                                            Id("isOdd")
                                                        ),
                                                        BooleanLiteral(True)
                                                    ),
                                                    Assign(
                                                        Id("isEven"),
                                                        BooleanLiteral(False)
                                                    )
                                                    
                                                ]
                                            ),
                                            Block(
                                                [],
                                                [
                                                    Assign(
                                                        Id("isEven"),
                                                        BooleanLiteral(True)
                                                    ),
                                                    Assign(
                                                        FieldAccess(
                                                            SelfLiteral(),
                                                            Id("isOdd")
                                                        ),
                                                        BooleanLiteral(False)
                                                    )
                                                ]
                                            ),
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 347))
    
    def test48(self):
        input = """
        class Test {
            int foo(){
                this.x.arr[1 + 2] := this.x.get();
                if x.arr == 1 then this.x.arr[0] := x.arr;
                else {
                    if this.x.arr == "PPL" then this.x.arr[0] := x.arr;
                    this.arr := x.arr;
                }
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("foo"),
                                [],
                                IntType(),
                                Block(
                                    [],
                                    [
                                        Assign(
                                            ArrayCell(
                                                FieldAccess(
                                                    FieldAccess(
                                                        SelfLiteral(),
                                                        Id("x")
                                                    ),
                                                    Id("arr")
                                                ),
                                                BinaryOp(
                                                    "+",
                                                    IntLiteral(1),
                                                    IntLiteral(2)
                                                )
                                            ),
                                            CallExpr(
                                                FieldAccess(
                                                    SelfLiteral(),
                                                    Id("x")
                                                ),
                                                Id("get"),
                                                []
                                            )
                                        ),
                                        If(
                                            BinaryOp(
                                                "==",
                                                FieldAccess(
                                                    Id("x"),
                                                    Id("arr")
                                                ),
                                                IntLiteral(1)
                                            ),
                                            Assign(
                                                ArrayCell(
                                                    FieldAccess(
                                                        FieldAccess(
                                                            SelfLiteral(),
                                                            Id("x")
                                                        ),
                                                        Id("arr")
                                                    ),
                                                    IntLiteral(0)
                                                ),
                                                FieldAccess(
                                                    Id("x"),
                                                    Id("arr")
                                                )
                                            ),
                                            Block(
                                                [],
                                                [
                                                    If(
                                                        BinaryOp(
                                                            '==',
                                                            FieldAccess(
                                                                FieldAccess(
                                                                    SelfLiteral(),
                                                                    Id("x")
                                                                ),
                                                                Id("arr")
                                                            ),
                                                            StringLiteral("PPL")
                                                        ),
                                                        Assign(
                                                            ArrayCell(
                                                                FieldAccess(
                                                                    FieldAccess(
                                                                        SelfLiteral(),
                                                                        Id("x")
                                                                    ),
                                                                    Id("arr")
                                                                ),
                                                                IntLiteral(0)
                                                            ),
                                                            FieldAccess(
                                                                Id("x"),
                                                                Id("arr")
                                                            )
                                                        )
                                                    ),
                                                    Assign(
                                                        FieldAccess(
                                                            SelfLiteral(),
                                                            Id("arr")
                                                        ),
                                                        FieldAccess(
                                                            Id("x"),
                                                            Id("arr")
                                                        )
                                                    )
                                                ]
                                            )   
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 348))
    
    # ! For statement 
    def test49(self):
        input = """
        class Test {
            string bar(){
                for i := 1 to 10 do {}
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("bar"),
                                [],
                                StringType(),
                                Block(
                                    [],
                                    [
                                        For(
                                            Id("i"),
                                            IntLiteral(1),
                                            IntLiteral(10),
                                            True,
                                            Block([],[])
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 349))
    
    def test50(self):
        input = """
        class Test {
            boolean bar(){
                for i := 10 downto 1 do {}
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("bar"),
                                [],
                                BoolType(),
                                Block(
                                    [],
                                    [
                                        For(
                                            Id("i"),
                                            IntLiteral(10),
                                            IntLiteral(1),
                                            False,
                                            Block([],[])
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 350))
    
    def test51(self):
        input = """
        class Test {
            void foo(int n){
                for i := 0 to n - 1 do {
                    for j := 0 to i do {
                    }
                }
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("foo"),
                                [VarDecl(Id("n"), IntType())],
                                VoidType(),
                                Block(
                                    [],
                                    [
                                        For(
                                            Id("i"),
                                            IntLiteral(0),
                                            BinaryOp(
                                                "-",
                                                Id("n"),
                                                IntLiteral(1)
                                            ),
                                            True,
                                            Block(
                                                [],
                                                [
                                                    For(
                                                        Id("j"),
                                                        IntLiteral(0),
                                                        Id("i"),
                                                        True,
                                                        Block([], [])
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 351))
    
    def test52(self):
        input = """
        class Test {
            int foo(){
                for i := this.size downto 0 do {
                    if i % 2 == 0 then i := i + 1;
                    else {
                        if i % 3 == 0 then i := this.arr[i];
                        else i := this.getValue(i);
                    }
                }
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("foo"),
                                [],
                                IntType(),
                                Block(
                                    [],
                                    [
                                        For(
                                            Id("i"),
                                            FieldAccess(
                                                SelfLiteral(),
                                                Id("size")
                                            ),
                                            IntLiteral(0),
                                            False,
                                            Block(
                                                [],
                                                [
                                                    If(
                                                        BinaryOp(
                                                            '==',
                                                            BinaryOp(
                                                                '%',
                                                                Id('i'),
                                                                IntLiteral(2)
                                                            ),
                                                            IntLiteral(0)
                                                        ),
                                                        Assign(
                                                            Id('i'),
                                                            BinaryOp(
                                                                '+',
                                                                Id('i'),
                                                                IntLiteral(1)
                                                            )
                                                        ),
                                                        Block(
                                                            [],
                                                            [
                                                                If(
                                                                    BinaryOp(
                                                                        '==',
                                                                        BinaryOp(
                                                                            '%',
                                                                            Id('i'),
                                                                            IntLiteral(3)
                                                                        ),
                                                                        IntLiteral(0)
                                                                    ),
                                                                    Assign(
                                                                        Id('i'),
                                                                        ArrayCell(
                                                                            FieldAccess(
                                                                                SelfLiteral(),
                                                                                Id("arr")
                                                                            ),
                                                                            Id('i')
                                                                        )
                                                                    ),
                                                                    Assign(
                                                                        Id("i"),
                                                                        CallExpr(
                                                                            SelfLiteral(),
                                                                            Id('getValue'),
                                                                            [Id('i')]
                                                                        )
                                                                    )
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 352))
    
    def test53(self):
        input =  """
        class Test {
            static void foo(int a, b; float c; float d){
                if this.x.getValue(i) != nil then {
                    for i := 0 to this.getValue(this.x[3], y.arr[0], z.calc(x.arr)) do {
                        i := x.arr[3] * x.get();
                        for j := i to c do {
                            if j == nil then {}
                            else {}
                        }
                    }
                }
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Static(),
                                Id("foo"),
                                [
                                    VarDecl(Id("a"), IntType()),
                                    VarDecl(Id("b"), IntType()),
                                    VarDecl(Id("c"), FloatType()),
                                    VarDecl(Id("d"), FloatType())
                                ],
                                VoidType(),
                                Block(
                                    [],
                                    [
                                        If(
                                            BinaryOp(
                                                '!=',
                                                CallExpr(
                                                    FieldAccess(
                                                        SelfLiteral(),
                                                        Id('x')
                                                    ),
                                                    Id('getValue'),
                                                    [Id('i')]
                                                ),
                                                NullLiteral()
                                            ),
                                            Block(
                                                [],
                                                [
                                                    For(
                                                        Id('i'),
                                                        IntLiteral(0),
                                                        CallExpr(
                                                            SelfLiteral(),
                                                            Id('getValue'),
                                                            [
                                                                ArrayCell(
                                                                    FieldAccess(
                                                                        SelfLiteral(),
                                                                        Id('x')
                                                                    ),
                                                                    IntLiteral(3)
                                                                ),
                                                                ArrayCell(
                                                                    FieldAccess(
                                                                        Id('y'),
                                                                        Id('arr')
                                                                    ),
                                                                    IntLiteral(0)
                                                                ),
                                                                CallExpr(
                                                                    Id('z'),
                                                                    Id('calc'),
                                                                    [
                                                                        FieldAccess(
                                                                            Id('x'),
                                                                            Id('arr')
                                                                        )
                                                                    ]
                                                                )
                                                            ]
                                                        ),
                                                        True,
                                                        Block(
                                                            [],
                                                            [
                                                                Assign(
                                                                    Id('i'),
                                                                    BinaryOp(
                                                                        '*',
                                                                        ArrayCell(
                                                                            FieldAccess(
                                                                                Id('x'),
                                                                                Id('arr')
                                                                            ),
                                                                            IntLiteral(3)
                                                                        ),
                                                                        CallExpr(
                                                                            Id('x'),
                                                                            Id('get'),
                                                                            []
                                                                        )
                                                                    )
                                                                ),
                                                                For(
                                                                    Id('j'),
                                                                    Id('i'),
                                                                    Id('c'),
                                                                    True,
                                                                    Block(
                                                                        [],
                                                                        [
                                                                            If(
                                                                                BinaryOp(
                                                                                    '==',
                                                                                    Id('j'),
                                                                                    NullLiteral()
                                                                                ),
                                                                                Block([], []),
                                                                                Block([], [])
                                                                            )
                                                                        ]
                                                                    )
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ]
                                            )
                                            
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 353))
    
    def test54(self):
        input = """
        class Test {
            void foo(){
                for i := 1 to 10 do {
                    j := i * 10;
                    if j % 3 == true then {
                        for j := j downto 3 do {
                            s := new Shape();
                        }
                    }
                    else {
                        s := nil;
                    }
                }
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("foo"),
                                [],
                                VoidType(),
                                Block(
                                    [],
                                    [
                                        For(
                                            Id('i'),
                                            IntLiteral(1),
                                            IntLiteral(10),
                                            True,
                                            Block(
                                                [],
                                                [
                                                    Assign(
                                                        Id('j'),
                                                        BinaryOp(
                                                            '*',
                                                            Id("i"),
                                                            IntLiteral(10)
                                                        )
                                                    ),
                                                    If(
                                                        BinaryOp(
                                                            '==',
                                                            BinaryOp(
                                                                '%',
                                                                Id('j'),
                                                                IntLiteral(3)
                                                            ),
                                                            BooleanLiteral(True)
                                                        ),
                                                        Block(
                                                            [],
                                                            [
                                                                For(
                                                                    Id('j'),
                                                                    Id('j'),
                                                                    IntLiteral(3),
                                                                    False,
                                                                    Block(
                                                                        [],
                                                                        [
                                                                            Assign(
                                                                                Id('s'),
                                                                                NewExpr(
                                                                                    Id('Shape'),
                                                                                    []
                                                                                )
                                                                            )
                                                                        ]
                                                                    )
                                                                )
                                                            ]
                                                        ),
                                                        Block(
                                                            [],
                                                            [
                                                                Assign(
                                                                    Id('s'),
                                                                    NullLiteral()
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 354))
    
    # ! break, continue, return
    def test55(self):
        input = """
        class Test {
            void foo(int n){
                if n % 2 == 0 then return n;
                else {
                    for i := 0 to n do {
                        if i == this.dp(n) then {
                            i := this.arr[n];
                            break;
                        }
                        else continue;
                    }
                }
                return i * 10;
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id('Test'),
                        [
                            MethodDecl(
                                Instance(),
                                Id("foo"),
                                [VarDecl(Id('n'), IntType())],
                                VoidType(),
                                Block(
                                    [],
                                    [
                                        If(
                                            BinaryOp(
                                                '==',
                                                BinaryOp(
                                                    '%',
                                                    Id("n"),
                                                    IntLiteral(2)
                                                ),
                                                IntLiteral(0)
                                            ),
                                            Return(Id("n")),
                                            Block(
                                                [],
                                                [
                                                    For(
                                                        Id("i"),
                                                        IntLiteral(0),
                                                        Id('n'),
                                                        True,
                                                        Block(
                                                            [],
                                                            [
                                                                If(
                                                                    BinaryOp(
                                                                        '==',
                                                                        Id('i'),
                                                                        CallExpr(
                                                                            SelfLiteral(),
                                                                            Id("dp"),
                                                                            [Id('n')]
                                                                        )
                                                                    ),
                                                                    Block(
                                                                        [],
                                                                        [
                                                                            Assign(
                                                                                Id('i'),
                                                                                ArrayCell(
                                                                                    FieldAccess(
                                                                                        SelfLiteral(),
                                                                                        Id("arr")
                                                                                    ),
                                                                                    Id('n')
                                                                                )
                                                                            ),
                                                                            Break()
                                                                        ]
                                                                    ),
                                                                    Continue()
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ]
                                            )
                                        ),
                                        Return(
                                            BinaryOp(
                                                '*',
                                                Id('i'),
                                                IntLiteral(10)
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 355))
    
    def test56(self):
        input = """
        class Test {
            void foo(){
                return this.n;
                return this.n();
                return n[3];
            }
            static int bar(){
                return nil;
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id('Test'),
                        [
                            MethodDecl(
                                Instance(),
                                Id("foo"),
                                [],
                                VoidType(),
                                Block(
                                    [],
                                    [
                                        Return(
                                            FieldAccess(
                                                SelfLiteral(),
                                                Id('n')
                                            )
                                        ),
                                        Return(
                                            CallExpr(
                                                SelfLiteral(),
                                                Id('n'),
                                                []
                                            )
                                        ),
                                        Return(
                                            ArrayCell(
                                                Id('n'),
                                                IntLiteral(3)
                                            )
                                        )
                                    ]
                                )
                            ),
                            MethodDecl(
                                Static(),
                                Id('bar'),
                                [],
                                IntType(),
                                Block(
                                    [],
                                    [
                                        Return(
                                            NullLiteral()
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 356))
        
    def test57(self):
        input = """
        class Test {
            int foo(){
                break;
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("foo"),
                                [],
                                IntType(),
                                Block(
                                    [],
                                    [Break()]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 357))
    
    def test58(self):
        input = """
        class Test {
            int foo(){
                continue;
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("foo"),
                                [],
                                IntType(),
                                Block(
                                    [],
                                    [Continue()]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 358))
    
    def test59(self):
        input = """
        class Test {
            static void foo(boolean n; string m; Shape s){
                if this.sum == n then{
                    for i := 0 to n - 1 do {
                        this.sum := this.sum + i * i;
                        if this.sum != nil then break;
                        else continue;
                    }
                }
                else this.sum := new Shape("Circle");
                return this.sum.getValue(1);
            }
        }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Test"),
                        [
                            MethodDecl(
                                Static(),
                                Id('foo'),
                                [
                                    VarDecl(Id("n"), BoolType()),
                                    VarDecl(Id("m"), StringType()),
                                    VarDecl(Id("s"), ClassType(Id("Shape")))
                                ],
                                VoidType(),
                                Block(
                                    [],
                                    [
                                        If(
                                            BinaryOp(
                                                '==',
                                                FieldAccess(
                                                    SelfLiteral(),
                                                    Id("sum")
                                                ),
                                                Id('n')
                                            ),
                                            Block(
                                                [],
                                                [
                                                    For(
                                                        Id("i"),
                                                        IntLiteral(0),
                                                        BinaryOp(
                                                            '-',
                                                            Id("n"),
                                                            IntLiteral(1)
                                                        ),
                                                        True,
                                                        Block(
                                                            [],
                                                            [
                                                                Assign(
                                                                    FieldAccess(
                                                                        SelfLiteral(),
                                                                        Id('sum')
                                                                    ),
                                                                    BinaryOp(
                                                                        '+',
                                                                        FieldAccess(
                                                                            SelfLiteral(),
                                                                            Id('sum')
                                                                        ),
                                                                        BinaryOp(
                                                                            '*',
                                                                            Id('i'),
                                                                            Id('i')
                                                                        )
                                                                    )
                                                                ),
                                                                If(
                                                                    BinaryOp(
                                                                        '!=',
                                                                        FieldAccess(
                                                                            SelfLiteral(),
                                                                            Id("sum")
                                                                        ),
                                                                        NullLiteral()
                                                                    ),
                                                                    Break(),
                                                                    Continue()
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ]
                                            ),
                                            Assign(
                                                FieldAccess(
                                                    SelfLiteral(),
                                                    Id('sum')
                                                ),
                                                NewExpr(
                                                    Id("Shape"),
                                                    [StringLiteral("Circle")]
                                                )
                                            )
                                        ),
                                        Return(
                                            CallExpr(
                                                FieldAccess(
                                                    SelfLiteral(),
                                                    Id('sum')
                                                ),
                                                Id('getValue'),
                                                [IntLiteral(1)]
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 359))
    # ! COPY 
    def test60(self):
        input = """
            class hello {
                int zalo, facbook, nikola;
                a(){
                    if notthing then statement := 0;
                }
                aloalo aloalo;
            }
            class goobye {}
        """
        expect = str(Program([ClassDecl(Id("hello"),[AttributeDecl(Instance(),VarDecl(Id("zalo"),IntType())),AttributeDecl(Instance(),VarDecl(Id("facbook"),IntType())),AttributeDecl(Instance(),VarDecl(Id("nikola"),IntType())),MethodDecl(Instance(),Id("<init>"),[],None,Block([],[If(Id("notthing"),Assign(Id("statement"),IntLiteral(0)))])),AttributeDecl(Instance(),VarDecl(Id("aloalo"),ClassType(Id("aloalo"))))],None),ClassDecl(Id("goobye"),[],None)]))
        self.assertTrue(TestAST.test(input, expect, 360))

    def test61(self):
        input = """
          class hello {
          string a(){
          a[2] := 0;
          }
          }

          """
        expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("a"),[],StringType(),Block([],[Assign(ArrayCell(Id("a"),IntLiteral(2)),IntLiteral(0))]))],None)]))
        self.assertTrue(TestAST.test(input, expect, 362))

    def test63(self):
        input = """
          class hello {
            string sting(){
          a[2] := 0;
          }

          }
          class goobye {
          }
          """
        expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("sting"),[],StringType(),Block([],[Assign(ArrayCell(Id("a"),IntLiteral(2)),IntLiteral(0))]))],None),ClassDecl(Id("goobye"),[],None)]))
        self.assertTrue(TestAST.test(input, expect, 363))

    def test64(self):
        input = """
          class hello {
            string a(){
          a := 0;
          }

          }
          class goobye {
          }
          """
        expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("a"),[],StringType(),Block([],[Assign(Id("a"),IntLiteral(0))]))],None),ClassDecl(Id("goobye"),[],None)]))
        self.assertTrue(TestAST.test(input, expect, 364))

    def test65(self):
        input = """
          class hello {
            string strin(){
          a[897] := 0;

          }

          }
          class goobye {
          }
          """
        expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("strin"),[],StringType(),Block([],[Assign(ArrayCell(Id("a"),IntLiteral(897)),IntLiteral(0))]))],None),ClassDecl(Id("goobye"),[],None)]))
        self.assertTrue(TestAST.test(input, expect, 365))

    def test66(self):
        input = """
          class hello {
          a(){
          for baukhiquyen := 0 to mattroi do {}
          }
          }
          class goobye {
          }
          """
        expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("<init>"),[],None,Block([],[For(Id("baukhiquyen"),IntLiteral(0),Id("mattroi"),True,Block([],[]))]))],None),ClassDecl(Id("goobye"),[],None)]))
        self.assertTrue(TestAST.test(input, expect, 366))
    
    def test67(self):
        input = """
          class hello {
          a(){
          {}{}{}{}
          {}{}{}{}{}{}
          }
          }
          class goobye {
          }
          """
        expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("<init>"),[],None,Block([],[Block([],[]),Block([],[]),Block([],[]),Block([],[]),Block([],[]),Block([],[]),Block([],[]),Block([],[]),Block([],[]),Block([],[])]))],None),ClassDecl(Id("goobye"),[],None)]))
        self.assertTrue(TestAST.test(input, expect, 367))

    def test68(self):
        input = """
          class hello {
          int main () {
          a := 6;
          b:= 8;
          if b >= a then return a;
          }
          }
          class goobye {
          }
          """
        expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[Assign(Id("a"),IntLiteral(6)),Assign(Id("b"),IntLiteral(8)),If(BinaryOp(">=",Id("b"),Id("a")),Return(Id("a")))]))],None),ClassDecl(Id("goobye"),[],None)]))
        self.assertTrue(TestAST.test(input, expect, 368))

    def test69(self):
        input = """
          class hello {
          a(){}
          b(){}
          c c ;
          }
          class goobye {
          }
          """
        expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("<init>"),[],None,Block([],[])),MethodDecl(Instance(),Id("<init>"),[],None,Block([],[])),AttributeDecl(Instance(),VarDecl(Id("c"),ClassType(Id("c"))))],None),ClassDecl(Id("goobye"),[],None)]))
        self.assertTrue(TestAST.test(input, expect, 369))

    def test70(self):
        input = """
          class hello {
          a a = a[a] + (a + this);
          }
          class goobye {
          }
          """
        expect = str(Program([ClassDecl(Id("hello"),[AttributeDecl(Instance(),VarDecl(Id("a"),ClassType(Id("a")),BinaryOp("+",ArrayCell(Id("a"),Id("a")),BinaryOp("+",Id("a"),SelfLiteral()))))],None),ClassDecl(Id("goobye"),[],None)]))
        self.assertTrue(TestAST.test(input, expect, 370))

    def test71(self):
        input = """
          class hello {
          a a = a + a - a ;
          }
          class goobye {
          }
          """
        expect = str(Program([ClassDecl(Id("hello"),[AttributeDecl(Instance(),VarDecl(Id("a"),ClassType(Id("a")),BinaryOp("-",BinaryOp("+",Id("a"),Id("a")),Id("a"))))],None),ClassDecl(Id("goobye"),[],None)]))
        self.assertTrue(TestAST.test(input, expect, 371))

    def test72(self):
        input = """
          class hello {
          a a = - a;
          }
          class goobye {
          }
          """
        expect = str(Program([ClassDecl(Id("hello"),[AttributeDecl(Instance(),VarDecl(Id("a"),ClassType(Id("a")),UnaryOp("-",Id("a"))))],None),ClassDecl(Id("goobye"),[],None)]))
        self.assertTrue(TestAST.test(input, expect, 372))

    def test73(self):
        input = """
          class hello {
          a a = + a;
          }
          class goobye {
          }
          """
        expect = str(Program([ClassDecl(Id("hello"),[AttributeDecl(Instance(),VarDecl(Id("a"),ClassType(Id("a")),UnaryOp("+",Id("a"))))],None),ClassDecl(Id("goobye"),[],None)]))
        self.assertTrue(TestAST.test(input, expect, 373))

    def test74(self):
        input = """
          class hello {
          /* asdasdkjdnlqw masd amdw */
          no(){pls stop;
          continue; break; return turn;
          }
          }
          class goobye {
          }
          """
        expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("<init>"),[],None,Block([VarDecl(Id("stop"),ClassType(Id("pls")))],[Continue(),Break(),Return(Id("turn"))]))],None),ClassDecl(Id("goobye"),[],None)]))
        self.assertTrue(TestAST.test(input, expect, 374))

    def test75(self):
        input = """
          class hello {
          aaasd asdasd ,asdasda ;

          }
          class goobye {
          }
          """
        expect = str(Program([ClassDecl(Id("hello"),[AttributeDecl(Instance(),VarDecl(Id("asdasd"),ClassType(Id("aaasd")))),AttributeDecl(Instance(),VarDecl(Id("asdasda"),ClassType(Id("aaasd"))))],None),ClassDecl(Id("goobye"),[],None)]))
        self.assertTrue(TestAST.test(input, expect, 375))

    def test76(self):
        input = """
          class hello {
          a a = 12312,asdasd = 1232,sadasd;

          }
          class goobye {
          }
          """
        expect = str(Program([ClassDecl(Id("hello"),[AttributeDecl(Instance(),VarDecl(Id("a"),ClassType(Id("a")),IntLiteral(12312))),AttributeDecl(Instance(),VarDecl(Id("asdasd"),ClassType(Id("a")),IntLiteral(1232))),AttributeDecl(Instance(),VarDecl(Id("sadasd"),ClassType(Id("a"))))],None),ClassDecl(Id("goobye"),[],None)]))
        self.assertTrue(TestAST.test(input, expect, 376))

    def test77(self):
        input = """
          class hello {
          a a = !!!!!!!!!!!!!!!!!a;
          }
          class goobye {
          }
          """
        expect = str(Program([ClassDecl(Id("hello"),[AttributeDecl(Instance(),VarDecl(Id("a"),ClassType(Id("a")),UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",Id("a"))))))))))))))))))))],None),ClassDecl(Id("goobye"),[],None)]))
        self.assertTrue(TestAST.test(input, expect, 377))

    def test78(self):
        input = """
          class hello {
          a(){
          if thisworld then {} if iff then {}
          }
          }
          class goobye {
          }
          """
        expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("<init>"),[],None,Block([],[If(Id("thisworld"),Block([],[])),If(Id("iff"),Block([],[]))]))],None),ClassDecl(Id("goobye"),[],None)]))
        self.assertTrue(TestAST.test(input, expect, 378))

    def test79(self):
        input = """class main {

            int x(){

                for i := 1 to 100 do {
io.writeIntLn(i);
Intarray[i] := i + 1;
}
for x := 5 downto 2 do
io.writeIntLn(x);
               }

           }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[For(Id("i"),IntLiteral(1),IntLiteral(100),True,Block([],[CallStmt(Id("io"),Id("writeIntLn"),[Id("i")]),Assign(ArrayCell(Id("Intarray"),Id("i")),BinaryOp("+",Id("i"),IntLiteral(1)))])),For(Id("x"),IntLiteral(5),IntLiteral(2),False,CallStmt(Id("io"),Id("writeIntLn"),[Id("x")]))]))],None)]))
        self.assertTrue(TestAST.test(input, expect, 379))

    def test80(self):
        input = """class main {
               int x(){
                a := a + b;

               }
           }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[Assign(Id("a"),BinaryOp("+",Id("a"),Id("b")))]))],None)]))
        self.assertTrue(TestAST.test(input, expect, 380))

    def test81(self):
        input = """class main {
               int x(){
                a := a * b;

               }
           }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[Assign(Id("a"),BinaryOp("*",Id("a"),Id("b")))]))],None)]))
        self.assertTrue(TestAST.test(input, expect, 381))



    def test82(self):
        input = """class main {
               int x(){
a := a * b;

               }
           }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[Assign(Id("a"),BinaryOp("*",Id("a"),Id("b")))]))],None)]))
        self.assertTrue(TestAST.test(input, expect, 382))

    def test83(self):
        input = """class main {
               int x(){

a := a + b + c + d;
               }
           }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[Assign(Id("a"),BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),Id("c")),Id("d")))]))],None)]))
        self.assertTrue(TestAST.test(input, expect, 383))

    def test84(self):
        input = """class main {
               int x(){
a := a + b + c * d;

               }
           }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[Assign(Id("a"),BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),BinaryOp("*",Id("c"),Id("d"))))]))],None)]))
        self.assertTrue(TestAST.test(input, expect, 384))

    def test85(self):
        input = """class main {
               int x(){

a := a * b * c + d;
               }
           }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[Assign(Id("a"),BinaryOp("+",BinaryOp("*",BinaryOp("*",Id("a"),Id("b")),Id("c")),Id("d")))]))],None)]))
        self.assertTrue(TestAST.test(input, expect, 385))

    def test86(self):
        input = """class main {
               int x(){

if a  then b :=a;
               }
           }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[If(Id("a"),Assign(Id("b"),Id("a")))]))],None)]))
        self.assertTrue(TestAST.test(input, expect, 386))

    def test87(self):
        input = """class main {
               int x(){

if a  then b :=a;else c:=c;
               }
           }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[If(Id("a"),Assign(Id("b"),Id("a")),Assign(Id("c"),Id("c")))]))],None)]))
        self.assertTrue(TestAST.test(input, expect, 387))

    def test88(self):
        input = """class main {
               int x(){

if a  then b :=a; else if a then c:=c;
               }
           }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[If(Id("a"),Assign(Id("b"),Id("a")),If(Id("a"),Assign(Id("c"),Id("c"))))]))],None)]))
        self.assertTrue(TestAST.test(input, expect, 388))

    def test389(self):
        input = """class main {
               int x(){

if a  then b :=a; else if a then c:=c ;else c := qweqw;
               }
           }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[If(Id("a"),Assign(Id("b"),Id("a")),If(Id("a"),Assign(Id("c"),Id("c")),Assign(Id("c"),Id("qweqw"))))]))],None)]))
        self.assertTrue(TestAST.test(input, expect, 389))

    def test90(self):
        input = """class main {
                           int x(){

                for i := 1 to 100 do {
io.writeIntLn(i);
Intarray[i] := i + 1;
}
for x := 5 downto 2 do
io.writeIntLn(x);
               }
           }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[For(Id("i"),IntLiteral(1),IntLiteral(100),True,Block([],[CallStmt(Id("io"),Id("writeIntLn"),[Id("i")]),Assign(ArrayCell(Id("Intarray"),Id("i")),BinaryOp("+",Id("i"),IntLiteral(1)))])),For(Id("x"),IntLiteral(5),IntLiteral(2),False,CallStmt(Id("io"),Id("writeIntLn"),[Id("x")]))]))],None)]))
        self.assertTrue(TestAST.test(input, expect, 390))

    def test91(self):
        input = """class main {
                           int x(){

                for i := 1 to 100 do {
                {
                }{ }{ }{ }{ }{ }{
                }
}
               }
           }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[For(Id("i"),IntLiteral(1),IntLiteral(100),True,Block([],[Block([],[]),Block([],[]),Block([],[]),Block([],[]),Block([],[]),Block([],[]),Block([],[])]))]))],None)]))
        self.assertTrue(TestAST.test(input, expect, 391))

    def test92(self):
        input = """class main {
                           int x(){

                for i := 1 to 100 do {
                {
                }{ }{ }{
if a  then b :=a; else if a then c:=c ;else c := qweqw; }{ }{ }{
                }
}
               }
           }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[For(Id("i"),IntLiteral(1),IntLiteral(100),True,Block([],[Block([],[]),Block([],[]),Block([],[]),Block([],[If(Id("a"),Assign(Id("b"),Id("a")),If(Id("a"),Assign(Id("c"),Id("c")),Assign(Id("c"),Id("qweqw"))))]),Block([],[]),Block([],[]),Block([],[])]))]))],None)]))
        self.assertTrue(TestAST.test(input, expect, 392))

    def test93(self):
        input = """class main {
                           int x(){

                for i := 1 to 100 do {
                {a := a + b + c * d;
                }{ }{ }{
if a  then b :=a; else if a then c:=c ;else c := qweqw; }{ }{ }{
                }
}
               }
           }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[For(Id("i"),IntLiteral(1),IntLiteral(100),True,Block([],[Block([],[Assign(Id("a"),BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),BinaryOp("*",Id("c"),Id("d"))))]),Block([],[]),Block([],[]),Block([],[If(Id("a"),Assign(Id("b"),Id("a")),If(Id("a"),Assign(Id("c"),Id("c")),Assign(Id("c"),Id("qweqw"))))]),Block([],[]),Block([],[]),Block([],[])]))]))],None)]))
        self.assertTrue(TestAST.test(input, expect, 393))

    def test94(self):
        input = """
          class hello {
            string sting(){
          a[2] := 0;for i:=1 to end do a:=0;
          }

          }
          class goobye {

          }
          """
        expect = str(Program([ClassDecl(Id("hello"),[MethodDecl(Instance(),Id("sting"),[],StringType(),Block([],[Assign(ArrayCell(Id("a"),IntLiteral(2)),IntLiteral(0)),For(Id("i"),IntLiteral(1),Id("end"),True,Assign(Id("a"),IntLiteral(0)))]))],None),ClassDecl(Id("goobye"),[],None)]))
        self.assertTrue(TestAST.test(input, expect, 394))

    def test95(self):
        input = """class main {
               int x(){
a:=9;b:=c;a:=21123+qweqwe+203123;

               }
           }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[Assign(Id("a"),IntLiteral(9)),Assign(Id("b"),Id("c")),Assign(Id("a"),BinaryOp("+",BinaryOp("+",IntLiteral(21123),Id("qweqwe")),IntLiteral(203123)))]))],None)]))
        self.assertTrue(TestAST.test(input, expect, 395))






    def test96(self):
        input = """class main {
               int x(){
break;break;break;break;break;break;break;break;break;

               }
           }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[Break(),Break(),Break(),Break(),Break(),Break(),Break(),Break(),Break()]))],None)]))
        self.assertTrue(TestAST.test(input, expect, 396))

    def test97(self):
        input = """class main {
               int x(){

continue;continue;continue;continue;continue;continue;continue;continue;
               }
           }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[Continue(),Continue(),Continue(),Continue(),Continue(),Continue(),Continue(),Continue()]))],None)]))
        self.assertTrue(TestAST.test(input, expect, 397))

    def test98(self):
        input = """class main {
               int x(){
return 0;
return 0; return 0; return 0; return 0; return 0; return 0;
               }
           }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[Return(IntLiteral(0)),Return(IntLiteral(0)),Return(IntLiteral(0)),Return(IntLiteral(0)),Return(IntLiteral(0)),Return(IntLiteral(0)),Return(IntLiteral(0))]))],None)]))
        self.assertTrue(TestAST.test(input, expect, 398))

    def test99(self):
        input = """class main {
               int x(){
a.a.a.a.a.a.a.a.a.a.a.a := b.b.b.b.b.bb.d.b.b.b.b.b.b.b.b.l;

               }
           }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[Assign(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("a"),Id("a")),Id("a")),Id("a")),Id("a")),Id("a")),Id("a")),Id("a")),Id("a")),Id("a")),Id("a")),Id("a")),FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("b"),Id("b")),Id("b")),Id("b")),Id("b")),Id("bb")),Id("d")),Id("b")),Id("b")),Id("b")),Id("b")),Id("b")),Id("b")),Id("b")),Id("b")),Id("l")))]))],None)]))
        self.assertTrue(TestAST.test(input, expect, 399))

    def test100(self):
        input = """class main {
               int x(){
a[2] := a.sdasd[3];

               }
           }"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Instance(),Id("x"),[],IntType(),Block([],[Assign(ArrayCell(Id("a"),IntLiteral(2)),ArrayCell(FieldAccess(Id("a"),Id("sdasd")),IntLiteral(3)))]))],None)]))
        self.assertTrue(TestAST.test(input, expect, 400))