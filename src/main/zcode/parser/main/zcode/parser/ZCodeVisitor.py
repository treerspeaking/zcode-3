# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#program_tail.
    def visitProgram_tail(self, ctx:ZCodeParser.Program_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt.
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#nullable_newline_list.
    def visitNullable_newline_list(self, ctx:ZCodeParser.Nullable_newline_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#nullable_newline_list_tail.
    def visitNullable_newline_list_tail(self, ctx:ZCodeParser.Nullable_newline_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#newline_list.
    def visitNewline_list(self, ctx:ZCodeParser.Newline_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#newline_list_tail.
    def visitNewline_list_tail(self, ctx:ZCodeParser.Newline_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#id_single.
    def visitId_single(self, ctx:ZCodeParser.Id_singleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl_array.
    def visitDecl_array(self, ctx:ZCodeParser.Decl_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl_array_list.
    def visitDecl_array_list(self, ctx:ZCodeParser.Decl_array_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl_array_list_tail.
    def visitDecl_array_list_tail(self, ctx:ZCodeParser.Decl_array_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ass_array.
    def visitAss_array(self, ctx:ZCodeParser.Ass_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ass_array_list.
    def visitAss_array_list(self, ctx:ZCodeParser.Ass_array_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ass_array_list_tail.
    def visitAss_array_list_tail(self, ctx:ZCodeParser.Ass_array_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arr.
    def visitArr(self, ctx:ZCodeParser.ArrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_list.
    def visitArray_list(self, ctx:ZCodeParser.Array_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_list_tail.
    def visitArray_list_tail(self, ctx:ZCodeParser.Array_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arr_content.
    def visitArr_content(self, ctx:ZCodeParser.Arr_contentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr1.
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr2.
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr3.
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr4.
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr5.
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr6.
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr7.
    def visitExpr7(self, ctx:ZCodeParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_op.
    def visitIndex_op(self, ctx:ZCodeParser.Index_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr8.
    def visitExpr8(self, ctx:ZCodeParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_expr.
    def visitIndex_expr(self, ctx:ZCodeParser.Index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl_typ_no_var.
    def visitDecl_typ_no_var(self, ctx:ZCodeParser.Decl_typ_no_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl_typ_arr.
    def visitDecl_typ_arr(self, ctx:ZCodeParser.Decl_typ_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var.
    def visitVar(self, ctx:ZCodeParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_decl.
    def visitVar_decl(self, ctx:ZCodeParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_decl_typ.
    def visitParam_decl_typ(self, ctx:ZCodeParser.Param_decl_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_decl.
    def visitParam_decl(self, ctx:ZCodeParser.Param_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_decl_content.
    def visitParam_decl_content(self, ctx:ZCodeParser.Param_decl_contentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_decl_list.
    def visitParam_decl_list(self, ctx:ZCodeParser.Param_decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_decl_list_tail.
    def visitParam_decl_list_tail(self, ctx:ZCodeParser.Param_decl_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_decl.
    def visitFunc_decl(self, ctx:ZCodeParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#body_content.
    def visitBody_content(self, ctx:ZCodeParser.Body_contentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#body_list.
    def visitBody_list(self, ctx:ZCodeParser.Body_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#body_list_tail.
    def visitBody_list_tail(self, ctx:ZCodeParser.Body_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_stmt.
    def visitBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ret_stmt.
    def visitRet_stmt(self, ctx:ZCodeParser.Ret_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ret_stmt_tail.
    def visitRet_stmt_tail(self, ctx:ZCodeParser.Ret_stmt_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ass_stmt.
    def visitAss_stmt(self, ctx:ZCodeParser.Ass_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_stmt_content.
    def visitIf_stmt_content(self, ctx:ZCodeParser.If_stmt_contentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_stmt.
    def visitIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_stmt_tail.
    def visitIf_stmt_tail(self, ctx:ZCodeParser.If_stmt_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_stmt.
    def visitFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#break_stmt.
    def visitBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#cont_stmt.
    def visitCont_stmt(self, ctx:ZCodeParser.Cont_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arg_list.
    def visitArg_list(self, ctx:ZCodeParser.Arg_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arg_list_tail.
    def visitArg_list_tail(self, ctx:ZCodeParser.Arg_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_call_stmt.
    def visitFunc_call_stmt(self, ctx:ZCodeParser.Func_call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_call_expr.
    def visitFunc_call_expr(self, ctx:ZCodeParser.Func_call_exprContext):
        return self.visitChildren(ctx)



del ZCodeParser