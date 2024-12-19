## 1611089

"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import *


### Xem xet lai
class Node:
    def __init__(self,name,method,attribute,parentname=None):
        self.name = name
        self.method = method
        self.attribute = attribute
        self.parentname = parentname
    def __str__(self):
        return "Node("+str(self.name)+","+str(self.method)+","+str(self.attribute)+","+str(self.parentname)+")"
        
class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype
    def __str__(self):
        return "MType("+str(self.partype)+","+str(self.rettype)+")"

class Symbol:
    def __init__(self,name,mtype,value=None):
        self.name = name
        self.mtype = mtype
        self.value = value
    def __str__(self):
        # for x in self.mtype:
        #     print(x)
        return "Symbol("+str(self.name)+","+str(self.mtype)+","+str(self.value)+")"

class StaticChecker(BaseVisitor,Utils):

    global_envi = [
                    Node(
                        "io",[
                        Symbol("readInt",MType([],IntType())),\
                        Symbol("writeInt",MType([IntType()],VoidType())),\
                        Symbol("writeIntLn",MType([IntType()],VoidType())),\
                        Symbol("readFloat",MType([],FloatType())),\
                        Symbol("writeFloat",MType([FloatType()],VoidType())),\
                        Symbol("writeFloatLn",MType([FloatType()],VoidType())),\
                        Symbol("readBool",MType([],BoolType())),\
                        Symbol("writeBool",MType([BoolType()],VoidType())),\
                        Symbol("writeBoolLn",MType([BoolType()],VoidType())),\
                        Symbol("readStr",MType([],StringType())),\
                        Symbol("writeStr",MType([StringType()],VoidType())),\
                        Symbol("writeStrLn",MType([StringType()],VoidType()))\
                        ],
                        []
                    )
        ]

    def __init__(self,ast):
        self.ast = ast
   
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def delete_symbol(self, env, name):
        [env.remove(it) for it in env if it.name == name.name]

    def check_exist(self,listDecl, decl, kind):
    #Nem loi neu loi, tra ve symbol neu khong bi loi
        if kind == "Method": ## Ok
            cc = self.lookup(decl.name.name,listDecl,lambda x: x.name)
            if not(cc is None):
                raise Redeclared(Method(),decl.name.name)
            return Symbol(decl.name.name, MType([x.varType for x in decl.param],decl.returnType))
        elif kind == "Constant": ## Ok
            cc = self.lookup(decl.constant.name,listDecl,lambda x: x.name)
            if not(cc is None):
                raise Redeclared(Constant(),decl.constant.name)
            return Symbol(decl.constant.name, decl.constType, 0)
        elif kind == "Variable": ## OK
            cc = self.lookup(decl.variable.name,listDecl,lambda x: x.name)
            if not(cc is None):
                raise Redeclared(Variable(),decl.variable.name)
            return Symbol(decl.variable.name, decl.varType, 1)
        elif kind == "Parameter":
            cc = self.lookup(decl.variable.name,listDecl,lambda x: x.name)
            if not(cc is None):
                raise Redeclared(Parameter(),decl.variable.name)
            return Symbol(decl.variable.name, decl.varType, 1)
        elif kind == "CallStmt":
            cc = self.lookup(decl.obj.name,listDecl,lambda x: x.name)
            if not(cc is None):
                raise TypeMismatchInStatement(decl)
            return None
        elif kind == "CallExpr":
            cc = self.lookup(decl.obj.name,listDecl,lambda x: x.name)
            if not(cc is None):
                raise TypeMismatchInExpression(decl)
            return None
        elif kind == "NewExpr":
            cc = self.lookup(decl.classname.name,listDecl,lambda x: x.name)
            if not(cc is None):
                raise TypeMismatchInExpression(decl)
            return None

        return decl

    def check_return(self, l, r):
        if type(l) is Symbol:
            l = l.mtype
        if type(r) is Symbol:
            r = r.mtype

        if ((type(l),type(r)) == (BoolType,BoolType)) or\
            ((type(l),type(r)) == (StringType,StringType)) or\
            ((type(l),type(r)) == (FloatType,FloatType)) or\
            ((type(l),type(r)) == (IntType,IntType)) or\
            ((type(l),type(r)) == (FloatType,IntType)) or\
            ((type(l),type(r)) == (ClassType,ClassType)):
            return True
        elif ((type(l),type(r)) == (ArrayType, ArrayType)):
            if (type(l.eleType) == type(r.eleType)) and l.size == r.size:
                return True

        return False

    def check_type_const(self, left, right):
        if type(left) is Symbol:
            left = left.mtype
        if type(right) is Symbol:
            right = right.mtype

        if ((type(left),type(right)) == (BoolType,BoolType)) or\
            ((type(left),type(right)) == (StringType,StringType)) or\
            ((type(left),type(right)) == (FloatType,FloatType)) or\
            ((type(left),type(right)) == (IntType,IntType)) or\
            ((type(left),type(right)) == (FloatType, IntType)):
            return True
        elif ((type(left),type(right)) == (ArrayType, ArrayType)):
            if (type(left.eleType) == type(right.eleType)) and left.size == right.size:
                return True

        return False

    def check_global(self, de, glo):
        for x in glo:
            if x.name == de.name:
                return de.name
            for y in x.method:
                if y.name == de.name:
                    return de.name
            for z in x.attribute:
                if z.name == de.name:
                    return de.name
        return None

    def check_Redeclared(self, lst, de, kind, value = None):
        dem = 0
        if kind == "Class":  
            for x in lst:
                if x.name == de.name:
                    dem += 1
                    if dem >= 2:
                        raise Redeclared(Class(),de.name)
        

    def Rule_assign(self, le, ri):
        if type(le) is Symbol:
            le = le.mtype
        if type(ri) is Symbol:
            ri = ri.mtype

        if ((type(le),type(ri)) == (ArrayType, ArrayType)):
            if (type(le.eleType) == type(ri.eleType)) and le.size == ri.size:
                return True
            else:
                return False
        elif not ((type(le),type(ri)) == (IntType,IntType) or\
            (type(le),type(ri)) == (FloatType,IntType) or\
            (type(le),type(ri)) == (FloatType,FloatType) or\
            (type(le),type(ri)) == (BoolType,BoolType) or\
            (type(le),type(ri)) == (StringType,StringType) or\
            (type(le),type(ri)) == (ClassType,ClassType)):
            return False

        return True

    def check_method_by_id_call_exp(self, ast, lst, name, c):
        for z in lst:
            if name == z.name:
                ## check method in x.method

                for xx in z.method:
                    if xx.name == ast.method.name:

                        ## check return
                        if type(xx.mtype.rettype) is VoidType:
                            return False
                            ## check para

                        if len(ast.param) != len(xx.mtype.partype):
                            return False
                        else:

                            for i in range(0,len(xx.mtype.partype)):
                                ret = self.visit(ast.param[i],c)
                                if type(ret) is Symbol:
                                    ret = ret.mtype
                                if self.Rule_assign(xx.mtype.partype[i],ret) is False:
                                    return False

                            ## Check xong 
                            return xx.mtype.rettype

                ### Check no co cha ko
                if z.parentname is None:
                    raise Undeclared(Method(),ast.method.name)
                else:
                    cc = self.check_method_by_id_call_exp(ast, lst, z.parentname, c)
                    if cc is False:
                        return False
                    else:
                        return cc

        return False      

    def check_method_by_id_call(self, ast, lst, name, c):
        for z in lst:
            if name == z.name:
                ## check method in x.method

                for xx in z.method:
                    if xx.name == ast.method.name:

                        ## check return
                        if type(xx.mtype.rettype) is not VoidType:
                            return False
                            ## check para

                        if len(ast.param) != len(xx.mtype.partype):
                            return False
                        else:

                            for i in range(0,len(xx.mtype.partype)):
                                ret = self.visit(ast.param[i],c)
                                if type(ret) is Symbol:
                                    ret = ret.mtype
                                if self.Rule_assign(xx.mtype.partype[i],ret) is False:
                                    return False

                            ## Check xong 
                            return True
                            #return xx.mtype.rettype

                ### Check no co cha ko
                if z.parentname is None:
                    #### Chu y raise
                    raise Undeclared(Method(),ast.method.name)
                else:
                    if self.check_method_by_id_call(ast, lst, z.parentname, c):
                        return True
                    else:
                        return False

        return False      

    def check_if_type_unknown(self,ast,c):
        ch = False
        if type(ast) is ClassType:
            for x in c:
                if x.name == ast.classname.name:
                    ch = True
                    break
            if ch is False:
                raise Undeclared(Class(),ast.classname.name)

    def check_access_field(self, ast, lst, name, c):
        for z in lst:
            if name == z.name:
                ## check method in x.method

                for xx in z.attribute:
                    if xx.name == ast.fieldname.name:
                        if xx.value == 0:
                            return Symbol(xx.name,xx.mtype)
                        return xx.mtype

                ### Check no co cha ko
                if z.parentname is None:
                    raise Undeclared(Attribute(), ast.fieldname.name)
                else:
                    cc = self.check_access_field(ast, lst, z.parentname, c)
                    if cc is False:
                        return False
                    else:
                        return cc

        return False   


    
    def visitProgram(self, ast, c):
        #decl:list(ClassDecl)
        env = c.copy()
        lst_class = []
        id_parent = None


        ### Duyet lan 1
        for decl in ast.decl:
            # ClassDecl: classname (Id), memlist (List[MemDecl]), parentname (Id)
            id_class = decl.classname.name 
            lst_method = []
            lst_attribute = []
            for mem in decl.memlist:
                if type(mem) is MethodDecl:

                    lst_para = []
                    for pp in mem.param:
                        lst_para.append(pp.varType)
                    lst_method.append(Symbol(mem.name.name,MType(lst_para,mem.returnType)))

                elif type(mem) is AttributeDecl:
                    if type(mem.kind) is Static:
                        if type(mem.decl) is ConstDecl:
                            lst_attribute.append(Symbol(mem.decl.constant.name,mem.decl.constType,0))
                        elif type(mem.decl) is VarDecl:
                            lst_attribute.append(Symbol(mem.decl.variable.name,mem.decl.varType,1))
                    else:
                        if type(mem.decl) is ConstDecl:
                            lst_attribute.append(Symbol(mem.decl.constant.name,mem.decl.constType,0))
                        elif type(mem.decl) is VarDecl:
                            lst_attribute.append(Symbol(mem.decl.variable.name,mem.decl.varType,1))
            lst_class.append(Node(id_class,lst_method,lst_attribute,decl.parentname.name if not(decl.parentname is None) else None))
        env += lst_class
        ### 
        
        for x in c:
            if type(x) is Node:
                print("name: ",x.name)
                print("method:")
                for item in x.method:
                    print(item)
                    for i in item.mtype.partype:
                        print(i)
                    print("\n")
                print("attribute: ",x.attribute)
                print("parentname: ",x.parentname)
                
            
        #### Duyet lan 2
        for decl in ast.decl:
            self.check_Redeclared(env,decl.classname,"Class")
            id_parent = decl.parentname
            if not(id_parent is None):
                dem = 0
                for a in env:
                    if a.name == id_parent.name:
                        dem += 1
                        
                if dem == 0:
                    raise Undeclared(Class(),id_parent.name)

        # env_class = []
        # for t in env:
        #     env_class.append(Symbol(t.name,Class()))

        ### Visit node tiep theo (env, loop?, return, envclass, parentname, classname)
        list(map(lambda x: self.visit(x,(env, False, None, None, id_parent, None)),ast.decl))

        return []

    def visitClassDecl(self, ast, c):
        #classname:Id
        #memlist:list(MemDecl) // Attri or Method
        #parentname: Id
        
        env = c[0].copy()
        env_class = []

        for mem in ast.memlist:
            
            if type(mem) is AttributeDecl:
                if type(mem.decl) is ConstDecl:
                    kq = self.check_exist(env_class, mem.decl, "Attribute")
                    ### check type voi expr
                    if mem.decl.value==None:
                        raise IllegalConstantExpression(None)
                    val = self.visit(mem.decl.value,(env, c[1], c[2], env_class, c[4], c[5]))
                    if self.check_type_const(mem.decl.constType, val) is False:
                        raise TypeMismatchInConstant(mem)

                    env_class.append(kq)
                elif type(mem.decl) is VarDecl:
                    env_class.append(self.check_exist(env_class, mem.decl, "Attribute"))
                

            elif type(mem) is MethodDecl:
                # --------------------- Method -----------------
                ### Check special method
                if mem.name.name == "<init>":
                    pass
                else:
                    # Check name Method
                    env_class.append(self.check_exist(env_class, mem, "Method"))
                        

                
                self.visit(mem,(env, False, None, env_class, ast.parentname, ast.classname.name))
                #############

    def visitMethodDecl(self, ast, c):
        #kind: kind
        #name: Id
        #param: list(VarDecl)
        #returnType: Type
        #body: Block
        print("visitMethodDecl: ")
        for x in c:
            print(x)
            if type(x) is list:
                for y in x:
                    print(y)

        env = c[0].copy()
        env_class = c[3].copy()
        id_parent = c[4]

        # Check param
        para = []
        for p in ast.param:   
            self.check_if_type_unknown(p.varType,env)
            para.append(self.check_exist(para, p, "Parameter"))
            self.delete_symbol(env_class, p.variable)  # remove neu trung ko thi thoi
        env_class += para

        # Check localvar
        local_var = para
        for vd in ast.body.decl:
            if type(vd) is ConstDecl:
                #############
                kq = self.check_exist(local_var, vd, "Constant")
                ### check type voi expr
                if vd.value == None:
                    raise IllegalConstantExpression(None)
                
                val = self.visit(vd.value,(env, c[1], c[2], env_class, c[4], c[5]))
                if self.check_type_const(vd.constType, val) is False:
                    raise TypeMismatchInConstant(vd)

                #local_var.append(self.check_exist(local_var, vd.decl, "Constant"))
                local_var.append(kq)
                self.delete_symbol(env_class, vd.constant)
            else:
                local_var.append(self.check_exist(local_var, vd, "Variable"))
                self.delete_symbol(env_class, vd.variable)
        env_class += local_var

        # visit list(stmt) khoi visit block

        ch = False
        if type(ast.returnType) is ClassType:
            for x in env:
                if x.name == ast.returnType.classname.name:
                    ch = True
                    break

            if ch is False:
                raise Undeclared(Class(),ast.returnType.classname.name)

        list(map(lambda x: self.visit(x,(env, False, ast.returnType, env_class, id_parent, c[5])) if x else None, ast.body.stmt))
        ### Ok ### ver2

    def visitBlock(self, ast, c): # đã fix
        #decl:list(VarDecl)
        #stmt:list(Stmt)
        env = c[0].copy()
        env_class = c[3].copy()
        # Check decl
        para = []
        for p in ast.decl:
            if type(p) is ConstDecl:
                # para.append(self.check_exist(local_var, p.decl, "Constant"))
                # self.delete_symbol(env_class, p.decl.constant)
                kq = self.check_exist(para, p, "Constant")
                ### check type voi expr
                if p.value == None:
                    raise IllegalConstantExpression(None)
                val = self.visit(p.value,(env, c[1], c[2], env_class, c[4], c[5]))
                if self.check_type_const(p.constType, val) is False:
                    raise TypeMismatchInConstant(p)
                para.append(kq)
                self.delete_symbol(env_class, p.constant)
            else:
                para.append(self.check_exist(para, p, "Variable"))
                self.delete_symbol(env_class, p.variable)  # remove neu trung ko thi thoi
        env_class += para

        list(map(lambda x: self.visit(x,(env, c[1], c[2], env_class, c[4], c[5])), ast.stmt))


    def visitAssign(self, ast, c):
        #lhs:Expr
        #exp:Expr
        env = c[0].copy() if c[0] is not None else []

        le = self.visit(ast.lhs,(env, c[1], c[2], c[3], c[4], c[5]))
        ri = self.visit(ast.exp,(env, c[1], c[2], c[3], c[4], c[5]))

        
        if type(le) is Symbol:
            raise CannotAssignToConstant(ast)

        if self.Rule_assign(le,ri) is False:
            raise TypeMismatchInStatement(ast)

    def visitFieldAccess(self, ast, c):
        #obj:Expr
        #fieldname:Id
        env = c[0].copy()
        env_class = c[3].copy()
        id_parent = c[4]
        if type(ast.obj) is SelfLiteral:
            for x in env_class:
                if x.name == ast.fieldname.name and not(x.mtype is MType):
                    return x.mtype

            ### Duyet toi node cha
            if id_parent is not None:
                cc = self.check_access_field(ast, env, id_parent.name, c)
                if cc is False:
                    raise TypeMismatchInExpression(ast)
                else:
                    return cc
            else:
                raise Undeclared(Attribute(),ast.fieldname.name)


            raise TypeMismatchInExpression(ast)
        elif type(ast.obj) is Id: #e.a   Ne.a
            for i in env:
                if ast.obj.name == i.name:
                    ### Check tiep trong class
                    for ii in i.attribute:
                        if ii.name == ast.fieldname.name:
                            return ii.mtype

                    if i.parentname is not None:
                        cc = self.check_access_field(ast, env, i.parentname, c)
                        if cc is False:
                            raise TypeMismatchInExpression(ast)
                        else:
                            return cc
                    else:
                        raise Undeclared(Attribute(),ast.fieldname.name)

                    raise TypeMismatchInExpression(ast)

            ### Ko trung class => check env_class
            for i in env_class:
                if ast.obj.name == i.name:
                    raise TypeMismatchInExpression(ast)
            ### Ko trung gi het
            raise Undeclared(Class(),ast.obj.name)

        else:
            obj = self.visit(ast.obj, c)
            if type(obj) is not ClassType:
                raise TypeMismatchInExpression(ast)
            else:
                cc = self.check_access_field(ast, env, obj.classname.name, c)
                if cc is False:
                    raise TypeMismatchInExpression(ast)
                else:
                    return cc



    def visitNewExpr(self, ast, c):
        #classname:Id
        #param:list(Expr)   
        env = c[0].copy()
        env_class = c[3].copy()
        id_class = c[5]
        for x in env:
            if ast.classname.name == x.name:
            ## check method in x.method

                for xx in x.method:
                    if xx.name == "<init>":
                        ## check para
                        if len(ast.param) != len(xx.mtype.partype):
                            raise TypeMismatchInExpression(ast)
                        else:
                            for i in range(0,len(ast.param)):
                                ret = self.visit(ast.param[i],(env,c[1],c[2],env_class,c[4],c[5]))
                                if type(ret) is Symbol:
                                    ret = ret.mtype
                                if self.Rule_assign(xx.mtype.partype[i],ret) is False:
                                    raise TypeMismatchInExpression(ast)

                        return ClassType(ast.classname)

                ##  Neu ko co init thi check param
                if len(ast.param) == 0:
                    return ClassType(ast.classname)

                raise TypeMismatchInExpression(ast)

        self.check_exist(env_class, ast, "NewExpr")
        raise Undeclared(Class(),ast.classname.name)

    def visitCallStmt(self, ast, c):
        #obj: Expr 
        #method:Id
        #param:list(Expr)
        env = c[0].copy()
        env_class = c[3].copy()
        id_class = c[5]
        id_parent = c[4]

        if type(ast.obj) is SelfLiteral:
            ##
            for x in env:
                if id_class == x.name:
                    ## check method in x.method

                    for xx in x.method:
                        if xx.name == ast.method.name:

                            ## check return
                            if type(xx.mtype.rettype) is not VoidType:
                                raise TypeMismatchInStatement(ast)
                            ## check para

                            if len(ast.param) != len(xx.mtype.partype):
                                raise TypeMismatchInStatement(ast)
                            else:

                                for i in range(0,len(ast.param)):
                                    ret = self.visit(ast.param[i],(env,c[1],c[2],env_class,c[4],c[5]))
                                    if type(ret) is Symbol:
                                        ret = ret.mtype
                                    if self.Rule_assign(xx.mtype.partype[i],ret) is False:
                                        raise TypeMismatchInStatement(ast)

                            ## Check xong 
                            return xx.mtype.rettype

                    ### Neu khong co method nao trong this thi check toi parent##################
                    if x.parentname is not None:
                        if self.check_method_by_id_call(ast, env, x.parentname, c) is False:
                            raise TypeMismatchInStatement(ast)
                        else:
                            return VoidType()
                    else:
                        raise Undeclared(Method(),ast.method.name)


                    ## Neu khong co method can phai Undeclared(method)
                    raise TypeMismatchInStatement(ast)

            raise TypeMismatchInStatement(ast)
        elif type(ast.obj) is Id:
            

            for x in env:
                if ast.obj.name == x.name:
                    ## check method in x.method
                    
                    for xx in x.method:
                        if xx.name == ast.method.name:

                            ## check return
                            if type(xx.mtype.rettype) is not VoidType:
                                raise TypeMismatchInStatement(ast)
                            ## check para

                            if len(ast.param) != len(xx.mtype.partype):
                                raise TypeMismatchInStatement(ast)
                            else:

                                for i in range(0,len(ast.param)):
                                    ret = self.visit(ast.param[i],(env,c[1],c[2],env_class,c[4],c[5]))
                                    if type(ret) is Symbol:
                                        ret = ret.mtype
                                    if self.Rule_assign(xx.mtype.partype[i],ret) is False:
                                        raise TypeMismatchInStatement(ast)

                            ## Check xong 
                            return xx.mtype.rettype

                    ### Neu khong co method nao trong this thi check toi parent##################
                    if x.parentname is not None:
                        if self.check_method_by_id_call(ast, env, x.parentname, c) is False:
                            raise TypeMismatchInStatement(ast)
                        else:
                            return VoidType()
                    else:
                        raise Undeclared(Method(), ast.method.name)


                    ## Neu khong co method can phai Undeclared(method)
                raise TypeMismatchInStatement(ast)
            ## Check Undeclared tuong tu may cai kia
            self.check_exist(env_class, ast, "CallStmt")
            raise Undeclared(Class(),ast.obj.name)


    def visitCallExpr(self, ast, c):
        #obj: Expr 
        #method:Id
        #param:list(Expr)
        env = c[0].copy()
        env_class = c[3].copy()
        id_class = c[5]
        if type(ast.obj) is SelfLiteral:
            ##
            for x in env:
                if id_class == x.name:
                    ## check method in x.method

                    for xx in x.method:
                        if xx.name == ast.method.name:

                            ## check return
                            if type(xx.mtype.rettype) is VoidType:
                                raise TypeMismatchInExpression(ast)
                            ## check para

                            if len(ast.param) != len(xx.mtype.partype):
                                raise TypeMismatchInExpression(ast)
                            else:

                                for i in range(0,len(ast.param)):
                                    ret = self.visit(ast.param[i],(env,c[1],c[2],env_class,c[4],c[5]))
                                    if type(ret) is Symbol:
                                        ret = ret.mtype
                                    if self.Rule_assign(xx.mtype.partype[i],ret) is False:
                                        raise TypeMismatchInExpression(ast)

                            ## Check xong return
                            return xx.mtype.rettype

                    ### Neu khong co method nao trong this thi check toi parent##################
                    if x.parentname is not None:
                        cc = self.check_method_by_id_call_exp(ast, env, x.parentname, c)
                        if cc is False:
                            raise TypeMismatchInExpression(ast)
                        else:
                            return cc
                    else:
                        raise Undeclared(Method(), ast.method.name)


                    ## Neu khong co method can phai Undeclared(method)
                    raise TypeMismatchInExpression(ast)
                    
            return None
        elif type(ast.obj) is Id:

            for x in env:
                if ast.obj.name == x.name:
                    ## check method in x.method

                    for xx in x.method:
                        if xx.name == ast.method.name:

                            ## check return
                            if type(xx.mtype.rettype) is VoidType:
                                raise TypeMismatchInExpression(ast)
                            ## check para

                            if len(ast.param) != len(xx.mtype.partype):
                                raise TypeMismatchInExpression(ast)
                            else:

                                for i in range(0,len(ast.param)):
                                    ret = self.visit(ast.param[i],(env,c[1],c[2],env_class,c[4],c[5]))
                                    if type(ret) is Symbol:
                                        ret = ret.mtype
                                    if self.Rule_assign(xx.mtype.partype[i],ret) is False:
                                        raise TypeMismatchInExpression(ast)

                            ## Check xong 
                            return xx.mtype.rettype

                    ### Neu khong co method nao trong this thi check toi parent##################
                    if x.parentname is not None:
                        cc = self.check_method_by_id_call_exp(ast, env, x.parentname, c)
                        if cc is False:
                            raise TypeMismatchInExpression(ast)
                        else:
                            return cc
                    else:
                        raise Undeclared(Method(), ast.method.name)

                    ## Neu khong co method can phai Undeclared(method)
                    raise TypeMismatchInExpression(ast)
                    
            ## Check Undeclared tuong tu may cai kia
            self.check_exist(env_class, ast, "CallExpr")
            raise Undeclared(Class(),ast.obj.name)

    def visitArrayCell(self, ast, c):
        #arr:Expr
        #idx:Expr
        arr = self.visit(ast.arr,c)
        idx = self.visit(ast.idx,c)

        if type(arr) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        if type(idx) is not IntType:
            raise TypeMismatchInExpression(ast)

        return arr.eleType



    def visitIf(self, ast, c):
        #expr:Expr
        #thenStmt:Stmt
        #elseStmt:Stmt
        env = c[0].copy()
        if type(self.visit(ast.expr,(env, c[1], c[2], c[3], c[4], c[5]))) != BoolType:
            raise TypeMismatchInStatement(ast)

        self.visit(ast.thenStmt,(env, c[1], c[2], c[3], c[4], c[5])) if ast.thenStmt else None
        self.visit(ast.elseStmt,(env, c[1], c[2], c[3], c[4], c[5])) if ast.elseStmt else None

    def visitFor(self, ast, c): # OK
        #id:Id
        #expr1,expr2:Expr
        #loop:Stmt
        #up:Boolean #True => increase; False => decrease
        env = c[0].copy()
        scalar_var = self.visit(ast.id,(env, c[1], c[2], c[3], c[4], c[5]))
        if type(scalar_var) is Symbol:
            raise CannotAssignToConstant(ast) # Xem lai cho nay in ra cai gi

        exp1 = self.visit(ast.expr1,(env, c[1], c[2], c[3], c[4], c[5]))
        exp2 = self.visit(ast.expr2,(env, c[1], c[2], c[3], c[4], c[5]))

        if type(exp1) is Symbol:
            exp1 = exp1.mtype
        if type(exp2) is Symbol:
            exp2 = exp2.mtype

        if type(exp1) is not IntType or type(exp2) is not IntType or type(scalar_var) is not IntType:
            raise TypeMismatchInStatement(ast)

        self.visit(ast.loop,(env, True, c[2], c[3], c[4], c[5]))

    def visitBreak(self, ast, c): 
        if (c[1] == False):
            raise MustInLoop(ast)

    def visitContinue(self, ast, c):
        if (c[1] == False):
            raise MustInLoop(ast)

    def visitReturn(self, ast, c):
        #expr
        env = c[0].copy()
        re = c[2]
        if ast.expr is not None and type(re) is VoidType:
            raise TypeMismatchInStatement(ast)
        elif ast.expr is None and type(re) is VoidType: ## du phong
            return True
        elif self.check_return(re, self.visit(ast.expr,(env, c[1], c[2], c[3], c[4], c[5]))) is False:
            raise TypeMismatchInStatement(ast)

    def visitBinaryOp(self, ast, c):
        #op:string
        #left:Expr
        #right:Expr
        env = c[0].copy()
        l = self.visit(ast.left,(env, c[1], c[2], c[3], c[4], c[5]))
        r = self.visit(ast.right,(env, c[1], c[2], c[3], c[4], c[5]))
        op = ast.op
        if type(l) is Symbol:
            l = l.mtype
        if type(r) is Symbol:
            r = r.mtype

        if op == "+" or op == "-" or op == "*" or op == "/":
            if (type(l),type(r)) == (IntType,IntType):
                return FloatType() if op == "/" else IntType()
            elif (type(l),type(r)) == (FloatType,IntType) or\
            (type(l),type(r)) == (IntType,FloatType) or\
            (type(l),type(r)) == (FloatType,FloatType):
                return FloatType()

            else: raise TypeMismatchInExpression(ast)
        elif op == "\\" or op == "%":
            if (type(l),type(r)) == (IntType,IntType):
                return IntType()
            raise TypeMismatchInExpression(ast)

        elif op == "<" or op == "<=" or op == ">" or op ==">=" or op == "==" or op == "!=":
            if (type(l),type(r)) == (IntType,IntType)or\
            (type(l),type(r)) == (FloatType,IntType) or\
            (type(l),type(r)) == (IntType,FloatType) or\
            (type(l),type(r)) == (FloatType,FloatType) or\
            ((type(l),type(r)) == (BoolType,BoolType) and\
            (op == "==" or op == "!=")) :
                return BoolType()
            else: raise TypeMismatchInExpression(ast)

        elif op == "&&" or op == "||":
            if (type(l),type(r)) == (BoolType,BoolType):
                return BoolType()
            raise TypeMismatchInExpression(ast)

        elif op == "^":
            if (type(l),type(r)) == (StringType,StringType):
                return StringType()
            raise TypeMismatchInExpression(ast)

        else: raise TypeMismatchInExpression(ast)


    def visitUnaryOp(self, ast, c):
        #op:string
        #body:Expr
        env = c[0].copy()
        rtype = self.visit(ast.body,(env, c[1], c[2], c[3], c[4], c[5]))

        if type(rtype) is Symbol:
            rtype = rtype.mtype

        if ast.op == "+" or ast.op == "-":
            if type(rtype) is not FloatType and type(rtype) is not IntType:
                raise TypeMismatchInExpression(ast)
        elif ast.op == "!":
            if type(rtype) is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()

        return rtype


    def visitId(self, ast, c):
        env = c[0].copy()
        env_class = c[3].copy() if c[3] else []
        res = self.lookup(ast.name,env_class,lambda x: x.name)
        
        if res is None or type(res.mtype) is MType or type(res.mtype) is Class:
            raise Undeclared(Identifier(),ast.name)
        elif type(res) is Symbol:
            return res.mtype if res.value != 0 else res
        else:
            raise Undeclared(Identifier(),ast.name)
               

    def visitConstDecl(self, ast, c):
        ## Tra ve para ko bi trung
        ##### Const
        #constant:Id
        #constType: Type
        #value: Expr
        env = c[0].copy()
        env_class = c[3].copy()
        kq = self.check_exist(env_class, ast, "Constant")
        ### check type voi expr
        # if type(ast.Expr) is BinaryOp():
        #     raise IllegalArrayLiteral(ast)
        val = self.visit(ast.value,(env, c[1], c[2], env_class, c[4], c[5]))
        
        if self.check_type_const(ast.constType, val) is False:
            raise TypeMismatchInExpression(ast)
        return kq

    def visitVarDecl(self, ast, c):
    #   variable : Id
    #   varType : Type
    #   varInit : Expr = None
        env = c[0].copy()
        env_class = c[3].copy()
        env_class.append(self.check_exist(env_class, ast, "Variable"))       
        self.check_if_type_unknown(ast.varType,env)



    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitStringLiteral(self, ast, c):
        return StringType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitNullLiteral(self, ast, c):
        return VoidType()

    def visitSelfLiteral(self, ast, c):
        return ClassType('<init>')
    
    def visitArrayLiteral(self, ast, c):
        types = [IntLiteral, FloatLiteral, BooleanLiteral, StringLiteral]
        if any(list(map(lambda typ: all(list(map(lambda value: type(value) == typ, ast.value))), types))):
            return ArrayType(len(ast.value), self.visit(ast.value[0], None))
        
        raise IllegalArrayLiteral(ast)

        



    def visitIntType(self, ast, c):
        pass

    def visitFloatType(self, ast, c):
        pass

    def visitBoolType(self, ast, c):
        pass

    def visitStringType(self, ast, c):
        pass

    def visitArrayType(self, ast, c):
        
        return ast

    def visitClassType(self, ast, c):
        return ast

    def visitVoidType(self, ast, c):
        pass

