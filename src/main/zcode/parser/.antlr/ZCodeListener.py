# Generated from /Users/leviettung/Library/CloudStorage/OneDrive-Personal/source/python/zcode-3/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete listener for a parse tree produced by ZCodeParser.
class ZCodeListener(ParseTreeListener):

    # Enter a parse tree produced by ZCodeParser#program.
    def enterProgram(self, ctx:ZCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by ZCodeParser#program.
    def exitProgram(self, ctx:ZCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by ZCodeParser#program_tail.
    def enterProgram_tail(self, ctx:ZCodeParser.Program_tailContext):
        pass

    # Exit a parse tree produced by ZCodeParser#program_tail.
    def exitProgram_tail(self, ctx:ZCodeParser.Program_tailContext):
        pass


    # Enter a parse tree produced by ZCodeParser#decl.
    def enterDecl(self, ctx:ZCodeParser.DeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#decl.
    def exitDecl(self, ctx:ZCodeParser.DeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt.
    def enterStmt(self, ctx:ZCodeParser.StmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt.
    def exitStmt(self, ctx:ZCodeParser.StmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#nullable_newline_list.
    def enterNullable_newline_list(self, ctx:ZCodeParser.Nullable_newline_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#nullable_newline_list.
    def exitNullable_newline_list(self, ctx:ZCodeParser.Nullable_newline_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#nullable_newline_list_tail.
    def enterNullable_newline_list_tail(self, ctx:ZCodeParser.Nullable_newline_list_tailContext):
        pass

    # Exit a parse tree produced by ZCodeParser#nullable_newline_list_tail.
    def exitNullable_newline_list_tail(self, ctx:ZCodeParser.Nullable_newline_list_tailContext):
        pass


    # Enter a parse tree produced by ZCodeParser#newline_list.
    def enterNewline_list(self, ctx:ZCodeParser.Newline_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#newline_list.
    def exitNewline_list(self, ctx:ZCodeParser.Newline_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#newline_list_tail.
    def enterNewline_list_tail(self, ctx:ZCodeParser.Newline_list_tailContext):
        pass

    # Exit a parse tree produced by ZCodeParser#newline_list_tail.
    def exitNewline_list_tail(self, ctx:ZCodeParser.Newline_list_tailContext):
        pass


    # Enter a parse tree produced by ZCodeParser#id_single.
    def enterId_single(self, ctx:ZCodeParser.Id_singleContext):
        pass

    # Exit a parse tree produced by ZCodeParser#id_single.
    def exitId_single(self, ctx:ZCodeParser.Id_singleContext):
        pass


    # Enter a parse tree produced by ZCodeParser#decl_array.
    def enterDecl_array(self, ctx:ZCodeParser.Decl_arrayContext):
        pass

    # Exit a parse tree produced by ZCodeParser#decl_array.
    def exitDecl_array(self, ctx:ZCodeParser.Decl_arrayContext):
        pass


    # Enter a parse tree produced by ZCodeParser#decl_array_list.
    def enterDecl_array_list(self, ctx:ZCodeParser.Decl_array_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#decl_array_list.
    def exitDecl_array_list(self, ctx:ZCodeParser.Decl_array_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#decl_array_list_tail.
    def enterDecl_array_list_tail(self, ctx:ZCodeParser.Decl_array_list_tailContext):
        pass

    # Exit a parse tree produced by ZCodeParser#decl_array_list_tail.
    def exitDecl_array_list_tail(self, ctx:ZCodeParser.Decl_array_list_tailContext):
        pass


    # Enter a parse tree produced by ZCodeParser#ass_array.
    def enterAss_array(self, ctx:ZCodeParser.Ass_arrayContext):
        pass

    # Exit a parse tree produced by ZCodeParser#ass_array.
    def exitAss_array(self, ctx:ZCodeParser.Ass_arrayContext):
        pass


    # Enter a parse tree produced by ZCodeParser#ass_array_list.
    def enterAss_array_list(self, ctx:ZCodeParser.Ass_array_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#ass_array_list.
    def exitAss_array_list(self, ctx:ZCodeParser.Ass_array_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#ass_array_list_tail.
    def enterAss_array_list_tail(self, ctx:ZCodeParser.Ass_array_list_tailContext):
        pass

    # Exit a parse tree produced by ZCodeParser#ass_array_list_tail.
    def exitAss_array_list_tail(self, ctx:ZCodeParser.Ass_array_list_tailContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arr.
    def enterArr(self, ctx:ZCodeParser.ArrContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arr.
    def exitArr(self, ctx:ZCodeParser.ArrContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_list.
    def enterArray_list(self, ctx:ZCodeParser.Array_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_list.
    def exitArray_list(self, ctx:ZCodeParser.Array_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_list_tail.
    def enterArray_list_tail(self, ctx:ZCodeParser.Array_list_tailContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_list_tail.
    def exitArray_list_tail(self, ctx:ZCodeParser.Array_list_tailContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arr_content.
    def enterArr_content(self, ctx:ZCodeParser.Arr_contentContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arr_content.
    def exitArr_content(self, ctx:ZCodeParser.Arr_contentContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr.
    def enterExpr(self, ctx:ZCodeParser.ExprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr.
    def exitExpr(self, ctx:ZCodeParser.ExprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr1.
    def enterExpr1(self, ctx:ZCodeParser.Expr1Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr1.
    def exitExpr1(self, ctx:ZCodeParser.Expr1Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr2.
    def enterExpr2(self, ctx:ZCodeParser.Expr2Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr2.
    def exitExpr2(self, ctx:ZCodeParser.Expr2Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr3.
    def enterExpr3(self, ctx:ZCodeParser.Expr3Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr3.
    def exitExpr3(self, ctx:ZCodeParser.Expr3Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr4.
    def enterExpr4(self, ctx:ZCodeParser.Expr4Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr4.
    def exitExpr4(self, ctx:ZCodeParser.Expr4Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr5.
    def enterExpr5(self, ctx:ZCodeParser.Expr5Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr5.
    def exitExpr5(self, ctx:ZCodeParser.Expr5Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr6.
    def enterExpr6(self, ctx:ZCodeParser.Expr6Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr6.
    def exitExpr6(self, ctx:ZCodeParser.Expr6Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr7.
    def enterExpr7(self, ctx:ZCodeParser.Expr7Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr7.
    def exitExpr7(self, ctx:ZCodeParser.Expr7Context):
        pass


    # Enter a parse tree produced by ZCodeParser#index_op.
    def enterIndex_op(self, ctx:ZCodeParser.Index_opContext):
        pass

    # Exit a parse tree produced by ZCodeParser#index_op.
    def exitIndex_op(self, ctx:ZCodeParser.Index_opContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr8.
    def enterExpr8(self, ctx:ZCodeParser.Expr8Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr8.
    def exitExpr8(self, ctx:ZCodeParser.Expr8Context):
        pass


    # Enter a parse tree produced by ZCodeParser#index_expr.
    def enterIndex_expr(self, ctx:ZCodeParser.Index_exprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#index_expr.
    def exitIndex_expr(self, ctx:ZCodeParser.Index_exprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#decl_typ_no_var.
    def enterDecl_typ_no_var(self, ctx:ZCodeParser.Decl_typ_no_varContext):
        pass

    # Exit a parse tree produced by ZCodeParser#decl_typ_no_var.
    def exitDecl_typ_no_var(self, ctx:ZCodeParser.Decl_typ_no_varContext):
        pass


    # Enter a parse tree produced by ZCodeParser#decl_typ_arr.
    def enterDecl_typ_arr(self, ctx:ZCodeParser.Decl_typ_arrContext):
        pass

    # Exit a parse tree produced by ZCodeParser#decl_typ_arr.
    def exitDecl_typ_arr(self, ctx:ZCodeParser.Decl_typ_arrContext):
        pass


    # Enter a parse tree produced by ZCodeParser#var.
    def enterVar(self, ctx:ZCodeParser.VarContext):
        pass

    # Exit a parse tree produced by ZCodeParser#var.
    def exitVar(self, ctx:ZCodeParser.VarContext):
        pass


    # Enter a parse tree produced by ZCodeParser#var_decl.
    def enterVar_decl(self, ctx:ZCodeParser.Var_declContext):
        pass

    # Exit a parse tree produced by ZCodeParser#var_decl.
    def exitVar_decl(self, ctx:ZCodeParser.Var_declContext):
        pass


    # Enter a parse tree produced by ZCodeParser#param_decl_typ.
    def enterParam_decl_typ(self, ctx:ZCodeParser.Param_decl_typContext):
        pass

    # Exit a parse tree produced by ZCodeParser#param_decl_typ.
    def exitParam_decl_typ(self, ctx:ZCodeParser.Param_decl_typContext):
        pass


    # Enter a parse tree produced by ZCodeParser#param_decl.
    def enterParam_decl(self, ctx:ZCodeParser.Param_declContext):
        pass

    # Exit a parse tree produced by ZCodeParser#param_decl.
    def exitParam_decl(self, ctx:ZCodeParser.Param_declContext):
        pass


    # Enter a parse tree produced by ZCodeParser#param_decl_content.
    def enterParam_decl_content(self, ctx:ZCodeParser.Param_decl_contentContext):
        pass

    # Exit a parse tree produced by ZCodeParser#param_decl_content.
    def exitParam_decl_content(self, ctx:ZCodeParser.Param_decl_contentContext):
        pass


    # Enter a parse tree produced by ZCodeParser#param_decl_list.
    def enterParam_decl_list(self, ctx:ZCodeParser.Param_decl_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#param_decl_list.
    def exitParam_decl_list(self, ctx:ZCodeParser.Param_decl_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#param_decl_list_tail.
    def enterParam_decl_list_tail(self, ctx:ZCodeParser.Param_decl_list_tailContext):
        pass

    # Exit a parse tree produced by ZCodeParser#param_decl_list_tail.
    def exitParam_decl_list_tail(self, ctx:ZCodeParser.Param_decl_list_tailContext):
        pass


    # Enter a parse tree produced by ZCodeParser#func_decl.
    def enterFunc_decl(self, ctx:ZCodeParser.Func_declContext):
        pass

    # Exit a parse tree produced by ZCodeParser#func_decl.
    def exitFunc_decl(self, ctx:ZCodeParser.Func_declContext):
        pass


    # Enter a parse tree produced by ZCodeParser#body_content.
    def enterBody_content(self, ctx:ZCodeParser.Body_contentContext):
        pass

    # Exit a parse tree produced by ZCodeParser#body_content.
    def exitBody_content(self, ctx:ZCodeParser.Body_contentContext):
        pass


    # Enter a parse tree produced by ZCodeParser#body_list.
    def enterBody_list(self, ctx:ZCodeParser.Body_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#body_list.
    def exitBody_list(self, ctx:ZCodeParser.Body_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#body_list_tail.
    def enterBody_list_tail(self, ctx:ZCodeParser.Body_list_tailContext):
        pass

    # Exit a parse tree produced by ZCodeParser#body_list_tail.
    def exitBody_list_tail(self, ctx:ZCodeParser.Body_list_tailContext):
        pass


    # Enter a parse tree produced by ZCodeParser#block_stmt.
    def enterBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#block_stmt.
    def exitBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#ret_stmt.
    def enterRet_stmt(self, ctx:ZCodeParser.Ret_stmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#ret_stmt.
    def exitRet_stmt(self, ctx:ZCodeParser.Ret_stmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#ret_stmt_tail.
    def enterRet_stmt_tail(self, ctx:ZCodeParser.Ret_stmt_tailContext):
        pass

    # Exit a parse tree produced by ZCodeParser#ret_stmt_tail.
    def exitRet_stmt_tail(self, ctx:ZCodeParser.Ret_stmt_tailContext):
        pass


    # Enter a parse tree produced by ZCodeParser#ass_stmt.
    def enterAss_stmt(self, ctx:ZCodeParser.Ass_stmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#ass_stmt.
    def exitAss_stmt(self, ctx:ZCodeParser.Ass_stmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#if_stmt_content.
    def enterIf_stmt_content(self, ctx:ZCodeParser.If_stmt_contentContext):
        pass

    # Exit a parse tree produced by ZCodeParser#if_stmt_content.
    def exitIf_stmt_content(self, ctx:ZCodeParser.If_stmt_contentContext):
        pass


    # Enter a parse tree produced by ZCodeParser#if_stmt.
    def enterIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#if_stmt.
    def exitIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#if_stmt_tail.
    def enterIf_stmt_tail(self, ctx:ZCodeParser.If_stmt_tailContext):
        pass

    # Exit a parse tree produced by ZCodeParser#if_stmt_tail.
    def exitIf_stmt_tail(self, ctx:ZCodeParser.If_stmt_tailContext):
        pass


    # Enter a parse tree produced by ZCodeParser#for_stmt.
    def enterFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#for_stmt.
    def exitFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#break_stmt.
    def enterBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#break_stmt.
    def exitBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#cont_stmt.
    def enterCont_stmt(self, ctx:ZCodeParser.Cont_stmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#cont_stmt.
    def exitCont_stmt(self, ctx:ZCodeParser.Cont_stmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arg_list.
    def enterArg_list(self, ctx:ZCodeParser.Arg_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arg_list.
    def exitArg_list(self, ctx:ZCodeParser.Arg_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arg_list_tail.
    def enterArg_list_tail(self, ctx:ZCodeParser.Arg_list_tailContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arg_list_tail.
    def exitArg_list_tail(self, ctx:ZCodeParser.Arg_list_tailContext):
        pass


    # Enter a parse tree produced by ZCodeParser#func_call_stmt.
    def enterFunc_call_stmt(self, ctx:ZCodeParser.Func_call_stmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#func_call_stmt.
    def exitFunc_call_stmt(self, ctx:ZCodeParser.Func_call_stmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#func_call_expr.
    def enterFunc_call_expr(self, ctx:ZCodeParser.Func_call_exprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#func_call_expr.
    def exitFunc_call_expr(self, ctx:ZCodeParser.Func_call_exprContext):
        pass



del ZCodeParser