#Nguyen Mai Thy 1912190
import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_0(self):
        input = Program([ClassDecl(Id("Ex"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),ConstDecl(Id("x"),IntType(),FieldAccess(Id("Ex"),Id("a"))))])])
        expect = "Illegal Constant Expression: FieldAccess(Id(Ex),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,400))

#
#     def test_1(self):
#         input = """
#         Class Program {
#         func(){
#         }
#         main(){
#             Return "No Error";
#         }
#         }
#         """
#         expect = "Type Mismatch In Statement: Return(StringLit(No Error))"
#         self.assertTrue(TestChecker.test(input,expect,401))
#
#     def test_2(self):
#         input = """
#         Class Program {
#         main(){
#                 Var x: Int = 1;
#                 If (x == 1){
#                     x = 3;
#                 }
#                 Return "No Error";
#         } }
#         """
#         expect = "Type Mismatch In Statement: Return(StringLit(No Error))"
#         self.assertTrue(TestChecker.test(input,expect,402))
#
#     def test_3(self):
#         input = """
#         Class Program {
#         main(){
#                 Var x: Int = 1;
#                 If (x == 2){
#                     x = 3;
#                 }
#                 Elseif (x == 1) {
#                     x = 5;
#                 }
#                 Else {
#                     x = 8;
#                 }
#                 Return "No Error";
#         } }
#         """
#         expect = "Type Mismatch In Statement: Return(StringLit(No Error))"
#         self.assertTrue(TestChecker.test(input,expect,403))
#
#     def test_4(self):
#         input = """
#         Class Lake {
#         main(){
#                 Var x: Int = 1;
#                 If (x == 2){
#                     x = 3;
#                 }
#                 Else {
#                     x = "Error";
#                 }
#         } }
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(x),StringLit(Error))"
#         self.assertTrue(TestChecker.test(input,expect,404))
#
#     def test_5(self):
#         input = """
#         Class Program {
#         main(){
#                 Var x: Int = 1;
#                 Var z: Int = 1;
#                 Val t: Int = 1;
#                 Var a: Int = 3;
#                 Val f: Int = t;
#                 Val y: Int = x;
#         } }
#         """
#         expect = "Illegal Constant Expression: Id(x)"
#         self.assertTrue(TestChecker.test(input,expect,405))
#
#     def test_6(self):
#         input = """
#         Class Program {
#         main(){
#                 Var a: Int;
#                 Val x: Int = 1;
#                 Val y: Int = 1 + a;
#         } }
#         """
#         expect = "Illegal Constant Expression: BinaryOp(+,IntLit(1),Id(a))"
#         self.assertTrue(TestChecker.test(input,expect,406))
#
#     def test_7(self):
#         input = """
#         Class Program {
#         main(){
#                 Val x,y: String = "String1", "String2";
#                 Var a,b: Boolean = True, False;
#         } }
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input,expect,407))
#
#     def test_8(self):
#         input = """
#         Class Program {
#         main(){
#                 Val x,y: String = "String", "a";
#                 x = "String1";
#                 y = "String2";
#         } }
#         """
#         expect = "Cannot Assign To Constant: AssignStmt(Id(x),StringLit(String1))"
#         self.assertTrue(TestChecker.test(input,expect,408))
#
#     def test_9(self):
#         input = """
#         Class Program {
#         main(){
#                 Var x,y: Float;
#                 x = 1.3;
#                 y = 2.e-4;
#                 Return "No Error";
#         } }
#         """
#         expect = "Type Mismatch In Statement: Return(StringLit(No Error))"
#         self.assertTrue(TestChecker.test(input,expect,409))
#
#     def test_10(self):
#         input = """
#         Class Program {
#         main(){
#                 Var x,y: Float;
#                 x = 1.3 + 2.7;
#                 y = 2.e-4 + 1;
#                 Return "No Error";
#         } }
#         """
#         expect = "Type Mismatch In Statement: Return(StringLit(No Error))"
#         self.assertTrue(TestChecker.test(input,expect,410))
#
#     def test_11(self):
#         input = """
#         Class Program {
#         main(){
#                 Var x,y: Boolean;
#                 x = 1 == 2;
#                 y = 2.0 != 2;
#         } }
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(!=,FloatLit(2.0),IntLit(2))"
#         self.assertTrue(TestChecker.test(input,expect,411))
#
#     def test_12(self):
#         input = """
#         Class Program {
#         main(){
#                 Var x: String;
#                 x = "String1" +. "String2";
#                 Var y: Boolean;
#                 y = x ==. "String2";
#                 Return "No Error";
#         } }
#         """
#         expect = "Type Mismatch In Statement: Return(StringLit(No Error))"
#         self.assertTrue(TestChecker.test(input,expect,412))
#
#     def test_13(self):
#         input = """
#         Class Program {
#         main(){
#         }
#         Var myVar: String = "Hello World";
#         Var myVar: Int;
#         }
#         """
#         expect = "Redeclared Attribute: myVar"
#         self.assertTrue(TestChecker.test(input,expect,413))
#
#     def test_14(self):
#         input = """
#         Class A {}
#         Class B {}
#         Class A {}
#
#         """
#         expect = "Redeclared Class: A"
#         self.assertTrue(TestChecker.test(input,expect,414))
#
#     def test_15(self):
#         input = """
#         Class A {}
#         Class B : C {}
#         Class A {}
#         """
#         expect = "Undeclared Class: C"
#         self.assertTrue(TestChecker.test(input,expect,415))
#
#     def test_16(self):
#         input = """
#             Class Program {
#                 main(){
#                     Var b: Int;
#                     Val a: Int=1;
#                     Foreach (a In b ..  2){
#
#                         Continue;
#                     }
#                     Break;
#                 }
#              }
#         """
#         expect = "Break Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,416))
#
#     def test_17(self):
#         input = """
#             Class Program {
#                 main(){
#                     Var b: Int;
#                     Val a: Int=1;
#                     Foreach (a In b ..  2){
#                         Break;
#
#                     }
#                     Continue;
#                 }
#              }
#         """
#         expect = "Continue Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,417))
#
#     def test_18(self):
#         input = """
#             Class Program {
#                 Var a:Array[Int,2]=Array(1,2.0);
#                 main(){}
#              }
#         """
#         expect = "Illegal Array Literal: [IntLit(1),FloatLit(2.0)]"
#
#         self.assertTrue(TestChecker.test(input,expect,418))
#
#     def test_19(self):
#         input = """Class Program {
#                 Val a:Int;
#                 main(){}
#              }"""
#         expect = "Illegal Constant Expression: None"
#         self.assertTrue(TestChecker.test(input,expect,419))
#
#     def test_20(self):
#         input = """Class Program { Var main:Int;}"""
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input,expect,420))
# #------------------------------------------
#     def test_21(self):
#         input = """
#             Class Program {
#                 main(){
#                     Var b: Array[Int,2];
#                     Var a: Array[Array[Int,2],2];
#                     b=Array(1,2);
#                     b[1]=2;
#                     a=Array(Array(1,2),Array(1,2));
#                     a[1]=Array(1,2);
#                     a[1][2]=1;
#                     a[1][2][3]=1;
#                 }
#              }
#         """
#         expect = "Type Mismatch In Expression: ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)])"
#
#         self.assertTrue(TestChecker.test(input,expect,421))
#
#     def test_22(self):
#         input = """
#             Class Program {
#                 main(){
#                     Var b: Float;
#                     Var a: Int;
#                     Foreach (a In b ..  2){}
#                 }
#              }
#         """
#         expect = "Type Mismatch In Statement: For(Id(a),Id(b),IntLit(2),IntLit(1),Block([])])"
#         self.assertTrue(TestChecker.test(input,expect,422))
#
#     def test_23(self):
#         input = """Class Program {
#                 Val a:Int = 2;
#                 main(){
#                     Var a : Array[Int,2];
#                     a = Array(2, 4);
#                     a = Array(1.5, 3);
#                 }
#              }"""
#         expect = "Illegal Array Literal: [FloatLit(1.5),IntLit(3)]"
#         self.assertTrue(TestChecker.test(input,expect,423))
#
#     def test_24(self):
#         input = """Class Program {
#                 Val a:Int = 2;
#                 main(){
#                     Var a : Array[Float,2];
#                     a = Array(2, 4);
#                     a = Array(True, 0);
#                 }
#              }"""
#         expect = "Illegal Array Literal: [BooleanLit(True),IntLit(0)]"
#         self.assertTrue(TestChecker.test(input,expect,424))
#
#     def test_25(self):
#         input = """Class A {
#                 Val a:Int;
#                 Val b: Float;
#                 Val a: Float;
#              }"""
#         expect = "Illegal Constant Expression: None"
#         self.assertTrue(TestChecker.test(input,expect,425))
#
#     def test_26(self):
#         input = """Class A {
#                 Var a:Int;
#                 Var b: Float;
#                 Var a: Float;
#              }"""
#         expect = "Redeclared Attribute: a"
#         self.assertTrue(TestChecker.test(input,expect,426))
# #--------------------------------------------------
#     def test_27(self):
#         input = """Class A {
#                 Val a: Int = 12;
#                 Var b: Float = 3;
#                 Val a: Float = 4.5;
#              }"""
#         expect = "Redeclared Attribute: a"
#         self.assertTrue(TestChecker.test(input,expect,427))
#
#     def test_28(self):
#         input = """Class Program {
#                 Var a: Int;
#                 Var b: Float;
#                 Val a: Float;
#              }"""
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input,expect,428))
#
#     def test_29(self):
#         input = """Class A {
#                 Var a: Int;
#                 Var b: Float;
#                 Val a: Float;
#              }"""
#         expect = "Redeclared Attribute: a"
#         self.assertTrue(TestChecker.test(input,expect,429))
#
#     def test_30(self):
#         input = """Class A {
#                 Var a:Int;
#                 Var b: Float;
#                 method1(){
#                     Var a : Int;
#                     Var a: Float;
#                 }
#              }"""
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input,expect,430))
#
# #=====================================================================
#     def test_31(self):
#         input = """Class A {
#                 Var a:Int;
#                 Var b: Float;
#                 method1(){
#                     Val a : Int = 18;
#                     Val a: Float = 20;
#                 }
#              }"""
#         expect = "Redeclared Constant: a"
#         self.assertTrue(TestChecker.test(input,expect,431))
#
#     def test_32(self):
#         input = """Class A {
#                 Var a:Int;
#                 Var b: Float;
#                 method1(){
#                     Var a : Int;
#                     Var b: Float;
#                 }
#              }
#                 Class A : C{}"""
#         expect = "Redeclared Class: A"
#         self.assertTrue(TestChecker.test(input,expect,432))
#
#     def test_33(self):
#         input = """Class A {
#                 Var a:Int;
#                 Var b: Float;
#                 method1(){
#                     Var a : Int;
#                     Var b: Float;
#                 }
#                 method1(){}
#              }"""
#         expect = "Redeclared Method: method1"
#         self.assertTrue(TestChecker.test(input,expect,433))
#
#     def test_34(self):
#         input = """Class A {
#                 Var a:Int;
#                 Var b: Float;
#                 method1(a, b: Int; c: Float; a: String){
#                     Var a : Int;
#                     Var a: Float;
#                 }
#              }"""
#         expect = "Redeclared Parameter: a"
#         self.assertTrue(TestChecker.test(input,expect,434))
#
#     def test_35(self):
#         input = """Class A {
#                 Var a:Int;
#                 Var b: Float;
#                 method1(){
#                     c = 12;
#                 }
#              }"""
#         expect = "Undeclared Identifier: c"
#         self.assertTrue(TestChecker.test(input,expect,435))
#
#     def test_36(self):
#         input = """Class A {
#                 Var a:Int;
#                 Var b: Float;
#                 method1(){
#                     Var a : Int;
#                     a = 10 + c;
#                 }
#              }"""
#         expect = "Undeclared Identifier: c"
#         self.assertTrue(TestChecker.test(input,expect,436))
#
#     def test_37(self):
#         input = """Class A {
#                 Var a:Int;
#                 Var b: A;
#                 method1(){
#                     Var a : Int;
#                     a = b.x;
#                 }
#              }"""
#         expect = "Undeclared Attribute: x"
#         self.assertTrue(TestChecker.test(input,expect,437))
#
#     def test_38(self):
#         input = """Class A {
#                 Var a:Int;
#                 Var b: Float;
#                 method1(){
#                     Var a : Int;
#                     c = b.x;
#                 }
#              }"""
#         expect = "Type Mismatch In Expression: FieldAccess(Id(b),Id(x))"
#         self.assertTrue(TestChecker.test(input,expect,438))
#
#     def test_39(self):
#         input = """Class A {
#                 Var a:Int;
#                 Var b: A;
#                 method1(){
#                     Var a : Int;
#                     c = b.x;
#                 }
#              }"""
#         expect = "Undeclared Attribute: x"
#         self.assertTrue(TestChecker.test(input,expect,439))
#
#     def test_40(self):
#         input = """Class A {
#                 Var a:Int;
#                 Var b: A;
#                 method1(){
#                     Var a : Int;
#                     c = Self.a;
#
#                 }
#              }"""
#         expect = "Undeclared Identifier: c"
#         self.assertTrue(TestChecker.test(input,expect,440))
#
#     def test_41(self):
#         input = """Class A {
#                  Var a:Int;
#                 Var b: A;
#                 method1(){
#                     Var a : Int;
#                     c = b.a;
#                 }
#              }"""
#         expect = "Undeclared Identifier: c"
#         self.assertTrue(TestChecker.test(input,expect,441))
# #=================================================================
#
#     def test_42(self):
#         input = """Class A {
#                 Var a:Int;
#                 Var b: A;
#                 method1(){
#                     Var a : Int;
#                     a = A.a;
#                 }
#              }"""
#         expect = "Illegal Member Access: FieldAccess(Id(A),Id(a))"
#         self.assertTrue(TestChecker.test(input,expect,442))
#
#     def test_43(self):
#         input = """Class A {
#                 Var a:Int;
#                 Var b: A;
#                 method1(){
#                     Var a: A;
#                     b = a.Hello();
#                 }
#              }"""
#         expect = "Undeclared Method: Hello"
#         self.assertTrue(TestChecker.test(input,expect,443))
#
#     def test_44(self):
#         input = """Class A {
#                 Var a:Int;
#                 Var b: A;
#                 method1(){
#                     Var a: A;
#                     a.Hello();
#                 }
#              }"""
#         expect = "Undeclared Method: Hello"
#         self.assertTrue(TestChecker.test(input,expect,444))
#
#     def test_45(self):
#         input = """Class A {
#                 Var a:Int;
#                 Var b: A;
#                 method1(a, b: Ho){
#
#                 }
#              }"""
#         expect = "Undeclared Class: Ho"
#         self.assertTrue(TestChecker.test(input,expect,445))
#
#     def test_46(self):
#         input = """Class A {
#                 Var a:Int;
#                 Var b: A;
#                 method1(a, b: Float){
#                     Val a : Int = 12;
#                 }
#              }"""
#         expect = "Redeclared Constant: a"
#         self.assertTrue(TestChecker.test(input,expect,446))
#
#     def test_47(self):
#         input = """Class A {
#                 Var a:Int;
#                 Var b: A;
#                 method1(a, b: Int){
#                     Val c : Int = 19;
#                     c = 12;
#                 }
#              }"""
#         expect = "Cannot Assign To Constant: AssignStmt(Id(c),IntLit(12))"
#         self.assertTrue(TestChecker.test(input,expect,447))
#
#     def test_48(self):
#         input = """
#             Class Program {
#                 Val a:String="a"+."b";
#                 Val b:Float=-1+1;
#                 Val c:Boolean=False&&(("a"+."b")==."ab");
#                 main(){
#                     Val a: Int=1;
#                     a=1;
#                 }
#              }
#         """
#         expect = "Cannot Assign To Constant: AssignStmt(Id(a),IntLit(1))"
#         self.assertTrue(TestChecker.test(input,expect,448))
#
#     def test_49(self):
#         input = """Class A {
#                 Var a:Int;
#                 Var b: A;
#                 method1(a, b: A){
#                     If(19 == 12){
#                         Return 19;
#                     }Elseif(b<c){
#
#                     }Else{
#
#                     }
#                 }
#              }"""
#         expect = "Undeclared Identifier: c"
#         self.assertTrue(TestChecker.test(input,expect,449))
#
#     def test_50(self):
#         input = """Class A {
#                 Var a:Int;
#                 Var b: A;
#                 method1(a, b: Int){
#                     If(19 == a){
#                         Return 19;
#                     }Elseif(b<c){
#
#                     }Else{
#
#                     }
#                 }
#              }"""
#         expect = "Undeclared Identifier: c"
#         self.assertTrue(TestChecker.test(input,expect,450))
# ##================================================================
#     def test_51(self):
#         input = """
#             Class B {
#                 Var c: Int = 12;
#                 method1(){
#                     Return;
#                 }
#             }
#             Class A {
#                 Var a:Int;
#                 Var b: A;
#                 Var c: B;
#                 method1(a, b: B){
#                     If(19 == c.c){
#                         Return 19;
#                     }Elseif(b<f){
#
#                     }Else{
#
#                     }
#                 }
#              }"""
#         expect = "Undeclared Identifier: f"
#         self.assertTrue(TestChecker.test(input,expect,451))
#
#     def test_52(self):
#         input = """Class B {
#                 Var c: Int = 12;
#                 method1(){
#                     Return;
#                 }
#             }
#             Class A {
#                 Var a:Int;
#                 Var b: A;
#                 Var c: B;
#                 method1(a, b: B){
#                     If(b == c.c){
#                         Return 19;
#                     }Elseif(b<c){
#
#                     }Else{
#
#                     }
#                 }
#              }"""
#         expect = "Type Mismatch In Expression: BinaryOp(==,Id(b),FieldAccess(Id(c),Id(c)))"
#         self.assertTrue(TestChecker.test(input,expect,452))
#
#     def test_53(self):
#         input = """
#             Class Program {
#                 Var a:String="a"+."b";
#                 Val b:Float=-1+1;
#                 Val c:Boolean=False&&(("a"+."b")==."ab");
#                 main(){
#                     Self.a = 1;
#                 }
#              }
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(FieldAccess(Self(),Id(a)),IntLit(1))"
#         self.assertTrue(TestChecker.test(input,expect,453))
#
#     def test_54(self):
#         input = """
#             Class A{
#
#                 Constructor(a:Int;b:Float){}
#             }
#
#             Class Program {
#
#
#                 main(){
#                 Var a:A=New A(2,3);
#                 Var b:A=New A(2,3.0);
#                 Var c:A=New A(2.0,3);}
#              }
#         """
#         expect = "Type Mismatch In Expression: NewExpr(Id(A),[FloatLit(2.0),IntLit(3)])"
#         self.assertTrue(TestChecker.test(input,expect,454))
#
#     def test_55(self):
#         input = """
#             Class A{
#                 Var a: Int=1;
#                 Var b: Float=1;
#                 Var $a: Int=1;
#                 Constructor(a:Int;b:Float){}
#             }
#             Class B{
#                 Var a: A;
#             }
#             Class Program {
#                 main(){
#                     Var b: B;
#                     Var a: Int;
#                     a=b.a.b;
#                 }
#              }
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a),FieldAccess(FieldAccess(Id(b),Id(a)),Id(b)))"
#         self.assertTrue(TestChecker.test(input,expect,455))
#
# ##=============================================================
#     def test_56(self):
#         #test for in stmt
#         input = """
#             Class Program {
#                 main(){
#                     Var b: Float;
#                     Var a: Int;
#                     Foreach (a In b ..  2){}
#                 }
#              }
#         """
#         expect = "Type Mismatch In Statement: For(Id(a),Id(b),IntLit(2),IntLit(1),Block([])])"
#         self.assertTrue(TestChecker.test(input,expect,456))
#
#     def test_57(self):
#         #test array cell
#         input = """
#             Class Program {
#                 main(){
#                     Var b: Array[Int,2];
#                     Var a: Array[Array[Int,2],2];
#                     b=Array(1,2);
#                     b[1]=2;
#                     a=Array(Array(1,2),Array(1,2));
#                     a[1]=Array(1,2);
#                     a[1][2]=1;
#                     a[1][2][3]=1;
#                 }
#              }
#         """
#         expect = "Type Mismatch In Expression: ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)])"
#         self.assertTrue(TestChecker.test(input,expect,457))
#
#     def test_58(self):
#         #test array cell
#         input = """
#             Class Program {
#                 main(){
#                     Var b: Array[Int,2];
#                     Var a: Array[Array[Int,2],2];
#                     b=Array(1,2);
#                     b[1]=2;
#                     a=Array(Array(1,2),Array(1,2));
#                     a[1]=Array(1,2);
#                     a[1][2]=1;
#                     a[1][2][3]=1;
#                 }
#              }
#         """
#         expect = "Type Mismatch In Expression: ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)])"
#         self.assertTrue(TestChecker.test(input,expect,458))
#
#     def test_59(self):
#         #test type in binop
#         input = """
#             Class Program {
#                 Val b:Float=-1+1;
#                 Val c:Boolean=!True&&False;
#                 Var d:Int=-1.0+1;
#                 main(){}
#              }
#         """
#         expect = "Type Mismatch In Statement: AttributeDecl(Instance,VarDecl(Id(d),IntType,BinaryOp(+,UnaryOp(-,FloatLit(1.0)),IntLit(1))))"
#         self.assertTrue(TestChecker.test(input,expect,459))
#
#     def test_60(self):
#         # test array type mismatch type
#         input = """
#             Class Program {
#                 Var a:Array[Int,2]=Array(1,2.0);
#                 main(){}
#              }
#         """
#         expect = "Illegal Array Literal: [IntLit(1),FloatLit(2.0)]"
#         self.assertTrue(TestChecker.test(input,expect,460))
#
#     def test_61(self):
#         # test array type mismatch size
#         input = """
#             Class Program {
#                 main(){
#                     Var a:Array[Int,2]=Array(1);
#                 }
#              }
#         """
#         expect = "Type Mismatch In Statement: VarDecl(Id(a),ArrayType(2,IntType),[IntLit(1)])"
#         self.assertTrue(TestChecker.test(input,expect,461))
#
#     def test_62(self):
#         # test array type mismatch size
#         input = """
#             Class Program {
#                 main(){
#                     Val a:Array[Int,2]=Array(1);
#                 }
#              }
#         """
#         expect = "Type Mismatch In Statement: ConstDecl(Id(a),ArrayType(2,IntType),[IntLit(1)])"
#         self.assertTrue(TestChecker.test(input,expect,462))
#
#     def test_63(self):
#         # test array type mismatch size
#         input = """
#             Class A {
#                 method1(){
#                     {
#                         Return 1;
#                     }
#                     {
#                         Return 2.5;
#                     }
#                     {
#                         Return 3;
#                     }
#                 }
#             }
#             Class Program {
#                 main(){
#                     Var b: A;
#                     Var a: Int = b.method1();
#                 }
#              }
#         """
#         expect = "Type Mismatch In Statement: VarDecl(Id(a),IntType,CallExpr(Id(b),Id(method1),[]))"
#         self.assertTrue(TestChecker.test(input,expect,463))
#
#     def test_64(self):
#         # test array type mismatch size
#         input = """
#             Class A {
#                 method1(){
#                     {
#                         Return 1;
#                     }
#                     {
#                         Return 2.5;
#                     }
#                     {
#                         Return 3;
#                     }
#                 }
#             }
#             Class Program {
#                 main(){
#                     Var b: A;
#                     Var a: Float = b.method1();
#                     Var a: String;
#                 }
#              }
#         """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input,expect,464))
#
#     def test_65(self):
#         # test array type mismatch size
#         #test for in stmt
#         input = """
#             Class Program {
#                 main(){
#                     Var b: Float;
#                     Var a: Int;
#                     Foreach (a In b ..  2){}
#                 }
#              }
#         """
#         expect = "Type Mismatch In Statement: For(Id(a),Id(b),IntLit(2),IntLit(1),Block([])])"
#         self.assertTrue(TestChecker.test(input,expect,465))
#
#     def test_66(self):
#         # test array type mismatch size
#         input = """
#             Class A {
#                 method1(){
#                     {
#                         Return 1;
#                     }
#                     {
#                         Return "hay" +. "chan";
#                     }
#                     {
#                         Return 3;
#                     }
#                 }
#             }
#             Class Program {
#                 main(){
#                     Var b: A;
#                     Var a: Float = b.method1();
#                 }
#              }
#         """
#         expect = "Type Mismatch In Statement: Block([Return(BinaryOp(+.,StringLit(hay),StringLit(chan)))])"
#         self.assertTrue(TestChecker.test(input,expect,466))