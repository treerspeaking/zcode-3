from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *



class ASTGeneration(ZCodeVisitor):

    # def visitProgram(self, ctx: ZCodeParser.ProgramContext):
    #     # return Program([VarDecl(Id(ctx.IDENTIFIER().getText()), NumberType())])
    #     return None
      
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
      
        # Decl_list = 
        # return Program.
        decl_list = [ctx.decl().accept(self)] + ctx.program_tail().accept(self)
        return Program(decl_list)


    # Visit a parse tree produced by ZCodeParser#program_tail.
    def visitProgram_tail(self, ctx:ZCodeParser.Program_tailContext):
        if(ctx.EOF()):
            return []
        elif(ctx.decl()):
            return [ctx.decl().accept(self)] + ctx.program_tail().accept(self)


    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        if(ctx.var_decl()):
            return ctx.var_decl().accept(self)
        elif(ctx.func_decl()):
            return ctx.func_decl().accept(self)


    # Visit a parse tree produced by ZCodeParser#stmt.
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        if(ctx.func_call_stmt()):
            return ctx.func_call_stmt().accept(self)
        elif(ctx.cont_stmt()):
            return ctx.cont_stmt().accept(self)
        elif(ctx.break_stmt()):
            return ctx.break_stmt().accept(self)
        elif(ctx.ret_stmt()):
            return ctx.ret_stmt().accept(self)
        elif(ctx.ass_stmt()):
            return ctx.ass_stmt().accept(self)
        elif(ctx.block_stmt()):
            return ctx.block_stmt().accept(self)
        elif(ctx.if_stmt()):
            return ctx.if_stmt().accept(self)
        elif(ctx.for_stmt()):
            return ctx.for_stmt().accept(self)
        # hmmmm this isn't good
        elif(ctx.var_decl()):
            return ctx.var_decl().accept(self)


    # Visit a parse tree produced by ZCodeParser#nullable_newline_list.
    def visitNullable_newline_list(self, ctx:ZCodeParser.Nullable_newline_listContext):
        return None


    # Visit a parse tree produced by ZCodeParser#nullable_newline_list_tail.
    def visitNullable_newline_list_tail(self, ctx:ZCodeParser.Nullable_newline_list_tailContext):
        return None


    # Visit a parse tree produced by ZCodeParser#newline_list.
    def visitNewline_list(self, ctx:ZCodeParser.Newline_listContext):
        return None


    # Visit a parse tree produced by ZCodeParser#newline_list_tail.
    def visitNewline_list_tail(self, ctx:ZCodeParser.Newline_list_tailContext):
        return None


    # Visit a parse tree produced by ZCodeParser#id_single.
    def visitId_single(self, ctx:ZCodeParser.Id_singleContext):
        return Id(ctx.IDENTIFIER().getText())


    # Visit a parse tree produced by ZCodeParser#decl_array.
    def visitDecl_array(self, ctx:ZCodeParser.Decl_arrayContext):
        # this will return the ID of the array and possibly the decl array
        # will probly need to fix it tomorrow when my friend rep
        arr_list = ctx.decl_array_list().accept(self) # this is [1.0, 2.0, 3.0]
        return (Id(ctx.IDENTIFIER().getText()), arr_list)


    # Visit a parse tree produced by ZCodeParser#decl_array_list.
    def visitDecl_array_list(self, ctx:ZCodeParser.Decl_array_listContext):
        # this return an array of float
        return [float(ctx.NUM_LIT().getText())] + ctx.decl_array_list_tail().accept(self)


    # Visit a parse tree produced by ZCodeParser#decl_array_list_tail.
    def visitDecl_array_list_tail(self, ctx:ZCodeParser.Decl_array_list_tailContext):
        if(ctx.getChildCount() == 0):
            return []
        else:
            return [float(ctx.NUM_LIT().getText())] + ctx.decl_array_list_tail().accept(self)


    # Visit a parse tree produced by ZCodeParser#ass_array.
    def visitAss_array(self, ctx:ZCodeParser.Ass_arrayContext):
        # this will return an array cell
        id = Id(ctx.IDENTIFIER().getText())
        idx = ctx.ass_array_list().accept(self)
        return ArrayCell(id, idx)


    # Visit a parse tree produced by ZCodeParser#ass_array_list.
    def visitAss_array_list(self, ctx:ZCodeParser.Ass_array_listContext):
        return [ctx.expr().accept(self)] + ctx.ass_array_list_tail().accept(self)


    # Visit a parse tree produced by ZCodeParser#ass_array_list_tail.
    def visitAss_array_list_tail(self, ctx:ZCodeParser.Ass_array_list_tailContext):
        if(ctx.getChildCount() == 0):
            return []
        else:
            return [ctx.expr().accept(self)] + ctx.ass_array_list_tail().accept(self)


    # Visit a parse tree produced by ZCodeParser#arr.
    def visitArr(self, ctx:ZCodeParser.ArrContext):
        # this will return an array litteral
        return ArrayLiteral(ctx.array_list().accept(self))


    # Visit a parse tree produced by ZCodeParser#array_list.
    def visitArray_list(self, ctx:ZCodeParser.Array_listContext):
        return [ctx.arr_content().accept(self)] + ctx.array_list_tail().accept(self)



    # Visit a parse tree produced by ZCodeParser#array_list_tail.
    def visitArray_list_tail(self, ctx:ZCodeParser.Array_list_tailContext):
        if(ctx.getChildCount() == 0):
            return []
        return [ctx.arr_content().accept(self)] + ctx.array_list_tail().accept(self)


    # Visit a parse tree produced by ZCodeParser#arr_content.
    def visitArr_content(self, ctx:ZCodeParser.Arr_contentContext):
        if(ctx.arr()):
            return ctx.arr().accept(self)
        elif(ctx.NUM_LIT()):
            return NumberLiteral(float(ctx.NUM_LIT().getText()))
        elif(ctx.STR_LIT()):
            return StringLiteral(ctx.STR_LIT().getText())
        elif(ctx.BOOL_LIT()):
            return BooleanLiteral(ctx.BOOL_LIT().getText() == "true")
        elif(ctx.expr()):
            return ctx.expr().accept(self)


    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        if(ctx.CONCAT()):
            lhs = ctx.expr1(0).accept(self)
            rhs = ctx.expr1(1).accept(self)
            op = ctx.CONCAT().getText()
            return BinaryOp(op, lhs, rhs)
        else:
            return ctx.expr1(0).accept(self)


    # Visit a parse tree produced by ZCodeParser#expr1.
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        if(
          ctx.EQUAL() or
          ctx.DEQUAL() or
          ctx.NOT_EQUAL() or 
          ctx.LESS() or 
          ctx.GREATER() or 
          ctx.LESS_EQUAL() or 
          ctx.GREATER_EQUAL() 
        ):
          lhs = ctx.expr2(0).accept(self)
          rhs = ctx.expr2(1).accept(self)
          op = ""
          if(ctx.EQUAL()):
            op = ctx.EQUAL().getText()
          elif(ctx.DEQUAL()):
            op = ctx.DEQUAL().getText()
          elif(ctx.NOT_EQUAL()):
            op = ctx.NOT_EQUAL().getText()
          elif(ctx.LESS()): 
            op = ctx.LESS().getText()
          elif(ctx.GREATER()):
            op = ctx.GREATER().getText()
          elif(ctx.LESS_EQUAL()):
            op = ctx.LESS_EQUAL().getText()
          elif(ctx.GREATER_EQUAL()):
            op = ctx.GREATER_EQUAL().getText()
            
          return BinaryOp(op, lhs, rhs)
        else:
          return ctx.expr2(0).accept(self)
        


    # Visit a parse tree produced by ZCodeParser#expr2.
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        if(ctx.AND() or ctx.OR()):
            lhs = ctx.expr2().accept(self)
            rhs = ctx.expr3().accept(self)
            op = ""
            if (ctx.AND()):
                op = ctx.AND().getText()
            else:
                op = ctx.OR().getText()

            return BinaryOp(op, lhs, rhs)
        else:
            return ctx.expr3().accept(self)

    # Visit a parse tree produced by ZCodeParser#expr3.
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        if(ctx.PLUS() or ctx.MINUS()):
            lhs = ctx.expr3().accept(self)
            rhs = ctx.expr4().accept(self)
            op = ""
            if(ctx.PLUS()):
                op = ctx.PLUS().getText()
            elif(ctx.MINUS()):
                op = ctx.MINUS().getText()
            return BinaryOp(op, lhs, rhs)
        else:
            return ctx.expr4().accept(self)


    # Visit a parse tree produced by ZCodeParser#expr4.
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        if (ctx.MULTIPLY() or ctx.DIVIDE() or ctx.MODULO()):
            lhs = ctx.expr4().accept(self) 
            rhs = ctx.expr5().accept(self)
            op = ""
            if(ctx.MULTIPLY()):
                op = ctx.MULTIPLY().getText()
            elif(ctx.DIVIDE()):
                op = ctx.DIVIDE().getText()
            elif(ctx.MODULO()):
                op = ctx.MODULO().getText()
            return BinaryOp(op, lhs, rhs)
        return ctx.expr5().accept(self)


    # Visit a parse tree produced by ZCodeParser#expr5.
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        if(ctx.NOT()):
            return UnaryOp(ctx.NOT().getText(), ctx.expr5().accept(self))
        else:
            return ctx.expr6().accept(self)


    # Visit a parse tree produced by ZCodeParser#expr6.
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        if(ctx.MINUS()):
            rhs = ctx.expr6().accept(self)
            return UnaryOp(ctx.MINUS().getText(), rhs)
        else:
            return ctx.expr7().accept(self)


    # Visit a parse tree produced by ZCodeParser#expr7.
    def visitExpr7(self, ctx:ZCodeParser.Expr7Context):
        
        if(ctx.index_op()):
            lhs = 0
            idx_list = ctx.index_op().accept(self) # [expr1, expr2, expr3, ... ,exprn]
            if(ctx.IDENTIFIER()):
                lhs = Id(ctx.IDENTIFIER().getText())
            elif(ctx.func_call_expr()):
                lhs = ctx.func_call_expr().accept(self)
            
            return ArrayCell(lhs, idx_list)
        
        else:
            return ctx.expr8().accept(self)
        
    # Visit a parse tree produced by ZCodeParser#index_op.
    def visitIndex_op(self, ctx:ZCodeParser.Index_opContext):
        # return [expr1, expr2, expr3, ..., exprn]
        
        if(ctx.getChildCount() == 1):
            return [ctx.expr().accept(self)]
        return [ctx.expr().accept(self)] + ctx.index_op().accept(self)


    # Visit a parse tree produced by ZCodeParser#expr8.
    def visitExpr8(self, ctx:ZCodeParser.Expr8Context):
        if(ctx.BOOL_LIT()):
            return BooleanLiteral(ctx.BOOL_LIT().getText() == "true")
        elif(ctx.NUM_LIT()):
            return NumberLiteral(float(ctx.NUM_LIT().getText()))
        elif(ctx.STR_LIT()):
            return StringLiteral(ctx.STR_LIT().getText())
        elif (ctx.IDENTIFIER()):
            return Id(ctx.IDENTIFIER().getText())
        elif (ctx.arr()):
            return ctx.arr().accept(self)
        elif (ctx.func_call_expr()):
            return ctx.func_call_expr().accept(self)
        elif (ctx.expr()):
            return ctx.expr().accept(self)
        
        # return "this is expr 8"



    # Visit a parse tree produced by ZCodeParser#index_expr.
    def visitIndex_expr(self, ctx:ZCodeParser.Index_exprContext):
        # return the same as expr but no expr8
        lhs = 0
        idx_list = ctx.index_op().accept(self) # [expr1, expr2, expr3, ... ,exprn]
        if(ctx.IDENTIFIER()):
            lhs = Id(ctx.IDENTIFIER().getText())
        elif(ctx.func_call_expr()):
            lhs = ctx.func_call_expr().accept(self)
        
        return ArrayCell(lhs, idx_list)


    # Visit a parse tree produced by ZCodeParser#decl_typ_no_var.
    def visitDecl_typ_no_var(self, ctx:ZCodeParser.Decl_typ_no_varContext):
        if(ctx.BOOL()):
            return BoolType()
        elif(ctx.NUM()):
            return NumberType()
        elif(ctx.STR()):
            return StringType()
        elif(ctx.DYNAMIC()):
            return None


    # Visit a parse tree produced by ZCodeParser#decl_typ_arr.
    def visitDecl_typ_arr(self, ctx:ZCodeParser.Decl_typ_arrContext):
        if(ctx.BOOL()):
            return BoolType()
        elif(ctx.NUM()):
            return NumberType()
        elif(ctx.STR()):
            return StringType()
        


    # Visit a parse tree produced by ZCodeParser#var.
    def visitVar(self, ctx:ZCodeParser.VarContext):
        return ctx.VAR().getText()


    # Visit a parse tree produced by ZCodeParser#var_decl.
    def visitVar_decl(self, ctx:ZCodeParser.Var_declContext):
        varInit = None
        if(ctx.expr()):
            varInit = ctx.expr().accept(self)
            
        if(ctx.decl_array()):
            (id, list) = ctx.decl_array().accept(self)
            arr_type = ctx.decl_typ_arr().accept(self)
            type = ArrayType(list, arr_type)
            
            return VarDecl(id, type, None, varInit)
            
        elif(ctx.decl_typ_no_var()):
            id = ctx.id_single().accept(self)
            type = ctx.decl_typ_no_var().accept(self)
            modifier = None
            if(type is None):
                modifier = "dynamic"
            return VarDecl(id, type, modifier, varInit)
        elif(ctx.var()):
            id = ctx.id_single().accept(self)
            type = None
            modifier = ctx.var().accept(self)
            return VarDecl(id, type, modifier, varInit)
            


    # Visit a parse tree produced by ZCodeParser#param_decl_typ.
    def visitParam_decl_typ(self, ctx:ZCodeParser.Param_decl_typContext):
        if(ctx.BOOL()):
            return BoolType()
        elif(ctx.NUM()):
            return NumberType()
        elif(ctx.STR()):
            return StringType()


    # Visit a parse tree produced by ZCodeParser#param_decl.
    def visitParam_decl(self, ctx:ZCodeParser.Param_declContext):
        # this will return a list of VarDecl
        return ctx.param_decl_list().accept(self)


    # Visit a parse tree produced by ZCodeParser#param_decl_content.
    def visitParam_decl_content(self, ctx:ZCodeParser.Param_decl_contentContext):
        # this will return vardecl 
        type = ctx.param_decl_typ().accept(self)
        id = None
        if(ctx.id_single()):
            id = ctx.id_single().accept(self)
        elif(ctx.decl_array()):
            (id, list) = ctx.decl_array().accept(self)
            type = ArrayType(list, type)
        return VarDecl(id, type, None, None)


    # Visit a parse tree produced by ZCodeParser#param_decl_list.
    def visitParam_decl_list(self, ctx:ZCodeParser.Param_decl_listContext):
        if(ctx.getChildCount() == 0):
            return []
        else:
            return [ctx.param_decl_content().accept(self)] + ctx.param_decl_list_tail().accept(self)


    # Visit a parse tree produced by ZCodeParser#param_decl_list_tail.
    def visitParam_decl_list_tail(self, ctx:ZCodeParser.Param_decl_list_tailContext):
        if(ctx.getChildCount() == 0):
            return []
        else:
            return [ctx.param_decl_content().accept(self)] + ctx.param_decl_list_tail().accept(self)


    # Visit a parse tree produced by ZCodeParser#func_decl.
    def visitFunc_decl(self, ctx:ZCodeParser.Func_declContext):
        name = Id(ctx.IDENTIFIER().getText())
        param = ctx.param_decl().accept(self)
        body = None
        if(ctx.block_stmt()):
            body = ctx.block_stmt().accept(self)
        elif(ctx.ret_stmt()):
            body = ctx.ret_stmt().accept(self)
        return FuncDecl(name, param, body)


    # Visit a parse tree produced by ZCodeParser#body_content.
    def visitBody_content(self, ctx:ZCodeParser.Body_contentContext):
        if(ctx.var_decl()):
            return ctx.var_decl().accept(self)
        elif(ctx.stmt()):
            return ctx.stmt().accept(self)


    # Visit a parse tree produced by ZCodeParser#body_list.
    def visitBody_list(self, ctx:ZCodeParser.Body_listContext):
        if(ctx.getChildCount() == 0):
            return []
        
        else :
            return [ctx.body_content().accept(self)] + ctx.body_list_tail().accept(self)


    # Visit a parse tree produced by ZCodeParser#body_list_tail.
    def visitBody_list_tail(self, ctx:ZCodeParser.Body_list_tailContext):
        if(ctx.getChildCount() == 0):
            return []
        else:
            return [ctx.body_content().accept(self)] + ctx.body_list_tail().accept(self)


    # Visit a parse tree produced by ZCodeParser#block_stmt.
    def visitBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        list_stmt = ctx.body_list().accept(self)
        
        return Block(list_stmt)


    # Visit a parse tree produced by ZCodeParser#ret_stmt.
    def visitRet_stmt(self, ctx:ZCodeParser.Ret_stmtContext):
        return Return(ctx.ret_stmt_tail().accept(self))


    # Visit a parse tree produced by ZCodeParser#ret_stmt_tail.
    def visitRet_stmt_tail(self, ctx:ZCodeParser.Ret_stmt_tailContext):
        if(ctx.getChildCount() == 0):
            return None
        else:
            return ctx.expr().accept(self)


    # Visit a parse tree produced by ZCodeParser#ass_stmt.
    def visitAss_stmt(self, ctx:ZCodeParser.Ass_stmtContext):
        lhs = None
        expr = ctx.expr().accept(self)
        if(ctx.id_single()):
            lhs = ctx.id_single().accept(self)
        elif(ctx.ass_array()):
            lhs = ctx.ass_array().accept(self)
        elif(ctx.index_expr()):
            lhs = ctx.index_expr().accept(self)
        
        return Assign(lhs, expr)


    # Visit a parse tree produced by ZCodeParser#if_stmt_content.
    def visitIf_stmt_content(self, ctx:ZCodeParser.If_stmt_contentContext):
        return ctx.stmt().accept(self)


    # Visit a parse tree produced by ZCodeParser#if_stmt.
    def visitIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        expr = ctx.expr().accept(self)
        thenStmt = ctx.if_stmt_content().accept(self)
        stmt_list = ctx.if_stmt_tail().accept(self)
        elifStmt = stmt_list[:-1]
        elseStmt = stmt_list[-1]
        return If(expr, thenStmt, elifStmt, elseStmt)


    # Visit a parse tree produced by ZCodeParser#if_stmt_tail.
    def visitIf_stmt_tail(self, ctx:ZCodeParser.If_stmt_tailContext):
        if(ctx.getChildCount() == 0):
            return [None]
        if(ctx.ELSE()):
            return [ctx.if_stmt_content().accept(self)]
        if(ctx.ELIF()):
            return [(ctx.expr().accept(self), ctx.if_stmt_content().accept(self))] + ctx.if_stmt_tail().accept(self)
 

    # Visit a parse tree produced by ZCodeParser#for_stmt.
    def visitFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        name = Id(ctx.IDENTIFIER().getText())
        condExpr = ctx.expr(0).accept(self)
        updExpr = ctx.expr(1).accept(self)
        body = ctx.stmt().accept(self)
        return For(name, condExpr, updExpr, body)


    # Visit a parse tree produced by ZCodeParser#break_stmt.
    def visitBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        return Break()


    # Visit a parse tree produced by ZCodeParser#cont_stmt.
    def visitCont_stmt(self, ctx:ZCodeParser.Cont_stmtContext):
        return Continue()


    # Visit a parse tree produced by ZCodeParser#arg_list.
    def visitArg_list(self, ctx:ZCodeParser.Arg_listContext):
        if(ctx.getChildCount() == 0):
            return []
        else:
            return [ctx.expr().accept(self)] + ctx.arg_list_tail().accept(self)


    # Visit a parse tree produced by ZCodeParser#arg_list_tail.
    def visitArg_list_tail(self, ctx:ZCodeParser.Arg_list_tailContext):
        if(ctx.getChildCount() == 0):
            return []
        else:
            return [ctx.expr().accept(self)] + ctx.arg_list_tail().accept(self)


    # Visit a parse tree produced by ZCodeParser#func_call_stmt.
    def visitFunc_call_stmt(self, ctx:ZCodeParser.Func_call_stmtContext):
        return CallStmt(Id(ctx.IDENTIFIER().getText()), ctx.arg_list().accept(self))
      
    def visitFunc_call_expr(self, ctx:ZCodeParser.Func_call_exprContext):
        return CallExpr(Id(ctx.IDENTIFIER().getText()), ctx.arg_list().accept(self))

      
    
