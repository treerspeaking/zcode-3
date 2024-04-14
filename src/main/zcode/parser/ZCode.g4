// java org.antlr.v4.Toolgrammar ZCode;
grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: nullable_newline_list decl program_tail ;
program_tail: decl program_tail | nullable_newline_list EOF;

// change this to declaration end in new line
decl: var_decl | func_decl;

// stmt
stmt:
  (func_call_stmt|
  cont_stmt|
  break_stmt|
  ret_stmt|
  ass_stmt|
  block_stmt) newline_list | // newline_list for block_stmt very good
  (if_stmt | for_stmt | var_decl )
  // good fucking language
  ;

//support stuff
nullable_newline_list: NEWLINE nullable_newline_list_tail |;
nullable_newline_list_tail: NEWLINE nullable_newline_list_tail | ;
newline_list: NEWLINE newline_list_tail;
newline_list_tail: newline_list newline_list_tail | ;

// declare id
id_single: IDENTIFIER;
// declare array
decl_array: IDENTIFIER LSB decl_array_list RSB;
decl_array_list: NUM_LIT decl_array_list_tail;
decl_array_list_tail: COMMA NUM_LIT decl_array_list_tail | ;

//assign array
ass_array: IDENTIFIER LSB ass_array_list RSB;
ass_array_list: expr ass_array_list_tail;
ass_array_list_tail: COMMA expr ass_array_list_tail | ;


// array list only
arr: LSB array_list RSB;
array_list: arr_content array_list_tail ; // this might not be an empty arr although dim 0 !!!???
array_list_tail: COMMA arr_content array_list_tail | ;
arr_content: arr | NUM_LIT | STR_LIT | BOOL_LIT | expr;

// [1,2,3]

// expr
expr: expr1 CONCAT expr1| expr1;
expr1: expr2 (EQUAL | DEQUAL | NOT_EQUAL | LESS | GREATER | LESS_EQUAL | GREATER_EQUAL) expr2 | expr2;
expr2: expr2 (AND | OR ) expr3 | expr3;
expr3: expr3 (PLUS | MINUS) expr4 | expr4;
expr4: expr4 (MULTIPLY | DIVIDE | MODULO ) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: MINUS expr6 | expr7;
expr7: (IDENTIFIER | func_call_expr) LSB index_op RSB | expr8; // 
index_op: expr COMMA index_op | expr; // expr1, expr2, expr3, ... exprn
expr8: STR_LIT | NUM_LIT | BOOL_LIT | IDENTIFIER 
| arr
| func_call_expr
| LRB expr RRB;

index_expr: (IDENTIFIER | func_call_expr) LSB index_op RSB; // for the situtation foo()[7]

// typ
decl_typ_no_var: DYNAMIC | NUM | BOOL | STR;
decl_typ_arr: NUM | BOOL | STR;
var: VAR;
 
// var declaration
var_decl: 
  (decl_typ_no_var id_single (ASSIGN expr)?|
  decl_typ_arr decl_array (ASSIGN expr)?|
  var id_single ASSIGN expr) newline_list
  ;
  // does var need to have assign at the start
  // does array need to be of diff typ

// param decl
param_decl_typ: NUM | BOOL | STR; 
param_decl: LRB param_decl_list RRB;
param_decl_content: param_decl_typ (id_single | decl_array);
param_decl_list: param_decl_content param_decl_list_tail  | ;
param_decl_list_tail: COMMA param_decl_content param_decl_list_tail | ;

// function
func_decl: FUNC IDENTIFIER param_decl (nullable_newline_list (ret_stmt|block_stmt) )? newline_list;

// body stmt
body_content: var_decl | stmt;
body_list: body_content body_list_tail | ;
body_list_tail: nullable_newline_list body_content body_list_tail | ;
// remember to fucking add newline_list at the end every time else 
block_stmt
		: BEGIN newline_list 
    body_list 
    END 
		;


// return stmt
ret_stmt: RETURN ret_stmt_tail;
ret_stmt_tail: expr | ;
// assignment
ass_stmt: (id_single | ass_array | index_expr) ASSIGN expr;

// if stmt
// if stmt does not require newline_list at the end ?
if_stmt_content: nullable_newline_list stmt;
if_stmt: IF LRB expr RRB if_stmt_content if_stmt_tail ;
if_stmt_tail: nullable_newline_list ELIF LRB expr RRB if_stmt_content if_stmt_tail| nullable_newline_list ELSE if_stmt_content | ;


// for stmt
for_stmt
		: FOR IDENTIFIER UNTIL expr BY expr nullable_newline_list
    stmt
		;

// break stmt
break_stmt: BREAK;

// continue stmt
cont_stmt: CONTINUE;


// func call stmt
// does this still have a line break?
arg_list: expr arg_list_tail | ;
arg_list_tail: COMMA expr arg_list_tail | ;
func_call_stmt: IDENTIFIER LRB arg_list RRB;
func_call_expr: IDENTIFIER LRB arg_list RRB;






BOOL_LIT: TRUE | FALSE;
NUM_LIT : [0-9]+ ('.'[0-9]*)? ([eE][+-]?[0-9]+)?;
// i shouldn't do this it feel fkin shit and antlr-parse can't parse it properly // wrong one for some reason
// STR_LIT   :["] ('\\' [bfrnt'\\] | [']["] | ~[\f\r\n"\\] )* ["]
// 			{self.text = self.text[1:-1]}
// 			;
STR_LIT   :["] ('\\' [bfrnt'\\] | ('\'' {self._input.LA(1)!=ord("\"")}? | '\'"') | ~[\r\n"'\\] )* ["] // right one
			{self.text = self.text[1:-1]}
			;
//KEYWORDS
TRUE: 'true';
FALSE: 'false';
NUM: 'number';
BOOL: 'bool';
STR: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';

// OPERATORS

PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
MODULO: '%';
NOT: 'not';
AND: 'and';
OR: 'or' ;
ASSIGN: '<-';
EQUAL: '=';
DEQUAL: '==';
NOT_EQUAL: '!=';
LESS: '<';
LESS_EQUAL: '<=';
GREATER: '>';
GREATER_EQUAL: '>=';
CONCAT: '...';

//SEPARATORS
LSB     : '[';
RSB     : ']';
// LCB      : '{';
// RCB      : '}';
LRB      : '(';
RRB      : ')';
// SEMI    : ';';
COMMA   : ',';



// {self._input.LA(1) != '"'}? 
NEWLINE: 
NL1  {if self.text == '\r\n':  
    self.text = '\n'
  }
| NL2 {self.text = '\n'}
| NL3 {self.text = '\n'}
;
NL1: '\r'? '\n' {
  if self.text == '\r\n':  
    self.text = '\n'
  }; // Handles both Windows (\r\n) and Unix (\n) line endings
NL2: '\r' {self.text = '\n'};
NL3: '\r\r\n' {self.text = '\n'};



// skip comment
COMMENT_LINE: '##' ~[\r\n]* -> skip;
IDENTIFIER: [a-zA-Z_] [a-z0-9A-Z_]*;

// fnewline: '\f';
WS: [ \t\b\f]+ -> skip; // skip spaces, tab



ILLEGAL_ESCAPE  :["]('\\' [bfrnt'\\] | ('\'' {self._input.LA(1)!=ord("\"")}? | '\'"') | ~[\r\n"'\\] )* ('\\' ~[bnrft'] |'\\' ) // right one
				{raise IllegalEscape(self.text[1:])}
				;


UNCLOSE_STRING  :["] ('\\' [bfrnt'\\] | ('\'' {self._input.LA(1)!=ord("\"")}? | '\'"') | ~[\r\n"'\\] )*
				{raise UncloseString(self.text[1:])}
				;
ERROR_CHAR: . 
 {raise ErrorToken(self.text)}
;

