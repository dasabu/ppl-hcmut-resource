from dataclasses import Field
import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test500(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        AttributeDecl(
                            Instance(),
                            VarDecl(
                                Id("b"),
                                IntType(),
                                IntLiteral(1),
                            ),
                        ),
                        AttributeDecl(
                            Static(),
                            VarDecl(
                                Id("a"),
                                IntType(),
                                IntLiteral(1),
                            ),
                        ),
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [],
                                [CallStmt(Id("io"), Id("writeInt"), [IntLiteral(1)])],
                            ),
                        ),
                    ],
                )
            ]
        )
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 500))

    def test501(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(Id("d"), IntType(), IntLiteral(1)),
                                    VarDecl(Id("e"), IntType(), IntLiteral(1)),
                                ],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeInt"),
                                        [BinaryOp("+", Id("d"), Id("e"))],
                                    )
                                ],
                            ),
                        ),
                    ],
                )
            ]
        )
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test502(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        AttributeDecl(
                            Static(), VarDecl(Id("a"), IntType(), IntLiteral(1))
                        ),
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(Id("d"), IntType(), IntLiteral(1)),
                                    VarDecl(Id("e"), IntType(), IntLiteral(1)),
                                ],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeInt"),
                                        [
                                            BinaryOp(
                                                "+",
                                                FieldAccess(Id("BKoolClass"), Id("a")),
                                                Id("e"),
                                            )
                                        ],
                                    )
                                ],
                            ),
                        ),
                    ],
                )
            ]
        )
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 502))

    def test503(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        AttributeDecl(
                            Static(), VarDecl(Id("a"), IntType(), IntLiteral(1))
                        ),
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(Id("d"), IntType(), IntLiteral(1)),
                                    VarDecl(Id("e"), IntType(), IntLiteral(1)),
                                ],
                                [
                                    Assign(Id("d"), IntLiteral(100)),
                                    Assign(Id("e"), IntLiteral(20)),
                                    CallStmt(
                                        Id("io"),
                                        Id("writeInt"),
                                        [UnaryOp("-", Id("e"))],
                                    ),
                                ],
                            ),
                        ),
                    ],
                )
            ]
        )
        expect = "-20"
        self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test504(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        AttributeDecl(
                            Instance(),
                            VarDecl(Id("a"), IntType(), IntLiteral(100)),
                        ),
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    # VarDecl(Id("d"), IntType(), IntLiteral(1)),
                                    VarDecl(
                                        Id("object1"),
                                        ClassType(Id("BKoolClass")),
                                        NewExpr(Id("BKoolClass"), []),
                                    ),
                                ],
                                [
                                    Assign(
                                        FieldAccess(Id("object1"), Id("a")),
                                        IntLiteral(20),
                                    ),
                                    CallStmt(
                                        Id("io"),
                                        Id("writeInt"),
                                        [FieldAccess(Id("object1"), Id("a"))],
                                    ),
                                ],
                            ),
                        ),
                    ],
                )
            ]
        )
        expect = "20"
        self.assertTrue(TestCodeGen.test(input, expect, 504))

    def test505(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeInt"),
                                        [IntLiteral(1)],
                                    ),
                                ],
                            ),
                        ),
                        MethodDecl(
                            Static(),
                            Id("add"),
                            [VarDecl(Id("a"), IntType()), VarDecl(Id("b"), IntType())],
                            IntType(),
                            Block([], [Return(BinaryOp("+", Id("a"), Id("b")))]),
                        ),
                    ],
                )
            ]
        )
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 505))

    def test506(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeInt"),
                                        [
                                            CallExpr(
                                                Id("BKoolClass"),
                                                Id("add"),
                                                [IntLiteral(10), IntLiteral(7)],
                                            )
                                        ],
                                    ),
                                ],
                            ),
                        ),
                        MethodDecl(
                            Static(),
                            Id("add"),
                            [VarDecl(Id("a"), IntType()), VarDecl(Id("b"), IntType())],
                            IntType(),
                            Block(
                                [],
                                [
                                    Return(BinaryOp("+", Id("a"), Id("b"))),
                                ],
                            ),
                        ),
                    ],
                )
            ]
        )
        expect = "17"
        self.assertTrue(TestCodeGen.test(input, expect, 506))

    def test507(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeBool"),
                                        [
                                            CallExpr(
                                                Id("BKoolClass"),
                                                Id("isEqual"),
                                                [IntLiteral(1), IntLiteral(1)],
                                            )
                                        ],
                                    ),
                                ],
                            ),
                        ),
                        MethodDecl(
                            Static(),
                            Id("isEqual"),
                            [VarDecl(Id("a"), IntType()), VarDecl(Id("b"), IntType())],
                            BoolType(),
                            Block(
                                [],
                                [
                                    If(
                                        BinaryOp(">", IntLiteral(1), Id("b")),
                                        Return(BooleanLiteral(True)),
                                        Return(BooleanLiteral(False)),
                                    ),
                                ],
                            ),
                        ),
                    ],
                )
            ]
        )
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 507))

    def test508(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(
                                        Id("a"),
                                        ClassType(Id("BKoolClass")),
                                        NewExpr(Id("BKoolClass"), []),
                                    )
                                ],
                                [
                                    CallStmt(Id("a"), Id("printD"), []),
                                    CallStmt(
                                        Id("io"),
                                        Id("writeInt"),
                                        [IntLiteral(1)],
                                    ),
                                ],
                            ),
                        ),
                        MethodDecl(
                            Instance(),
                            Id("printD"),
                            [],
                            VoidType(),
                            Block(
                                [],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeStr"),
                                        [StringLiteral('"D"')],
                                    ),
                                ],
                            ),
                        ),
                    ],
                )
            ]
        )
        expect = "D1"
        self.assertTrue(TestCodeGen.test(input, expect, 508))

    def test509(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("<init>"),
                            [VarDecl(Id("b"), IntType())],
                            None,
                            Block([], []),
                        ),
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(
                                        Id("a"),
                                        ClassType(Id("BKoolClass")),
                                        NewExpr(Id("BKoolClass"), [IntLiteral(100)]),
                                    )
                                ],
                                [
                                    CallStmt(Id("a"), Id("printD"), []),
                                    CallStmt(
                                        Id("io"),
                                        Id("writeInt"),
                                        [IntLiteral(1)],
                                    ),
                                ],
                            ),
                        ),
                        MethodDecl(
                            Instance(),
                            Id("printD"),
                            [],
                            VoidType(),
                            Block(
                                [],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeStr"),
                                        [StringLiteral('"D"')],
                                    ),
                                ],
                            ),
                        ),
                    ],
                )
            ]
        )
        expect = "D1"
        self.assertTrue(TestCodeGen.test(input, expect, 509))

    def test510(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(
                                        Id("a"),
                                        IntType(),
                                    ),
                                    # VarDecl(Id("b"), IntType(), IntLiteral(1)),
                                ],
                                [
                                    For(
                                        Id("a"),
                                        IntLiteral(1),
                                        IntLiteral(2),
                                        True,
                                        Block([], []),
                                    ),
                                    CallStmt(
                                        Id("io"),
                                        Id("writeInt"),
                                        [Id("a")],
                                    ),
                                ],
                            ),
                        ),
                    ],
                )
            ]
        )
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 510))

    def test511(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(Id("n1"), IntType(), IntLiteral(0)),
                                    VarDecl(Id("n2"), IntType(), IntLiteral(1)),
                                    VarDecl(Id("n3"), IntType(), IntLiteral(0)),
                                    VarDecl(Id("i"), IntType(), IntLiteral(0)),
                                    VarDecl(Id("count"), IntType(), IntLiteral(10)),
                                ],
                                [
                                    CallStmt(Id("io"), Id("writeInt"), [Id("n1")]),
                                    CallStmt(Id("io"), Id("writeInt"), [Id("n2")]),
                                    For(
                                        Id("i"),
                                        IntLiteral(2),
                                        BinaryOp("-", Id("count"), IntLiteral(1)),
                                        True,
                                        Block(
                                            [],
                                            [
                                                Assign(
                                                    Id("n3"),
                                                    BinaryOp("+", Id("n1"), Id("n2")),
                                                ),
                                                CallStmt(
                                                    Id("io"), Id("writeInt"), [Id("n3")]
                                                ),
                                                CallStmt(
                                                    Id("io"),
                                                    Id("writeStr"),
                                                    [StringLiteral('"  "')],
                                                ),
                                                Assign(Id("n1"), Id("n2")),
                                                Assign(Id("n2"), Id("n3")),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                )
            ]
        )
        expect = "011  2  3  5  8  13  21  34  "
        self.assertTrue(TestCodeGen.test(input, expect, 511))

    def test521(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(
                                        Id("a"), StringType(), StringLiteral('"a"')
                                    ),
                                    VarDecl(
                                        Id("b"), StringType(), StringLiteral('"b"')
                                    ),
                                ],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeStr"),
                                        [
                                            BinaryOp(
                                                "^",
                                                StringLiteral('"abc"'),
                                                Id("b"),
                                            )
                                        ],
                                    )
                                ],
                            ),
                        ),
                    ],
                )
            ]
        )
        expect = "abcb"
        self.assertTrue(TestCodeGen.test(input, expect, 521))

    def test512(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(
                                        Id("b"),
                                        ArrayType(2, IntType()),
                                    )
                                ],
                                [
                                    Assign(
                                        Id("b"),
                                        ArrayLiteral(
                                            [IntLiteral(1200), IntLiteral(200)]
                                        ),
                                    ),
                                    If(
                                        BooleanLiteral(True),
                                        Block(
                                            [],
                                            [
                                                CallStmt(
                                                    Id("io"),
                                                    Id("writeInt"),
                                                    [ArrayCell(Id("b"), IntLiteral(0))],
                                                )
                                            ],
                                        ),
                                        Block(
                                            [],
                                            [
                                                CallStmt(
                                                    Id("io"),
                                                    Id("writeInt"),
                                                    [ArrayCell(Id("b"), IntLiteral(1))],
                                                )
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                )
            ]
        )
        expect = "1200"
        self.assertTrue(TestCodeGen.test(input, expect, 512))

    def test513(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        AttributeDecl(
                            Static(), VarDecl(Id("b"), IntType(), IntLiteral(10))
                        ),
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeInt"),
                                        [FieldAccess(Id("BKoolClass"), Id("b"))],
                                    )
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 513))

    def test514(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeStr"),
                                        [StringLiteral('"Hello World"')],
                                    )
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "Hello World"
        self.assertTrue(TestCodeGen.test(input, expect, 514))

    def test515(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(
                                        Id("name"),
                                        StringType(),
                                        StringLiteral('"John"'),
                                    ),
                                ],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeStr"),
                                        [Id("name")],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "John"
        self.assertTrue(TestCodeGen.test(input, expect, 515))

    def test516(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(
                                        Id("myNum"),
                                        IntType(),
                                        IntLiteral(15),
                                    ),
                                ],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeInt"),
                                        [Id("myNum")],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "15"
        self.assertTrue(TestCodeGen.test(input, expect, 516))

    def test517(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(
                                        Id("myNum"),
                                        IntType(),
                                    ),
                                ],
                                [
                                    Assign(Id("myNum"), IntLiteral(15)),
                                    CallStmt(
                                        Id("io"),
                                        Id("writeInt"),
                                        [Id("myNum")],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "15"
        self.assertTrue(TestCodeGen.test(input, expect, 517))

    def test518(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    ConstDecl(Id("myNum"), IntType(), IntLiteral(15)),
                                ],
                                [
                                    # Assign(Id("myNum"), IntLiteral(20)),
                                    CallStmt(
                                        Id("io"),
                                        Id("writeInt"),
                                        [Id("myNum")],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "15"
        self.assertTrue(TestCodeGen.test(input, expect, 518))

    def test519(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    ConstDecl(
                                        Id("myNum"), FloatType(), FloatLiteral(15.1)
                                    ),
                                ],
                                [
                                    Assign(Id("myNum"), FloatLiteral(20.1)),
                                    CallStmt(
                                        Id("io"),
                                        Id("writeFloat"),
                                        [Id("myNum")],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "20.1"
        self.assertTrue(TestCodeGen.test(input, expect, 519))

    def test520(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(
                                        Id("myNum"), BoolType(), BooleanLiteral(True)
                                    ),
                                ],
                                [
                                    Assign(Id("myNum"), BooleanLiteral(False)),
                                    CallStmt(
                                        Id("io"),
                                        Id("writeBool"),
                                        [Id("myNum")],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 520))

    def test522(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(
                                        Id("name"),
                                        StringType(),
                                        StringLiteral('"John"'),
                                    ),
                                ],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeStr"),
                                        [
                                            BinaryOp(
                                                "^",
                                                StringLiteral('"Hello "'),
                                                Id("name"),
                                            )
                                        ],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "Hello John"
        self.assertTrue(TestCodeGen.test(input, expect, 522))

    def test523(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(
                                        Id("firstName"),
                                        StringType(),
                                        StringLiteral('"John "'),
                                    ),
                                    VarDecl(
                                        Id("lastName"),
                                        StringType(),
                                        StringLiteral('"Doe"'),
                                    ),
                                    VarDecl(
                                        Id("fullName"),
                                        StringType(),
                                        BinaryOp("^", Id("firstName"), Id("lastName")),
                                    ),
                                ],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeStr"),
                                        [Id("fullName")],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "John Doe"
        self.assertTrue(TestCodeGen.test(input, expect, 523))

    def test524(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(
                                        Id("x"),
                                        IntType(),
                                        IntLiteral(5),
                                    ),
                                    VarDecl(
                                        Id("y"),
                                        IntType(),
                                        IntLiteral(6),
                                    ),
                                    VarDecl(
                                        Id("z"),
                                        IntType(),
                                        IntLiteral(50),
                                    ),
                                ],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeInt"),
                                        [
                                            BinaryOp(
                                                "+",
                                                BinaryOp("+", Id("x"), Id("y")),
                                                Id("z"),
                                            )
                                        ],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "61"
        self.assertTrue(TestCodeGen.test(input, expect, 524))

    def test525(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(
                                        Id("sum1"),
                                        IntType(),
                                        BinaryOp("+", IntLiteral(100), IntLiteral(50)),
                                    ),
                                    VarDecl(
                                        Id("sum2"),
                                        IntType(),
                                        BinaryOp("+", Id("sum1"), IntLiteral(250)),
                                    ),
                                    VarDecl(
                                        Id("sum3"),
                                        IntType(),
                                        BinaryOp("+", Id("sum2"), Id("sum2")),
                                    ),
                                ],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeInt"),
                                        [Id("sum3")],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "800"
        self.assertTrue(TestCodeGen.test(input, expect, 525))

    def test526(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeBool"),
                                        [
                                            BinaryOp(
                                                "<",
                                                IntLiteral(10),
                                                FloatLiteral(3.0),
                                            )
                                        ],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 526))

    def test527(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeStr"),
                                        [
                                            BinaryOp(
                                                "^",
                                                StringLiteral('"John"'),
                                                BinaryOp(
                                                    "^",
                                                    StringLiteral('" "'),
                                                    StringLiteral('"Doe"'),
                                                ),
                                            )
                                        ],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "John Doe"
        self.assertTrue(TestCodeGen.test(input, expect, 527))

    def test528(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(
                                        Id("x"),
                                        IntType(),
                                        IntLiteral(10),
                                    ),
                                    VarDecl(
                                        Id("y"),
                                        IntType(),
                                        IntLiteral(9),
                                    ),
                                ],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeBool"),
                                        [
                                            BinaryOp(
                                                "==", IntLiteral(15), IntLiteral(10)
                                            )
                                        ],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 528))

    def test529(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(Id("x"), IntType(), IntLiteral(20)),
                                    VarDecl(Id("y"), IntType(), IntLiteral(18)),
                                ],
                                [
                                    If(
                                        BinaryOp(">", Id("x"), Id("y")),
                                        CallStmt(
                                            Id("io"),
                                            Id("writeStr"),
                                            [StringLiteral('"x is greater than y"')],
                                        ),
                                    )
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "x is greater than y"
        self.assertTrue(TestCodeGen.test(input, expect, 529))

    def test530(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(Id("i"), IntType()),
                                ],
                                [
                                    For(
                                        Id("i"),
                                        IntLiteral(0),
                                        IntLiteral(4),
                                        True,
                                        Block(
                                            [VarDecl(Id("y"), IntType())],
                                            [
                                                CallStmt(
                                                    Id("io"),
                                                    Id("writeIntLn"),
                                                    [Id("i")],
                                                )
                                            ],
                                        ),
                                    )
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "0\n1\n2\n3\n4\n"
        self.assertTrue(TestCodeGen.test(input, expect, 530))

    def test531(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(Id("i"), IntType()),
                                ],
                                [
                                    For(
                                        Id("i"),
                                        IntLiteral(0),
                                        IntLiteral(9),
                                        True,
                                        Block(
                                            [],
                                            [
                                                If(
                                                    BinaryOp(
                                                        "==", Id("i"), IntLiteral(4)
                                                    ),
                                                    Break(),
                                                ),
                                                CallStmt(
                                                    Id("io"),
                                                    Id("writeInt"),
                                                    [Id("i")],
                                                ),
                                            ],
                                        ),
                                    )
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "0123"
        self.assertTrue(TestCodeGen.test(input, expect, 531))

    def test532(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(Id("i"), IntType()),
                                ],
                                [
                                    For(
                                        Id("i"),
                                        IntLiteral(0),
                                        IntLiteral(9),
                                        True,
                                        Block(
                                            [
                                                VarDecl(Id("y"), IntType()),
                                            ],
                                            [
                                                If(
                                                    BinaryOp(
                                                        "==", Id("i"), IntLiteral(4)
                                                    ),
                                                    Break(),
                                                ),
                                                CallStmt(
                                                    Id("io"),
                                                    Id("writeInt"),
                                                    [Id("i")],
                                                ),
                                            ],
                                        ),
                                    )
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "0123"
        self.assertTrue(TestCodeGen.test(input, expect, 532))

    def test533(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(Id("i"), IntType()),
                                ],
                                [
                                    For(
                                        Id("i"),
                                        IntLiteral(0),
                                        IntLiteral(9),
                                        True,
                                        Block(
                                            [
                                                VarDecl(Id("y"), IntType()),
                                            ],
                                            [
                                                If(
                                                    BinaryOp(
                                                        "==", Id("i"), IntLiteral(4)
                                                    ),
                                                    Continue(),
                                                ),
                                                CallStmt(
                                                    Id("io"),
                                                    Id("writeInt"),
                                                    [Id("i")],
                                                ),
                                            ],
                                        ),
                                    )
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "012356789"
        self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test534(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(
                                        Id("cars"),
                                        ArrayType(4, StringType()),
                                        ArrayLiteral(
                                            [
                                                StringLiteral('"Volvo"'),
                                                StringLiteral('"BMW"'),
                                                StringLiteral('"Ford"'),
                                                StringLiteral('"Mazda"'),
                                            ]
                                        ),
                                    )
                                ],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeStr"),
                                        [ArrayCell(Id("cars"), IntLiteral(0))],
                                    )
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "Volvo"
        self.assertTrue(TestCodeGen.test(input, expect, 534))

    def test535(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(
                                        Id("cars"),
                                        ArrayType(4, StringType()),
                                        ArrayLiteral(
                                            [
                                                StringLiteral('"Volvo"'),
                                                StringLiteral('"BMW"'),
                                                StringLiteral('"Ford"'),
                                                StringLiteral('"Mazda"'),
                                            ]
                                        ),
                                    )
                                ],
                                [
                                    Assign(
                                        ArrayCell(Id("cars"), IntLiteral(0)),
                                        StringLiteral('"Opel"'),
                                    ),
                                    CallStmt(
                                        Id("io"),
                                        Id("writeStr"),
                                        [ArrayCell(Id("cars"), IntLiteral(0))],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "Opel"
        self.assertTrue(TestCodeGen.test(input, expect, 535))
    def test536(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(
                                        Id("cars"),
                                        ArrayType(4, StringType()),
                                        ArrayLiteral(
                                            [
                                                StringLiteral('"Volvo"'),
                                                StringLiteral('"BMW"'),
                                                StringLiteral('"Ford"'),
                                                StringLiteral('"Mazda"'),
                                            ]
                                        ),
                                    ),
                                    VarDecl(Id("i"), IntType()),
                                ],
                                [
                                    For(
                                        Id("i"),
                                        IntLiteral(0),
                                        IntLiteral(3),
                                        True,
                                        Block(
                                            [],
                                            [
                                                CallStmt(
                                                    Id("io"),
                                                    Id("writeStr"),
                                                    [ArrayCell(Id("cars"), Id("i"))],
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "VolvoBMWFordMazda"
        self.assertTrue(TestCodeGen.test(input, expect, 536))
    def test537(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [],
                                [
                                    CallStmt(Id("BKoolClass"), Id("myMethod"), []),
                                ],
                            ),
                        ),
                        MethodDecl(
                            Static(),
                            Id("myMethod"),
                            [],
                            VoidType(),
                            Block(
                                [],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeStr"),
                                        [StringLiteral('"I just got executed!"')],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "I just got executed!"
        self.assertTrue(TestCodeGen.test(input, expect, 537))
    def test538(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [],
                                [
                                    CallStmt(Id("BKoolClass"), Id("myMethod"), []),
                                    CallStmt(Id("BKoolClass"), Id("myMethod"), []),
                                    CallStmt(Id("BKoolClass"), Id("myMethod"), []),
                                ],
                            ),
                        ),
                        MethodDecl(
                            Static(),
                            Id("myMethod"),
                            [],
                            VoidType(),
                            Block(
                                [],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeStr"),
                                        [StringLiteral('"I just got executed!"')],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "I just got executed!I just got executed!I just got executed!"
        self.assertTrue(TestCodeGen.test(input, expect, 538))
    def test539(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [],
                                [
                                    CallStmt(
                                        Id("BKoolClass"),
                                        Id("myMethod"),
                                        [StringLiteral('"Liam"')],
                                    ),
                                    CallStmt(
                                        Id("BKoolClass"),
                                        Id("myMethod"),
                                        [StringLiteral('"Jenny"')],
                                    ),
                                    CallStmt(
                                        Id("BKoolClass"),
                                        Id("myMethod"),
                                        [StringLiteral('"Anja"')],
                                    ),
                                ],
                            ),
                        ),
                        MethodDecl(
                            Static(),
                            Id("myMethod"),
                            [VarDecl(Id("fname"), StringType())],
                            VoidType(),
                            Block(
                                [],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeStrLn"),
                                        [
                                            BinaryOp(
                                                "^",
                                                Id("fname"),
                                                StringLiteral('" Refsnes"'),
                                            )
                                        ],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "Liam Refsnes\nJenny Refsnes\nAnja Refsnes\n"
        self.assertTrue(TestCodeGen.test(input, expect, 539))
    def test540(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeInt"),
                                        [
                                            CallExpr(
                                                Id("BKoolClass"),
                                                Id("myMethod"),
                                                [IntLiteral(5), IntLiteral(3)],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ),
                        MethodDecl(
                            Static(),
                            Id("myMethod"),
                            [VarDecl(Id("x"), IntType()), VarDecl(Id("y"), IntType())],
                            IntType(),
                            Block(
                                [],
                                [Return(BinaryOp("+", Id("y"), Id("x")))],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "8"
        self.assertTrue(TestCodeGen.test(input, expect, 540))
    def test541(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(
                                        Id("z"),
                                        IntType(),
                                        CallExpr(
                                            Id("BKoolClass"),
                                            Id("myMethod"),
                                            [IntLiteral(5), IntLiteral(3)],
                                        ),
                                    )
                                ],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeInt"),
                                        [Id("z")],
                                    ),
                                ],
                            ),
                        ),
                        MethodDecl(
                            Static(),
                            Id("myMethod"),
                            [VarDecl(Id("x"), IntType()), VarDecl(Id("y"), IntType())],
                            IntType(),
                            Block(
                                [],
                                [Return(BinaryOp("+", Id("y"), Id("x")))],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "8"
        self.assertTrue(TestCodeGen.test(input, expect, 541))

    def test542(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [],
                                [
                                    CallStmt(
                                        Id("BKoolClass"),
                                        Id("checkAge"),
                                        [IntLiteral(20)],
                                    ),
                                ],
                            ),
                        ),
                        MethodDecl(
                            Static(),
                            Id("checkAge"),
                            [
                                VarDecl(Id("age"), IntType()),
                            ],
                            VoidType(),
                            Block(
                                [],
                                [
                                    If(
                                        BinaryOp("<", Id("age"), IntLiteral(18)),
                                        CallStmt(
                                            Id("io"),
                                            Id("writeStr"),
                                            [
                                                StringLiteral(
                                                    '"Access denied - You are not old enough!"'
                                                )
                                            ],
                                        ),
                                        CallStmt(
                                            Id("io"),
                                            Id("writeStr"),
                                            [
                                                StringLiteral(
                                                    '"Access granted - You are old enough!"'
                                                )
                                            ],
                                        ),
                                    )
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "Access granted - You are old enough!"
        self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test543(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(
                                        Id("result"),
                                        IntType(),
                                        CallExpr(
                                            Id("BKoolClass"),
                                            Id("sum"),
                                            [IntLiteral(10)],
                                        ),
                                    )
                                ],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeInt"),
                                        [Id("result")],
                                    ),
                                ],
                            ),
                        ),
                        MethodDecl(
                            Static(),
                            Id("sum"),
                            [VarDecl(Id("k"), IntType())],
                            IntType(),
                            Block(
                                [],
                                [
                                    If(
                                        BinaryOp(">", Id("k"), IntLiteral(0)),
                                        Block(
                                            [],
                                            [
                                                Return(
                                                    BinaryOp(
                                                        "+",
                                                        Id("k"),
                                                        CallExpr(
                                                            Id("BkoolClass"),
                                                            Id("sum"),
                                                            [
                                                                BinaryOp(
                                                                    "-",
                                                                    Id("k"),
                                                                    IntLiteral(1),
                                                                )
                                                            ],
                                                        ),
                                                    )
                                                )
                                            ],
                                        ),
                                        Block([], [Return(IntLiteral(0))]),
                                    )
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "55"
        self.assertTrue(TestCodeGen.test(input, expect, 543))

    def test544(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        AttributeDecl(
                            Instance(), VarDecl(Id("x"), IntType(), IntLiteral(5))
                        ),
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(
                                        Id("myObj1"),
                                        ClassType(Id("BKoolClass")),
                                        NewExpr(Id("BKoolClass"), []),
                                    ),
                                    VarDecl(
                                        Id("myObj2"),
                                        ClassType(Id("BKoolClass")),
                                        NewExpr(Id("BKoolClass"), []),
                                    ),
                                ],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeIntLn"),
                                        [FieldAccess(Id("myObj1"), Id("x"))],
                                    ),
                                    CallStmt(
                                        Id("io"),
                                        Id("writeInt"),
                                        [FieldAccess(Id("myObj2"), Id("x"))],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "5\n5"
        self.assertTrue(TestCodeGen.test(input, expect, 544))

    def test545(self):
        input = Program(
            [
                ClassDecl(
                    Id("Main"),
                    [
                        AttributeDecl(
                            Instance(), VarDecl(Id("x"), IntType(), IntLiteral(5))
                        ),
                    ],
                ),
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(
                                        Id("myObj"),
                                        ClassType(Id("Main")),
                                        NewExpr(Id("Main"), []),
                                    ),
                                ],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeInt"),
                                        [FieldAccess(Id("myObj"), Id("x"))],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 545))

    def test546(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        AttributeDecl(
                            Instance(), ConstDecl(Id("x"), IntType(), IntLiteral(10))
                        ),
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(
                                        Id("myObj"),
                                        ClassType(Id("BKoolClass")),
                                        NewExpr(Id("BKoolClass"), []),
                                    ),
                                ],
                                [
                                    Assign(
                                        FieldAccess(Id("myObj"), Id("x")),
                                        IntLiteral(25),
                                    ),
                                    CallStmt(
                                        Id("io"),
                                        Id("writeInt"),
                                        [FieldAccess(Id("myObj"), Id("x"))],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "25"
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test547(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        AttributeDecl(
                            Instance(), VarDecl(Id("x"), IntType(), IntLiteral(5))
                        ),
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(
                                        Id("myObj1"),
                                        ClassType(Id("BKoolClass")),
                                        NewExpr(Id("BKoolClass"), []),
                                    ),
                                    VarDecl(
                                        Id("myObj2"),
                                        ClassType(Id("BKoolClass")),
                                        NewExpr(Id("BKoolClass"), []),
                                    ),
                                ],
                                [
                                    Assign(
                                        FieldAccess(Id("myObj2"), Id("x")),
                                        IntLiteral(25),
                                    ),
                                    CallStmt(
                                        Id("io"),
                                        Id("writeInt"),
                                        [FieldAccess(Id("myObj1"), Id("x"))],
                                    ),
                                    CallStmt(
                                        Id("io"),
                                        Id("writeInt"),
                                        [FieldAccess(Id("myObj2"), Id("x"))],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "525"
        self.assertTrue(TestCodeGen.test(input, expect, 547))

    def test548(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        AttributeDecl(
                            Instance(),
                            VarDecl(Id("fname"), StringType(), StringLiteral('"John"')),
                        ),
                        AttributeDecl(
                            Instance(),
                            VarDecl(Id("lname"), StringType(), StringLiteral('"Doe"')),
                        ),
                        AttributeDecl(
                            Instance(), VarDecl(Id("age"), IntType(), IntLiteral(24))
                        ),
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(
                                        Id("myObj"),
                                        ClassType(Id("BKoolClass")),
                                        NewExpr(Id("BKoolClass"), []),
                                    ),
                                ],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeStr"),
                                        [
                                            BinaryOp(
                                                "^",
                                                FieldAccess(Id("myObj"), Id("fname")),
                                                FieldAccess(Id("myObj"), Id("lname")),
                                            )
                                        ],
                                    ),
                                    CallStmt(
                                        Id("io"),
                                        Id("writeInt"),
                                        [FieldAccess(Id("myObj"), Id("age"))],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "JohnDoe24"
        self.assertTrue(TestCodeGen.test(input, expect, 548))

    def test549(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("myStaticMethod"),
                            [],
                            VoidType(),
                            Block(
                                [],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeStrLn"),
                                        [
                                            StringLiteral(
                                                '"Static methods can be called without creating objects"'
                                            )
                                        ],
                                    ),
                                ],
                            ),
                        ),
                        MethodDecl(
                            Instance(),
                            Id("myPublicMethod"),
                            [],
                            VoidType(),
                            Block(
                                [],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeStr"),
                                        [
                                            StringLiteral(
                                                '"Public methods must be called by creating objects"'
                                            )
                                        ],
                                    ),
                                ],
                            ),
                        ),
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(
                                        Id("myObj"),
                                        ClassType(Id("BKoolClass")),
                                        NewExpr(Id("BKoolClass"), []),
                                    ),
                                ],
                                [
                                    CallStmt(
                                        Id("BKoolClass"),
                                        Id("myStaticMethod"),
                                        [],
                                    ),
                                    CallStmt(
                                        Id("myObj"),
                                        Id("myPublicMethod"),
                                        [],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "Static methods can be called without creating objects\nPublic methods must be called by creating objects"
        self.assertTrue(TestCodeGen.test(input, expect, 549))

    def test550(self):
        input = Program(
            [
                ClassDecl(
                    Id("BKoolClass"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            VoidType(),
                            Block(
                                [
                                    VarDecl(
                                        Id("myCar"),
                                        ClassType(Id("Main")),
                                        NewExpr(Id("Main"), []),
                                    ),
                                ],
                                [
                                    CallStmt(
                                        Id("myCar"),
                                        Id("fullThrottle"),
                                        [],
                                    ),
                                    CallStmt(
                                        Id("myCar"),
                                        Id("speed"),
                                        [StringLiteral('"200"')],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
                ClassDecl(
                    Id("Main"),
                    [
                        MethodDecl(
                            Instance(),
                            Id("fullThrottle"),
                            [],
                            VoidType(),
                            Block(
                                [],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeStrLn"),
                                        [
                                            StringLiteral(
                                                '"The car is going as fast as it can!"'
                                            )
                                        ],
                                    ),
                                ],
                            ),
                        ),
                        MethodDecl(
                            Instance(),
                            Id("speed"),
                            [VarDecl(Id("maxSpeed"), StringType())],
                            VoidType(),
                            Block(
                                [],
                                [
                                    CallStmt(
                                        Id("io"),
                                        Id("writeStrLn"),
                                        [
                                            BinaryOp(
                                                "^",
                                                StringLiteral('"Max speed is: "'),
                                                Id("maxSpeed"),
                                            )
                                        ],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ]
        )
        expect = "The car is going as fast as it can!\nMax speed is: 200\n"
        self.assertTrue(TestCodeGen.test(input, expect, 550))
    def test_51(self):
        input = """
            class BKoolClass {
                int x=5;
                static void main(){
                    BkoolClass myObj1 = new BKoolClass();
                    BkoolClass myObj2 = new BKoolClass();
                    int a=100;
                    myObj2.x := 25;
                    io.writeInt(myObj2.x+myObj1.x+a);
                }
            }
        """
        expect = "130"
        self.assertTrue(TestCodeGen.test(input,expect,551))
    def test_52(self):
        input = """
            class BKoolClass{
                int b=1;
                static void main(){
                    BKoolClass bk = new BKoolClass();
                    io.writeInt(bk.b);
                }
            }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,552))
    def test_53(self):
        input = """
            class BKoolClass{
                int a=10;
                static void main(){
                    BKoolClass bk = new BKoolClass();
                    if 1 < 17 then {
                        io.writeInt(bk.a);
                    }
                }
            }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,553))
    def test_54(self):
        input = """
            class BKoolClass{
                int a=10;
                float b=2.5;
                string c="bk";
                boolean d= true;
                static void main(){
                    BKoolClass bk = new BKoolClass();
                    if 1 < 17 then {
                        io.writeInt(bk.a);
                    }
                }
            }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,554))
    def test_55(self):
        input = """
            class BKoolClass{
                int a=10;
                float b=2.5;
                string c="bk";
                boolean d= true;
                static void main(){
                    BKoolClass bk = new BKoolClass();
                    if bk.d then {
                        io.writeInt(bk.a);
                    }
                }
            }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,555))
    def test_56(self):
        input = """
            class BKoolClass{
                int a=10;
                float b=2.5;
                string c="bk";
                boolean d= true;
                static void main(){
                    BKoolClass bk = new BKoolClass();
                    if bk.d then {
                        io.writeStr(bk.c);
                    }
                }
            }
        """
        expect = "bk"
        self.assertTrue(TestCodeGen.test(input,expect,556))
    def test_57(self):
        input = """
            class BKoolClass{
                int value = 100;
                void foo(int x){
                    io.writeInt(x);
                }
                static void main(){ 
                    BKoolClass bk = new BKoolClass();
                    bk.foo(100);
                    
                }
            }
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,557))
    def test_58(self):
        input = """
            class BKoolClass{
                int a=10;
                int b=20;
                int foo(int x){
                    return x;
                }
                static void main(){ 
                    BKoolClass bk = new BKoolClass();
                    if bk.a < bk.b then
                        bk.a := bk.b;             
                    io.writeInt(bk.a);       
                }
            }
        """
        expect = "20"
        self.assertTrue(TestCodeGen.test(input,expect,558))
    def test_59(self):
        input = """
            class BKoolClass{
                
                static void main(){ 
                    int a=0;
                    for a := 5 to 10 do
                        io.writeInt(a);
                }
            }
        """
        expect = "5678910"
        self.assertTrue(TestCodeGen.test(input,expect,559))
    def test_60(self):
        input = """
            class BKoolClass{
                int z=0;                
                static void main(){ 
                    BKoolClass bk = new BKoolClass();
                    int a=0;
                    for a := 5 to 10 do
                        bk.z := bk.z +1;
                    io.writeInt(bk.z);
                }
            }
        """
        expect = "6"
        self.assertTrue(TestCodeGen.test(input,expect,560))
    def test_60(self):
        input = """
            class BKoolClass{
                int z=6;   
                void foo(){
                    io.writeInt(this.z);
                }             
                static void main(){ 
                    BKoolClass bk = new BKoolClass();
                    bk.foo();
                }
            }
        """
        expect = "6"
        self.assertTrue(TestCodeGen.test(input,expect,560))
    def test_61(self):
        input = """
            class A {
                int e;
            }
            class BKoolClass {
                int x = 0;
                static void main(){ 
                    BKoolClass bk = new BKoolClass();
                    bk.x := 25;
                    io.writeInt(bk.x);   
                }
            }
        """
        expect = "25"
        self.assertTrue(TestCodeGen.test(input,expect,561))
    
    def test_62(self):
        input = """class BKoolClass {static void main() {io.writeBool(true);}}"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,562))
    
    def test_63(self):
        input = """
        class BKoolClass {
            static float d;
            float bb;
            static void main(){
                float d;
                boolean e;
                e := (1<5);
                io.writeBool(e);
            }
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,563))
    
    def test_64(self):
        input = """
        class BKoolClass {
            static float d;
            float bb;
            static void main(){
                float d;
                boolean e;
                e := (1<0) || (7>8);
                io.writeBool(e);
            }
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,564))
    
    def test_65(self):
        input = """
        class BKoolClass {
            static float d;
            float bb;
            static void main(){
                float d;
                boolean e;
                d := 19\\10;
                io.writeFloat(d);
            }
        }
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input,expect,565))
    
    def test_66(self):
        input = """
        class BKoolClass {
            static void main(){
                float d;
                boolean e;
                e := (1<5);
                io.writeBool(e);
            }
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,566))
    
    def test_67(self):
        input = """
        class BKoolClass {
            static float d;
            float bb;
            static void main(){
                boolean e;
                e := (1<0) || (7>8);
                io.writeBool(e);
            }
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,567))
    
    def test_68(self):
        input = """
        class BKoolClass {
            static float d;
            float bb;
            static void main(){
                float d;
                boolean e;
                d := 50\\47;
                io.writeFloat(d);
            }
        }
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input,expect,568))
    
    def test_69(self):
        input = """
        class BKoolClass {
            static void main(){
                float d;
                boolean e;
                e := (1<5);
                io.writeBool(e);
            }
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,569))
    
    def test_70(self):
        input = """
        class BKoolClass {
            static float d;
            float bb;
            static void main(){
                boolean e;
                e := (1<0) || (7>8);
                io.writeBool(e);
            }
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,570))
    
    def test_71(self):
        input = """
        class BKoolClass {
            static float d;
            float bb;
            static void main(){
                float d;
                boolean e;
                d := 50\\47;
                io.writeFloat(d);
            }
        }
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input,expect,571))
        
    def test_72(self):
        input = """
        class BKoolClass {
            static void main(){
                float d;
                boolean e;
                e := (1<5);
                io.writeBool(e);
            }
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,572))
    
    def test_73(self):
        input = """
        class BKoolClass {
            static float d;
            float bb;
            static void main(){
                boolean e;
                e := (1<0) || (7>8);
                io.writeBool(e);
            }
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,573))
    
    def test_74(self):
        input = """
        class BKoolClass {
            static float d;
            float bb;
            static void main(){
                float d;
                boolean e;
                d := 50\\47;
                io.writeFloat(d);
            }
        }
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input,expect,574))

    def test_75(self):
        input = """
        class BKoolClass {
            int foo(){
                return 100;
            }
            static void main(){
                BKoolClass bk = new BKoolClass();
                int zoo=bk.foo();
                io.writeInt(zoo);
            }
        }
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,575))
        
    def test_76(self):
        input = """
        class BKoolClass {
            int foo(){
                return 100;
            }
            static void main(){
                BKoolClass bk = new BKoolClass();
                io.writeInt(bk.foo());
            }
        }
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,576))
        
    def test_77(self):
        input = """
        class BKoolClass {
            int foo(){
                return 100;
            }
            static void main(){
                BKoolClass bk = new BKoolClass();
                BKoolClass spkt = new BKoolClass();
                int zoo=bk.foo();
                io.writeInt(zoo+spkt.foo());
            }
        }
        """
        expect = "200"
        self.assertTrue(TestCodeGen.test(input,expect,577))
        
    def test_78(self):
        input = """
        class BKoolClass {
            static int foo(){
                return 100;
            }
            static void main(){
                io.writeInt(BKoolClass.foo());
            }
        }
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,578))
    
    def test_79(self):
        input = """
        class BKoolClass {
            static void foo(){
                io.writeFloat(2.51);
            }
            static void main(){
                BKoolClass.foo();
            }
        }
        """
        expect = "2.51"
        self.assertTrue(TestCodeGen.test(input,expect,579))
    
    def test_80(self):
        input = """
        class BKoolClass {
            void foo(){
                io.writeInt(100);
            }
            static void main(){
                BKoolClass bk = new BKoolClass();
                bk.foo();
            }
        }
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,580))
    
    def test_81(self):
        input = """
        class BKoolClass {
            int att=20;
            void foo(){
                this.att := 30;
            }
            static void main(){
                BKoolClass bk = new BKoolClass();
                bk.foo();
                io.writeInt(bk.att);
            }
        }
        """
        expect = "30"
        self.assertTrue(TestCodeGen.test(input,expect,581))
    
    def test_82(self):
        input = """
        class BKoolClass {
            int z=10;
            static void main(){
                BKoolClass bk = new BKoolClass();
                io.writeInt(bk.z);
            }
        }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,582))
    
    def test_83(self):
        input = """
        class BKoolClass {
            int att=20;
            void foo(){
                this.att := 70;
            }
            static void main(){
                BKoolClass bk = new BKoolClass();
                bk.foo();
                io.writeInt(bk.att);
            }
        }
        """
        expect = "70"
        self.assertTrue(TestCodeGen.test(input,expect,583))
    
    def test_84(self):
        input = """
        class BKoolClass {
            void foo(){
                io.writeInt(101);
            }
            static void main(){
                BKoolClass bk = new BKoolClass();
                bk.foo();
            }
        }
        """
        expect = "101"
        self.assertTrue(TestCodeGen.test(input,expect,584))
    def test_85(self):
        input = """
        class BKoolClass {
            void foo(){
                io.writeInt(1);
            }
            static void main(){
                BKoolClass bk = new BKoolClass();
                int i=0;
                for i:=1 to 5 do
                    bk.foo();
            }
        }
        """
        expect = "11111"
        self.assertTrue(TestCodeGen.test(input,expect,585))
    def test_86(self):
        input = """
        class BKoolClass {
            static void main(){
                int i=7;
                io.writeBool(i==7);
            }
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,586))
    def test_87(self):
        input = """
            class BKoolClass{
                static void main(){
                    int a;
                    boolean e;
                    e := false;
                    for a := 3 downto 1 do {
                        if a == 2 then {
                            e := 1 < 1;
                            break;
                        }
                    }
                    io.writeBool(e);
                }
            }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,587))
    
    def test_87(self):
        input = """
            class BKoolClass{
                static void main(){
                    int p = (5%2);
                    io.writeInt(p);
                }
            }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,587))
    
    def test_87(self):
        input = """
            class BKoolClass{
                static void main(){
                    int i=0;
                    for i:=0 to 10 do{
                        if i%2==0 then{
                            io.writeInt(i);
                        }
                    }
                }
            }
        """
        expect = "0246810"
        self.assertTrue(TestCodeGen.test(input,expect,587))
    def test_88(self):
        input = """
            class BKoolClass {
                int[4] total={0,0,0,0};
                string name;
            
                static void main(){
                    BKoolClass bk = new BKoolClass();
                    bk.total[0] := 9;
                    io.writeInt(bk.total[0]);
                    io.writeInt(bk.total[1]);
                    io.writeInt(bk.total[2]);
                    io.writeInt(bk.total[3]);
            }
        }
        """
        expect = "9000"
        self.assertTrue(TestCodeGen.test(input,expect,588))
    def test_89(self):
        input = """
            class BKoolClass {
                int[4] total={0,0,0,0};
                void change(int i){
                    this.total[i] := 100;
                }
            
                static void main(){
                    BKoolClass bk = new BKoolClass();
                    int i=0;
                    for i:=0 to 3 do{
                        io.writeInt(bk.total[i]);
                    }
            }
        }
        """
        expect = "0000"
        self.assertTrue(TestCodeGen.test(input,expect,589))
    def test_90(self):
        input = """
            class BKoolClass {
                int[4] total={0,0,0,0};
                void change(int i){
                    this.total[i] := 7;
                }
            
                static void main(){
                    BKoolClass bk = new BKoolClass();
                    bk.change(2);
                    io.writeInt(bk.total[0]);
                    io.writeInt(bk.total[1]);
                    io.writeInt(bk.total[2]);
                    io.writeInt(bk.total[3]);
                }
            }
        """
        expect = "0070"
        self.assertTrue(TestCodeGen.test(input,expect,590))
    
    def test_91(self):
        input = """
            class BKoolClass{
                static void main(){
                    io.writeInt(5+10);
                }
            }
            
        """
        expect = "15"
        self.assertTrue(TestCodeGen.test(input,expect,591))
    
    def test_92(self):
        input = """
            class BKoolClass{
                static void main(){
                    io.writeInt(88-44);
                }
            }
            
        """
        expect = "44"
        self.assertTrue(TestCodeGen.test(input,expect,592))
    
    def test_93(self):
        input = """
            class BKoolClass{
                static void main(){
                    io.writeInt(5*10);
                }
            }
            
        """
        expect = "50"
        self.assertTrue(TestCodeGen.test(input,expect,593))
    
    def test_94(self):
        input = """
            class BKoolClass{
                static void main(){
                    io.writeInt(14%7);
                }
            }
            
        """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,594))
    
    def test_95(self):
        input = """
            class BKoolClass{
                static void main(){
                    io.writeStr("a"^"bb");
                }
            }
            
        """
        expect = "abb"
        self.assertTrue(TestCodeGen.test(input,expect,595))
    
    def test_96(self):
        input = """
            class BKoolClass{
                static void main(){
                    io.writeBool((5<7));
                }
            }
            
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,596))
    
    def test_97(self):
        input = """
            class BKoolClass{
                static void main(){
                    io.writeFloat(10/5);
                }
            }
            
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input,expect,597))
    
    def test_98(self):
        input = """
            class BKoolClass{
                static void main(){
                    io.writeBool((1<2) || (5<7));
                }
            }
            
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,598))
    
    def test_99(self):
        input = """
            class MP{
                int a=11;
                void foo(){
                    io.writeInt(11);
                }
            }
            class BKoolClass extends MP{
                static void main(){
                    BKoolClass bk = new BKoolClass();
                    bk.foo();
                }
            }
            
        """
        expect = "11"
        self.assertTrue(TestCodeGen.test(input,expect,599))
        
    