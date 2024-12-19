# 1912190
# Nguyễn Mai Thy

import unittest
from TestUtils import TestAST
# from AST import *
 
class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        input = """Class Test{}"""
        expect=r"Program([ClassDecl(Id(Test),[])])"
        self.assertTrue(TestAST.test(input,expect,300))

    def test_2(self):
        input = """Class Test1{} Class Test2{}"""
        expect=r"Program([ClassDecl(Id(Test1),[]),ClassDecl(Id(Test2),[])])"
        self.assertTrue(TestAST.test(input,expect,301))

    def test_3(self):
        input = """Class Program{}"""
        expect=r"Program([ClassDecl(Id(Program),[])])"
        self.assertTrue(TestAST.test(input,expect,302))
   
    def test_4(self):
        input= """
            Class Program{
                Main(){
                    Val My1stCons: Int=1 ;
                    Var My1stVar,My2ndVar: Float = 1.0 , 2.0;
                    Var trueVar,falseVar: Boolean = True, False;
                    Val stringVal:String="123";
                    Var classVar: abc=1;
                    Var arrVar: Array[Int,2]=Array(0,1,2);
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Program),[MethodDecl(Id(Main),Instance,[],Block([ConstDecl(Id(My1stCons),IntType,IntLit(1)),VarDecl(Id(My1stVar),FloatType,FloatLit(1.0)),VarDecl(Id(My2ndVar),FloatType,FloatLit(2.0)),VarDecl(Id(trueVar),BoolType,BooleanLit(True)),VarDecl(Id(falseVar),BoolType,BooleanLit(False)),ConstDecl(Id(stringVal),StringType,StringLit(123)),VarDecl(Id(classVar),ClassType(Id(abc)),IntLit(1)),VarDecl(Id(arrVar),ArrayType(2,IntType),[IntLit(0),IntLit(1),IntLit(2)])]))])])"
        self.assertTrue(TestAST.test(input,expect,303))
    
    def test_5(self):
        input= """
            Class Program{
                Main(){
                    Var hello: Int; ##need none##
                    Var a, b: Heo; ##need null lit##
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(Main),Instance,[],Block([VarDecl(Id(hello),IntType),VarDecl(Id(a),ClassType(Id(Heo)),NullLiteral()),VarDecl(Id(b),ClassType(Id(Heo)),NullLiteral())]))])])"
        self.assertTrue(TestAST.test(input,expect,304))

    def test_6(self):
        input= """
            Class Program: bigpro{
                main(){
                }
            }
            Class Program{
                main(){
                }
                main(a, b: Int){
                }
            }
            Class hello{
                main(){
                }
            }
            Class Shape {
                Val abc: Int =1;
            }
        """
        expect = r"Program([ClassDecl(Id(Program),Id(bigpro),[MethodDecl(Id(main),Static,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([])),MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([]))]),ClassDecl(Id(hello),[MethodDecl(Id(main),Instance,[],Block([]))]),ClassDecl(Id(Shape),[AttributeDecl(Instance,ConstDecl(Id(abc),IntType,IntLit(1)))])])"
        self.assertTrue(TestAST.test(input,expect,305))

    def test_7(self):
        input= """
            Class Shape {
                Hello(a,b,c: Int; b: Float){
                    {
                        a = b + c;
                    }
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Shape),[MethodDecl(Id(Hello),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(b),FloatType)],Block([Block([AssignStmt(Id(a),BinaryOp(+,Id(b),Id(c)))])]))])])"
        self.assertTrue(TestAST.test(input,expect,306))

    def test_8(self):
        input= """
            Class Shape {
                $getNumOfShape() {
                    a = "Mai Thy";
                }
                Val abc:Int=1;
            }
        """
        expect = r"Program([ClassDecl(Id(Shape),[MethodDecl(Id($getNumOfShape),Static,[],Block([AssignStmt(Id(a),StringLit(Mai Thy))])),AttributeDecl(Instance,ConstDecl(Id(abc),IntType,IntLit(1)))])])"
        self.assertTrue(TestAST.test(input,expect,307))

    def test_9(self):
        input= """
            Class Program{
                Hello(a,b,c: Int; b: Float; c: MaiThy; e: Array[Array[Float, 2], 4]){
                    {
                        a = b + c;
                    }
                    hello = a - c/3 + 19.8;
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(Hello),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(b),FloatType),param(Id(c),ClassType(Id(MaiThy))),param(Id(e),ArrayType(4,ArrayType(2,FloatType)))],Block([Block([AssignStmt(Id(a),BinaryOp(+,Id(b),Id(c)))]),AssignStmt(Id(hello),BinaryOp(+,BinaryOp(-,Id(a),BinaryOp(/,Id(c),IntLit(3))),FloatLit(19.8)))]))])])"
        self.assertTrue(TestAST.test(input,expect,308))
##################### xem lai thu tu ket hop cac exp #####

    def test_10(self):
        input= """
            Class Program{
                main(){
                    Val My1stCons,My2ndCons: Int ;
                    Var My1stVar: Float;
                    Var trueVar,falseVar:Boolean;
                    Val classVal: abc;
                    Val stringVal:String;
                    Var classVar: abc;
                    Var arrVar: Array[Int,2];
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(My1stCons),IntType,None),ConstDecl(Id(My2ndCons),IntType,None),VarDecl(Id(My1stVar),FloatType),VarDecl(Id(trueVar),BoolType),VarDecl(Id(falseVar),BoolType),ConstDecl(Id(classVal),ClassType(Id(abc)),None),ConstDecl(Id(stringVal),StringType,None),VarDecl(Id(classVar),ClassType(Id(abc)),NullLiteral()),VarDecl(Id(arrVar),ArrayType(2,IntType))]))])])"
        self.assertTrue(TestAST.test(input,expect,309))

    def test_11(self):
        input= """
            Class Program{
                Val My1stCons: Int=1 ;
                Var My1stVar,$My2ndVar: Float=1.0,2.0;
                Val My1stCons: Int=1 ;
                Var My1stVar,My2ndVar: Float=1.0,2.0;
                Var trueVar,falseVar:Boolean=True,False;
                Val stringVal:String="123";
                Var classVar: abc=1;
                Var arrVar: Array[Int,2]=Array(0,1,2);
            }
        """
        expect=r"Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(My1stCons),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(My1stVar),FloatType,FloatLit(1.0))),AttributeDecl(Static,VarDecl(Id($My2ndVar),FloatType,FloatLit(2.0))),AttributeDecl(Instance,ConstDecl(Id(My1stCons),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(My1stVar),FloatType,FloatLit(1.0))),AttributeDecl(Instance,VarDecl(Id(My2ndVar),FloatType,FloatLit(2.0))),AttributeDecl(Instance,VarDecl(Id(trueVar),BoolType,BooleanLit(True))),AttributeDecl(Instance,VarDecl(Id(falseVar),BoolType,BooleanLit(False))),AttributeDecl(Instance,ConstDecl(Id(stringVal),StringType,StringLit(123))),AttributeDecl(Instance,VarDecl(Id(classVar),ClassType(Id(abc)),IntLit(1))),AttributeDecl(Instance,VarDecl(Id(arrVar),ArrayType(2,IntType),[IntLit(0),IntLit(1),IntLit(2)]))])])"
        self.assertTrue(TestAST.test(input,expect,310))

    def test_12(self):
        input= """
            Class Program{
                Val My1stCons,$My2ndCons: Int ;
                Var My1stVar: Float;
                Val My1stCons,My2ndCons: Int ;
                Var My1stVar: Float;
                Var trueVar,falseVar:Boolean;
                Val classVal: abc;
                Val stringVal:String;
                Var classVar: abc;
                Var arrVar: Array[Int,2];
            }
        """
        expect=r"Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(My1stCons),IntType,None)),AttributeDecl(Static,ConstDecl(Id($My2ndCons),IntType,None)),AttributeDecl(Instance,VarDecl(Id(My1stVar),FloatType)),AttributeDecl(Instance,ConstDecl(Id(My1stCons),IntType,None)),AttributeDecl(Instance,ConstDecl(Id(My2ndCons),IntType,None)),AttributeDecl(Instance,VarDecl(Id(My1stVar),FloatType)),AttributeDecl(Instance,VarDecl(Id(trueVar),BoolType)),AttributeDecl(Instance,VarDecl(Id(falseVar),BoolType)),AttributeDecl(Instance,ConstDecl(Id(classVal),ClassType(Id(abc)),None)),AttributeDecl(Instance,ConstDecl(Id(stringVal),StringType,None)),AttributeDecl(Instance,VarDecl(Id(classVar),ClassType(Id(abc)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(arrVar),ArrayType(2,IntType)))])])"
        self.assertTrue(TestAST.test(input,expect,311))

    def test_13(self):
        input= """
            Class Program{
                Val My1stCons,$My2ndCons: Int ;
                Var My1stVar: Float;
                Constructor(){}
                Destructor(){}
                method1(){}
                $method2(){}
                method3(a,b,c:Int;x,y,z:Float;wut:String){}
            }
        """
        expect=r"Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(My1stCons),IntType,None)),AttributeDecl(Static,ConstDecl(Id($My2ndCons),IntType,None)),AttributeDecl(Instance,VarDecl(Id(My1stVar),FloatType)),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(method1),Instance,[],Block([])),MethodDecl(Id($method2),Static,[],Block([])),MethodDecl(Id(method3),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(x),FloatType),param(Id(y),FloatType),param(Id(z),FloatType),param(Id(wut),StringType)],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,312))

    def test_14(self):
        input= """
            Class Program{
                Val My1stCons,$My2ndCons: Int ;
                Var My1stVar: Float;
                Constructor(){
                    lhs=1;
                    a.b=1;
                    abc::$xyz=1;
                    abc::$xyz.a=1;
                    a::$b[1]=2;
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(My1stCons),IntType,None)),AttributeDecl(Static,ConstDecl(Id($My2ndCons),IntType,None)),AttributeDecl(Instance,VarDecl(Id(My1stVar),FloatType)),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(Id(lhs),IntLit(1)),AssignStmt(FieldAccess(Id(a),Id(b)),IntLit(1)),AssignStmt(FieldAccess(Id(abc),Id($xyz)),IntLit(1)),AssignStmt(FieldAccess(FieldAccess(Id(abc),Id($xyz)),Id(a)),IntLit(1)),AssignStmt(ArrayCell(FieldAccess(Id(a),Id($b)),[IntLit(1)]),IntLit(2))]))])])"
        self.assertTrue(TestAST.test(input,expect,313))

    def test_15(self):
        input= """
            Class Program{
                Main(){
                    If(a==b){}
                    If(b<c){}Else{}
                    If(a==b){}Elseif(b<c){}
                    If(a==b){}Elseif(b<c){}Else{}
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Program),[MethodDecl(Id(Main),Instance,[],Block([If(BinaryOp(==,Id(a),Id(b)),Block([])),If(BinaryOp(<,Id(b),Id(c)),Block([]),Block([])),If(BinaryOp(==,Id(a),Id(b)),Block([]),If(BinaryOp(<,Id(b),Id(c)),Block([]))),If(BinaryOp(==,Id(a),Id(b)),Block([]),If(BinaryOp(<,Id(b),Id(c)),Block([]),Block([])))]))])])"
        self.assertTrue(TestAST.test(input,expect,314))

    def test_16(self):
        input= """
            Class Program{
                Main(){
                    Foreach (i In 1 .. 100 By 2) {
                        Out.printInt(i);
                    }
                    Foreach (x In 5 .. 2) {
                        Out.printInt(arr[x]);
                    }
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Program),[MethodDecl(Id(Main),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([Call(Id(Out),Id(printInt),[Id(i)])])]),For(Id(x),IntLit(5),IntLit(2),IntLit(1),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(arr),[Id(x)])])])])]))])])"
        self.assertTrue(TestAST.test(input,expect,315))

    def test_17(self):
        input= """
            Class Program{
                Main(){
                    Foreach (i In 1 .. 100 By 2) {
                        Continue;
                    }
                    Foreach (x In 5 .. 2) {
                        Break;
                    }
                    Return;
                    Return (a==1);
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Program),[MethodDecl(Id(Main),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([Continue])]),For(Id(x),IntLit(5),IntLit(2),IntLit(1),Block([Break])]),Return(),Return(BinaryOp(==,Id(a),IntLit(1)))]))])])"
        self.assertTrue(TestAST.test(input,expect,316))

    def test_18(self):
        input= """
            Class Phong
            {
                main() {
                    a = x::$y.z.t;
                    b = (x + 1 ).y.z.t;
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Phong),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(a),FieldAccess(FieldAccess(FieldAccess(Id(x),Id($y)),Id(z)),Id(t))),AssignStmt(Id(b),FieldAccess(FieldAccess(FieldAccess(BinaryOp(+,Id(x),IntLit(1)),Id(y)),Id(z)),Id(t)))]))])])"
        self.assertTrue(TestAST.test(input,expect,317))

    def test_19(self):
        input= """
            Class Rectangle: Shape {
                getArea() {
                    Return Self.length * Self.width;
                }
            }
            Class Program {
                main() {
                    Out.printInt(Shape::$numOfShape);
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))])]))])])"
        self.assertTrue(TestAST.test(input,expect,318))

    def test_20(self):
        input= """
            Class Program {
                main(){}
            }
        """
        expect=r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,319))

    def test_21(self):
        input= """
            Class B{
                main(){
                    Var x, y, z, t: Array[Int, 5];
                }
            }
            Class Program {
                Var d: B = New B();
                main(t: Array[Int, 5]){
                    Return t[0];
                }
                main(){
                    Return;
                }
            }
        """
        expect=r"Program([ClassDecl(Id(B),[MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(x),ArrayType(5,IntType)),VarDecl(Id(y),ArrayType(5,IntType)),VarDecl(Id(z),ArrayType(5,IntType)),VarDecl(Id(t),ArrayType(5,IntType))]))]),ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(d),ClassType(Id(B)),NewExpr(Id(B),[]))),MethodDecl(Id(main),Instance,[param(Id(t),ArrayType(5,IntType))],Block([Return(ArrayCell(Id(t),[IntLit(0)]))])),MethodDecl(Id(main),Static,[],Block([Return()]))])])"
        self.assertTrue(TestAST.test(input,expect,320))

    def test_22(self):
        input= """
            Class C{
                $forfunc(i : Int){
                    Foreach(a In 1 .. 0x45){
                        Foreach(b In i - a .. i + 2*a By i){
                            Out::$println(b, a, i);
                        }
                    }
                }
            }
            Class Program {
                main(){
                    C::$forfunc(1);
                }
            }
        """
        expect=r"Program([ClassDecl(Id(C),[MethodDecl(Id($forfunc),Static,[param(Id(i),IntType)],Block([For(Id(a),IntLit(1),IntLit(69),IntLit(1),Block([For(Id(b),BinaryOp(-,Id(i),Id(a)),BinaryOp(+,Id(i),BinaryOp(*,IntLit(2),Id(a))),Id(i),Block([Call(Id(Out),Id($println),[Id(b),Id(a),Id(i)])])])])])]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(C),Id($forfunc),[IntLit(1)])]))])])"
        self.assertTrue(TestAST.test(input,expect,321))

    def test_23(self):
        input= """
            Class Program{
                Val My1stCons,oct,hex,bin: Int=1,011,0x11,0b11 ;
                Main(){
                    Val My1stCons,oct,hex,bin: Int=1,011,0x11,0b11 ;
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(My1stCons),IntType,IntLit(1))),AttributeDecl(Instance,ConstDecl(Id(oct),IntType,IntLit(9))),AttributeDecl(Instance,ConstDecl(Id(hex),IntType,IntLit(17))),AttributeDecl(Instance,ConstDecl(Id(bin),IntType,IntLit(3))),MethodDecl(Id(Main),Instance,[],Block([ConstDecl(Id(My1stCons),IntType,IntLit(1)),ConstDecl(Id(oct),IntType,IntLit(9)),ConstDecl(Id(hex),IntType,IntLit(17)),ConstDecl(Id(bin),IntType,IntLit(3))]))])])"
        self.assertTrue(TestAST.test(input,expect,322))

    def test_24(self):
        input= """
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
        expect=r"Program([ClassDecl(Id(Shape),[MethodDecl(Id($getNumOfShape),Static,[],Block([AssignStmt(Id(a),StringLit(Mai Thy))])),AttributeDecl(Static,VarDecl(Id($Student),ClassType(Id(Student)),NewExpr(Id(Student),[]))),MethodDecl(Id(Hello),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(b),FloatType),param(Id(c),ClassType(Id(MaiThy))),param(Id(e),ArrayType(4,ArrayType(2,BoolType)))],Block([Block([If(BinaryOp(>=,ArrayCell(Id(a),[IntLit(5)]),FieldAccess(Id(X),Id($hello))),Block([AssignStmt(Id(a),BinaryOp(&&,Id(b),Id(c)))]),If(BinaryOp(<,Id(a),Id(b)),Block([For(Id(lehoe),Id(a),ArrayCell(Id(b),[BinaryOp(+,IntLit(9),IntLit(2))]),BinaryOp(+,BinaryOp(-,IntLit(5),IntLit(9)),IntLit(1)),Block([AssignStmt(Id(x),BinaryOp(-,Id(x),IntLit(1)))])])]),If(BinaryOp(>,Id(c),Id(d)),Block([]),Block([]))))])]))])])"
        self.assertTrue(TestAST.test(input,expect,323))

    def test_25(self):
        input= """
            Class Program{
                test_if(){
                    If(a == b){
                    }
                    Elseif(c == d){
                    }
                    Elseif(e == f){
                    }
                    Else{

                    }
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Program),[MethodDecl(Id(test_if),Instance,[],Block([If(BinaryOp(==,Id(a),Id(b)),Block([]),If(BinaryOp(==,Id(c),Id(d)),Block([]),If(BinaryOp(==,Id(e),Id(f)),Block([]),Block([]))))]))])])"
        self.assertTrue(TestAST.test(input,expect,324))

#-------------------------------------------------------------------------
    def test_26(self):
        input= """
            Class Shape {
                Var $Student : Student = New Student();
                Hello(){
                        If(a >= b){
                        }
                        Elseif(a < b){
                            Foreach(lehoe In a .. b By 1){
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
        """
        expect=r"Program([ClassDecl(Id(Shape),[AttributeDecl(Static,VarDecl(Id($Student),ClassType(Id(Student)),NewExpr(Id(Student),[]))),MethodDecl(Id(Hello),Instance,[],Block([If(BinaryOp(>=,Id(a),Id(b)),Block([]),If(BinaryOp(<,Id(a),Id(b)),Block([For(Id(lehoe),Id(a),Id(b),IntLit(1),Block([AssignStmt(Id(x),BinaryOp(-,Id(x),IntLit(1))),If(BinaryOp(==,Id(a),Id(b)),Block([Break]),Block([Return()]))])]),Continue,If(BinaryOp(!=,ArrayCell(FieldAccess(Id(a),Id(b)),[IntLit(5)]),IntLit(9)),Block([Return(ArrayCell(FieldAccess(Id(a),Id(c)),[IntLit(9)]))]))])))]))])])"
        self.assertTrue(TestAST.test(input,expect,325))

    def test_27(self):
        input= """
            Class Program{
                Main(){
                    a = b + c;
                    thy = -dopo + (ngoc - quang);
                    x = (a[1]).hello;
                    y = a.b().c.d();
                    z = New Y().Hello();
                    Var Student : Student = New Student();
                }
                Var Student : Student = New Student();
            }
        """
        expect=r"Program([ClassDecl(Id(Program),[MethodDecl(Id(Main),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+,Id(b),Id(c))),AssignStmt(Id(thy),BinaryOp(+,UnaryOp(-,Id(dopo)),BinaryOp(-,Id(ngoc),Id(quang)))),AssignStmt(Id(x),FieldAccess(ArrayCell(Id(a),[IntLit(1)]),Id(hello))),AssignStmt(Id(y),CallExpr(FieldAccess(CallExpr(Id(a),Id(b),[]),Id(c)),Id(d),[])),AssignStmt(Id(z),CallExpr(NewExpr(Id(Y),[]),Id(Hello),[])),VarDecl(Id(Student),ClassType(Id(Student)),NewExpr(Id(Student),[]))])),AttributeDecl(Instance,VarDecl(Id(Student),ClassType(Id(Student)),NewExpr(Id(Student),[])))])])"
        self.assertTrue(TestAST.test(input,expect,326))

    def test_28(self):
        input= """
            Class Shape {
                Val $Student : Student = New Student(a,12.4);
                Var $a, b, $c, d: Int = 1,2,3,4;

                Hello(){
                    {
                        Var hello : Array[Boolean, 3];
                        Val length : Int = 1;
                    }
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($Student),ClassType(Id(Student)),NewExpr(Id(Student),[Id(a),FloatLit(12.4)]))),AttributeDecl(Static,VarDecl(Id($a),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),AttributeDecl(Static,VarDecl(Id($c),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(d),IntType,IntLit(4))),MethodDecl(Id(Hello),Instance,[],Block([Block([VarDecl(Id(hello),ArrayType(3,BoolType)),ConstDecl(Id(length),IntType,IntLit(1))])]))])])"
        self.assertTrue(TestAST.test(input,expect,327))

    def test_29(self):
        input= """
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
        expect=r"Program([ClassDecl(Id(Shape),[MethodDecl(Id(Hi),Instance,[param(Id(a),ClassType(Id(baby))),param(Id(b),ClassType(Id(baby))),param(Id(s),ClassType(Id(baby))),param(Id(x),IntType),param(Id(y),IntType)],Block([AssignStmt(ArrayCell(FieldAccess(Id(a),Id(b)),[IntLit(3)]),BinaryOp(&&,IntLit(12),BinaryOp(+,BinaryOp(-,IntLit(4),IntLit(15)),BinaryOp(-,IntLit(12),UnaryOp(-,Id(a)))))),AssignStmt(FieldAccess(CallExpr(Id(a),Id(b),[BinaryOp(+,IntLit(12),IntLit(3)),UnaryOp(!,Id(b)),NewExpr(Id(X),[])]),Id(bruh)),IntLit(12)),AssignStmt(FieldAccess(Id(a),Id($c)),IntLit(19))])),MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(e),ClassType(Id(Bay))),param(Id(f),ClassType(Id(Bay)))],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([])),AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(b)),NewExpr(Id(b),[Id(x),BinaryOp(-,BinaryOp(/,IntLit(100),IntLit(4)),IntLit(2)),NewExpr(Id(c),[Id(Hello),IntLit(1)])])))])])"
        self.assertTrue(TestAST.test(input,expect,328))

    def test_30(self):
        input= """
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
        expect=r"Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([AssignStmt(Id(a),[[[IntLit(1),IntLit(2)],[IntLit(2),IntLit(3)]],[[IntLit(1),IntLit(2)],[IntLit(2),IntLit(3)]]])]))])])"
        self.assertTrue(TestAST.test(input,expect,329))

#-----------------------------------------------------------------------------
    def test_31(self):
        input= """
            Class Shape {
                Hi(){
                }
                Var $hi: Array[Array[Int,2],2] = Array(Array(15-9, Array(2,3,12)), Array(0,1));
            }
        """
        expect=r"Program([ClassDecl(Id(Shape),[MethodDecl(Id(Hi),Instance,[],Block([])),AttributeDecl(Static,VarDecl(Id($hi),ArrayType(2,ArrayType(2,IntType)),[[BinaryOp(-,IntLit(15),IntLit(9)),[IntLit(2),IntLit(3),IntLit(12)]],[IntLit(0),IntLit(1)]]))])])"
        self.assertTrue(TestAST.test(input,expect,330))

    def test_32(self):
        input= """
            Class Shape {
                Hi(){
                    a[1][b-c] = (a[i])[j];
                }
                Var $hi: Array[Array[Int,2],2] = "Hello this is \\f some nmice \\t string hehe";
            }
        """
        expect=r"Program([ClassDecl(Id(Shape),[MethodDecl(Id(Hi),Instance,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),BinaryOp(-,Id(b),Id(c))]),ArrayCell(ArrayCell(Id(a),[Id(i)]),[Id(j)]))])),AttributeDecl(Static,VarDecl(Id($hi),ArrayType(2,ArrayType(2,IntType)),StringLit(Hello this is \f some nmice \t string hehe)))])])"
        self.assertTrue(TestAST.test(input,expect,331))

    def test_33(self):
        input= """
            Class Program{
                Val Babe : Boolean = (!b).c();
                Var hel : Float = (2-(b/2)+-12)[5][9];
                Var hey: Int = c::$hello;
            }
        """
        expect=r"Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(Babe),BoolType,CallExpr(UnaryOp(!,Id(b)),Id(c),[]))),AttributeDecl(Instance,VarDecl(Id(hel),FloatType,ArrayCell(BinaryOp(+,BinaryOp(-,IntLit(2),BinaryOp(/,Id(b),IntLit(2))),UnaryOp(-,IntLit(12))),[IntLit(5),IntLit(9)]))),AttributeDecl(Instance,VarDecl(Id(hey),IntType,FieldAccess(Id(c),Id($hello))))])])"
        self.assertTrue(TestAST.test(input,expect,332))

    def test_34(self):
        input= """
            Class Shape {
                Hi(){
                    a::$baby();
                    a = b::$baby();
                    a = b::$baby;
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Shape),[MethodDecl(Id(Hi),Instance,[],Block([Call(Id(a),Id($baby),[]),AssignStmt(Id(a),CallExpr(Id(b),Id($baby),[])),AssignStmt(Id(a),FieldAccess(Id(b),Id($baby)))]))])])"
        self.assertTrue(TestAST.test(input,expect,333))

    def test_35(self):
        input= """
            Class Shape {
                Hi(){
                    a.b[3][5][c-9] = 12 && 4 - 15 + (12--a);
                    a.b(12+3, !b, New X()).bruh = 12;
                    a::$c = 19;
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Shape),[MethodDecl(Id(Hi),Instance,[],Block([AssignStmt(ArrayCell(FieldAccess(Id(a),Id(b)),[IntLit(3),IntLit(5),BinaryOp(-,Id(c),IntLit(9))]),BinaryOp(&&,IntLit(12),BinaryOp(+,BinaryOp(-,IntLit(4),IntLit(15)),BinaryOp(-,IntLit(12),UnaryOp(-,Id(a)))))),AssignStmt(FieldAccess(CallExpr(Id(a),Id(b),[BinaryOp(+,IntLit(12),IntLit(3)),UnaryOp(!,Id(b)),NewExpr(Id(X),[])]),Id(bruh)),IntLit(12)),AssignStmt(FieldAccess(Id(a),Id($c)),IntLit(19))]))])])"
        self.assertTrue(TestAST.test(input,expect,334))

    def test_36(self):
        input= """
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
        expect=r"Program([ClassDecl(Id(Shape),[MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(e),ClassType(Id(Bay))),param(Id(f),ClassType(Id(Bay)))],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Circle),Id(Shape),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(Conheo)),IntLit(10))),AttributeDecl(Static,VarDecl(Id($b),ClassType(Id(Conheo)),IntLit(20))),AttributeDecl(Instance,VarDecl(Id(c),ClassType(Id(Conheo)),IntLit(49))),MethodDecl(Id(Test),Instance,[],Block([AssignStmt(FieldAccess(ArrayCell(FieldAccess(Id(aimabiet),Id(jztr)),[IntLit(5)]),Id(a)),IntLit(12)),Call(ArrayCell(FieldAccess(Id(a),Id(b)),[BinaryOp(+,BinaryOp(-,IntLit(9),IntLit(2)),UnaryOp(-,IntLit(12)))]),Id(b),[]),ConstDecl(Id(x),StringType,StringLit(hello hihi \t alo))]))])])"
        self.assertTrue(TestAST.test(input,expect,335))

##------------------------------------------------------------------
    def test_37(self):
        input= """
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
        expect=r"Program([ClassDecl(Id(Shape),[AttributeDecl(Static,VarDecl(Id($b),ClassType(Id(Huhu)),BinaryOp(+,CallExpr(Id(a),Id(b),[]),FieldAccess(Id(b),Id(x))))),AttributeDecl(Instance,VarDecl(Id(c),ClassType(Id(Huhu)),IntLit(12))),AttributeDecl(Static,VarDecl(Id($d),ClassType(Id(Huhu)),IntLit(83))),MethodDecl(Id(Test),Instance,[],Block([AssignStmt(Id(a),IntLit(12)),AssignStmt(Id($c),IntLit(16)),AssignStmt(ArrayCell(FieldAccess(CallExpr(Id(a),Id(b),[]),Id(e)),[IntLit(5)]),IntLit(19)),AssignStmt(ArrayCell(FieldAccess(CallExpr(NewExpr(Id(X),[]),Id(b),[]),Id(e)),[IntLit(3)]),IntLit(20)),AssignStmt(FieldAccess(Id(b),Id($c)),IntLit(21)),AssignStmt(FieldAccess(ArrayCell(FieldAccess(BinaryOp(+,Id(a),Id(b)),Id(c)),[IntLit(5)]),Id(d)),[[BinaryOp(-,IntLit(15),IntLit(9)),[IntLit(2),IntLit(3),IntLit(12)]],[IntLit(0),IntLit(1)]])]))])])"
        self.assertTrue(TestAST.test(input,expect,336))

    def test_38(self):
        input= """
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
        expect=r"Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(x),ClassType(Id(b)),IntLit(12))),AttributeDecl(Instance,VarDecl(Id(y),ClassType(Id(b)),IntLit(0))),MethodDecl(Id(test),Instance,[],Block([AssignStmt(Id(a),IntLit(12)),AssignStmt(Id($c),IntLit(16))]))])])"
        self.assertTrue(TestAST.test(input,expect,337))

    def test_39(self):
        input= """
            Class Shape {
                test(a,b : Int; c : Float){
                    t2 = !(2+9) - !123_4 + - 0X0 + "hello \\t haha" / 1000;
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Shape),[MethodDecl(Id(test),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],Block([AssignStmt(Id(t2),BinaryOp(+,BinaryOp(+,BinaryOp(-,UnaryOp(!,BinaryOp(+,IntLit(2),IntLit(9))),UnaryOp(!,IntLit(1234))),UnaryOp(-,IntLit(0))),BinaryOp(/,StringLit(hello \t haha),IntLit(1000))))]))])])"
        self.assertTrue(TestAST.test(input,expect,338))

    def test_40(self):
        input= """
            Class Shape {
                test(){
                    t1 = (12+3)%x - 9 +. (New X(New y(), (a/b)).haha().hihi - hihi::$ok); 
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Shape),[MethodDecl(Id(test),Instance,[],Block([AssignStmt(Id(t1),BinaryOp(+.,BinaryOp(-,BinaryOp(%,BinaryOp(+,IntLit(12),IntLit(3)),Id(x)),IntLit(9)),BinaryOp(-,FieldAccess(CallExpr(NewExpr(Id(X),[NewExpr(Id(y),[]),BinaryOp(/,Id(a),Id(b))]),Id(haha),[]),Id(hihi)),FieldAccess(Id(hihi),Id($ok)))))]))])])"
        self.assertTrue(TestAST.test(input,expect,339))

#----------------------------------------------------------
    def test_41(self):
        input= """
            Class Shape {
                test(){
                    d1 = a +. b;
                    d2 = a ==. b;
                    d3 = !(a<=b);
                    d4 = c*d%x;
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Shape),[MethodDecl(Id(test),Instance,[],Block([AssignStmt(Id(d1),BinaryOp(+.,Id(a),Id(b))),AssignStmt(Id(d2),BinaryOp(==.,Id(a),Id(b))),AssignStmt(Id(d3),UnaryOp(!,BinaryOp(<=,Id(a),Id(b)))),AssignStmt(Id(d4),BinaryOp(%,BinaryOp(*,Id(c),Id(d)),Id(x)))]))])])"
        self.assertTrue(TestAST.test(input,expect,340))

    def test_42(self):
        input= """
            Class Shape {
                Var x, y : b = 12, 0;
                Val $e : Array[Array[Array[Int, 3],4],5];
                Var $x : Array[String, 2] = "hello";
            }
        """
        expect=r"Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(x),ClassType(Id(b)),IntLit(12))),AttributeDecl(Instance,VarDecl(Id(y),ClassType(Id(b)),IntLit(0))),AttributeDecl(Static,ConstDecl(Id($e),ArrayType(5,ArrayType(4,ArrayType(3,IntType))),None)),AttributeDecl(Static,VarDecl(Id($x),ArrayType(2,StringType),StringLit(hello)))])])"
        self.assertTrue(TestAST.test(input,expect,341))

    def test_43(self):
        input= """
            Class Shape {
                test(){
                    e = a[b*c];
                    e1 = a[e[2]][4];
                    e2 = a[4][5][c[b[9]]];
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Shape),[MethodDecl(Id(test),Instance,[],Block([AssignStmt(Id(e),ArrayCell(Id(a),[BinaryOp(*,Id(b),Id(c))])),AssignStmt(Id(e1),ArrayCell(Id(a),[ArrayCell(Id(e),[IntLit(2)]),IntLit(4)])),AssignStmt(Id(e2),ArrayCell(Id(a),[IntLit(4),IntLit(5),ArrayCell(Id(c),[ArrayCell(Id(b),[IntLit(9)])])]))]))])])"
        self.assertTrue(TestAST.test(input,expect,342))

    def test_44(self):
        input= """
            Class Shape {
                test(){
                    b = 2;
                    c = True;
                    d = False;
                    e = f;
                    a = tRue;
                    g = 90_3.E+2;
                    a2 = (9+15 / (--29 + 3))[6];

                }
            }
        """
        expect=r"Program([ClassDecl(Id(Shape),[MethodDecl(Id(test),Instance,[],Block([AssignStmt(Id(b),IntLit(2)),AssignStmt(Id(c),BooleanLit(True)),AssignStmt(Id(d),BooleanLit(False)),AssignStmt(Id(e),Id(f)),AssignStmt(Id(a),Id(tRue)),AssignStmt(Id(g),FloatLit(90300.0)),AssignStmt(Id(a2),ArrayCell(BinaryOp(+,IntLit(9),BinaryOp(/,IntLit(15),BinaryOp(+,UnaryOp(-,UnaryOp(-,IntLit(29))),IntLit(3)))),[IntLit(6)]))]))])])"
        self.assertTrue(TestAST.test(input,expect,343))

    def test_45(self):
        input= """
            Class Shape {
                test(){
                    a = !b;
                    b = ---c;
                    d = e + ---f;
                    g = !---h;
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Shape),[MethodDecl(Id(test),Instance,[],Block([AssignStmt(Id(a),UnaryOp(!,Id(b))),AssignStmt(Id(b),UnaryOp(-,UnaryOp(-,UnaryOp(-,Id(c))))),AssignStmt(Id(d),BinaryOp(+,Id(e),UnaryOp(-,UnaryOp(-,UnaryOp(-,Id(f)))))),AssignStmt(Id(g),UnaryOp(!,UnaryOp(-,UnaryOp(-,UnaryOp(-,Id(h))))))]))])])"
        self.assertTrue(TestAST.test(input,expect,344))

#----------------------------------------------------------------

    def test_46(self):
        input= """
            Class Phong
            {
                main() {
                    x = New Ngan().yeuPhong;
                    y = New Ngan().yeuPhong.yeuP;
                }
            }
        """

        expect = r"Program([ClassDecl(Id(Phong),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(x),FieldAccess(NewExpr(Id(Ngan),[]),Id(yeuPhong))),AssignStmt(Id(y),FieldAccess(FieldAccess(NewExpr(Id(Ngan),[]),Id(yeuPhong)),Id(yeuP)))]))])])"
        self.assertTrue(TestAST.test(input,expect,345))

    def test_47(self):
        input= """
            Class Program {
                main() {
                    Val a : Int;
                    Foreach (i In 1 .. 100)
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
        expect=r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a),IntType,None),For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([Call(Self(),Id(printf),[StringLit(enter the number:)]),If(BinaryOp(==,Id(self),IntLit(0)),Block([Break]))])]),Return(IntLit(0))]))])])"
        self.assertTrue(TestAST.test(input,expect,346))

    def test_48(self):
        input= """
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
        expect=r"Program([ClassDecl(Id(Shape),[MethodDecl(Id(test),Instance,[],Block([For(Id(i),BinaryOp(-,Id(a),UnaryOp(-,Id(b))),ArrayCell(CallExpr(BinaryOp(/,Id(e),Id(f)),Id(b),[]),[IntLit(5)]),IntLit(12),Block([For(Id(j),IntLit(1),IntLit(4),Id(a),Block([AssignStmt(Id(a),IntLit(9)),AssignStmt(Id(c),UnaryOp(!,BinaryOp(==,Id(c),Id(b))))])]),Continue])])]))])])"
        self.assertTrue(TestAST.test(input,expect,347))

    def test_49(self):
        input= """
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
        expect=r"Program([ClassDecl(Id(Shape),[MethodDecl(Id(test),Instance,[],Block([If(BinaryOp(==,ArrayCell(CallExpr(ArrayCell(Id(a),[IntLit(5)]),Id(b),[]),[IntLit(4)]),UnaryOp(!,BooleanLit(True))),Block([Return(Id(a))]),Block([Call(Self(),Id(Donothing),[])]))]))])])"
        self.assertTrue(TestAST.test(input,expect,348))

    def test_50(self):
        input= """
            Class Shape {
                test(){
                    Self.Foo();
                    (1+1).X = 12;
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Shape),[MethodDecl(Id(test),Instance,[],Block([Call(Self(),Id(Foo),[]),AssignStmt(FieldAccess(BinaryOp(+,IntLit(1),IntLit(1)),Id(X)),IntLit(12))]))])])"
        self.assertTrue(TestAST.test(input,expect,349))

#------------------------------------------------------------------
    def test_51(self):
        input= """
            Class Phong
            {
                main() {
                    Ngan[1+1-5] = 1+7-8;
                    Self.x = 2*5%3;
                    Ngan::$YeuPhong = 1212.115;
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Phong),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(ArrayCell(Id(Ngan),[BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(1)),IntLit(5))]),BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(7)),IntLit(8))),AssignStmt(FieldAccess(Self(),Id(x)),BinaryOp(%,BinaryOp(*,IntLit(2),IntLit(5)),IntLit(3))),AssignStmt(FieldAccess(Id(Ngan),Id($YeuPhong)),FloatLit(1212.115))]))])])"
        self.assertTrue(TestAST.test(input,expect,350))

    def test_52(self):
        input= """
            Class Phong
            {
                main() {
                    Foreach(x In start..end By x+5/8-9*3) {
                        Continue;
                    }
                    Foreach(y In a + 9 .. b + 100) {
                        Break;
                    }
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Phong),[MethodDecl(Id(main),Instance,[],Block([For(Id(x),Id(start),Id(end),BinaryOp(-,BinaryOp(+,Id(x),BinaryOp(/,IntLit(5),IntLit(8))),BinaryOp(*,IntLit(9),IntLit(3))),Block([Continue])]),For(Id(y),BinaryOp(+,Id(a),IntLit(9)),BinaryOp(+,Id(b),IntLit(100)),IntLit(1),Block([Break])])]))])])"
        self.assertTrue(TestAST.test(input,expect,351))

    def test_53(self):
        input= """
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
        expect=r"Program([ClassDecl(Id(Shape),[MethodDecl(Id(test),Instance,[],Block([VarDecl(Id(a),IntType,IntLit(0)),If(BinaryOp(==,Id(a),IntLit(0)),Block([For(Id(i),Id(i),Id(j),IntLit(1),Block([If(BinaryOp(==,BinaryOp(-,Id(i),Id(j)),IntLit(12)),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(2))),Return()]),Block([Continue]))])])]))]))])])"
        self.assertTrue(TestAST.test(input,expect,352))

    def test_54(self):
        input= """
            Class Shape {
                _(){
                }
                test(){
                    _.b(a, b+c, 12);
                }
                X(){
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Shape),[MethodDecl(Id(_),Instance,[],Block([])),MethodDecl(Id(test),Instance,[],Block([Call(Id(_),Id(b),[Id(a),BinaryOp(+,Id(b),Id(c)),IntLit(12)])])),MethodDecl(Id(X),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,353))

    def test_55(self):
        input= """
            Class Shape {
                test(){
                    a = true + True && False;
                    a = true + "True ## && ## False";
                    b = !False;
                    c = true + (True && False);
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Shape),[MethodDecl(Id(test),Instance,[],Block([AssignStmt(Id(a),BinaryOp(&&,BinaryOp(+,Id(true),BooleanLit(True)),BooleanLit(False))),AssignStmt(Id(a),BinaryOp(+,Id(true),StringLit(True ## && ## False))),AssignStmt(Id(b),UnaryOp(!,BooleanLit(False))),AssignStmt(Id(c),BinaryOp(+,Id(true),BinaryOp(&&,BooleanLit(True),BooleanLit(False))))]))])])"
        self.assertTrue(TestAST.test(input,expect,354))

#--------------------------------------------------------------

    def test_56(self):
        input= """
            Class Program
            {
                main() {
                    Var sum : Int = 0;
                    Var i : Int = 0;
                    Foreach(i In 1 .. 10 By (a + 5 - 6 * 7 /10)%2) {
                        sum = sum + i;
                    }
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(sum),IntType,IntLit(0)),VarDecl(Id(i),IntType,IntLit(0)),For(Id(i),IntLit(1),IntLit(10),BinaryOp(%,BinaryOp(-,BinaryOp(+,Id(a),IntLit(5)),BinaryOp(/,BinaryOp(*,IntLit(6),IntLit(7)),IntLit(10))),IntLit(2)),Block([AssignStmt(Id(sum),BinaryOp(+,Id(sum),Id(i)))])])]))])])"
        self.assertTrue(TestAST.test(input,expect,355))
##################### check \n hay \\n ####
    def test_57(self):
        input= """
            Class Program {
                main() {
                    Foreach (i In 0 .. 100) {
                        Break;
                    }
                    Return 0;
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(i),IntLit(0),IntLit(100),IntLit(1),Block([Break])]),Return(IntLit(0))]))])])"
        self.assertTrue(TestAST.test(input,expect,356))

    def test_58(self):
        input= """
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
        expect=r"Program([ClassDecl(Id(Shape),[MethodDecl(Id(Count_Xgiaithua_),Instance,[param(Id(x),IntType)],Block([If(BinaryOp(<=,Id(x),IntLit(0)),Block([Return(StringLit(Error))])),VarDecl(Id(GT),IntType,IntLit(1)),For(Id(i),IntLit(1),Id(x),IntLit(1),Block([AssignStmt(Id(GT),BinaryOp(*,Id(GT),Id(i)))])]),Return(Id(GT))]))])])"
        self.assertTrue(TestAST.test(input,expect,357))

    def test_59(self):
        input= """
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
        expect=r"Program([ClassDecl(Id(Shape),[MethodDecl(Id(Tinhtong_khoang),Instance,[param(Id(start),IntType),param(Id(end),IntType)],Block([If(BinaryOp(<,Id(start),Id(end)),Block([Return(StringLit(Bye))]),If(BinaryOp(==,Id(start),Id(end)),Block([Return(Id(start))]),Block([VarDecl(Id(a),IntType,IntLit(0)),For(Id(i),Id(start),Id(end),IntLit(1),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),Id(i)))])]),Return(Id(a))])))]))])])"
        self.assertTrue(TestAST.test(input,expect,358))

    def test_60(self):
        input= """
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
        expect=r"Program([ClassDecl(Id(Shape),[MethodDecl(Id(demsophantu_duong),Instance,[param(Id(start),IntType),param(Id(end),IntType),param(Id(arr),ArrayType(12,FloatType))],Block([VarDecl(Id(count),IntType,IntLit(0)),For(Id(i),Id(start),Id(end),IntLit(1),Block([If(BinaryOp(>=,ArrayCell(Id(arr),[Id(i)]),IntLit(0)),Block([AssignStmt(Id(count),BinaryOp(+,Id(count),IntLit(1)))])),Return(Id(count))])])]))])])"
        self.assertTrue(TestAST.test(input,expect,359))

#---------------------------------------------------------------------

    def test_61(self):
        input= """
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
        expect=r"Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(x),FloatType)),AttributeDecl(Instance,VarDecl(Id(y),FloatType)),MethodDecl(Id(TinhS),Instance,[param(Id(x),FloatType),param(Id(y),FloatType)],Block([Return(BinaryOp(*,Id(x),Id(y)))])),MethodDecl(Id(TinhC),Instance,[param(Id(x),FloatType),param(Id(y),FloatType)],Block([Return(BinaryOp(*,IntLit(2),BinaryOp(+,Id(x),Id(y))))]))])])"
        self.assertTrue(TestAST.test(input,expect,360))

    def test_62(self):
        input= """
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
                    thucan = "an hai";
                }
                Destructor(){
                    Self.nhayvaolo();
                }
                Keu(){
                    Return "lehoe";
                }
            }
        """
        expect=r"Program([ClassDecl(Id(DongVat),[AttributeDecl(Instance,VarDecl(Id(moitruongsong),ClassType(Id(moitruong)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(thucan),ClassType(Id(loaithucan)),NullLiteral())),MethodDecl(Id(Keu),Instance,[],Block([Call(Self(),Id(keu),[])]))]),ClassDecl(Id(ConHeo),Id(DongVat),[MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(Id(moitruongsong),StringLit(Ba Ria)),AssignStmt(Id(thucan),StringLit(an hai))])),MethodDecl(Id(Destructor),Instance,[],Block([Call(Self(),Id(nhayvaolo),[])])),MethodDecl(Id(Keu),Instance,[],Block([Return(StringLit(lehoe))]))])])"
        self.assertTrue(TestAST.test(input,expect,361))

    def test_63(self):
        input= """
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
        expect=r"Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(chuvi),FloatType)),AttributeDecl(Instance,VarDecl(Id(dientich),FloatType))]),ClassDecl(Id(Hinhchunhat),Id(Shape),[MethodDecl(Id(TinhS),Instance,[],Block([Return(BinaryOp(*,Id(x),Id(y)))]))]),ClassDecl(Id(Hinhvuong),Id(Hinhchunhat),[])])"
        self.assertTrue(TestAST.test(input,expect,362))

    def test_64(self):
        input= """
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
        expect=r"Program([ClassDecl(Id(VatNuoi),[AttributeDecl(Instance,VarDecl(Id(giatien),IntType)),MethodDecl(Id(Choan),Instance,[],Block([Call(Id(chunhan),Id(nauan),[]),Call(Id(chunhan),Id(choan),[])])),MethodDecl(Id(Chamsoc),Instance,[],Block([Call(Id(chunhan),Id(choditam),[]),Call(Id(chunhan),Id(datdidao),[])]))]),ClassDecl(Id(conmeo),Id(VatNuoi),[MethodDecl(Id(Anhai),Instance,[],Block([Call(Id(self),Id(an),[]),Call(Id(self),Id(ngu),[Id(cangay)])]))])])"
        self.assertTrue(TestAST.test(input,expect,363))

    def test_65(self):
        input= """
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
        expect=r"Program([ClassDecl(Id(Banhkem),[AttributeDecl(Instance,VarDecl(Id(giatien),IntType)),MethodDecl(Id(Tanggia),Instance,[],Block([AssignStmt(Id(giatien),BinaryOp(+,Id(giatien),IntLit(10)))])),MethodDecl(Id(Lambanh),Instance,[],Block([AssignStmt(Id(bot),Id(botmi)),AssignStmt(Id(kem),Id(kembo)),Call(Id(tho),Id(quaybot),[Id(bot)]),Call(Id(tho),Id(trangtri),[Id(kem)])]))])])"
        self.assertTrue(TestAST.test(input,expect,364))

#---------------------------------------------------------------

    def test_66(self):
        input= """
            Class NhanVien{
                Var msnv, tuoi: Int;
                Var ten: String;
                Var $dem: Int;
                Constructor(msnv, tuoi: Int; ten: String){
                    Self.msnv = msnv;
                    Self.ten = ten;
                    Self.tuoi = tuoi;
                    NhanVien::$dem = NhanVien::$dem + 1;
                }
                HienThi(){
                    iostream.Printf("Co ", NhanVien::$dem, " doi tuong duoc tao. \\n");
                }
            }

            Class Program{
                main(){
                    NhanVien::$dem = 0;
                    Var n1, n2, n3 : NhanVien = New NhanVien(111231, "Nguyen Van A", 25), New NhanVien(213214, "Nguyen Van B", 40), New NhanVien(213215, "Nguyen Van C", 67);
                    n1.HienThi();
                    n2.HienThi();
                    n3.HienThi();
                    Return;
                }
            }
        """
        expect = r"Program([ClassDecl(Id(NhanVien),[AttributeDecl(Instance,VarDecl(Id(msnv),IntType)),AttributeDecl(Instance,VarDecl(Id(tuoi),IntType)),AttributeDecl(Instance,VarDecl(Id(ten),StringType)),AttributeDecl(Static,VarDecl(Id($dem),IntType)),MethodDecl(Id(Constructor),Instance,[param(Id(msnv),IntType),param(Id(tuoi),IntType),param(Id(ten),StringType)],Block([AssignStmt(FieldAccess(Self(),Id(msnv)),Id(msnv)),AssignStmt(FieldAccess(Self(),Id(ten)),Id(ten)),AssignStmt(FieldAccess(Self(),Id(tuoi)),Id(tuoi)),AssignStmt(FieldAccess(Id(NhanVien),Id($dem)),BinaryOp(+,FieldAccess(Id(NhanVien),Id($dem)),IntLit(1)))])),MethodDecl(Id(HienThi),Instance,[],Block([Call(Id(iostream),Id(Printf),[StringLit(Co ),FieldAccess(Id(NhanVien),Id($dem)),StringLit( doi tuong duoc tao. \n)])]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(FieldAccess(Id(NhanVien),Id($dem)),IntLit(0)),VarDecl(Id(n1),ClassType(Id(NhanVien)),NewExpr(Id(NhanVien),[IntLit(111231),StringLit(Nguyen Van A),IntLit(25)])),VarDecl(Id(n2),ClassType(Id(NhanVien)),NewExpr(Id(NhanVien),[IntLit(213214),StringLit(Nguyen Van B),IntLit(40)])),VarDecl(Id(n3),ClassType(Id(NhanVien)),NewExpr(Id(NhanVien),[IntLit(213215),StringLit(Nguyen Van C),IntLit(67)])),Call(Id(n1),Id(HienThi),[]),Call(Id(n2),Id(HienThi),[]),Call(Id(n3),Id(HienThi),[]),Return()]))])])"
        self.assertTrue(TestAST.test(input,expect,365))
############# check \n hay \\n #############

    def test_67(self):
        input= """
            Class Program{
                main(){
                    Var a : Array[Array[Int, 100], 10];
                    Var m, n, sum: Int = 10, 100, 0;
                    Foreach(i In 0 .. m ){
                        Foreach(j In 0 .. n){
                            If (a[i][j] % 2 == 0){
                                sum = sum + a[i][j];
                            }
                        }
                    }
                    iostream.Printf("Tong cac phan tu chan la: ", sum);
                    Return;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ArrayType(10,ArrayType(100,IntType))),VarDecl(Id(m),IntType,IntLit(10)),VarDecl(Id(n),IntType,IntLit(100)),VarDecl(Id(sum),IntType,IntLit(0)),For(Id(i),IntLit(0),Id(m),IntLit(1),Block([For(Id(j),IntLit(0),Id(n),IntLit(1),Block([If(BinaryOp(==,BinaryOp(%,ArrayCell(Id(a),[Id(i),Id(j)]),IntLit(2)),IntLit(0)),Block([AssignStmt(Id(sum),BinaryOp(+,Id(sum),ArrayCell(Id(a),[Id(i),Id(j)])))]))])])])]),Call(Id(iostream),Id(Printf),[StringLit(Tong cac phan tu chan la: ),Id(sum)]),Return()]))])])"
        self.assertTrue(TestAST.test(input,expect,366))

    def test_68(self):
        input= """
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
        expect=r"Program([ClassDecl(Id(Banhtrangtron),[AttributeDecl(Instance,ConstDecl(Id(Topping),ArrayType(5,StringType),[StringLit(Tom),StringLit(Hanh),StringLit(Muoi ot),StringLit(Sa te),StringLit(Toi phi)])),AttributeDecl(Instance,VarDecl(Id(Banhtrang),ClassType(Id(Banhtrang)),NullLiteral())),MethodDecl(Id(Tron),Instance,[],Block([Call(Id(chuquan),Id(laybanhtrang),[]),Call(Id(chuquan),Id(botopping),[Id(Topping)]),Call(Id(chuquan),Id(baogia),[])]))])])"
        self.assertTrue(TestAST.test(input,expect,367))

    def test_69(self):
        input= """
            Class Program{
                isPrimeNumber(n: Int){
                    If (n < 2){
                        Return 0;
                    }

                    Var squareRoot : Int = iostream.sqrt(n);
                    Var i: Int;
                    Foreach(i In 2 .. squareRoot){
                        If (n % i == 0) {
                            Return 0;
                        }
                    }
                    Return 1;
                }

                main(){
                    Var i: Int;
                    iostream.Printf("Cac so nguyen to nho hon 100 la: ");
                    Foreach (i In 0 .. 100){
                        If (Self.isPrimeNumber(i)){
                            iostream.Printf(i, " ");
                        }
                    }
                    Return;
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(isPrimeNumber),Instance,[param(Id(n),IntType)],Block([If(BinaryOp(<,Id(n),IntLit(2)),Block([Return(IntLit(0))])),VarDecl(Id(squareRoot),IntType,CallExpr(Id(iostream),Id(sqrt),[Id(n)])),VarDecl(Id(i),IntType),For(Id(i),IntLit(2),Id(squareRoot),IntLit(1),Block([If(BinaryOp(==,BinaryOp(%,Id(n),Id(i)),IntLit(0)),Block([Return(IntLit(0))]))])]),Return(IntLit(1))])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(i),IntType),Call(Id(iostream),Id(Printf),[StringLit(Cac so nguyen to nho hon 100 la: )]),For(Id(i),IntLit(0),IntLit(100),IntLit(1),Block([If(CallExpr(Self(),Id(isPrimeNumber),[Id(i)]),Block([Call(Id(iostream),Id(Printf),[Id(i),StringLit( )])]))])]),Return()]))])])"
        self.assertTrue(TestAST.test(input,expect,368))

    def test_70(self):
        input= """
            Class Shape {
                Hi(){
                    a = ("Self").strlength();
                    b = (True).ascii;
                    c = 90_45.E0;
                    d = Hello.b("Self").hello;
                    Hello.b("Self").hello();
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Shape),[MethodDecl(Id(Hi),Instance,[],Block([AssignStmt(Id(a),CallExpr(StringLit(Self),Id(strlength),[])),AssignStmt(Id(b),FieldAccess(BooleanLit(True),Id(ascii))),AssignStmt(Id(c),FloatLit(9045.0)),AssignStmt(Id(d),FieldAccess(CallExpr(Id(Hello),Id(b),[StringLit(Self)]),Id(hello))),Call(CallExpr(Id(Hello),Id(b),[StringLit(Self)]),Id(hello),[])]))])])"
        self.assertTrue(TestAST.test(input,expect,369))

#-------------------------------------------------------------------
    def test_71(self):
        input= """
            Class Shape {
                Hi(){
                    hesay = "hello i'm lehoe";
                    shesay = "who iz the hoehoe";
                    hesayagain = "It\'s me";
                    hehe = "This is a tring" + "This is another string";
                    b = 0e000;
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Shape),[MethodDecl(Id(Hi),Instance,[],Block([AssignStmt(Id(hesay),StringLit(hello i'm lehoe)),AssignStmt(Id(shesay),StringLit(who iz the hoehoe)),AssignStmt(Id(hesayagain),StringLit(It's me)),AssignStmt(Id(hehe),BinaryOp(+,StringLit(This is a tring),StringLit(This is another string))),AssignStmt(Id(b),FloatLit(0.0))]))])])"
        self.assertTrue(TestAST.test(input,expect,370))

    def test_72(self):
        input= """
            Class Banhchuoi{
                Val $botbanh :bot;
                Var chuoi: chuoixiem = chuoi && chuoingon;
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
        expect=r"Program([ClassDecl(Id(Banhchuoi),[AttributeDecl(Static,ConstDecl(Id($botbanh),ClassType(Id(bot)),None)),AttributeDecl(Instance,VarDecl(Id(chuoi),ClassType(Id(chuoixiem)),BinaryOp(&&,Id(chuoi),Id(chuoingon)))),MethodDecl(Id(test),Instance,[],Block([If(BinaryOp(==,FieldAccess(Id(Banhchuoi),Id(Ngon)),BooleanLit(True)),Block([Call(Self(),Id(tratien),[])]),Block([Call(Self(),Id(Anquit),[])]))]))])])"
        self.assertTrue(TestAST.test(input,expect,371))

    def test_73(self):
        input= """
            Class Banhchuoi{
                test(){
                    _e12 = 0x0;
                    _ = hello * 2 - !baby;
                    sth = sth - sthth + sththth;
                    spamming = spaming1 - spamming2[3][spamming[4]];
                    spam = Self.Spamminghere();
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Banhchuoi),[MethodDecl(Id(test),Instance,[],Block([AssignStmt(Id(_e12),IntLit(0)),AssignStmt(Id(_),BinaryOp(-,BinaryOp(*,Id(hello),IntLit(2)),UnaryOp(!,Id(baby)))),AssignStmt(Id(sth),BinaryOp(+,BinaryOp(-,Id(sth),Id(sthth)),Id(sththth))),AssignStmt(Id(spamming),BinaryOp(-,Id(spaming1),ArrayCell(Id(spamming2),[IntLit(3),ArrayCell(Id(spamming),[IntLit(4)])]))),AssignStmt(Id(spam),CallExpr(Self(),Id(Spamminghere),[]))]))])])"
        self.assertTrue(TestAST.test(input,expect,372))

    def test_74(self):
        input= """
            Class Banhchuoi{
                test(){
                    ## i just want some error $%#() ##
                    a = Self + Self.next;
                    b.c(Self);
                    a = 12_23_4_455_6789;
                    b = 90_234.E12;
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Banhchuoi),[MethodDecl(Id(test),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+,Self(),FieldAccess(Self(),Id(next)))),Call(Id(b),Id(c),[Self()]),AssignStmt(Id(a),IntLit(122344556789)),AssignStmt(Id(b),FloatLit(9.0234e+16))]))])])"
        self.assertTrue(TestAST.test(input,expect,373))

    def test_75(self):
        input= """
            Class Banhchuoi{
                test(){
                    lazy = sleepy + tired + boring;
                    spamming_here_ = " hehe he's cool; haha 242 @Q$# ";
                    hihi = haha + hehe;
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Banhchuoi),[MethodDecl(Id(test),Instance,[],Block([AssignStmt(Id(lazy),BinaryOp(+,BinaryOp(+,Id(sleepy),Id(tired)),Id(boring))),AssignStmt(Id(spamming_here_),StringLit( hehe he's cool; haha 242 @Q$# )),AssignStmt(Id(hihi),BinaryOp(+,Id(haha),Id(hehe)))]))])])"
        self.assertTrue(TestAST.test(input,expect,374))

#------------------------------------------------------------------

    def test_76(self):
        input= """
            Class Program
            {
                main()
                {
                    Val s1: String = "Hello \\n";
                    Var s2: String = "World \\n";
                    If(s1 ==. s2)
                    {
                        System.print("You are right");
                    }
                    Else
                    {
                        System.print("Noooo");
                    }
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(s1),StringType,StringLit(Hello \n)),VarDecl(Id(s2),StringType,StringLit(World \n)),If(BinaryOp(==.,Id(s1),Id(s2)),Block([Call(Id(System),Id(print),[StringLit(You are right)])]),Block([Call(Id(System),Id(print),[StringLit(Noooo)])]))]))])])"
        self.assertTrue(TestAST.test(input,expect,375))

    def test_77(self):
        input= """
            Class A{
                Var a1, $a2: Int = 0x12, 0434;
                Var a4, $a3: Float = 1.23445, 340.041e-4;
                Var a5, $a_6: Boolean = True, False;   
                Var a_7, $a_8, a_9: String = "No", "Seeya", "Gozen";
            }
            Class Program {
                main(){
                    Var a1, a2: Int = 0x12, 0434;
                    Var a4, a3: Float = 1.23445, 340.041e-4;
                    Var a5, a_6: Boolean = True, False;   
                    Var a_7, a_8, a_9: String = "No", "Seeya", "Gozen";
                    Var demo: A = New A(True);
                    Return;
                }
            }
        """
        expect=r"Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a1),IntType,IntLit(18))),AttributeDecl(Static,VarDecl(Id($a2),IntType,IntLit(284))),AttributeDecl(Instance,VarDecl(Id(a4),FloatType,FloatLit(1.23445))),AttributeDecl(Static,VarDecl(Id($a3),FloatType,FloatLit(0.0340041))),AttributeDecl(Instance,VarDecl(Id(a5),BoolType,BooleanLit(True))),AttributeDecl(Static,VarDecl(Id($a_6),BoolType,BooleanLit(False))),AttributeDecl(Instance,VarDecl(Id(a_7),StringType,StringLit(No))),AttributeDecl(Static,VarDecl(Id($a_8),StringType,StringLit(Seeya))),AttributeDecl(Instance,VarDecl(Id(a_9),StringType,StringLit(Gozen)))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a1),IntType,IntLit(18)),VarDecl(Id(a2),IntType,IntLit(284)),VarDecl(Id(a4),FloatType,FloatLit(1.23445)),VarDecl(Id(a3),FloatType,FloatLit(0.0340041)),VarDecl(Id(a5),BoolType,BooleanLit(True)),VarDecl(Id(a_6),BoolType,BooleanLit(False)),VarDecl(Id(a_7),StringType,StringLit(No)),VarDecl(Id(a_8),StringType,StringLit(Seeya)),VarDecl(Id(a_9),StringType,StringLit(Gozen)),VarDecl(Id(demo),ClassType(Id(A)),NewExpr(Id(A),[BooleanLit(True)])),Return()]))])])"
        self.assertTrue(TestAST.test(input,expect,376))

    def test_78(self):
        input= """
            Class Program {
                main() {
                    Foreach (i In 0 .. 100) {
                        Continue;
                    }
                    Return 0;
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(i),IntLit(0),IntLit(100),IntLit(1),Block([Continue])]),Return(IntLit(0))]))])])"
        self.assertTrue(TestAST.test(input,expect,377))

    def test_79(self):
        input= """
            Class foo {
                Constructor(a: Int) { } 
            }
            Class foo {
                Constructor(a: Int; b: Float) { } 
            }
            Class foo {
                Constructor(a: Int; b: Float; c: Boolean) { } 
            }
            Class foo {
                Constructor(a: Int; b: Float; c: Boolean; d: String) { } 
            }
            Class foo {
                Constructor(a: Int; b: Float; c: Boolean; d: String; e: Array[Int, 5]) { } 
            }
        """
        expect = r"Program([ClassDecl(Id(foo),[MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType)],Block([]))]),ClassDecl(Id(foo),[MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),FloatType)],Block([]))]),ClassDecl(Id(foo),[MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),FloatType),param(Id(c),BoolType)],Block([]))]),ClassDecl(Id(foo),[MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),FloatType),param(Id(c),BoolType),param(Id(d),StringType)],Block([]))]),ClassDecl(Id(foo),[MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),FloatType),param(Id(c),BoolType),param(Id(d),StringType),param(Id(e),ArrayType(5,IntType))],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,378))

    def test_80(self):
        input= """
            Class Chim{
                main() {
                    If(a){
                        a = 1;
                        If(b){b=1;}
                        Elseif(c){c=1;}
                        Elseif(d){d=1;}
                        Else{e=1;}
                    }
                    Elseif(c){c=1;}
                    Elseif(d){
                        If(b){b=1;}
                        Elseif(c){c=1;}
                        Elseif(d){d=1;}
                        Else{e=1;}    
                    }
                    Else{
                        If(b){b=1;}
                        Elseif(c){c=1;}
                        Elseif(d){d=1;}
                        Else{e=1;}   
                    }
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Chim),[MethodDecl(Id(main),Instance,[],Block([If(Id(a),Block([AssignStmt(Id(a),IntLit(1)),If(Id(b),Block([AssignStmt(Id(b),IntLit(1))]),If(Id(c),Block([AssignStmt(Id(c),IntLit(1))]),If(Id(d),Block([AssignStmt(Id(d),IntLit(1))]),Block([AssignStmt(Id(e),IntLit(1))]))))]),If(Id(c),Block([AssignStmt(Id(c),IntLit(1))]),If(Id(d),Block([If(Id(b),Block([AssignStmt(Id(b),IntLit(1))]),If(Id(c),Block([AssignStmt(Id(c),IntLit(1))]),If(Id(d),Block([AssignStmt(Id(d),IntLit(1))]),Block([AssignStmt(Id(e),IntLit(1))]))))]),Block([If(Id(b),Block([AssignStmt(Id(b),IntLit(1))]),If(Id(c),Block([AssignStmt(Id(c),IntLit(1))]),If(Id(d),Block([AssignStmt(Id(d),IntLit(1))]),Block([AssignStmt(Id(e),IntLit(1))]))))]))))]))])])"
        self.assertTrue(TestAST.test(input,expect,379))

#----------------------------------------------------------------------

    def test_81(self):
        input= """
            Class Program {
            main() {
                If(True){
                    Break;
                }
                Else{
                    Continue;
                }
                Return;
            }
        }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BooleanLit(True),Block([Break]),Block([Continue])),Return()]))])])"
        self.assertTrue(TestAST.test(input,expect,380))

    def test_82(self):
        input= """
            Class Shape {
                test(){
                    j = i + i + i;
                    j = i * i * i;
                    j = i / i / i;
                    j = i - i - i;
                    j = i % i % i;
                    j = i +. i;
                    j = i || i || i;
                    j = i && i && i;
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Shape),[MethodDecl(Id(test),Instance,[],Block([AssignStmt(Id(j),BinaryOp(+,BinaryOp(+,Id(i),Id(i)),Id(i))),AssignStmt(Id(j),BinaryOp(*,BinaryOp(*,Id(i),Id(i)),Id(i))),AssignStmt(Id(j),BinaryOp(/,BinaryOp(/,Id(i),Id(i)),Id(i))),AssignStmt(Id(j),BinaryOp(-,BinaryOp(-,Id(i),Id(i)),Id(i))),AssignStmt(Id(j),BinaryOp(%,BinaryOp(%,Id(i),Id(i)),Id(i))),AssignStmt(Id(j),BinaryOp(+.,Id(i),Id(i))),AssignStmt(Id(j),BinaryOp(||,BinaryOp(||,Id(i),Id(i)),Id(i))),AssignStmt(Id(j),BinaryOp(&&,BinaryOp(&&,Id(i),Id(i)),Id(i)))]))])])"
        self.assertTrue(TestAST.test(input,expect,381))

    def test_83(self):
        input= """
            Class Program {
                main() {
                    Var arr: Array[Int, 5] = Array(1,2,3,4,5);
                    ## test index operator ##
                    x = (((((a.foo(b.foo(c.foo(arr))))))))[10]; 
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(arr),ArrayType(5,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)]),AssignStmt(Id(x),ArrayCell(CallExpr(Id(a),Id(foo),[CallExpr(Id(b),Id(foo),[CallExpr(Id(c),Id(foo),[Id(arr)])])]),[IntLit(10)]))]))])])"
        self.assertTrue(TestAST.test(input,expect,382))

    def test_84(self):
        input= """
            Class Banhchuoi{
                test(){
                    a = b || c && d == e && (!f != g);
                    If (you){
                        Self.Try();
                    }
                    Else {
                        Self.Quit();
                    }
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Banhchuoi),[MethodDecl(Id(test),Instance,[],Block([AssignStmt(Id(a),BinaryOp(==,BinaryOp(&&,BinaryOp(||,Id(b),Id(c)),Id(d)),BinaryOp(&&,Id(e),BinaryOp(!=,UnaryOp(!,Id(f)),Id(g))))),If(Id(you),Block([Call(Self(),Id(Try),[])]),Block([Call(Self(),Id(Quit),[])]))]))])])"
        self.assertTrue(TestAST.test(input,expect,383))

    def test_85(self):
        input= """
            Class Program {
                main() {
                    ## operators ##
                    Var arr: Array[Array[Array[Int, 5], 5], 5] = Array(1,2,3,4,5);
                    x = 1 * 5 + 2 - 7 * arr[9 * i + j] / 2.0 +. 1.0 && True || k;
                    x = i >= j;
                    x = ! k;
                    Self.foo(k,l,m,n,arr,100,"Arg",x);
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(arr),ArrayType(5,ArrayType(5,ArrayType(5,IntType))),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)]),AssignStmt(Id(x),BinaryOp(+.,BinaryOp(-,BinaryOp(+,BinaryOp(*,IntLit(1),IntLit(5)),IntLit(2)),BinaryOp(/,BinaryOp(*,IntLit(7),ArrayCell(Id(arr),[BinaryOp(+,BinaryOp(*,IntLit(9),Id(i)),Id(j))])),FloatLit(2.0))),BinaryOp(||,BinaryOp(&&,FloatLit(1.0),BooleanLit(True)),Id(k)))),AssignStmt(Id(x),BinaryOp(>=,Id(i),Id(j))),AssignStmt(Id(x),UnaryOp(!,Id(k))),Call(Self(),Id(foo),[Id(k),Id(l),Id(m),Id(n),Id(arr),IntLit(100),StringLit(Arg),Id(x)])]))])])"
        self.assertTrue(TestAST.test(input,expect,384))

#-----------------------------------------------------------------------------

    def test_86(self):
        input= """
            Class Program {
                main() {
                    ## test built-in functions, ignore args (type,number)
                        just consider syntax ##
                    chim.printLn("string");
                    chim::$printLn(Array(1,2,3));
                    Self.print(a,b,1,True,100.e1);
                    Self.printStrLn("string and new line");
                    Self.read();
                    x = Self.read();	
                } 
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(chim),Id(printLn),[StringLit(string)]),Call(Id(chim),Id($printLn),[[IntLit(1),IntLit(2),IntLit(3)]]),Call(Self(),Id(print),[Id(a),Id(b),IntLit(1),BooleanLit(True),FloatLit(1000.0)]),Call(Self(),Id(printStrLn),[StringLit(string and new line)]),Call(Self(),Id(read),[]),AssignStmt(Id(x),CallExpr(Self(),Id(read),[]))]))])])"
        self.assertTrue(TestAST.test(input,expect,385))

    def test_87(self):
        input= """
            ## index is Octal,hexa number ##
            Class Program {}
            Class Program {main(){}}
            Class Program {main(){}}
            Class Program {$main(){}}
            Class Program {$main(){}}
            Class Program {main(a: Int){}}
            Class Program {$main(a: Float){}}
            Class Program {Var arr: String = arr[0b11111101][0XAF];}
        """
        expect = r"Program([ClassDecl(Id(Program),[]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id($main),Static,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id($main),Static,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id($main),Static,[param(Id(a),FloatType)],Block([]))]),ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(arr),StringType,ArrayCell(Id(arr),[IntLit(253),IntLit(175)])))])])"
        self.assertTrue(TestAST.test(input,expect,386))

    def test_88(self):
        input= """
            Class Program{
                removeDuplicates(s: String){
                    Var temp: String;
                    Var flag: Boolean = False;
                    Foreach(i In 0 .. iostream.len(s) By 1){
                        If (temp[temp.length() - 1] == S[i]){
                            temp.pop_back();
                            flag = True;
                        }
                        Else {
                            temp.push_back(S[i]);
                        }
                    }
                    If (flag){
                        Return Self.removeDuplicates(temp);
                    }
                    Else{
                        Return temp;
                    }
                }

                main(){
                    iostream.Printf(Self.removeDuplicates("aab"));
                    Return;
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Program),[MethodDecl(Id(removeDuplicates),Instance,[param(Id(s),StringType)],Block([VarDecl(Id(temp),StringType),VarDecl(Id(flag),BoolType,BooleanLit(False)),For(Id(i),IntLit(0),CallExpr(Id(iostream),Id(len),[Id(s)]),IntLit(1),Block([If(BinaryOp(==,ArrayCell(Id(temp),[BinaryOp(-,CallExpr(Id(temp),Id(length),[]),IntLit(1))]),ArrayCell(Id(S),[Id(i)])),Block([Call(Id(temp),Id(pop_back),[]),AssignStmt(Id(flag),BooleanLit(True))]),Block([Call(Id(temp),Id(push_back),[ArrayCell(Id(S),[Id(i)])])]))])]),If(Id(flag),Block([Return(CallExpr(Self(),Id(removeDuplicates),[Id(temp)]))]),Block([Return(Id(temp))]))])),MethodDecl(Id(main),Static,[],Block([Call(Id(iostream),Id(Printf),[CallExpr(Self(),Id(removeDuplicates),[StringLit(aab)])]),Return()]))])])"
        self.assertTrue(TestAST.test(input,expect,387))

    def test_89(self):
        input= """
            Class Program{
                Var a, $b : Int = 0x34, 0b101;
                notMain(f: Boolean; arr: Array[Array[Float, 3], 4]){
                    Var s : Int = 3;
                    Foreach(i In 1 .. 2){
                        s = s + i;
                        Out.print("2346", i);
                        Continue;
                        Break;
                    }
                    Self.notMain();
                    Return s;
                }
                main(){
                    Var sdf : Array[Array[Float, 3], 4];
                    Self.notMain(True, sdf);
                    Return;
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(52))),AttributeDecl(Static,VarDecl(Id($b),IntType,IntLit(5))),MethodDecl(Id(notMain),Instance,[param(Id(f),BoolType),param(Id(arr),ArrayType(4,ArrayType(3,FloatType)))],Block([VarDecl(Id(s),IntType,IntLit(3)),For(Id(i),IntLit(1),IntLit(2),IntLit(1),Block([AssignStmt(Id(s),BinaryOp(+,Id(s),Id(i))),Call(Id(Out),Id(print),[StringLit(2346),Id(i)]),Continue,Break])]),Call(Self(),Id(notMain),[]),Return(Id(s))])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(sdf),ArrayType(4,ArrayType(3,FloatType))),Call(Self(),Id(notMain),[BooleanLit(True),Id(sdf)]),Return()]))])])"
        self.assertTrue(TestAST.test(input,expect,388))

    def test_90(self):
        input= """
            Class Program {
                Constructor(a: Int) { } 
                Destructor(){ }
                $sum(){ Return True; }
                main(){}
            }
            Class Proram {
                Constructor(a: Int; b: Float) { } 
                Destructor(){ Break; }
                $sum(){ Return False; }
                main(){}
            }
            Class Program {
                Constructor(a: Int; b: Float; c: Boolean) { }
                Destructor(){ Continue; }
                $sum(){ Return True && False; }
                main(){}
            }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType)],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id($sum),Static,[],Block([Return(BooleanLit(True))])),MethodDecl(Id(main),Static,[],Block([]))]),ClassDecl(Id(Proram),[MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),FloatType)],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([Break])),MethodDecl(Id($sum),Static,[],Block([Return(BooleanLit(False))])),MethodDecl(Id(main),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),FloatType),param(Id(c),BoolType)],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([Continue])),MethodDecl(Id($sum),Static,[],Block([Return(BinaryOp(&&,BooleanLit(True),BooleanLit(False)))])),MethodDecl(Id(main),Static,[],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,389))

#-------------------------------------------------------------
    def test_91(self):
        input= """
            Class Banhchuoi{
                test(){
                    a = (12/12_0_9_3 + 0XAF_BE) --(a[5] + b[9][New X().Y().id]);
                    Break;
                    Continue;
                    Return;
                    Return Main;
                }
                main(){
                    If(!True){
                        x = x + 1;
                    }
                }
                sum(){ 
                    If(x[1][1*2][1*3]){
                        x[1][1+1][1+1+1] = x[1][2][3];
                    }
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Banhchuoi),[MethodDecl(Id(test),Instance,[],Block([AssignStmt(Id(a),BinaryOp(-,BinaryOp(+,BinaryOp(/,IntLit(12),IntLit(12093)),IntLit(44990)),UnaryOp(-,BinaryOp(+,ArrayCell(Id(a),[IntLit(5)]),ArrayCell(Id(b),[IntLit(9),FieldAccess(CallExpr(NewExpr(Id(X),[]),Id(Y),[]),Id(id))]))))),Break,Continue,Return(),Return(Id(Main))])),MethodDecl(Id(main),Instance,[],Block([If(UnaryOp(!,BooleanLit(True)),Block([AssignStmt(Id(x),BinaryOp(+,Id(x),IntLit(1)))]))])),MethodDecl(Id(sum),Instance,[],Block([If(ArrayCell(Id(x),[IntLit(1),BinaryOp(*,IntLit(1),IntLit(2)),BinaryOp(*,IntLit(1),IntLit(3))]),Block([AssignStmt(ArrayCell(Id(x),[IntLit(1),BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(1)),IntLit(1))]),ArrayCell(Id(x),[IntLit(1),IntLit(2),IntLit(3)]))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,390))

    def test_92(self):
        input= """
            Class Banhchuoi{
                test(){
                    Val _Var : Array[Array[Int, 9],1];
                    a = b.c().d;
                    a1 = ("Int").strlength;
                }
                sum(){
                    Foreach( i In i .. i By i){
                        Foreach( i In i .. i By i){
                            Foreach( i In i .. i By i){
                            }
                        }
                    }
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Banhchuoi),[MethodDecl(Id(test),Instance,[],Block([ConstDecl(Id(_Var),ArrayType(1,ArrayType(9,IntType)),None),AssignStmt(Id(a),FieldAccess(CallExpr(Id(b),Id(c),[]),Id(d))),AssignStmt(Id(a1),FieldAccess(StringLit(Int),Id(strlength)))])),MethodDecl(Id(sum),Instance,[],Block([For(Id(i),Id(i),Id(i),Id(i),Block([For(Id(i),Id(i),Id(i),Id(i),Block([For(Id(i),Id(i),Id(i),Id(i),Block([])])])])])])]))])])"
        self.assertTrue(TestAST.test(input,expect,391))

    def test_93(self):
        input= """
            Class Banhchuoi{
                test(){
                    lazy = sleepy + tired + boring;
                    spamming_here_ = " hehe he's cool; haha 242 @Q$# ";
                    hihi = haha + hehe;
                }
                $main(){
                    If(a){
                        If(b){
                            If(c){} 
                            Else{}
                        } 
                        Else{}
                    } 
                    Else{}
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Banhchuoi),[MethodDecl(Id(test),Instance,[],Block([AssignStmt(Id(lazy),BinaryOp(+,BinaryOp(+,Id(sleepy),Id(tired)),Id(boring))),AssignStmt(Id(spamming_here_),StringLit( hehe he's cool; haha 242 @Q$# )),AssignStmt(Id(hihi),BinaryOp(+,Id(haha),Id(hehe)))])),MethodDecl(Id($main),Static,[],Block([If(Id(a),Block([If(Id(b),Block([If(Id(c),Block([]),Block([]))]),Block([]))]),Block([]))]))])])"
        self.assertTrue(TestAST.test(input,expect,392))

    def test_94(self):
        input= """
            Class Program {
            main() {
                x[0][a+b][0b11] = y[2] + 3;
            }
        }
        """
        expect = r"Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(ArrayCell(Id(x),[IntLit(0),BinaryOp(+,Id(a),Id(b)),IntLit(3)]),BinaryOp(+,ArrayCell(Id(y),[IntLit(2)]),IntLit(3)))]))])])"
        self.assertTrue(TestAST.test(input,expect,393))

    def test_95(self):
        input= """
            Class Banhchuoi{
                test(){
                    Var flag : Int = 0123 + 0123;
                    flag = (True != 123) + !3 * (False && kj % 123 <= chim.f());
                    Self.praaa(----------(!123 == kk * 12 - 3) || False + !!!!!!9==4);
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Banhchuoi),[MethodDecl(Id(test),Instance,[],Block([VarDecl(Id(flag),IntType,BinaryOp(+,IntLit(83),IntLit(83))),AssignStmt(Id(flag),BinaryOp(+,BinaryOp(!=,BooleanLit(True),IntLit(123)),BinaryOp(*,UnaryOp(!,IntLit(3)),BinaryOp(<=,BinaryOp(&&,BooleanLit(False),BinaryOp(%,Id(kj),IntLit(123))),CallExpr(Id(chim),Id(f),[]))))),Call(Self(),Id(praaa),[BinaryOp(==,BinaryOp(||,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,BinaryOp(==,UnaryOp(!,IntLit(123)),BinaryOp(-,BinaryOp(*,Id(kk),IntLit(12)),IntLit(3))))))))))))),BinaryOp(+,BooleanLit(False),UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,IntLit(9))))))))),IntLit(4))])]))])])"
        self.assertTrue(TestAST.test(input,expect,394))

## ---------------------------------------------------------

    def test_96(self):
        input= """
            Class Banhchuoi{
                test(){
                    Foreach(i In 1 .. i) {
                        dt[dt[dt[arr[i]]]] = dt[arr[dt[arr[i]]]] + 1;
                        chim::$f(dt, k * Array(1, 2, 3, 4));
                    }
                    If( ----(!Chim) > 055 + 0xB0B) {
                        chim.print()[13] = Array(1,2,3,4,5,6,7,8,9);
                        chim::$chim( ----(!Chim) > 055 + 0xB0B);
                    }
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Banhchuoi),[MethodDecl(Id(test),Instance,[],Block([For(Id(i),IntLit(1),Id(i),IntLit(1),Block([AssignStmt(ArrayCell(Id(dt),[ArrayCell(Id(dt),[ArrayCell(Id(dt),[ArrayCell(Id(arr),[Id(i)])])])]),BinaryOp(+,ArrayCell(Id(dt),[ArrayCell(Id(arr),[ArrayCell(Id(dt),[ArrayCell(Id(arr),[Id(i)])])])]),IntLit(1))),Call(Id(chim),Id($f),[Id(dt),BinaryOp(*,Id(k),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)])])])]),If(BinaryOp(>,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(!,Id(Chim)))))),BinaryOp(+,IntLit(45),IntLit(2827))),Block([AssignStmt(ArrayCell(CallExpr(Id(chim),Id(print),[]),[IntLit(13)]),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5),IntLit(6),IntLit(7),IntLit(8),IntLit(9)]),Call(Id(chim),Id($chim),[BinaryOp(>,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(!,Id(Chim)))))),BinaryOp(+,IntLit(45),IntLit(2827)))])]))]))])])"
        self.assertTrue(TestAST.test(input,expect,395))

    def test_97(self):
        input= """
            Class Banhchuoi{
                test(){
                    Foreach(i In 0x1 .. 0b1 By 01) {
                        If (i % 2 == 0) {
                            Break;
                            Continue;
                        }
                        Elseif (i > 10) {
                            Self.w(i);
                        }
                    }
                }
            }
        """
        expect=r"Program([ClassDecl(Id(Banhchuoi),[MethodDecl(Id(test),Instance,[],Block([For(Id(i),IntLit(1),IntLit(1),IntLit(1),Block([If(BinaryOp(==,BinaryOp(%,Id(i),IntLit(2)),IntLit(0)),Block([Break,Continue]),If(BinaryOp(>,Id(i),IntLit(10)),Block([Call(Self(),Id(w),[Id(i)])])))])])]))])])"
        self.assertTrue(TestAST.test(input,expect,396))

    def test_98(self):
        input= """
            Class Banhchuoi{
                test(){
                    Self.chim = Null;
                    If ("Neu nhu troi sap..."){
                        If ("Neu nhu troi sap..."){
                            If ("Neu nhu troi sap..."){
                                If ("Neu nhu troi sap..."){
                                    If ("Neu nhu troi sap..."){
                                        Break; Continue;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Banhchuoi),[MethodDecl(Id(test),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(chim)),NullLiteral()),If(StringLit(Neu nhu troi sap...),Block([If(StringLit(Neu nhu troi sap...),Block([If(StringLit(Neu nhu troi sap...),Block([If(StringLit(Neu nhu troi sap...),Block([If(StringLit(Neu nhu troi sap...),Block([Break,Continue]))]))]))]))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,397))

    def test_99(self):
        input= """
            Class Calculator
            {
                main(){
                    window = New JFrame("Calculator");
                    window.setSize(WINDOW_WIDTH, WINDOW_HEIGHT);
                    window.setLocationRelativeTo(Null);
                }
            }
        """
        expect = r"Program([ClassDecl(Id(Calculator),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(window),NewExpr(Id(JFrame),[StringLit(Calculator)])),Call(Id(window),Id(setSize),[Id(WINDOW_WIDTH),Id(WINDOW_HEIGHT)]),Call(Id(window),Id(setLocationRelativeTo),[NullLiteral()])]))])])"
        self.assertTrue(TestAST.test(input,expect,398))

    def test_100(self):
        input= """
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
        expect=r"Program([ClassDecl(Id(Banhchuoi),[MethodDecl(Id(test),Instance,[],Block([Call(CallExpr(Self(),Id(colen),[Self()]),Id(hello),[StringLit(self)]),VarDecl(Id(a),IntType,BinaryOp(+,Self(),IntLit(4))),AssignStmt(Id(X),CallExpr(FieldAccess(Id(a),Id($hello)),Id(haha),[])),AssignStmt(ArrayCell(Id(a),[IntLit(9),IntLit(12)]),Id(hello)),AssignStmt(Id(b),BinaryOp(+,Self(),Self()))])),AttributeDecl(Instance,VarDecl(Id(x),IntType,IntLit(2))),AttributeDecl(Static,VarDecl(Id($y),IntType,IntLit(3)))])])"
        self.assertTrue(TestAST.test(input,expect,399))

### ==============================================================