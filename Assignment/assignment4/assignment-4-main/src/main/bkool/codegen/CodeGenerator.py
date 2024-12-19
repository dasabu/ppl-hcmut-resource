from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *


class Utils:
    def lookup(self, name, lst, func):
        for x in lst:
            if name == func(x):
                return x
        return None

    def lookupField(self, name, lst, func):
        for x in lst:
            if name == func(x) and type(x.value) == CName:
                return x
        return None


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + self.name + "," + str(self.mtype) + ")"


from Emitter import Emitter


class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [
            Symbol("readInt", MType(list(), IntType()), CName(self.libName)),
            Symbol("writeInt", MType([IntType()], VoidType()), CName(self.libName)),
            Symbol("writeIntLn", MType([IntType()], VoidType()), CName(self.libName)),
            Symbol("readFloat", MType(list(), FloatType()), CName(self.libName)),
            Symbol("writeFloat", MType([FloatType()], VoidType()), CName(self.libName)),
            Symbol(
                "writeFloatLn", MType([FloatType()], VoidType()), CName(self.libName)
            ),
            Symbol("readBool", MType(list(), BoolType()), CName(self.libName)),
            Symbol("writeBool", MType([BoolType()], VoidType()), CName(self.libName)),
            Symbol("writeBoolLn", MType([BoolType()], VoidType()), CName(self.libName)),
            Symbol("readStr", MType(list(), StringType()), CName(self.libName)),
            Symbol("writeStr", MType([StringType()], VoidType()), CName(self.libName)),
            Symbol(
                "writeStrLn", MType([StringType()], VoidType()), CName(self.libName)
            ),
        ]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, path)
        gc.visit(ast, None)


class SubBody:
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym


class Access:
    def __init__(self, frame, sym, isLeft, isFirst=False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst
   

class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        self.value = value


class CName(Val):
    def __init__(self, value):
        self.value = value


class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.path = path

    def visitProgram(self, ast: Program, c):
        self.classEnv = []
        for x in ast.decl:
            self.classEnv += self.visit(x, 3)
        [self.visit(i, c) for i in ast.decl]
        return c

    def visitClassDecl(self, ast: ClassDecl, c):
        if c == 3:
            self.className = ast.classname.name
            self.emit = Emitter(self.path + "/" + self.className + ".j")
            classEnv = []
            for x in ast.memlist:
                classEnv.append(self.visit(x, 3))
            return classEnv
        self.className = ast.classname.name
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        if not ast.parentname:
            self.isHaveParent = False
            self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        else:
            self.isHaveParent = True
            self.emit.printout(
                self.emit.emitPROLOG(self.className, ast.parentname.name)
            )
        self.cast = ast
        isHaveCon = False
        for x in ast.memlist:
            self.visit(x, 0)
            if type(x) == MethodDecl and x.name.name == "<init>":
                isHaveCon = True
        # generate default constructor
        if not isHaveCon:
            self.genMETHOD(
                MethodDecl(Instance(), Id("<init>"), list(), None, Block([], [])),
                self.env + self.classEnv,
                Frame("<init>", VoidType()),
            )
        self.genMETHOD(
            MethodDecl(Static(), Id("<clinit>"), list(), None, Block([], [])),
            self.env + self.classEnv,
            Frame("<clinit>", VoidType()),
        )

        [
            self.visit(ele, SubBody(None, self.env + self.classEnv))
            for ele in ast.memlist
            if type(ele) == MethodDecl
        ]
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl: MethodDecl, o, frame):
        isInit = consdecl.returnType is None and consdecl.name.name == "<init>"
        isClassInit = consdecl.returnType is None and consdecl.name.name == "<clinit>"
        isMain = (
            consdecl.name.name == "main"
            and len(consdecl.param) == 0
            and type(consdecl.returnType) is VoidType
        )
        returnType = VoidType() if isInit or isClassInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        methodName = "<clinit>" if isClassInit else methodName

        intype = (
            [ArrayType(0, StringType())]
            if isMain
            else list(map(lambda x: x.varType, consdecl.param))
        )

        mtype = MType(intype, returnType)
        if isInit:
            self.contype = mtype
        body = consdecl.body

        isStatic = True if isinstance(consdecl.kind, Static) else False
        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, isStatic, frame))

        frame.enterScope(True)

        glenv = o
        lcenv = []
        e = SubBody(frame, lcenv)
        penv = []
        p = SubBody(frame, penv)
        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(
                self.emit.emitVAR(
                    frame.getNewIndex(),
                    "this",
                    ClassType(Id(self.className)),
                    frame.getStartLabel(),
                    frame.getEndLabel(),
                    frame,
                )
            )
            for x in consdecl.param:
                p = self.visit(x, p)
        elif isMain:
            self.emit.printout(
                self.emit.emitVAR(
                    frame.getNewIndex(),
                    "args",
                    ArrayType(0, StringType()),
                    frame.getStartLabel(),
                    frame.getEndLabel(),
                    frame,
                )
            )

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(
                self.emit.emitREADVAR("this", ClassType(Id(self.className)), 0, frame)
            )       
                 
            if not self.isHaveParent:
                self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
            else:
                self.emit.printout(self.emit.emitINVOKESPECIAL(frame, self.cast.parentname.name + "/<init>", self.contype))
                
            for x in self.cast.memlist:
                if type(x) == AttributeDecl and type(x.kind) == Instance:
                    if isinstance(x.decl, VarDecl) and x.decl.varInit:
                        self.emit.printout(
                            self.emit.emitREADVAR(
                                "this", ClassType(Id(self.className)), 0, frame
                            )
                        )
                        self.emit.printout(self.visit(x, frame))
        elif isClassInit:
            for x in self.cast.memlist:
                if type(x) == AttributeDecl and type(x.kind) == Static:
                    if isinstance(x.decl, VarDecl) and x.decl.varInit:
                        self.emit.printout(self.visit(x, frame))
        elif type(consdecl.kind) == Instance:
            self.emit.printout(
                self.emit.emitVAR(
                    frame.getNewIndex(),
                    "this",
                    ClassType(Id(self.className)),
                    frame.getStartLabel(),
                    frame.getEndLabel(),
                    frame,
                )
            )
            for x in consdecl.param:
                p = self.visit(x, p)
        elif type(consdecl.kind) == Static:
            for x in consdecl.param:
                p = self.visit(x, p)
        for x in body.decl:
            e = self.visit(x, SubBody(frame, p.sym + e.sym + glenv))

        list(
            map(
                lambda x: self.visit(x, SubBody(frame, p.sym + e.sym + glenv)),
                body.stmt,
            )
        )
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))

        frame.exitScope()

    def visitAttributeDecl(self, ast: AttributeDecl, o):
        self.isStatic = isinstance(ast.kind, Static)
        return self.visit(ast.decl, o)

    def visitVarDecl(self, ast: VarDecl, o):

        if o == 3:
            return Symbol(ast.variable.name, ast.varType, CName(self.className))
        elif o == 0:
            self.emit.printout(
                self.emit.emitATTRIBUTE(
                    ast.variable.name, ast.varType, False, None, self.isStatic
                )
            )
            return

        if isinstance(o, Frame):  # constructor and static init
            if ast.varInit:
                if self.isStatic:
                    self.emit.printout(self.visit(ast.varInit, o)[0])
                    return self.emit.emitPUTSTATIC(
                        self.className + "/" + ast.variable.name, ast.varType, o
                    )
                else:
                    self.emit.printout(self.visit(ast.varInit, o)[0])
                    return self.emit.emitPUTFIELD(
                        self.className + "/" + ast.variable.name, ast.varType, o
                    )
            else:
                return
        frame = o.frame

        env = o.sym
        idx = frame.getNewIndex()
        self.emit.printout(
            self.emit.emitVAR(
                idx,
                ast.variable.name,
                ast.varType,
                frame.getStartLabel(),
                frame.getEndLabel(),
                frame,
            )
        )
        if ast.varInit:
            self.emit.printout(self.visit(ast.varInit, o)[0])
            self.emit.printout(
                self.emit.emitWRITEVAR(ast.variable.name, ast.varType, idx, frame)
            )
        return SubBody(
            frame, [Symbol(ast.variable.name, ast.varType, Index(idx))] + env
        )

    def visitConstDecl(self, ast: ConstDecl, o):

        if o == 3:
            return Symbol(ast.constant.name, ast.constType, CName(self.className))

        elif o == 0:
            self.emit.printout(
                self.emit.emitATTRIBUTE(
                    ast.constant.name, ast.constType, False, None, self.isStatic
                )
            )
            return

        if isinstance(o, Frame):  # constructor and static init
            if ast.varInit:
                if self.isStatic:
                    self.emit.printout(self.visit(ast.varInit, o)[0])
                    return self.emit.emitPUTSTATIC(
                        self.className + "/" + ast.constant.name, ast.constType, o
                    )
                else:
                    self.emit.printout(self.visit(ast.varInit, o)[0])
                    return self.emit.emitPUTFIELD(
                        self.className + "/" + ast.constant.name, ast.constType, o
                    )
            else:
                return
        frame = o.frame

        env = o.sym
        idx = frame.getNewIndex()
        self.emit.printout(
            self.emit.emitVAR(
                idx,
                ast.constant.name,
                ast.constType,
                frame.getStartLabel(),
                frame.getEndLabel(),
                frame,
            )
        )
        if ast.value:
            self.emit.printout(self.visit(ast.value, o)[0])
            self.emit.printout(
                self.emit.emitWRITEVAR(ast.constant.name, ast.constType, idx, frame)
            )
        return SubBody(
            frame, [Symbol(ast.constant.name, ast.constType, Index(idx))] + env
        )

    def visitMethodDecl(self, ast: MethodDecl, o):

        if o == 0 or o == 3:
            return Symbol(
                ast.name.name,
                MType([x.varType for x in ast.param], ast.returnType),
                CName(self.className),
            )

        frame = Frame(ast.name.name, ast.returnType)
        self.genMETHOD(ast, o.sym, frame)
        return Symbol(
            ast.name.name,
            MType([x.varType for x in ast.param], ast.returnType),
            CName(self.className),
        )

    def visitCallStmt(self, ast: CallStmt, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        # sym = next(filter(lambda x: ast.method.name == x.name, nenv), None)
        lo = self.visit(
            ast.obj,
            Access(frame, o.sym, False, True),
        )[0]
        sym = self.lookupField(ast.method.name, o.sym, lambda x: x.name)
        cname = sym.value.value
        ctype = sym.mtype
        in_ = ("", list())
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        if lo:
            self.emit.printout(
            lo+in_[0]+self.emit.emitINVOKEVIRTUAL(cname + "/" + ast.method.name, ctype, frame)
            )
        else:
            self.emit.printout(
            in_[0]+self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame)
            )
            

    
    def visitCallExpr(self, ast: CallExpr, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        id_code= self.visit(ast.obj, Access(o.frame, o.sym, False))[0]
        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value
        ctype = sym.mtype
        in_ = ""
        for x in ast.param:
            str1 = self.visit(x, Access(frame, nenv, False, True))[0]
            in_ += str1
        if id_code:
            return (
            in_ + id_code + self.emit.emitINVOKEVIRTUAL(cname + "/" + ast.method.name, ctype, frame),
            ctype.rettype,
            )
        else:
            return (
            in_ + self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame),
            ctype.rettype,
            )
            
        
    def visitAssign(self, ast: Assign, o):
        frame = o.frame
        frame.push()
        frame.push()
        expCode, expType = self.visit(ast.exp, Access(frame, o.sym, False, True))
        lhsCode, lhsType = self.visit(ast.lhs, Access(frame, o.sym, True, True))
        if isinstance(lhsType, FloatType) and isinstance(expType, IntType):
            expCode = expCode + self.emit.emitI2F(frame)
        if isinstance(ast.lhs, ArrayCell):
            self.emit.printout(
                lhsCode
                + expCode
                + self.visit(ast.lhs, Access(frame, o.sym, True, False))
            )
        elif isinstance(ast.lhs, FieldAccess):
            self.emit.printout(
                lhsCode
                + expCode
                + self.visit(ast.lhs, Access(frame, o.sym, True, False))[0]
            )
        else:
            self.emit.printout(expCode + lhsCode)
        frame.pop()
        frame.pop()

    def visitIf(self, ast: If, o):
        # expr:Expr
        # thenStmt:list(Stmt)
        # elseStmt:list(Stmt)
        ctxt = o
        frame: Frame
        frame = ctxt.frame
        nenv = ctxt.sym
        exp, exptype = self.visit(ast.expr, Access(frame, nenv, False, True))
        label1 = frame.getNewLabel()
        self.emit.printout(exp)
        self.emit.printout(self.emit.emitIFFALSE(label1, frame))
        self.visit(ast.thenStmt, o)

        if ast.elseStmt:
            label2 = frame.getNewLabel()
            if type(frame.returnType) == VoidType:
                self.emit.printout(self.emit.emitGOTO(label2, frame))
        self.emit.printout(self.emit.emitLABEL(label1, frame))
        if ast.elseStmt:
            self.visit(ast.elseStmt, o)
            self.emit.printout(self.emit.emitLABEL(label2, frame))

    def visitFieldAccess(self, ast: FieldAccess, o):
        frame = o.frame
        lo = self.visit(
            ast.obj,
            Access(frame, o.sym, False, True),
        )[0]
        sym = self.lookupField(ast.fieldname.name, o.sym, lambda x: x.name)
        if isinstance(o, Access):
            if o.isLeft:
                if lo:
                    if o.isFirst:
                        rs = lo
                    else:
                        rs = self.emit.emitPUTFIELD(
                            sym.value.value + "/" + ast.fieldname.name, sym.mtype, frame
                        )
                    return (
                        rs,
                        sym.mtype,
                    )
                return (
                    self.emit.emitPUTSTATIC(
                        sym.value.value + "/" + sym.name, sym.mtype, frame
                    ),
                    sym.mtype,
                )
            else:
                if lo:
                    rs = lo + self.emit.emitGETFIELD(
                        sym.value.value + "/" + ast.fieldname.name, sym.mtype, frame
                    )
                    return (
                        rs,
                        sym.mtype,
                    )
                return (
                    self.emit.emitGETSTATIC(
                        sym.value.value + "/" + sym.name, sym.mtype, frame
                    ),
                    sym.mtype,
                )

    def visitId(self, ast: Id, o):
        frame = o.frame
        sym = self.lookup(ast.name, o.sym, lambda x: x.name)
        if sym:
            _type = sym.mtype
            if isinstance(o, Access) and o.isLeft:
                return (
                    self.emit.emitWRITEVAR(sym.name, _type, sym.value.value, frame),
                    sym.mtype,
                )
            else:
                return (
                    self.emit.emitREADVAR(sym.name, _type, sym.value.value, frame),
                    sym.mtype,
                )
        return None, None

    def visitReturn(self, ast: Return, o):
        ctxt = o
        frame = o.frame
        expcode, exptype = self.visit(ast.expr, Access(frame, o.sym, False, True))
        if type(frame.returnType) is FloatType and type(exptype) is IntType:
            self.emit.printout(expcode + self.emit.emitI2F(frame) + self.emit.emitRETURN(FloatType(), frame))
        else:
            self.emit.printout(expcode + self.emit.emitRETURN(exptype, frame))

    def visitIntLiteral(self, ast: IntLiteral, o):
        frame = o if isinstance(o, Frame) else o.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLiteral(self, ast, o):
        frame = o if isinstance(o, Frame) else o.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()

    def visitBooleanLiteral(self, ast, o):
        frame = o if isinstance(o, Frame) else o.frame
        return self.emit.emitPUSHICONST(str(ast.value).lower(), frame), BoolType()

    def visitStringLiteral(self, ast, o):
        frame = o if isinstance(o, Frame) else o.frame
        return self.emit.emitPUSHCONST(ast.value, StringType(), frame), StringType()

    def visitNewExpr(self, ast: NewExpr, o):
        frame = o if isinstance(o, Frame) else o.frame
        newO = self.emit.emitNEW(ast.classname.name, frame)
        dup = self.emit.emitDUP(frame)
        para = "".join([self.visit(para, frame)[0] for para in ast.param])

        invcon = self.emit.emitINVOKESPECIAL(
            frame, ast.classname.name + "/<init>", self.contype
        )
        return newO + dup + para + invcon , ClassType(ast.classname)

    # -------------------------Visit Binary, Unary------------------------------------

    
    
    def visitBinaryOp(self, ast: BinaryOp, o):
        ctxt = o
        frame = o if isinstance(o, Frame) else ctxt.frame
        leftcode, lefttype = self.visit(ast.left, o)
        rightcode, righttype = self.visit(ast.right, o)
        leftcode2 = (
            leftcode + self.emit.emitI2F(frame)
            if (type(lefttype) is IntType)
            else leftcode
        )
        rightcode2 = (
            rightcode + self.emit.emitI2F(frame)
            if (type(righttype) is IntType)
            else rightcode
        )
        if type(lefttype) == type(righttype):
            if ast.op in ["+", "-"]:
                return (
                    leftcode + rightcode + self.emit.emitADDOP(ast.op, lefttype, frame),
                    lefttype,
                )
            elif ast.op == "*":
                return (
                    leftcode + rightcode + self.emit.emitMULOP(ast.op, lefttype, frame),
                    lefttype,
                )
            elif ast.op == "/":
                return (
                    leftcode2
                    + rightcode2
                    + self.emit.emitMULOP(ast.op, FloatType(), frame),
                    FloatType(),
                )
            elif ast.op == "\\":
                return (
                    leftcode + rightcode + self.emit.emitMULOP(ast.op, lefttype, frame),
                    IntType(),
                )
            elif ast.op == "%":
                return leftcode + rightcode + self.emit.emitMOD(frame), IntType()
            # elif ast.op == "^":
            elif ast.op == "&&":
                return leftcode + rightcode + self.emit.emitANDOP(frame), BoolType()
            elif ast.op == "||":
                return leftcode + rightcode + self.emit.emitOROP(frame), BoolType()
            elif ast.op in ["==", "!=", ">", "<", ">=", "<="]:
                return (
                    leftcode + rightcode + self.emit.emitREOP(ast.op, lefttype, frame),
                    BoolType(),
                )
            elif ast.op == "^":
                return (
                    leftcode
                    + rightcode
                    + self.emit.emitINVOKEVIRTUAL(
                        "java/lang/String/concat",
                        MType([StringType()], StringType()),
                        frame,
                    ),
                    StringType(),
                )
        else:
            if ast.op in ["+", "-"]:
                return (
                    leftcode2
                    + rightcode2
                    + self.emit.emitADDOP(ast.op, FloatType(), frame),
                    FloatType(),
                )
            elif ast.op in ["*", "/"]:
                return (
                    leftcode2
                    + rightcode2
                    + self.emit.emitMULOP(ast.op, FloatType(), frame),
                    FloatType(),
                )
            elif ast.op in ["==", "!=", ">", "<", ">=", "<="]:
                return (
                    leftcode2
                    + rightcode2
                    + self.emit.emitREOP(ast.op, FloatType(), frame),
                    BoolType(),
                )

    def visitUnaryOp(self, ast, o):
        ctxt = o
        frame = o if isinstance(o, Frame) else ctxt.frame
        bodyCode, bodyType = self.visit(ast.body, o)
        if ast.op == "!":
            return bodyCode + self.emit.emitNOT(StringType(), frame), BoolType()
        elif ast.op == "-":
            return bodyCode + self.emit.emitNEGOP(bodyType, frame), bodyType
        else:
            return bodyCode, bodyType

    # ------------------------------Visit for----------------------------
    def visitFor(self, ast: For, o):
        ctxt = o
        frame = ctxt.frame

        nenv = ctxt.sym
        op = "<=" if ast.up else ">="
        op2 = "+" if ast.up else "-"
        # op3 = "-" if ast.up else "+"
        frame.enterLoop()
        label1 = frame.getContinueLabel()
        # raise Exception(label1)
        label2 = frame.getBreakLabel()
        self.visit(Assign(ast.id, ast.expr1), o)
        self.emit.printout(self.emit.emitLABEL(label1, frame))
        self.emit.printout(
            self.visit(
                BinaryOp(op, ast.id, ast.expr2), Access(frame, nenv, False, True)
            )[0]
        )

        self.emit.printout(self.emit.emitIFFALSE(label2, frame))
        self.visit(ast.loop, o)
        self.visit(Assign(ast.id, BinaryOp(op2, ast.id, IntLiteral(1))), o)

        self.emit.printout(self.emit.emitGOTO(label1, frame))
        self.emit.printout(self.emit.emitLABEL(label2, frame))
        frame.exitLoop()

    def visitBlock(self, ast: Block, o):
        frame = o.frame
        frame.enterScope(False)

        glenv = o.sym
        lcenv = []
        e = SubBody(frame, lcenv)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        for x in ast.decl:
            e = self.visit(x, e)

        list(
            map(
                lambda x: self.visit(x, SubBody(frame, e.sym + glenv)),
                ast.stmt,
            )
        )
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))

        frame.exitScope()

    def visitBreak(self, ast: Break, o):
        ctxt = o
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(), frame))

    def visitContinue(self, ast: Continue, o):
        ctxt = o
        frame: Frame
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getEndLabel(), frame))

    def visitArrayLiteral(self, ast: ArrayLiteral, o):
        if len(ast.value) == 0:
            return
        frame = o if isinstance(o, Frame) else o.frame

        typ = ""
        in_ = VoidType()
        if type(ast.value[0]) == IntLiteral:
            typ = "int"
            in_ = IntType()
        elif type(ast.value[0]) == FloatLiteral:
            typ = "float"
            in_ = FloatType()
        elif type(ast.value[0]) == StringLiteral:
            typ = "java/lang/String"
            in_ = StringType()
        elif type(ast.value[0]) == BooleanLiteral:
            typ = "boolean"
            in_ = BoolType()

        rs = ""
        rs += self.emit.emitPUSHICONST(len(ast.value), frame)
        if typ == "java/lang/String":
            rs += self.emit.emitANEWARRAY(typ, frame)
        else:
            rs += self.emit.emitNEWARRAY(typ, frame)
        for i in range(len(ast.value)):
            rs += self.emit.emitDUP(frame)
            rs += self.emit.emitPUSHICONST(i, frame)
            rs += self.visit(ast.value[i], o)[0]
            rs += self.emit.emitASTORE(in_, frame)

        return rs, ArrayType(len(ast.value), in_)

    def visitArrayCell(self, ast: ArrayCell, o):
        # arr:Expr
        # idx:Expr

        frame = o if isinstance(o, Frame) else o.frame
        arr, arrtype = self.visit(ast.arr, Access(frame, o.sym, False, True))
        idx, idxtype = self.visit(ast.idx, Access(frame, o.sym, False, True))

        if isinstance(o, Access) and o.isLeft and o.isFirst:
            return arr + idx, arrtype.eleType
        elif isinstance(o, Access) and o.isLeft and not o.isFirst:
            return self.emit.emitASTORE(arrtype.eleType, frame)
        else:
            return (
                arr + idx + self.emit.emitALOAD(arrtype.eleType, frame),
                arrtype.eleType,
            )

    def visitSelfLiteral(self, ast, o):
        frame = o.frame
        if isinstance(o, Access) and o.isLeft:
            return (
                self.emit.emitWRITEVAR("", ClassType(Id(self.className)), 0, frame),
                ClassType(Id(self.className)),
            )
        else:
            return (
                self.emit.emitREADVAR("", ClassType(Id(self.className)), 0, frame),
                ClassType(Id(self.className)),
            )