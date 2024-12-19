from Visitor import Visitor
from AST import *
from StaticError import *
from main.bkool.utils.AST import Type, VarDecl


class FunctionPrototype:
    # FunctionPrototype contains info function prototype
    # FunctionPrototype(Id name, Id type/return type,
    #       params = List of ParamPrototype, inherit = name of father func)
    def __init__(self, name_: str, type_: Type, params: list or None, inherit: str or None):
        self.name_ = name_
        self.type_ = type_
        self.inherit = inherit
        self.params = params


class ParamPrototype:
    def __init__(self, name_: str, type_: Type, out_: bool, inherit_: bool):
        self.name_ = name_
        self.type_ = type_
        self.out_ = out_
        self.inherit_ = inherit_


class VarPrototype:
    def __init__(self, name_: str, type_: Type):
        self.name_ = name_
        self.type_ = type_


class FindBreak_Continue:
    def __init__(self, ctx):
        self.ctx = ctx

    def visit(self, ast, param):
        return ast.accept(self, param)

    def find(self):
        # Return ctx if there is a break/continue stmt in stmt
        flag = None
        flag = self.visit(self.ctx, flag)
        return flag

    def visitBlockStmt(self, ctx: BlockStmt, o: object):
        # body: List[Stmt or VarDecl]
        # return list of stmt, not vardecl
        for stmt in ctx.body:
            if type(stmt) in [BreakStmt, ContinueStmt]:
                o = stmt
                break
            else:
                o = self.visit(stmt, o)
                if type(o) in [BreakStmt, ContinueStmt] \
                        and type(stmt) not in [ForStmt, WhileStmt, DoWhileStmt]:
                    return o
        return o

    def visitIfStmt(self, ctx: IfStmt, o: object):
        # cond: Expr, tstmt: Stmt, fstmt: Stmt or None = None
        if type(ctx.tstmt) in [BreakStmt, ContinueStmt]:
            o = ctx.tstmt
        elif type(ctx.fstmt) in [BreakStmt, ContinueStmt]:
            o = ctx.fstmt
        elif type(ctx.tstmt) in [BlockStmt, IfStmt]:
            o = self.visit(ctx.tstmt, o)
        elif type(ctx.fstmt) in [BlockStmt, IfStmt]:
            o = self.visit(ctx.fstmt, o)

        return o

    def visitForStmt(self, ctx: ForStmt, o: object):
        return None

    def visitWhileStmt(self, ctx: WhileStmt, o: object):
        return None

    def visitDoWhileStmt(self, ctx: DoWhileStmt, o: object):
        return None

    def visitVarDecl(self, ctx, o):
        return None

    def visitCallStmt(self, ctx, o):
        return None

    def visitAssignStmt(self, ctx, o):
        return None

    def visitReturnStmt(self, ctx, o):
        return None

    def visitBreakStmt(self, ctx: BreakStmt, o: object):
        return ctx

    def visitContinueStmt(self, ctx: ContinueStmt, o: object):
        return ctx


class FindReturnStmt:
    def __init__(self, ctx):
        self.ctx = ctx

    def visit(self, ast, param):
        return ast.accept(self, param)

    def find(self):
        # Return ctx if there is a break/continue stmt in stmt
        flag = []
        flag = self.visit(self.ctx, flag)
        return flag

    def visitBlockStmt(self, ctx: BlockStmt, o: object):
        # body: List[Stmt or VarDecl]
        for stmt in ctx.body:
            if type(stmt) is ReturnStmt:
                o += [stmt]
            else:
                o = self.visit(stmt, o)

        return o

    def visitIfStmt(self, ctx: IfStmt, o: object):
        # cond: Expr, tstmt: Stmt, fstmt: Stmt or None = None
        o = self.visit(ctx.tstmt, o)
        if ctx.fstmt is not None:
            o = self.visit(ctx.fstmt, o)

        return o

    def visitForStmt(self, ctx: ForStmt, o: object):
        o = self.visit(ctx.stmt, o)
        return o

    def visitWhileStmt(self, ctx: WhileStmt, o: object):
        o = self.visit(ctx.stmt, o)
        return o

    def visitDoWhileStmt(self, ctx: DoWhileStmt, o: object):
        o = self.visit(ctx.stmt, o)
        return o

    def visitVarDecl(self, ctx, o):
        return o

    def visitCallStmt(self, ctx, o):
        return o

    def visitAssignStmt(self, ctx, o):
        return o

    def visitReturnStmt(self, ctx, o):
        return o

    def visitBreakStmt(self, ctx: BreakStmt, o: object):
        return o

    def visitContinueStmt(self, ctx: ContinueStmt, o: object):
        return o


class PreTraversal(Visitor):
    # PreTraversal has a mission that collect all function prototype and global vardecl
    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visitProgram(self.ast, None)

    def visitProgram(self, ctx: Program, o: object):
        o = []
        for decl in ctx.decls:
            o = self.visit(decl, o)
        return o

    def visitVarDecl(self, ctx: VarDecl, o: object):
        # name: str, typ: Type, init: Expr or None = None
        for decl in o:
            if ctx.name == decl.name_:
                raise Redeclared(Variable(), ctx.name)
        o += [VarPrototype(ctx.name, ctx.typ)]
        return o

    def visitParamDecl(self, ctx: ParamDecl, o: object):
        # name: str, typ: Type, out: bool = False, inherit: bool = False
        # It's useless
        return o

    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt
        for decl in o:
            if ctx.name == decl.name_:
                raise Redeclared(Function(), ctx.name)

        if len(ctx.params) == 0:
            paramdecl = []
        else:
            paramdecl = []
            for pdecl in ctx.params:
                paramdecl += [ParamPrototype(pdecl.name,
                                             pdecl.typ, pdecl.out, pdecl.inherit)]

        o += [FunctionPrototype(ctx.name, ctx.return_type,
                                paramdecl, ctx.inherit)]
        return o


class StaticChecker(Visitor):
    declaredName = ['readInteger', 'readFloat', 'readBoolean', 'readString',
                    'printInteger', 'printFloat', 'printBoolean', 'printString',
                    'super', 'preventDefault']

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visitProgram(self.ast, None)

    def visitProgram(self, ctx: Program, o: object):
        o = PreTraversal(self.ast).check()
        # In PreTraversal, we get info of all global decl and store in o
        funcdecls = []
        for fdecl in o:
            funcdecls += [fdecl]

        # env[0] = local env, env[-1] = global env, else is nonlocal
        env = [[]] + [o]
        for decl in ctx.decls:
            env = self.visit(decl, env)

        # Check for no void main() in program
        hasEntryPoint = False
        for fdecl in funcdecls:
            if (fdecl.name_ == 'main' and len(fdecl.params) == 0 and type(fdecl.type_) == VoidType):
                hasEntryPoint = True

        if not hasEntryPoint:
            raise NoEntryPoint()

    def visitVarDecl(self, ctx: VarDecl, o: object):
        # name: str, typ: Type, init: Expr or None = None

        # Check redeclared if redeclared in env of vardecl
        for decl in o[0]:
            if ctx.name == decl.name_:
                raise Redeclared(Variable(), ctx.name)
        varinfo = VarPrototype(ctx.name, ctx.typ)
        # Raise Invalid: <variable name> if AutoType and init is None
        if type(varinfo.type_) is AutoType:
            if ctx.init is None:
                raise Invalid(Variable(), ctx.name)
            else:
                varinfo.type_ = self.visit(ctx.init, o)

        init_type = self.visit(ctx.init, o) if ctx.init is not None else None
        if type(varinfo.type_) is FloatType and type(init_type) is IntegerType:
            varinfo.type_ = FloatType()
        elif type(varinfo.type_) is ArrayType and type(init_type) is ArrayType:
            decl_dimen = list(map(lambda x: int(x), varinfo.type_.dimensions))
            init_dimen = init_type.dimensions
            decl_atomicType = varinfo.type_.typ
            init_atomicType = init_type.typ
            if len(decl_dimen) != len(init_dimen):
                raise TypeMismatchInVarDecl(ctx)
            else:
                for i in range(len(decl_dimen)):
                    if type(decl_dimen[i]) is IntegerType:
                        continue
                    elif decl_dimen[i] == init_dimen[i]:
                        continue
                    else:
                        raise TypeMismatchInVarDecl(ctx)
            if type(decl_atomicType) == AutoType:
                decl_atomicType = init_atomicType
                varinfo.type_.typ = init_atomicType
            if type(decl_atomicType) != type(init_atomicType):
                raise TypeMismatchInVarDecl(ctx)
        elif type(init_type) == AutoType:
            if type(ctx.init) in [FuncCall, CallStmt]:
                self.infer(ctx.init, o, ctx.typ)
            if type(ctx.init) is UnExpr:
                if type(ctx.init.val) in [FuncCall, CallStmt]:
                    self.infer(ctx.init.val, o, ctx.typ)
        elif type(varinfo.type_) is not type(init_type) and init_type is not None:
            raise TypeMismatchInVarDecl(ctx)
        # varinfo.type_ = init_type if init_type is not None else varinfo.type_
        o[0] += [varinfo]

        return o

    def visitParamDecl(self, ctx: ParamDecl, o: object):
        # name: str, typ: Type, out: bool = False, inherit: bool = False
        # It's useless
        return ctx.name

    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt
        # Check redeclared func
        for decl in o[0]:
            if ctx.name == decl.name_:
                raise Redeclared(Function(), ctx.name)
        childParam = []

        env = [[]] + o
        # Check redeclared params
        if len(ctx.params) > 0:
            childParamName = [cparam.name for cparam in ctx.params]
        else:
            childParamName = []
        childParam = [ParamPrototype(
            x.name, x.typ, x.out, x.inherit) for x in ctx.params]
        for i in range(len(childParamName) - 1):
            for j in range(i+1, len(childParamName)):
                if childParamName[i] == childParamName[j]:
                    raise Redeclared(Parameter(), childParamName[i])
        # If this is child function
        if ctx.inherit is not None:
            # If child function inherit non-declared father function, raise Undeclared Function
            hasDeclared = False
            for fdecl in env[-1]:
                if fdecl.name_ == ctx.inherit:
                    hasDeclared = True
                    break
            if not hasDeclared:
                raise Undeclared(Function(), ctx.inherit)

            # Else, get father params
            fatherParams = list(filter(lambda x: x.name_ == ctx.inherit and type(
                x) == FunctionPrototype, env[-1]))[0].params
            # Get father params with inherit keyword
            fatherParams = list(
                filter(lambda x: x.inherit_ == True, fatherParams))

            # If name inherit param appear in child param decl, raise Invalid(Param(), name)
            if fatherParams is not None:
                for fatherParam in fatherParams:
                    if fatherParam.inherit_ == True:
                        if fatherParam.name_ in childParamName:
                            raise Invalid(Parameter(), fatherParam.name_)

            # Check first statement in body of childfunction
            if len(ctx.body.body) > 0:
                firstStmt = ctx.body.body[0]
            else:
                firstStmt = None
            # If len(fatherFunc.params == 0) then firstStmt must be preventDefault()
            if type(firstStmt) not in [FuncCall, CallStmt]:
                raise InvalidStatementInFunction(ctx.name)
            if fatherParams is None:
                if firstStmt.name != "preventDefault":
                    raise InvalidStatementInFunction(ctx.name)
            else:
                # if 1st stmt is not super, prevent, so invalidstmt in func
                if firstStmt.name not in ["super", 'preventDefault']:
                    raise InvalidStatementInFunction(ctx.name)
                elif firstStmt.name == 'super':
                    # Check args binding of super()
                    if len(firstStmt.args) > len(fatherParams):
                        raise TypeMismatchInExpression(
                            firstStmt.args[len(fatherParams)])
                    elif len(firstStmt.args) < len(fatherParams):
                        raise TypeMismatchInExpression(None)
                    else:
                        paramPairs = list(map(lambda x, y: (type(self.visit(
                            x, None)), y), firstStmt.args, fatherParams))
                        for pair in paramPairs:
                            flag = pair[0] == type(pair[1].type_) or \
                                (pair[0] == FloatType and type(
                                    pair[1].type_) == IntegerType)
                            if not flag:
                                raise TypeMismatchInExpression(pair[1])
                            else:
                                childParam += [pair[1]]
                elif firstStmt.name == 'preventDefault':
                    # Check args binding of prevent
                    if len(firstStmt.args) > 0:
                        raise TypeMismatchInStatement(firstStmt)
                    # Cause preventDefault() is deactivate inherit,
                    # so we don't inherit param in parent func
                    childParam = [ParamPrototype(
                        x.name, x.typ, x.out, x.inherit) for x in ctx.params]

        # After all, we append childparam as local VarPrototype of childFunction
        env[0] += childParam

        self.visit(ctx.body, env)

        # Check if there is a Continue/Break stmt in directly/ indirectly blockstmt
        found = FindBreak_Continue(ctx.body).find()
        if found is not None:
            raise MustInLoop(found)

        # Find return stmt
        indoorReturnStmt = []  # ReturnStmt that lay in another stmt else this blockstmt

        outdoorReturnStmt = []  # ReturnStmt that lay directly in this blockstmt
        hasReturnStmts = []
        returnTyp = None
        func_info = None
        for stmt in ctx.body.body:
            if type(stmt) is ReturnStmt:
                returnTyp = self.visit(stmt, env)
                outdoorReturnStmt = [stmt]
                # We only need to check first outdoor returnstmt,
                # another with same kind but lay after the first is pass by
                break
        for stmt in ctx.body.body:
            if type(stmt) is not ReturnStmt:
                indoorReturnStmt = FindReturnStmt(stmt).find()
                # Find all returnstmt that lay in another stmt that is not this blockstmt
                # Each of them must be check type

        # This procedure to get 2 kinds of returnstmt in this blockstmt, store in hasReturnStmts.
        # returnTyp is the type of firstly seen returnstmt
        if len(outdoorReturnStmt) == 0:
            if len(indoorReturnStmt) == 0:
                hasReturnStmts = []
            else:
                returnTyp = self.visit(indoorReturnStmt[0], env)
                hasReturnStmts = indoorReturnStmt
        else:
            if len(indoorReturnStmt) == 0:
                hasReturnStmts = outdoorReturnStmt
            else:
                firstReturnStmt = FindReturnStmt(ctx.body).find()[0]
                returnTyp = self.visit(firstReturnStmt, env)
                hasReturnStmts = outdoorReturnStmt + indoorReturnStmt

        # Find func_info in env[-1]
        for decl in env[-1]:
            if decl.name_ == ctx.name:
                func_info = decl

        if len(hasReturnStmts) > 0:
            for hasReturnStmt in hasReturnStmts:
                # Type inferring
                if hasReturnStmt.expr is None:
                    if type(func_info.type_) == AutoType:
                        func_info.type_ = VoidType()
                    if type(func_info.type_) != VoidType:
                        raise TypeMismatchInStatement(hasReturnStmt)
                elif type(hasReturnStmt.expr) in [FuncCall, CallStmt]:
                    if type(returnTyp) is AutoType:
                        # Then infer type of Id in expr with return type of function
                        for envi in env:
                            for decl in envi:
                                # return expr is AutoType, so it is Id, or FuncCall/CallStmt,
                                # all of them have .name field
                                if decl.name_ == hasReturnStmt.expr.name and type(decl.type_) == AutoType:
                                    decl.type_ = func_info.type_
                    # If type of function is Auto and returntype is not None, then infer its type to returntype
                    if type(func_info.type_) == AutoType:
                        func_info.type_ = returnTyp
                elif type(hasReturnStmt.expr) is Id:
                    if type(func_info.type_) == AutoType:
                        func_info.type_ = returnTyp
                else:
                    # return expr is Literal/binexpr/unexpr => value
                    if type(func_info.type_) == AutoType:
                        func_info.type_ = returnTyp

                # Type checking
                if type(self.visit(hasReturnStmt, env)) is IntegerType and type(func_info.type_) not in [FloatType, IntegerType]:
                    # Cause it implicit coercion rhs as hasReturnStmt.expr, lhs as function type
                    raise TypeMismatchInStatement(hasReturnStmt)
                if type(self.visit(hasReturnStmt, env)) != type(func_info.type_):
                    raise TypeMismatchInStatement(hasReturnStmt)

        return o

    def visitAssignStmt(self, ctx: AssignStmt, o: object):
        # lhs: LHS (Id or ArrayCell), rhs: Expr
        left = self.visit(ctx.lhs, o)
        right = self.visit(ctx.rhs, o)
        if type(left) == AutoType:
            for decl in o[-1]:
                if left.name == decl.name_:
                    decl.type_ = right
        if type(right) == AutoType:
            for decl in o[-1]:
                if left.name == decl.name_:
                    decl.type_ = left

        left = self.visit(ctx.lhs, o)
        right = self.visit(ctx.rhs, o)

        if type(left) in [VoidType, ArrayType]:
            raise TypeMismatchInStatement(ctx)
        isCompatible = False
        if (type(left) == FloatType and type(right) in [IntegerType, FloatType]) \
                or (type(left) == type(right)):
            isCompatible = True

        if not isCompatible:
            raise TypeMismatchInStatement(ctx)

    def visitBlockStmt(self, ctx: BlockStmt, o: object):
        # body: List[Stmt or VarDecl]

        if len(ctx.body) > 0:
            for stmt in ctx.body:
                if type(stmt) is not ReturnStmt:
                    # Cause we check returnstmt in funcdecl
                    self.visit(stmt, o)

    def visitIfStmt(self, ctx: IfStmt, o: object):
        # cond: Expr, tstmt: Stmt, fstmt: Stmt or None = None
        if type(self.visit(ctx.cond, o)) != BooleanType:
            raise TypeMismatchInStatement(ctx)
        if type(ctx.tstmt) is BlockStmt:
            env = [[]] + o
            self.visit(ctx.tstmt, env)
        else:
            self.visit(ctx.tstmt, o)
        if ctx.fstmt is not None:
            if type(ctx.fstmt) is BlockStmt:
                env = [[]] + o
                self.visit(ctx.fstmt, env)
            else:
                self.visit(ctx.fstmt, o)

    def visitForStmt(self, ctx: ForStmt, o: object):
        # init: AssignStmt, cond: Expr, upd: Expr, stmt: Stmt
        isCompatible = True
        if type(self.visit(ctx.cond, o)) != BooleanType:
            isCompatible = False
        if type(self.visit(Id(ctx.init.lhs.name), o)) != IntegerType:
            isCompatible = False
        if type(self.visit(ctx.upd, o)) != IntegerType:
            isCompatible = False
        if not isCompatible:
            raise TypeMismatchInStatement(ctx)
        if type(ctx.stmt) is BlockStmt:
            env = [[]] + o
            self.visit(ctx.stmt, env)
        else:
            self.visit(ctx.stmt, o)

    def visitWhileStmt(self, ctx: WhileStmt, o: object):
        # cond: Expr, stmt: Stmt
        if type(self.visit(ctx.cond, o)) != BooleanType:
            raise TypeMismatchInStatement(ctx)
        if type(ctx.stmt) is BlockStmt:
            env = [[]] + o
            self.visit(ctx.stmt, env)
        else:
            self.visit(ctx.stmt, o)

    def visitDoWhileStmt(self, ctx: DoWhileStmt, o: object):
        # cond: Expr, stmt: BlockStmt
        if type(self.visit(ctx.cond, o)) != BooleanType:
            raise TypeMismatchInStatement(ctx)

        env = [[]] + o
        self.visit(ctx.stmt, env)

    def visitBreakStmt(self, ctx: BreakStmt, o: object): pass

    def visitContinueStmt(self, ctx: ContinueStmt, o: object): pass

    def visitReturnStmt(self, ctx: ReturnStmt, o: object):
        # expr: Expr or None = None
        return self.visit(ctx.expr, o) if ctx.expr is not None else VoidType()

    def visitCallStmt(self, ctx: CallStmt, o: object):
        # name: str, args: List[Expr]
        # Raise Undeclared if Function not declared in o[-1]
        isDeclared = False
        func_info = None
        for func_info in o[-1]:
            if type(func_info) == FunctionPrototype:
                if func_info.name_ == ctx.name:
                    isDeclared = True
                    break
        if ctx.name in self.declaredName:
            isDeclared = True

        if not isDeclared:
            raise Undeclared(Function(), ctx.name)

        if ctx.name in ['readInteger', 'readFloat', 'readBoolean', 'readString']:
            raise TypeMismatchInStatement(ctx)
        elif ctx.name == 'preventDefault':
            if len(ctx.args) > 0:
                raise TypeMismatchInExpression(ctx)
        elif ctx.name in ['printInteger', 'printFloat', 'printBoolean', 'printString']:
            if len(ctx.args) != 1:
                raise TypeMismatchInExpression(ctx)
            arguTyp = self.visit(ctx.args[0], o)
            if ctx.name == 'printInteger':
                if type(arguTyp) == AutoType:
                    self.infer(ctx.args[0], o, IntegerType())
                elif type(arguTyp) != IntegerType:
                    raise TypeMismatchInExpression(ctx)
            if ctx.name == 'printFloat':
                if type(arguTyp) == AutoType:
                    self.infer(ctx.args[0], o, FloatType())
                elif type(arguTyp) != FloatType:
                    raise TypeMismatchInExpression(ctx)
            if ctx.name == 'printBoolean':
                if type(arguTyp) == AutoType:
                    self.infer(ctx.args[0], o, BooleanType())
                elif type(arguTyp) != BooleanType:
                    raise TypeMismatchInExpression(ctx)
            if ctx.name == 'printString':
                if type(arguTyp) == AutoType:
                    self.infer(ctx.args[0], o, StringType())
                elif type(arguTyp) != StringType:
                    raise TypeMismatchInExpression(ctx)
            # To do, check type binding and coercion of dafault function
        elif ctx.name == 'super':
            pass
        else:
            if len(ctx.args) != len(func_info.params):
                raise TypeMismatchInStatement(ctx)
            else:
                for i in range(len(ctx.args)):
                    argTyp = type(self.visit(ctx.args[i], o))
                    paramTyp = type(func_info.params[i].type_)
                    if argTyp == AutoType:
                        argTyp = paramTyp
                    if paramTyp == AutoType:
                        func_info.type_ = argTyp
                        paramTyp = argTyp
                    canCoerrion = (
                        argTyp == IntegerType and paramTyp == FloatType)
                    if not (canCoerrion or paramTyp == argTyp):
                        raise TypeMismatchInStatement(ctx)
        return VoidType()

    def visitFuncCall(self, ctx: FuncCall, o: object):
        # name: str, args: List[Expr]
        # Raise Undeclared if Function not declared in o[-1]
        isDeclared = False
        func_info = None
        returnTyp = None
        for func_info in o[-1]:
            if func_info.name_ == ctx.name:
                isDeclared = True
                returnTyp = func_info.type_
                break
        if ctx.name in self.declaredName:
            isDeclared = True
            returnTyp = VoidType()

        if not isDeclared:
            raise Undeclared(Function(), ctx.name)

        if ctx.name in ['readInteger', 'readFloat', 'readBoolean', 'readString']:
            if len(ctx.args) > 0:
                raise TypeMismatchInExpression(ctx)
            if ctx.name == 'readInteger':
                returnTyp = IntegerType()
            if ctx.name == 'readFloat':
                returnTyp = FloatType()
            if ctx.name == 'readBoolean':
                returnTyp = BooleanType()
            if ctx.name == 'readString':
                returnTyp = StringType()
        elif ctx.name in ['printInteger', 'printFloat', 'printBoolean', 'printString', 'super', 'preventDefault']:
            raise TypeMismatchInExpression(ctx)
        elif len(ctx.args) != len(func_info.params):
            raise TypeMismatchInExpression(ctx)
        else:
            for i in range(len(ctx.args)):
                argTyp = self.visit(ctx.args[i], o)
                paramTyp = func_info.params[i].type_
                if type(argTyp) == AutoType:
                    argTyp = paramTyp
                if type(paramTyp) == AutoType:
                    func_info.type_ = argTyp
                    paramTyp = argTyp
                canCoerrion = (
                    type(argTyp) == IntegerType and type(paramTyp) == FloatType)
                isSame = False
                if type(paramTyp) == type(argTyp):
                    if type(paramTyp) == ArrayType:
                        paramTyp.dimensions = list(
                            map(lambda x: int(x), paramTyp.dimensions))
                        argTyp.dimensions = list(
                            map(lambda x: int(x), argTyp.dimensions))
                        canCoerrion = type(argTyp) == IntegerType and type(
                            paramTyp) == FloatType
                        if paramTyp.dimensions == argTyp.dimensions and (type(paramTyp) == type(paramTyp) or canCoerrion):
                            isSame = True
                    else:
                        isSame = True
                if not (canCoerrion or isSame):
                    raise TypeMismatchInExpression(ctx)
        if type(returnTyp) is VoidType:
            raise TypeMismatchInExpression(ctx)
        return returnTyp

    def infer(self, ctx, o, targetType):
        for env in o:
            for decl in env:
                if decl.name_ == ctx.name and type(decl.type_) == AutoType:
                    decl.type_ = targetType

    def visitBinExpr(self, ctx: BinExpr, o: object):
        # op: str, left: Expr, right: Expr
        exp_1 = self.visit(ctx.left, o)
        exp_2 = self.visit(ctx.right, o)
        # Infertype
        # Check compatible type
        isCompatible = False
        returnTyp = BooleanType()
        if type(exp_1) == type(exp_2):
            isCompatible = True
            returnTyp = exp_1
        if ctx.op in ['+', '-', '*', '/']:
            if type(exp_1) == AutoType:
                self.infer(ctx.left, o, exp_2)
            if type(exp_2) == AutoType:
                self.infer(ctx.right, o, exp_1)
            exp_1 = self.visit(ctx.left, o)
            exp_2 = self.visit(ctx.right, o)
            if type(exp_1) == IntegerType and type(exp_2) == IntegerType:
                returnTyp = FloatType() if ctx.op == '/' else IntegerType()
                isCompatible = True
            elif type(exp_1) in [IntegerType, FloatType] and type(exp_2) in [IntegerType, FloatType]:
                returnTyp = FloatType()
                isCompatible = True

        if ctx.op == '%':
            if type(exp_1) == AutoType:
                self.infer(ctx.left, o, IntegerType())
            if type(exp_2) == AutoType:
                self.infer(ctx.right, o, IntegerType())
            exp_1 = self.visit(ctx.left, o)
            exp_2 = self.visit(ctx.right, o)
            if type(exp_1) == IntegerType and type(exp_2) == IntegerType:
                returnTyp = IntegerType()
                isCompatible = True

        if ctx.op in ['&&', '||']:
            if type(exp_1) == AutoType:
                self.infer(ctx.left, o, exp_2)
            if type(exp_2) == AutoType:
                self.infer(ctx.right, o, exp_1)
            exp_1 = self.visit(ctx.left, o)
            exp_2 = self.visit(ctx.right, o)
            if type(exp_1) in [BooleanType, IntegerType] and type(exp_2) in [BooleanType, IntegerType]:
                returnTyp = BooleanType()
                isCompatible = True

        if ctx.op == '::':
            if type(exp_1) == AutoType:
                self.infer(ctx.left, o, StringType())
            if type(exp_2) == AutoType:
                self.infer(ctx.right, o, StringType())
            exp_1 = self.visit(ctx.left, o)
            exp_2 = self.visit(ctx.right, o)
            if type(exp_1) == StringType and type(exp_2) == StringType:
                returnTyp = StringType()
                isCompatible = True

        if ctx.op in ['>', '>=', '<', '<=', '==', '!=']:
            if type(exp_1) == AutoType:
                self.infer(ctx.left, o, exp_2)
            if type(exp_2) == AutoType:
                self.infer(ctx.right, o, exp_1)
            exp_1 = self.visit(ctx.left, o)
            exp_2 = self.visit(ctx.right, o)
            if type(exp_1) in [IntegerType, FloatType] and type(exp_2) in [IntegerType, FloatType]:
                returnTyp = BooleanType()
                isCompatible = True
            # if type(exp_1) == FloatType and type(exp_2) == FloatType:
            #     returnTyp = BooleanType()
            #     isCompatible = True

        if not isCompatible:
            raise TypeMismatchInExpression(ctx)
        return returnTyp

    def visitUnExpr(self, ctx: UnExpr, o: object):
        # op: str, val: Expr
        isCompatible = False
        returnTyp = BooleanType()
        exp = self.visit(ctx.val, o)
        if ctx.op == '!':
            if type(exp) == AutoType:
                self.infer(ctx.val, o, BooleanType())
                exp = self.visit(ctx.val, o)
            if type(exp) == BooleanType:
                returnTyp = BooleanType()
                isCompatible = True

        if ctx.op == '-':
            if type(exp) == IntegerType:
                returnTyp = IntegerType()
                isCompatible = True
            if type(exp) == FloatType:
                returnTyp = FloatType()
                isCompatible = True
            if type(exp) == AutoType:
                returnTyp = AutoType()
                isCompatible = True

        if not isCompatible:
            raise TypeMismatchInExpression(ctx)
        return returnTyp

    def visitId(self, ctx: Id, o: object):
        # name: str
        # Find in all env, if id name not appear in all env, raise Undeclared
        for env in o:
            for decl in env:
                if type(decl) in [VarPrototype, ParamPrototype]:
                    if decl.name_ == ctx.name:
                        return decl.type_

        raise Undeclared(Identifier(), ctx.name)

    def visitArrayCell(self, ctx: ArrayCell, o: object):
        # name: str, cell: List[Expr]

        idtyp = self.visit(Id(ctx.name), o)

        cellVal = []
        if type(idtyp) is not ArrayType:
            raise TypeMismatchInExpression(ctx)
        elif len(ctx.cell) == 0:
            raise TypeMismatchInExpression(ctx)
        else:
            for exp in ctx.cell:
                e = self.visit(exp, o)
                if type(e) == AutoType:
                    # If auto type funccall then infer to IntegerType
                    for decl in o[-1]:
                        if exp.name == decl.name_ and decl.type_ == AutoType:
                            decl.type_ = IntegerType
                elif type(e) != IntegerType:
                    raise TypeMismatchInExpression(ctx)
                elif type(exp) is IntegerLit:
                    cellVal += [int(exp.val)]
                elif type(e) == IntegerType:
                    cellVal += [e]

        # Check if cell is differ from dimesions, or cell[i] is not compatible to dimesions[i]
        idtyp.dimensions = list(map(lambda x: int(x), idtyp.dimensions))
        if len(cellVal) != len(idtyp.dimensions):
            raise TypeMismatchInExpression(ctx)
        else:
            for i in range(len(cellVal)):
                if type(cellVal[i]) is int:
                    if (cellVal[i] >= 0) and (cellVal[i] < idtyp.dimensions[i]):
                        continue
                    else:
                        raise TypeMismatchInExpression(ctx)
                elif (type(cellVal[i]) is IntegerType):
                    continue
                else:
                    raise TypeMismatchInExpression(ctx)

        return idtyp.typ

    def visitArrayLit(self, ctx: ArrayLit, o: object):
        # explist: List[Expr]
        typeMatrix = []
        commonType = AutoType
        for exp in ctx.explist:
            eleTyp = self.visit(exp, o)
            if type(eleTyp) != AutoType:
                commonType = eleTyp
            typeMatrix += [eleTyp]

        if len(typeMatrix) == 0:
            # Arraylit is empty
            raise IllegalArrayLiteral(ctx)

        for i in range(len(ctx.explist)):
            if type(typeMatrix[i]) == AutoType:
                # It must be function with auto type return
                for decl in o[-1]:
                    if decl.name_ == ctx.explist[i].name:
                        decl.type_ = commonType
                        typeMatrix[i] = commonType

        # That arraylit have different element type => illegal
        for i in range(len(ctx.explist)-1):
            for j in range(i+1, len(ctx.explist)):
                if type(typeMatrix[i]) == ArrayType:
                    typDecl1 = self.visit(ctx.explist[i], o)
                    typDecl2 = self.visit(ctx.explist[j], o)
                    typDecl1.dimensions = list(
                        map(lambda x: int(x), typDecl1.dimensions))
                    typDecl2.dimensions = list(
                        map(lambda x: int(x), typDecl2.dimensions))
                    if typDecl1.dimensions != typDecl2.dimensions:
                        raise IllegalArrayLiteral(ctx)
                    if type(typDecl1.typ) != type(typDecl2.typ):
                        raise IllegalArrayLiteral(ctx)
                else:
                    if type(typeMatrix[i]) != type(typeMatrix[j]):
                        raise IllegalArrayLiteral(ctx)
        dimension = [len(ctx.explist)]

        if type(commonType) == ArrayType:
            resolutionArrayType = self.visit(ctx.explist[0], o)
            resolutionArrayType.dimensions = list(
                map(lambda x: int(x), resolutionArrayType.dimensions))
            dimension += resolutionArrayType.dimensions
            commonType = resolutionArrayType.typ

        return ArrayType(dimension, commonType)

    def visitIntegerLit(self, ctx: IntegerLit, o: object):
        return IntegerType()

    def visitFloatLit(self, ctx: FloatLit, o: object):
        return FloatType()

    def visitStringLit(self, ctx: StringLit, o: object):
        return StringType()

    def visitBooleanLit(self, ctx: BooleanLit, o: object):
        return BooleanType()
