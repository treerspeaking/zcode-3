from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class GlobalInfo: pass

class FuncInfo: pass

class BlockInfo: pass
class VarDeclInfo: 
    def __init__(self, name: Id, varType : Type = None, modifier: str = None, varInit: Expr = None):
        self.name = name
        self.type = varType
        self.modifier = modifier
        self.varInit = varInit
    
    def __str__(self) -> str:
        return f"Variable: {self.name.name} | Type: {self.type} | Modifier: {self.modifier} | Initialization: {self.varInit}"

class FuncDeclInfo: 
    def __init__(self, name: Id, returnType, param: List[VarDecl], body : Stmt = None):
        self.name = name
        self.type = returnType
        self.param = param
        self.body = body
    def __str__(self) -> str:
        param_str = ', '.join(str(p) for p in self.param)
        return f"Function: {self.name.name} | Return Type: {self.type} | Parameters: {param_str}"

class LightFuncVisitor(BaseVisitor):
    
    def __init__(self, ast: Program):
        self.ast = ast
        self.funcEnv = []
    
    def visitProgram(self):
        ### This will search every function in the program and check if that function body is declared or not
        ### If a function is declared without body it will add to the env at first and then continue searching and when it found the body it will update the env
        ### If a function is declared with a body and found the same function that has a body, then it will raise Redeclared
        
        for i in self.ast.decl:
            if isinstance(i, FuncDecl):
                self.visit(i, self.funcEnv)
        
        # for func in self.funcEnv:
        #     if func.body is None:
        #         funcName = func.name.name
        #         raise NoDefinition(funcName)
        
        return self.funcEnv
                
    def visitFuncDecl(self, ast: FuncDecl, param):
        
        funcName = ast.name.name
        for i in range(len(ast.param)):
            for j in range(i + 1, len(ast.param)):
                if ast.param[i].name == ast.param[j].name:
                    paramName = ast.param[i].name.name
                    raise Redeclared(Parameter(), paramName)
        
        for i in param:
            if isinstance(i, FuncDeclInfo) and i.name == ast.name:
                ### Cần phải check cái param của nó coi có giống nhau không giữa cái declared vs cái redeclare
                ### Might need to change this shit to fit with the current description
                if (i.body is None and ast.body is not None):
                    if len(i.param) != len(ast.param):
                        raise Redeclared(Function(), funcName)
                    for j, k in zip(i.param, ast.param):
                        ### j, k is Vardecl
                        if str(j.varType) != str(k.varType):
                            raise Redeclared(Function(), funcName)
                    i.body = ast.body
                    i.param = ast.param
                    return
                else:
                    raise Redeclared(Function(), funcName)
        param.append(FuncDeclInfo(ast.name, None, ast.param, ast.body))
        return param
    
    def visitNumberType(self, ast : NumberType, param):
        return NumberType()

    def visitBoolType(self, ast : BoolType, param):
        return BoolType()

    def visitStringType(self, ast : StringType, param):
        return StringType()

    def visitArrayType(self, ast : ArrayType, param):
        # hmmmm how to vist an array inside an array
        return ArrayType(ast.size, self.visit(ast.eleType, param))

class StaticChecker(BaseVisitor, Utils):
    def __init__(self, ast):
        self.ast = ast
        self.global_env = []
        # self.default_func = ["readNumber", "writeNumber", "readBool", "write", "readString", "writeString"]
        self.default_func = [FuncDeclInfo(Id("readNumber"), NumberType(), [VarDecl(Id("x"), NumberType, None, None)], None), 
                             FuncDeclInfo(Id("writeNumber"), VoidType(), [VarDecl(Id("x"), NumberType, None, None)], None), 
                             FuncDeclInfo(Id("readBool"), BoolType(), [VarDecl(Id("x"), BoolType, None, None)], None), 
                             FuncDeclInfo(Id("writeBool"), VoidType(), [VarDecl(Id("x"), BoolType, None, None)], None), 
                            FuncDeclInfo(Id("readString"), StringType(), [VarDecl(Id("x"), BoolType, None, None)], None), 
                             FuncDeclInfo(Id("writeString"), VoidType(), [VarDecl(Id("x"), BoolType, None, None)], None) ]
        
    def check(self):
        return self.visit(self.ast, [])

    
    def visitProgram(self, ast: Program, param):
        # env chỉ để chứa tất cả các previous declaration
        env = []
        env = env + self.default_func
        allSeachedFunc = LightFuncVisitor(ast).visitProgram()
        for i in ast.decl: 
            if isinstance(i, VarDecl):
                self.visitVarDecl(i, env)
            else:
                self.visitFuncDecl(i, env, allSeachedFunc)
        
        
        ### Will probly move this later
        for func in allSeachedFunc:
            if func.body is None:
                funcName = func.name.name
                raise NoDefinition(funcName)
        return ""

        
        

    def visitVarDecl(self, ast: VarDecl, param):
        for i in param:
            if i.name == ast.name:
                ### Might need to change this shit to fit with the current description 
                IdName = ast.name.name
                raise Redeclared(Variable(), IdName)
        param.append(VarDeclInfo(ast.name, ast.varType, ast.modifier, ast.varInit))
        if(ast.varInit is not None):
            self.visit(ast.varInit, param)
        

    def visitFuncDecl(self, ast: FuncDecl, param, allSeachedFunc = []):
        ### luôn luôn tìm được body nó
        # for i in allSeachedFunc:
        #     if i.name == ast.name:
        #         if ast.body is None:
        #             ast.body = i.body
        #             ast.param = i.param
        #             break
        param.append(FuncDeclInfo(ast.name, None, ast.param, ast.body))
        func_scope = [] + ast.param + param
        if(ast.body is not None):
            self.visit(ast.body, func_scope)
        

    def visitNumberType(self, ast : NumberType, param):
        return NumberType()

    def visitBoolType(self, ast : BoolType, param):
        return BoolType()

    def visitStringType(self, ast : StringType, param):
        return StringType()

    def visitArrayType(self, ast : ArrayType, param):
        # hmmmm how to vist an array inside an array
        return ArrayType(ast.size, self.visit(ast.eleType, param))

    def visitBinaryOp(self, ast: BinaryOp, param):
        pass

    def visitUnaryOp(self, ast: UnaryOp, param):
        pass

    def visitCallExpr(self, ast: CallExpr, param):
        funcName = ast.name.name
        for i in param:
            if ast.name.name == i.name.name:
                for j in ast.args:
                    self.visit(j, param)
                return i
        raise Undeclared(Function(), funcName)

    def visitId(self, ast: Id, param):
        idName = ast.name
        for i in param:
            if ast.name == i.name.name:
                return i
        raise Undeclared(Identifier(), idName)
            

    def visitArrayCell(self, ast: ArrayCell, param):
       self.visit(ast.arr, param)
       for i in ast.idx:
           self.visit(i, param)

    def visitBlock(self, ast: Block, param):
        local_env = param.copy()
        for i in ast.stmt:
            self.visit(i, local_env)

    def visitIf(self, ast: If, param):
        self.visit(ast.expr, param)
        self.visit(ast.thenStmt, param)
        for expr, stmt in ast.elifStmt:
            self.visit(expr, param)
            self.visit(expr, param)

    def visitFor(self, ast: For, param):
        self.visit(ast.name, param)
        self.visit(ast.condExpr, param)
        self.visit(ast.updExpr, param)
        self.visit(ast.body, param)

    def visitContinue(self, ast: Continue, param):
        pass

    def visitBreak(self, ast: Break, param):
        pass

    def visitReturn(self, ast: Return, param):
        if ast.expr is not None:
            return self.visit(ast.expr, param)
        return VoidType()

    def visitAssign(self, ast: Assign, param):
        self.visit(ast.rhs, param)
        self.visit(ast.lhs, param)

    def visitCallStmt(self, ast: CallStmt, param):
        funcName = ast.name.name
        for i in param:
            if ast.name.name == i.name.name:
                for j in ast.args:
                    self.visit(j, param)
                return i
        raise Undeclared(Function(), funcName)

    def visitNumberLiteral(self, ast: NumberLiteral, param):
        return NumberLiteral(ast.value)

    def visitBooleanLiteral(self, ast : BooleanLiteral, param):
        return BooleanLiteral(ast.value)

    def visitStringLiteral(self, ast: StringLiteral, param):
        return StringLiteral(ast.value)

    def visitArrayLiteral(self, ast: ArrayLiteral, param):
        # because the array is a list of expression
        # i will worry about why later
        return ArrayLiteral([self.visit(i, param) for i in ast.value])
