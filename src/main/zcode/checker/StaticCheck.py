from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class DeclarationInfo:
    def __init__(self, name: Id, varType: Type = None):
        self.name = name
        self.type = varType # the return type of function and the varType of variable could be None

class VarDeclInfo(DeclarationInfo):
    def __init__(self, name: Id, varType: Type = None, modifier: str = None, varInit: Expr = None):
        super().__init__(name, varType)
        self.modifier = modifier
        self.varInit = varInit

    def __str__(self) -> str:
        return f"Variable: {self.name.name} | Type: {self.type} | Modifier: {self.modifier} | Initialization: {self.varInit}"

class FuncDeclInfo(DeclarationInfo):
    def __init__(self, name: Id, returnType, param: List[VarDecl], body: Stmt = None):
        super().__init__(name, returnType)
        self.param = param
        self.body = body

    def __str__(self) -> str:
        param_str = ', '.join(str(p) for p in self.param)
        return f"Function: {self.name.name} | Return Type: {self.type} | Parameters: {param_str}"

class LightFuncVisitor(BaseVisitor):
    
    def __init__(self, ast: Program):
        self.ast = ast
        ### Func chỉ có tồn tại trong 1 scope so probly fine 
        self.funcEnv = [FuncDeclInfo(Id("readNumber"), NumberType(), [], 1), 
                             FuncDeclInfo(Id("writeNumber"), VoidType(), [VarDecl(Id("x"), NumberType(), None, None)], 1), 
                             FuncDeclInfo(Id("readBool"), BoolType(), [], 1), 
                             FuncDeclInfo(Id("writeBool"), VoidType(), [VarDecl(Id("x"), BoolType(), None, None)], 1), 
                            FuncDeclInfo(Id("readString"), StringType(), [], 1), 
                             FuncDeclInfo(Id("writeString"), VoidType(), [VarDecl(Id("x"), StringType(), None, None)], 1) ]
    
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
        
        funcName = ast.name.name # string
        for i in range(len(ast.param)):
            for j in range(i + 1, len(ast.param)):
                if ast.param[i].name == ast.param[j].name:
                    paramName = ast.param[i].name.name # string
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
        self.default_func = [FuncDeclInfo(Id("readNumber"), NumberType(), [], 1), 
                             FuncDeclInfo(Id("writeNumber"), VoidType(), [VarDecl(Id("x"), NumberType(), None, None)], 1), 
                             FuncDeclInfo(Id("readBool"), BoolType(), [], 1), 
                             FuncDeclInfo(Id("writeBool"), VoidType(), [VarDecl(Id("x"), BoolType(), None, None)], 1), 
                            FuncDeclInfo(Id("readString"), StringType(), [], 1), 
                             FuncDeclInfo(Id("writeString"), VoidType(), [VarDecl(Id("x"), StringType(), None, None)], 1) ]
        self.inForLoop = 0
        self.Return = False
        self.ReturnType = None
        self.ReturnFuncDeclRef = None
        self.currentStmt = None
        
    def check(self):
        return self.visit(self.ast, [])
    
    def updateType(self, info: DeclarationInfo, typ, param):
        for scope in param:
            for i in scope:
                if info == i:
                    i.type = typ
        return typ
    
    def handleArrayTypeStmt(self, ast_left, ast_right, ast_left_type, ast_right_type, ast, param):
        left_type_core = self.extractArrayType(ast_left_type)
        right_type_core = self.extractArrayType(ast_right_type)
        if left_type_core is None and right_type_core is None:
            raise TypeCannotBeInferred(ast)
        if left_type_core is not None and right_type_core is not None:
            return ast_left_type, ast_right_type
        if left_type_core is None:
            if isinstance(ast_left_type, ArrayType):
                ast_left_type = self.updateArrayType(ast_left,ast_left_type, ast_right_type, param)
            else:
                ast_left_type = self.updateAstType(ast_left, ast_right_type, param)
            if ast_left_type is False:
                raise TypeMismatchInStatement(ast)
        if right_type_core is None:
            if isinstance(ast_right_type, ArrayType):
                ast_right_type = self.updateArrayType(ast_right,ast_right_type, ast_left_type, param)
            else:
                ast_right_type = self.updateAstType(ast_right, ast_left_type, param)
            if ast_right_type is False:
                raise TypeMismatchInStatement(ast)
        return ast_left_type, ast_right_type
        
    
    def updateAstType(self, ast, typ, param):
        updated = False
        if isinstance(ast, Id):
            for scope in param:
                for i in scope:
                    if isinstance(i, VarDeclInfo) and ast.name == i.name.name:
                        i.type = typ
                        updated = True
            return False
        elif isinstance(ast, CallExpr):
            for scope in param:
                for i in scope:
                    if isinstance(i, FuncDeclInfo) and ast.name.name == i.name.name:
                        i.type = typ
                        updated = True
            return False
        if updated is False:
            return False
        else:
            return typ
        
    def extractTrueType(self, info):
        if isinstance(info, DeclarationInfo):
            return info.type
        return info
    
    def compareParamType(self, param: List[Expr], func_param_type: List[VarDecl], param_env):
        # thanks copilot 
        if len(param) != len(func_param_type):
            return False
        for i, j in zip(param, func_param_type):
            # i is array litteral
            argument_type = self.extractTrueType(self.visit(i, param_env))
            parameter_type = j.varType
            if argument_type is None:
                self.updateAstType(i, parameter_type, param_env)
                argument_type = parameter_type
            elif isinstance(argument_type, ArrayType) and isinstance(parameter_type, ArrayType):
                if argument_type.eleType is None:
                    argument_type = self.updateArrayType(i, argument_type, parameter_type, param_env)
                    if argument_type is False:
                        return False
            if str(argument_type) != str(parameter_type):
                return False
        return True
    
    def extractArrayType(self, array_type):
        if isinstance(array_type, ArrayType):
            return array_type.eleType
        return array_type
    
    def updateArrayType(self, ast, ast_og_type, eleType, param):
        if isinstance(ast, ArrayLiteral):
            # ast_type = self.visit(ast, param)
            next_ast_og_type = ast_og_type
            arr_type = None
            if isinstance(eleType, NumberType) or isinstance(eleType, BoolType) or isinstance(eleType, StringType):
                if isinstance(ast_og_type, ArrayType):
                    # fail since they should be the same shape by now
                    return True
                next_ast_og_type = ast_og_type
                arr_type = eleType
            elif len(eleType.size) == 1:
                if isinstance(ast_og_type, ArrayType) and ast_og_type.size[0] != eleType.size[0]:
                    ### failed to update so we return true
                    return True
                if isinstance(ast_og_type, ArrayType) and len(ast_og_type.size) == 1:
                    next_ast_og_type = ast_og_type.eleType
                elif isinstance(ast_og_type, ArrayType):
                    next_ast_og_type = ArrayType(ast_og_type.size[1:], ast_og_type.eleType)
                arr_type = eleType.eleType
            else:
                if isinstance(ast_og_type, ArrayType) and ast_og_type.size[0] != eleType.size[0]:
                    return True
                if isinstance(ast_og_type, ArrayType) and len(ast_og_type.size) == 1:
                    next_ast_og_type = ast_og_type.eleType
                elif isinstance(ast_og_type, ArrayType):
                    next_ast_og_type = ArrayType(ast_og_type.size[1:], ast_og_type.eleType)
                arr_type = ArrayType(eleType.size[1:], eleType.eleType)
            for i in ast.value:
                fail = self.updateArrayType(i, next_ast_og_type, arr_type, param)
                if fail is True:
                    return True
        elif isinstance(ast, Id):
            for scope in param:
                for i in scope:
                    if isinstance(i, VarDeclInfo) and ast.name == i.name.name:
                        if i.type is None or str(i.type) == str(eleType):
                            i.type = eleType
                            # update success so we return False
                            return False
                        else:
                            return True
        elif isinstance(ast, CallExpr):
            for scope in param:
                for i in scope:
                    if isinstance(i, FuncDeclInfo) and ast.name.name == i.name.name:
                        if i.type is None or str(i.type) == str(eleType):
                            i.type = eleType
                            return False
                        else:
                            return True
                    
        return eleType
                

    
    def visitProgram(self, ast: Program, param):
        # env chỉ để chứa tất cả các previous declaration
        env = []
        env.append(self.default_func)
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
        
        scope = env[0]
        find_main = False
        for i in scope:
            if isinstance(i, FuncDeclInfo):
                if i.name.name == "main":
                    find_main = True
                if i.name.name == "main" and not (isinstance(i.type, VoidType) and len(i.param) == 0):
                    raise NoEntryPoint()
        
        if not find_main:
            raise NoEntryPoint()
        return ""

        
        

    def visitVarDecl(self, ast: VarDecl, param):
        # for scope in param:
        #     for i in scope:
        #         if i.name == ast.name:
        #             ### Might need to change this shit to fit with the current description 
        #             IdName = ast.name.name
        #             raise Redeclared(Variable(), IdName)
        scope = param[0]
        for i in scope:
            if i.name == ast.name and isinstance(i, VarDeclInfo):
                ### Might need to change this shit to fit with the current description 
                IdName = ast.name.name # string
                raise Redeclared(Variable(), IdName)
        # new_param_without_ast_name = 
        left_type = ast.varType
        if(ast.varInit is not None):
            right = self.visit(ast.varInit, param)
            right_type = self.extractTrueType(right)
            if left_type is None and right_type is None:
                raise TypeCannotBeInferred(ast)
            if (left_type is None):
                left_type = right_type
            if (right_type is None):
                ### only run when it is func decl for some reason
                right_type = self.updateType(right, left_type, param)
            
            if isinstance(left_type, ArrayType) and isinstance(right_type, ArrayType):
                left_type, right_type = self.handleArrayTypeStmt(ast.name, ast.varInit, left_type, right_type, ast, param)
            
            if str(left_type) != str(right_type):
                raise TypeMismatchInStatement(ast)
                # failed = False
                # if isinstance(left_type, ArrayType) and isinstance(right_type, ArrayType):
                #     if left_type.eleType is None and right_type.eleType is None:
                #         raise TypeCannotBeInferred(ast)
                #     elif left_type.eleType is None:
                #         self.updateArrayType(ast.name, right_type, param)
                #     elif right_type.eleType is None:
                #         self.updateArrayType(ast.varInit, left_type, param)
                #     else:
                #         raise TypeMismatchInStatement(ast)
                # if failed is True:
                #     raise TypeMismatchInStatement(ast)
                    
            
        param[0].append(VarDeclInfo(ast.name, left_type, ast.modifier, ast.varInit))
        

    def visitFuncDecl(self, ast: FuncDecl, param, allSeachedFunc = []):
        ### luôn luôn tìm được body nó
        # for i in allSeachedFunc:
        #     if i.name == ast.name:
        #         if ast.body is None:
        #             ast.body = i.body
        #             ast.param = i.param
        #             break
        FuncDeclInfoRef = FuncDeclInfo(ast.name, None, ast.param, ast.body)
        # param[0].append(FuncDeclInfoRef)
        scope = param[0]
        funcDeclAlreadyExist = False
        for i in scope:
            if isinstance(i, FuncDeclInfo) and i.name.name == ast.name.name:
                funcDeclAlreadyExist = True
                FuncDeclInfoRef = i
                if i.body is None:
                    i.body = ast.body
                    i.param = ast.param
                    break
        if funcDeclAlreadyExist is False:
            param[0].append(FuncDeclInfoRef)
                
        ast_param = [[]]
        for i in ast.param:
            self.visit(i, ast_param)
        # func_scope = [ast.param] + param
        func_scope = ast_param + param
        if(ast.body is not None):
            self.ReturnFuncDeclRef = FuncDeclInfoRef
            ### nếu như đã có type từ đc infer 
            if (FuncDeclInfoRef.type is not None):
                self.ReturnType = FuncDeclInfoRef.type
            self.visit(ast.body, func_scope)
            if not self.Return:
                self.updateType(FuncDeclInfoRef, VoidType(), param)
            # else:
            #     self.updateType(FuncDeclInfoRef, self.ReturnType, param)
            self.Return = False
            self.ReturnType = None
            self.ReturnFuncDeclRef = None
        # func_scope = [] + ast.param + param
        

    def visitNumberType(self, ast : NumberType, param):
        return ast

    def visitBoolType(self, ast : BoolType, param):
        return ast

    def visitStringType(self, ast : StringType, param):
        return ast

    def visitArrayType(self, ast : ArrayType, param):
        # hmmmm how to vist an array inside an array
        # return ArrayType(ast.size, self.visit(ast.eleType, param))
        return ast

    def visitBinaryOp(self, ast: BinaryOp, param):
        left = self.visit(ast.left, param)
        left_None = False
        left_type = left
        
        if isinstance(left, DeclarationInfo):
            left_type = left.type
            if left.type is None:
                left_None = True
        # right = self.visit(ast.right, param)
        # right_type = right
        # right_None = False
        # if isinstance(right, DeclarationInfo):
        #     right_type = right.type
        #     if right.type is None:
        #         right_None = True
        
        if ast.op in ['+', '-', '*', '/', '%']:
            if left_None:
                left_type = self.updateType(left, NumberType(), param)
                
            right = self.visit(ast.right, param)
            right_type = right
            right_None = False
            if isinstance(right, DeclarationInfo):
                right_type = right.type
                if right.type is None:
                    right_None = True
                    
            if right_None:
                right_type = self.updateType(right, NumberType(), param)
            
            if (type(left_type) is not NumberType) or (type(right_type) is not NumberType):
                raise TypeMismatchInExpression(ast)
            
            return NumberType()
            # if isinstance(left, NumberType) and isinstance(right, NumberType):
            #     return NumberType()
            # raise TypeMismatchInExpression(ast)
        elif ast.op in ['=', '!=', '<', '>', '<=', '>=']:
            
            if left_None:
                left_type = self.updateType(left, NumberType(), param)
                
            right = self.visit(ast.right, param)
            right_type = right
            right_None = False
            if isinstance(right, DeclarationInfo):
                right_type = right.type
                if right.type is None:
                    right_None = True
                    
            if right_None:
                right_type = self.updateType(right, NumberType(), param)
            if type(left_type) is not NumberType or type(right_type) is not NumberType:
                raise TypeMismatchInExpression(ast)
            
            return BoolType()
        elif ast.op in ['and', 'or']:
            if left_None:
                left_type = self.updateType(left, BoolType(), param)
                
            right = self.visit(ast.right, param)
            right_type = right
            right_None = False
            if isinstance(right, DeclarationInfo):
                right_type = right.type
                if right.type is None:
                    right_None = True
                    
            if right_None:
                right_type = self.updateType(right, BoolType(), param)

            if type(left_type) is not BoolType or type(right_type) is not BoolType:
                raise TypeMismatchInExpression(ast)
            
            return BoolType()
            # if isinstance(left, BoolType) and isinstance(right, BoolType):
            #     return BoolType()
            # raise TypeMismatchInExpression(ast)
        elif ast.op in ['==']:
            if left_None:
                left_type = self.updateType(left, StringType(), param)
                
            right = self.visit(ast.right, param)
            right_type = right
            right_None = False
            if isinstance(right, DeclarationInfo):
                right_type = right.type
                if right.type is None:
                    right_None = True
                    
            if right_None:
                right_type = self.updateType(right, StringType(), param)
            if type(left_type) is not StringType or type(right_type) is not StringType:
                raise TypeMismatchInExpression(ast)
            
            return BoolType()
        elif ast.op in ['...']:
            if left_None:
                left_type = self.updateType(left, StringType(), param)
            right = self.visit(ast.right, param)
            right_type = right
            right_None = False
            if isinstance(right, DeclarationInfo):
                right_type = right.type
                if right.type is None:
                    right_None = True
                    
            if right_None:
                right_type = self.updateType(right, StringType(), param)
            if type(left_type) is not StringType or type(right_type) is not StringType:
                raise TypeMismatchInExpression(ast)
            
            return StringType()
            

    def visitUnaryOp(self, ast: UnaryOp, param):
        right = self.visit(ast.operand, param)
        right_None = False
        right_type = self.extractTrueType(right)
        if isinstance(right, DeclarationInfo) and right.type is None:
            right_None = True
        if ast.op in ['-']:
            if right_None:
                right_type = self.updateType(right, NumberType(), param)
            if type(right_type) is not NumberType:
                raise TypeMismatchInExpression(ast)
            return NumberType()
        elif ast.op == 'not':
            if right_None:
                right_type = self.updateType(right, BoolType(), param)
            if type(right_type) is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()

    def visitCallExpr(self, ast: CallExpr, param):
        funcName = ast.name.name # string
        for scope in param:
            for i in scope:
                if ast.name.name == i.name.name and isinstance(i, FuncDeclInfo):
                    # if(i.type is None):
                    #     raise TypeCannotBeInferred(ast)
                    if isinstance(i.type, VoidType):
                        raise TypeMismatchInExpression(ast)
                    # for j in ast.args:
                    #     self.visit(j, param)
                    if not self.compareParamType(ast.args, i.param, param):
                        raise TypeMismatchInExpression(ast)
                    return i
        raise Undeclared(Function(), funcName)

    def visitId(self, ast: Id, param):
        idName = ast.name # string
        for scope in param:
            for i in scope:
                if isinstance(i, VarDeclInfo) and ast.name == i.name.name:
                    return i
        raise Undeclared(Identifier(), idName)
            

    def visitArrayCell(self, ast: ArrayCell, param):
        E1 = self.visit(ast.arr, param)
        if not isinstance(E1, DeclarationInfo):
            raise TypeMismatchInExpression(ast)
        if not isinstance(E1.type, ArrayType):
            raise TypeMismatchInExpression(ast)
        arr_size = E1.type.size.copy()
        if (len(arr_size) < len(ast.idx)):
            raise TypeMismatchInExpression(ast)
        ret_type = E1.type
        for i in ast.idx:
            # typ = self.extractTrueType(self.visit(i, param))
            left = self.visit(i, param)
            left_type = self.extractTrueType(left)
            if isinstance(left, DeclarationInfo) and left.type is None:
                left_type = self.updateType(left, NumberType(), param)
            if isinstance(left_type, NumberType) is False:
                raise TypeMismatchInExpression(ast)
            arr_size.pop(0)
        
        if len(arr_size) == 0:
            return ret_type.eleType
        return ArrayType(arr_size, ret_type.eleType)
        
    

    def visitBlock(self, ast: Block, param):
        # local_env = param.copy()
        local_env = [[]] + param
        # local_env.append(param)
        for i in ast.stmt:
            self.visit(i, local_env)

    def visitIf(self, ast: If, param):
        left = self.visit(ast.expr, param)
        left_type = self.extractTrueType(left)
        if isinstance(left, DeclarationInfo) and left.type is None:
            left_type = self.updateType(left, BoolType(), param)
        if isinstance(left_type, BoolType) is False:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt, param)
        for expr, stmt in ast.elifStmt:
            left = self.visit(expr, param)
            left_type = self.extractTrueType(left)
            if isinstance(left, DeclarationInfo) and left.type is None:
                left_type = self.updateType(left, BoolType(), param)
            if isinstance(left_type, BoolType) is False:
                raise TypeMismatchInStatement(ast)
            self.visit(stmt, param)
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, param)

    def visitFor(self, ast: For, param):
        VarDeclInfoFor = self.visit(ast.name, param)
        if isinstance(VarDeclInfoFor, DeclarationInfo) and VarDeclInfoFor.type is None:
            VarDeclInfoFor.type = NumberType()
        if isinstance(VarDeclInfoFor, DeclarationInfo) is False or isinstance(VarDeclInfoFor.type, NumberType) is False:
            raise TypeMismatchInStatement(ast)
        left = self.visit(ast.condExpr, param)
        left_type = self.extractTrueType(left)
        if isinstance(left, DeclarationInfo) and left.type is None:
            left_type = self.updateType(left, BoolType(), param)
        if isinstance(left_type, BoolType) is False:
            raise TypeMismatchInStatement(ast)
        right = self.visit(ast.updExpr, param)
        right_type = self.extractTrueType(right)
        if isinstance(right, DeclarationInfo) and right.type is None:
            right_type = self.updateType(right, NumberType(), param)
        if isinstance(right_type, NumberType) is False:
            raise TypeMismatchInStatement(ast)
        self.inForLoop += 1
        self.visit(ast.body, param)
        self.inForLoop -= 1

    def visitContinue(self, ast: Continue, param):
        if self.inForLoop == 0:
            raise MustInLoop(ast)

    def visitBreak(self, ast: Break, param):
        if self.inForLoop == 0:
            raise MustInLoop(ast)

    def visitReturn(self, ast: Return, param):
        self.Return = True
        if ast.expr is not None:
            return_type = self.extractTrueType(self.visit(ast.expr, param))
            return_type_core = self.extractArrayType(return_type)
            if return_type_core is None:
                raise TypeCannotBeInferred(ast)
            if self.ReturnType is None or str(self.ReturnType) == str(return_type):
                self.updateType(self.ReturnFuncDeclRef, return_type, param)
                self.ReturnType = return_type
            else:  
                raise TypeMismatchInStatement(ast)
        ### when it "return"
        else :
            # self.ReturnType = VoidType()
            if self.ReturnType is None :
                self.updateType(self.ReturnFuncDeclRef, VoidType(), param)
                self.ReturnType = VoidType()
            elif str(self.ReturnType) != str(VoidType()):
                raise TypeMismatchInStatement(ast)
            

    def visitAssign(self, ast: Assign, param):
        right = self.visit(ast.rhs, param)
        left = self.visit(ast.lhs, param)
        left_type = self.extractTrueType(left)
        right_type = self.extractTrueType(right)
        if left_type is None and right_type is None:
            raise TypeCannotBeInferred(ast)
        if (left_type is None):
            left_type = self.updateType(left, right_type, param)
        if (right_type is None):
            right_type = self.updateType(right, left_type, param)
        if isinstance(left_type, ArrayType) and isinstance(right_type, ArrayType):
            left_type, right_type = self.handleArrayTypeStmt(ast.lhs, ast.rhs, left_type, right_type, ast, param)
        if str(left_type) != str(right_type):
            raise TypeMismatchInStatement(ast)
        
        

    def visitCallStmt(self, ast: CallStmt, param):
        funcName = ast.name.name # string
        for scope in param:
            for i in scope:
                if ast.name.name == i.name.name and isinstance(i, FuncDeclInfo):
                    if i.type is None:
                        self.updateType(i, VoidType(), param)
                    if not isinstance(i.type, VoidType):
                        raise TypeMismatchInStatement(ast)
                    # for j in ast.args:
                    #     self.visit(j, param)
                    if self.compareParamType(ast.args, i.param, param) == False:
                        raise TypeMismatchInStatement(ast)
                    return VoidType()
        raise Undeclared(Function(), funcName)

    def visitNumberLiteral(self, ast: NumberLiteral, param):
        # return ast
        return NumberType()

    def visitBooleanLiteral(self, ast : BooleanLiteral, param):
        return BoolType()

    def visitStringLiteral(self, ast: StringLiteral, param):
        return StringType()

    def visitArrayLiteral(self, ast: ArrayLiteral, param):
        # because the array is a list of expression
        # i will worry about why later
        if(ast.value == []):
            return ArrayType([], None)
        # find first typ_check``
        # typ_check = self.extractTrueType(self.visit(ast.value[0], param))
        first = self.visit(ast.value[0], param)
        second = self.extractTrueType(first)
        # typ_none = self.extractArrayType(self.extractTrueType(self.visit(ast.value[0], param)))
        typ_none = self.extractArrayType(second)
        update_Type = second
        need_update = False
        
        ### [0,1,2,3] visit từ 0 dô 1 dô 2 dô 3 rồi dô 3
        
        for i in ast.value:
            typ = self.extractTrueType(self.visit(i, param))
            typ_none = self.extractArrayType(typ)
            ### why did i put not isinstance(i, Literal) here
            
            # if typ_none is not None and not isinstance(i, Literal):
            if typ_none is not None:
                if need_update == False:
                    update_Type = typ
                    need_update = True
                else:
                    if str(update_Type) != str(typ):
                        raise TypeMismatchInExpression(ast)
            else:
                if need_update == True:
                    if isinstance(update_Type, ArrayType) and isinstance(typ, ArrayType):
                        for i in range(len(ast.value)):
                            if update_Type.size[i] == typ.size[i]:
                                continue
                            else:
                                raise TypeMismatchInExpression(ast)
                    elif isinstance(typ, ArrayType) and not isinstance(update_Type, ArrayType):
                        raise TypeMismatchInExpression(ast)
                            
                    
            # if str(typ) != str(typ_check):
            #     raise TypeMismatchInExpression(ast)
        theoratical_next_arrayType = None
        if isinstance(update_Type, ArrayType):
            prev_arr_len = [] + update_Type.size
            theoratical_next_arrayType =  ArrayType([float(len(ast.value))] + prev_arr_len, update_Type.eleType)
        else :
            theoratical_next_arrayType =  ArrayType([float(len(ast.value))], update_Type)
        if need_update:
            failed = self.updateArrayType(ast, theoratical_next_arrayType, theoratical_next_arrayType, param)
            if failed is True:
                raise TypeMismatchInExpression(ast)
        return theoratical_next_arrayType
        # prev_arr_len = []
        # if isinstance(update_Type, ArrayType):
        #     prev_arr_len = [] + update_Type.size
        #     return ArrayType([float(len(ast.value))] + prev_arr_len, update_Type.eleType)
        # else :
        #     return ArrayType([float(len(ast.value))], update_Type)
