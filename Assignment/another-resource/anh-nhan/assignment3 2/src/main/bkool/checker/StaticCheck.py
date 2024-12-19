
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from StaticError import *
from functools import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value


class StaticChecker(BaseVisitor):
    global_envi = [
        Symbol("getInt", MType([], IntType())),
        Symbol("putIntLn", MType([IntType()], VoidType()))
    ]
    

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    __InLoop = 0
    __IdIsVar = False
    
            
    # ------------------Program---------------
    # decl: List[ClassDecl]
    def visitProgram(self, ast, c): #context
        #c = {"Global": [{}], "Class": {}, "Method": {}, "Local": [], "FirstCheck" = 1}
        c =
        
        #c = {"Global": {'}, }
        
        
        reduce(lambda x,y: self.visit(y,x), ast.decl, c)
        
        # "Global": [{name, isFunc, type, [{name,type}]}]
        # "global += [{name, 1, Auto, [{a,[auto]}]}]
        # inherit: if local += []
        #"Method": {parent}
        #"Local": [{name, type}]
        # for i in ast.decl:
        #     self.visit(i, c)
        c["FirtCheck"] = False
        #foo() inherit bar {super(Integer(1)}
        # bar(x:auto) {x = "str"}
        #foo(1)
        reduce(lambda x, y: self.visit(y, x), ast.decl, c)

    # ------------------Class-----------------
    # classname: Id, memlist: List[MemDecl], parentname: Id = None
    def visitClassDecl(self, ast, c):
        class_name = ast.classname.name
        if class_name in c["Global"]:
            raise Redeclared(Class(), class_name)
        # Parent class is undeclared
        if ast.parentname is not None:
            if ast.parentname.name not in c["Global"]:
                raise Undeclared(Class(), ast.parentname.name)

        # Create new classes and add to dict
        newClass = {"Attribute": {}, "Method": {}}
        c["Global"][class_name] = newClass
        c["Class"] = newClass
        #visit memlist of class
        reduce(lambda x, y: self.visit(y, x), ast.memlist, c)
        return c


    # kind: SIKind  decl: StoreDecl
    def visitAttributeDecl(self, ast, c):
        if fisrtCheck()
        attribute_name = ast.decl.constant.name if type(ast.decl) is ConstDecl else ast.decl.variable.name
        IsStatic = True if type(ast.kind) is Static else False
        IsConst = True if type(ast.decl) is ConstDecl else False
        attribute_type = ast.decl.constType if type(ast.decl) is ConstDecl else ast.decl.varType

        if attribute_name in c["Class"]["Attribute"]:
            raise Redeclared(Attribute(), attribute_name)
        if type(attribute_type) is ClassType or (
                type(attribute_type) is ArrayType and type(attribute_type.eleType) is ClassType):
            if attribute_type.classname.name not in c["Global"]:
                raise Undeclared(Class(), attribute_type.classname.name)

        temp = {"Static": 1}
        flag_init = self.visit(ast.decl, temp)
        print(flag_init)

        if flag_init[0]:
            raise TypeMismatchInStatement(ast)
        print(c)
        newAttribute = {"IsConst": IsConst, "IsStatic": IsStatic, "Type": attribute_type}
        c["Class"]["Attribute"][attribute_name] = newAttribute
        return c


    # kind: SIKind name: Id param: List[VarDecl] body: Block
    def visitMethodDecl(self, ast, c):
        method_name = ast.name.name
        IsStatic = True if type(ast.kind) is Static else False
        # redeclared
        if method_name in c["Class"]["Method"]:
            raise Redeclared(Method(), method_name)
        # change in Method to change in class
        newMethod = {"IsStatic": IsStatic, "Type": VoidType(), "Param": {}}
        c["Class"]["Method"][method_name] = newMethod
        c["Method"] = newMethod

        print(c)
        # param list
        temp = {}
        c["Method"]["Param"] = temp
        for i in ast.param:
            j = self.visit(i, temp)
            if j[2] == True:
                raise Redeclared(Parameter(), i.variable.name)
            if j[3] is not None:
                if j[3] not in c["Global"]:
                    raise Undeclared(Class(), j[3])
        # visit body to find type
        method_type = self.visit(ast.body, c)
        if method_type == []:
            method_type = VoidType()
        c["Method"]["Type"] = method_type


    # ------------------Stmts-----------------
    # decl:List[StoreDecl]   #     stmt:List[Stmt]
    def visitBlock(self, ast, c):

        c["Local"] = [{}] + c["Local"]
        block_type_lst = []
        for i in ast.decl:
            temp = self.visit(i, c)
            if type(temp) is tuple:
                temp = temp[1]
            block_type_lst += [temp]

        block_type = None
        if len(block_type_lst) != 0:
            # print(block_type_lst)
            for i in range(len(block_type_lst)):
                if block_type_lst[0] != block_type_lst[i]:
                    if (type(IntType()) is block_type_lst[0] or type(FloatType()) is block_type_lst[0]) and (
                            type(IntType()) is block_type_lst[i] or type(FloatType()) is block_type_lst[i]):
                        block_type_lst[0] = type(FloatType())
                    else:
                        raise TypeMismatchInStatement(ast.inst[i])
            block_type = type(block_type_lst[0])
        else:
            block_type = []

        c["Local"] = c["Local"][1:]
        return block_type

    # variable: Id, varType: Type, varInit: Expr
    def visitVarDecl(self, ast, c):
        var_name = ast.variable.name
        var_type = ast.varType
        IsStatic = True if c["Static"] == 1 else False
        flag_param_redeclare = False
        if checkRedeclared(var_name,
                           c) == True:  # trong truong hop var => check trong local, trong truong hop param, attri, check trong c
            if "Local" in c:
                raise Redeclared(Variable(), var_name)

        newVar = {"IsConst": False, "IsStatic": IsStatic, "Type": var_type}
        if "Local" in c:
            c["Local"][0][var_name] = newVar
        else:
            if var_name in c:  # khai bao param lan 2
                flag_param_redeclare = True
            c[var_name] = newVar

        # print("||||||||||||||||||")
        # print(c)
        maybe_classtype = None

        if type(var_type) is ClassType:
            if "Local" in c:
                if var_type.classname.name not in c["Global"]:
                    raise Undeclared(Class(), var_type.classname.name)
            else:
                maybe_classtype = var_type.classname.name

        if (type(var_type) is ArrayType and type(var_type.eleType) is ClassType):
            if "Local" in c:
                if var_type.eleType.classname.name not in c["Global"]:
                    raise Undeclared(Class(), var_type.eleType.classname.name)
            else:
                maybe_classtype = var_type.eleType.classname.name

        flag = False
        if ast.varInit is not None:
            init_type = self.visit(ast.varInit, c)
            if type(init_type) is not tuple:
                if type(init_type) is ArrayType and type(var_type) is ArrayType:
                    if init_type.size != var_type.size:
                        raise TypeMismatchInStatement(ast)
                    elif type(var_type.eleType) != init_type.eleType:
                        raise TypeMismatchInStatement(ast)

                if type(init_type) != type(var_type):
                    if type(init_type) is not IntType and type(var_type) is not FloatType:
                        if "Local" in c:
                            raise TypeMismatchInStatement(ast)
                        flag = True
            else:
                return init_type

        return (flag, [], flag_param_redeclare, maybe_classtype)

    # constant: Id, constType: Type, value: Expr = None
    def visitConstDecl(self, ast, c):
        flag = False
        const_name = ast.constant.name
        const_type = ast.constType
        IsStatic = True if c["Static"] == 1 else False

        if checkRedeclared(const_name, c) == True:
            raise Redeclared(Constant(), const_name)

        if type(const_type) is ClassType or (type(const_type) is ArrayType and type(const_type.eleType) is ClassType):
            if const_type.classname.name not in c["Global"]:
                raise Undeclared(Class(), const_type.classname.name)

        newConst = {"IsConst": True, "IsStatic": IsStatic, "Type": const_type}

        if "Local" in c:
            c["Local"][0][const_name] = newConst

        if ast.value is None:
            raise IllegalConstantExpression(None)
        else:
            temp = self.visit(ast.value, c)
            if self.__IdIsVar == True:
                raise IllegalConstantExpression(ast.value)
            self.__IdIsVar = False

            if type(temp) is ArrayType and type(temp) is ArrayType:
                if temp.size != temp.size:
                    raise TypeMismatchInStatement(ast)
                elif type(temp.eleType) != temp.eleType:
                    raise TypeMismatchInStatement(ast)

            if type(temp) != type(const_type):
                if type(temp) is not IntType and type(const_type) is not FloatType:
                    if "Local" in c:
                        raise TypeMismatchInConstant(ast)
                    flag = True

        return (flag, [])

    # lhs: Expr, exp: Expr
    def visitAssign(self, ast, c):

        right = self.visit(ast.exp, c)
        left = self.visit(ast.lhs, c)

        if type(ast.lhs) is Id:
            if (isIdConst(ast.lhs.name, c)):
                raise CannotAssignToConstant(ast)

        if type(left) is VoidType:
            raise TypeMismatchInStatement(ast)
        if type(left) != type(right):
            if type(left) is not FloatType or type(right) is not IntType:
                # print(type(left))
                # print(type(right))
                raise TypeMismatchInStatement(ast)

        if type(left) is ArrayType:
            if right.size == 0:
                # print(2)
                raise TypeMismatchInStatement(ast)
            if right.size != left.size:
                # print(2)
                raise TypeMismatchInStatement(ast)
            temp = left
            temp2 = right
            while type(temp.eleType) is ArrayType:
                if temp.size != temp2.size:
                    # print(3)
                    raise TypeMismatchInStatement(ast)

                temp = temp.eleType
                temp2 = temp2.eleType
            if type(temp.eleType) != temp2.eleType:
                if type(temp.eleType) is not FloatType and type(temp2.eleType) is not IntType:
                    raise TypeMismatchInStatement(ast)

        return []

    # expr: Expr, thenStmt: Stmt, elseStmt: Stmt
    def visitIf(self, ast, c):
        if type(self.visit(ast.expr, c)) is not BoolType:
            raise TypeMismatchInStatement(ast)
        # print("xxxxxxxxxxx")
        then_stmt = self.visit(ast.thenStmt, c)
        # print("yyyyyyyyyyyy")
        else_stmt = None
        if ast.elseStmt:
            else_stmt = self.visit(ast.elseStmt, c)
        # print("zzzzzzz")

        ret_type = None

        if else_stmt is not None:
            if then_stmt == [] and else_stmt == []:
                ret_type = []
            elif then_stmt != [] and else_stmt == []:
                ret_type = type(then_stmt)
            else:
                if type(then_stmt) != type(else_stmt):
                    raise TypeMismatchInStatement(ast.elseStmt)
                else:
                    ret_type = type(then_stmt)
        else:
            if then_stmt != []:
                ret_type = type(then_stmt)
            else:
                ret_type = []
        return ret_type

    # id: Id, expr1: Expr, expr2: Expr, loop: Stmt, expr3: Expr = None
    def visitFor(self, ast, c):
        flag = checkUndeclared(ast.id.name, c)
        if flag:
            raise Undeclared(Identifier(), ast.name.name)

        id_type = getIdType(ast.id.name, c)
        if type(id_type) is not IntType:
            raise TypeMismatchInStatement(ast)

        exp1 = self.visit(ast.expr1, c)
        exp2 = self.visit(ast.expr2, c)
        if type(exp1) is not IntType or type(exp2) is not IntType:
            raise TypeMismatchInStatement(ast)
        if ast.expr3 is not None:
            exp3 = self.visit(ast.expr3, c)
            if type(exp3) is not IntType:
                raise TypeMismatchInStatement(ast)

        self.__InLoop += 1
        loop_type = self.visit(ast.loop, c)
        self.__InLoop -= 1

        return loop_type

    def visitBreak(self, ast, c):
        if self.__InLoop == 0:
            raise MustInLoop(ast)
        return []

    def visitContinue(self, ast, c):
        if self.__InLoop == 0:
            raise MustInLoop(ast)
        return []

    # expr: Expr = None
    def visitReturn(self, ast, c):
        if ast.expr == None:
            return VoidType()
        else:
            if list(c["Class"]["Method"].keys())[-1] == "main" and list(c["Global"].keys())[-1] == "Program":
                raise TypeMismatchInStatement(ast)
            return self.visit(ast.expr, c)

    # obj: Expr, method: Id, param: List[Expr]
    def visitCallStmt(self, ast, c):
        left = self.visit(ast.obj, c)
        method_name = ast.method.name

        if type(left) is not ClassType:
            raise TypeMismatchInStatement(ast)
        if method_name not in c["Global"][left.classname.name]["Method"]:
            raise Undeclared(Method(), method_name)
        else:
            method_type = c["Global"][left.classname.name]["Method"][method_name]["Type"]
            if type(method_type) is not VoidType:
                raise TypeMismatchInStatement(ast)

        if (type(ast.obj) is Id and ast.obj.name in c["Global"]) and ast.method.name[0] != "$":
            raise IllegalMemberAccess(ast)
        elif left.classname.name == "SelfLit" and ast.method.name[0] == "$":
            raise IllegalMemberAccess(ast)

        method_param = c["Global"][left.classname.name]["Method"][method_name]["Param"]
        if len(ast.param) != len(method_param):
            raise TypeMismatchInStatement(ast)
        else:
            for i in range(len(ast.param)):
                in_type = self.visit(ast.param[i], c)
                param_type = method_param[list(method_param.keys())[i]]["Type"]
                if type(in_type) != type(param_type):
                    if type(param_type) is not FloatType and type(in_type) is not IntType:
                        raise TypeMismatchInStatement(ast)

        return []

    ##--------------- Expr -------------------
    # op: str, left: Expr, right: Expr
    def visitBinaryOp(self, ast, c):
        left = self.visit(ast.left, c)
        right = self.visit(ast.right, c)
        if ast.op in ["+", "-", "*", "/"]:
            if (type(left) is not IntType and type(left) is not FloatType) or (
                    type(right) is not IntType and type(right) is not FloatType):
                raise TypeMismatchInExpression(ast)
            elif type(left) is type(right):
                return left
            else:
                return FloatType()
        elif ast.op == "%":
            if (type(left) is not IntType) or (type(right) is not IntType):
                raise TypeMismatchInExpression(ast)
            else:
                return IntType()
        elif ast.op == "&&" or ast.op == "||":
            if type(left) is not BoolType or type(right) is not BoolType:
                raise TypeMismatchInExpression(ast)
            else:
                return BoolType()
        elif ast.op == "==.":
            if type(left) is not StringType or type(right) is not StringType:
                raise TypeMismatchInExpression(ast)
            else:
                return BoolType()
        elif ast.op == "+.":
            if type(left) is not StringType or type(right) is not StringType:
                raise TypeMismatchInExpression(ast)
            else:
                return StringType()
        elif ast.op == "==" or ast.op == "!=":
            if (type(left) is not IntType and type(left) is not BoolType) or (
                    type(right) is not IntType and type(right) is not BoolType):
                raise TypeMismatchInExpression(ast)
            if type(left) != type(right):
                raise TypeMismatchInExpression(ast)
            else:
                return BoolType()
        elif ast.op in ["<", "<=", ">", ">="]:
            if (type(left) is not IntType and type(left) is not FloatType) or (
                    type(right) is not IntType and type(right) is not FloatType):
                raise TypeMismatchInExpression(ast)
            return BoolType()
        else:
            return []

    # op: str, body: Expr
    def visitUnaryOp(self, ast, c):
        body = self.visit(ast.body, c)
        if ast.op == "-":
            if type(body) is not IntType and type(body) is not FloatType:
                raise TypeMismatchInExpression(ast)
            else:
                return body
        else:  # op is !
            if type(body) is not BoolType:
                raise TypeMismatchInExpression(ast)
            else:
                return body

    # obj: Expr, method: Id, param: List[Expr] #check ca vu $ va id
    def visitCallExpr(self, ast, c):
        left = self.visit(ast.obj, c)
        method_name = ast.method.name

        if type(left) is not ClassType:
            raise TypeMismatchInExpression(ast)

        if method_name not in c["Global"][left.classname.name]["Method"]:
            raise Undeclared(Method(), method_name)
        else:
            method_type = c["Global"][left.classname.name]["Method"][method_name]["Type"]
            if type(method_type) is VoidType:
                raise TypeMismatchInExpression(ast)

        if (type(ast.obj) is Id and ast.obj.name in c["Global"]) and ast.method.name[0] != "$":
            raise IllegalMemberAccess(ast)
        elif left.classname.name == "SelfLit" and ast.method.name[0] == "$":
            raise IllegalMemberAccess(ast)

        method_param = c["Global"][left.classname.name]["Method"][method_name]["Param"]
        if len(ast.param) != len(method_param):
            raise TypeMismatchInExpression(ast)
        else:
            for i in range(len(ast.param)):
                in_type = self.visit(ast.param[i], c)
                param_type = method_param[list(method_param.keys())[i]]["Type"]
                if type(in_type) != type(param_type):
                    if type(param_type) is not FloatType and type(in_type) is not IntType:
                        raise TypeMismatchInExpression(ast)

        ret = c["Global"][left.classname.name]["Method"][method_name]["Type"]
        return ret

    # classname: Id, param: List[Expr]
    def visitNewExpr(self, ast, c):
        class_name = ast.classname.name
        if "Global" in c:
            if class_name not in c["Global"]:
                raise Undeclared(Class(), class_name)
            # do tim constructor
            flag = False
            if len(ast.param) == 0 and "Constructor" not in c["Global"][class_name]["Method"]:
                flag = True
            elif "Constructor" in c["Global"][class_name]["Method"]:
                temp = c["Global"][class_name]["Method"]["Constructor"]["Param"]
                if len(temp) != len(ast.param):
                    raise TypeMismatchInExpression(ast)
                else:
                    for i in range(len(ast.param)):
                        in_type = self.visit(ast.param[i], c)
                        param_type = temp[list(temp.keys())[i]]["Type"]
                        if type(in_type) != type(param_type):
                            if type(param_type) is not FloatType and type(in_type) is not IntType:
                                raise TypeMismatchInExpression(ast)

            return ClassType(Id(class_name))
        else:
            return (class_name, ast)

    # ---------------- LHS -------------------
    # arr: Expr, idx: List[Expr]
    def visitArrayCell(self, ast, c):
        id_type = self.visit(ast.arr, c)
        if type(id_type) is not ArrayType:
            raise TypeMismatchInExpression(ast)

        for i in ast.idx:
            idx_type = self.visit(i, c)
            if type(idx_type) is not IntType:
                raise TypeMismatchInExpression(ast)
        temp = id_type  # Arr(3, Array(2, Array(3, Int))) 0
        temp2 = 0
        ret = temp
        while type(temp.eleType) is ArrayType:
            temp = temp.eleType
            temp2 += 1
            if temp2 == len(ast.idx):
                ret = temp
        temp2 += 1
        if temp2 == len(ast.idx):
            ret = temp.eleType
        if len(ast.idx) > temp2:
            # print("EEEEEEEEEEEEEE")
            raise TypeMismatchInExpression(ast)
        return ret

    # obj: Expr, fieldname: Id #illegal + t mm in exp
    def visitFieldAccess(self, ast, c):
        left = self.visit(ast.obj, c)

        if type(left) is not ClassType:
            raise TypeMismatchInExpression(ast)

        class_name = left.classname.name
        attribute_name = ast.fieldname.name
        if left.classname.name != "SelfLit":
            if attribute_name not in c["Global"][class_name]["Attribute"]:
                raise Undeclared(Attribute(), attribute_name)

        if (type(ast.obj) is Id and ast.obj.name in c["Global"]) and ast.fieldname.name[0] != "$":
            raise IllegalMemberAccess(ast)
        elif left.classname.name == "SelfLit" and ast.fieldname.name[0] == "$":
            raise IllegalMemberAccess(ast)

        if left.classname.name != "SelfLit":
            ret = c["Global"][class_name]["Attribute"][attribute_name]["Type"]
        else:
            ret = c["Class"]["Attribute"][attribute_name]["Type"]
        return ret

    # name: str
    def visitId(self, ast, c):

        flag = checkUndeclared(ast.name, c)
        if flag:
            raise Undeclared(Identifier(), ast.name)
        id_type = getIdType(ast.name, c)
        self.__IdIsVar = True if isIdConst(ast.name, c) == False else False
        return id_type

    # ------------------Litteral--------------
    # Intlit
    def visitIntLiteral(self, ast, c):
        return IntType()

    # FloatLiteral
    def visitFloatLiteral(self, ast, c):
        return FloatType()

    # String literal
    def visitStringLiteral(self, ast, c):
        return StringType()

    # BooleanLiteral
    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    # NullLiteral #bo
    def visitNullLiteral(self, ast, c):
        return ClassType(Id("NullLit"))

    # SelfLiteral #can co the loai rieng
    def visitSelfLiteral(self, ast, c):
        return ClassType(Id("SelfLit"))

    # value: List[Expr] vdu [2, 3, 4] # arraytype (size, type)
    def visitArrayLiteral(self, ast, c):
        ele_list = [self.visit(ele, c) for ele in ast.value]
        if not ele_list:
            return ArrayType(0, VoidType)

        elem = ele_list[0]
        flag = False
        for i in ele_list:
            if type(elem) != type(i):
                flag = True
        if flag:
            raise IllegalArrayLiteral(ast)

        if type(elem) is not ArrayType:
            return ArrayType(len(ast.value), type(elem))
        return ArrayType(len(ast.value), self.visit(ast.value[0], c))


# ----------------------------------Handler----------------------------------------
# ---------------------------------------------------------------------------------
def checkRedeclared(find_name, c):
    if "Local" in c:
        for i in range(len(c["Local"])):
            if find_name in c["Local"][i]:
                return True
            elif find_name in c["Method"]["Param"]:
                return True
    else:
        if find_name in c:
            return True
    return False


def checkUndeclared(find_name, c):
    for i in range(len(c["Local"])):
        if find_name in c["Local"][i]:
            return False
    if find_name in c["Method"]["Param"]:
        return False
    elif find_name in c["Class"]["Attribute"]:
        return False
    elif find_name in c["Global"]:
        return False
    return True


def getIdType(name, c):
    for i in range(len(c["Local"])):
        if name in c["Local"][i]:
            return c["Local"][i][name]["Type"]
    if name in c["Method"]["Param"]:
        return c["Method"]["Param"][name]["Type"]
    elif name in c["Class"]["Attribute"]:
        return c["Class"]["Attribute"][name]["Type"]
    elif name in c["Global"]:
        return ClassType(Id(name))


def isIdConst(name, c):
    for i in range(len(c["Local"])):
        if name in c["Local"][i]:
            return c["Local"][i][name]["IsConst"]
    if name in c["Method"]["Param"]:
        return c["Method"]["Param"][name]["IsConst"]
    return False
