grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
    language=Python3;
}



program: decl EOF;
decl: class_decl decl | class_decl;

//-----------------------------------------------------------------
//-------------------- 2 PROGRAM STRUCTURE ------------------------
//-----------------------------------------------------------------

//---------Class declaration----------
class_decl: CLASS ID superclass LB memberlist RB;
superclass: EXTENDS ID | ;
memberlist: member memberlist |;
member: variable_decl | method_decl;

//---------Attribute declaration-------

variable_decl: (FINAL STATIC | STATIC FINAL | STATIC | FINAL |) type_name attribute_list SEMI;

attribute_list: attribute COMMA attribute_list | attribute;
attribute: ID | ID EQ expr;

//---------Method declaration ---------
method_decl: normalMethod | constructor | mainMethod | voidMethod;
normalMethod: STATIC? type_name ID LB paramlist? RB block_stmt;
mainMethod: STATIC? VOID 'main' LB RB block_stmt;
voidMethod: STATIC? VOID ID LB paramlist? RB block_stmt;
constructor: ID LB paramlist? RB block_stmt;



type_name: INT | FLOAT | BOOLEAN | STRING | array_type | class_type;
paramlist: param COMMA paramlist | param;
param: idlist COLON type_name;
idlist: ID COMMA idlist | ID;



//-----------------------------------------------------------------
//-------------------- 6 STATEMENT --------------------------------
//-----------------------------------------------------------------
block_stmt: LB block_body RB;
block_body: blocks | ;
blocks: stmt blocks | stmt;

stmt: variable_decl | assignment_stmt | if_stmt | for_stmt | break_stmt | continue_stmt | return_stmt | method_invo_stmt | block_stmt;



//------- 6.1 assignment ------------
assignment_stmt: lhs ASSIGN expr SEMI;

lhs: exp9 indexop| scalar_variable ;
scalar_variable: ID | exp9 DOT ID | exp10_access;

//------- 6.2 if else ----------------
if_stmt: IF expr THEN (stmt|block_stmt) else_stmt?;
else_stmt: ELSE (stmt|block_stmt);

//------- 6.3 for in ------------------
for_stmt: FOR scalar_variable ASSIGN expr (DOWNTO|TO) expr (stmt|block_stmt);

//------- 6.4 break continue return-- ##############
break_stmt: BREAK SEMI;

continue_stmt: CONTINUE SEMI;

return_stmt: RETURN expr? SEMI;

//-------- 6.5 method invocation-------
method_invo_stmt: method_invo SEMI;
method_invo: exp9_method;
exp9_method: exp9 DOT ID LR exp_list RR;



//-----------------------------------------------------------------
//-------------------- 5 EXPRESSION -------------------------------
//-----------------------------------------------------------------

expr: exp2 CONCAT exp2 | exp2;

exp2: 	exp3 relational exp3 | exp3;
relational: EQQ | NOTEQ | LT | GT | LTEQ | GTEQ;

exp3: exp3 AND exp4 | exp3 OR exp4 | exp4;

exp4: exp4 ADD exp5 | exp4 SUB exp5 | exp5;

exp5: exp5 MUL exp6 | exp5 DIV exp6 | exp5 MOD exp6 | exp5 IDIV exp6 | exp6 ;

exp6: NOT exp6 | exp7;

exp7: (SUB | ADD) exp7 | exp8;

//index exp
exp8: exp9 indexop | exp9;
indexop: LS expr RS indexop|LS expr RS;

exp9: exp9 DOT tail_part | exp13;
tail_part: ID | ID LR exp_list RR;


exp13: THIS | exp10 ;

exp10: exp10_access | exp10_call | exp11;
exp10_access: ID DOT ID;
exp10_call: ID DOT ID LR exp_list RR;

//new value(exp) in rhs
exp11: NEW ID LR exp_list RR | exp12;
exp_list: exps | ;
exps: expr COMMA exps | expr;

//operand
exp12: literal | ID | LR expr RR;
//-----------------------------------------------------------------
//-------------------- 4 TYPE AND VALUE ---------------------------
//-----------------------------------------------------------------

//----------4.1 primitive type------
primitive_type: INT | FLOAT | BOOLEAN | STRING | VOID;

//----------4.2 array type----------
array_type: element_type LS  (size)? RS;
element_type: INT | FLOAT | BOOLEAN | STRING | class_type;
size: INTLIT;

//----------4.3 class type----------D
class_type: ID;

//-----------------------------------------------------------------
//-------------------- 3 LEXICAL STRUCTURE ------------------------
//-----------------------------------------------------------------

//----------3.1 Char set------------
WS : [ \f\t\r\n]+ -> skip ;

//-----------3.2 comment------------
COMMENT : (('/*' .*? '*/') | ('#' .*? EOF ))-> skip;

//------------3.4 keyword-----------
BOOLEAN: 'boolean';
BREAK: 'break';
CLASS: 'class';
CONTINUE: 'continue';
DO: 'do';
IF: 'if';
ELSE: 'else';
EXTENDS: 'extends';
INT: 'int';
FLOAT: 'float';
NEW: 'new';
STRING: 'string';
THEN: 'then';
FOR: 'for';
RETURN: 'return';
TRUE: 'true';
FALSE: 'false';
VOID: 'void';
NIL: 'nil';
THIS: 'this';
FINAL: 'final';
STATIC: 'static';
TO: 'to';
DOWNTO: 'downto';

//----------3.5 operator------------
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/'; //float division
IDIV: '\\'; //int division
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQQ: '==';
EQ: '=';
NOTEQ: '!=';
LT: '<';
LTEQ: '<=';
GT: '>';
GTEQ: '>=';
CONCAT: '^';
SCOPE: '::';
ASSIGN: ':=';
//NEW: 'new'

//----------3.6 seperator-----------
LR: '(';
RR: ')';
LS: '[';
RS: ']';
DOT: '.';
COMMA: ',';
SEMI: ';';
COLON: ':';
LB: '{';
RB: '}';

//------------3.7 literal -----------
literal: INTLIT | FLOATLIT | boolean_lit | STRING_LIT | indexarr_lit| NIL;

//------int-------
INTLIT: DIGIT+;

//------float-----
FLOATLIT	: (INT_PART DEC_PART
            | INT_PART EXP_PART
            | INT_PART DEC_PART EXP_PART) ;

fragment INT_PART: INTLIT;
fragment DEC_PART: '.'[0-9]*;
fragment EXP_PART: [eE][+-]?[0-9]+;

//------boolean-----
boolean_lit: TRUE | FALSE;
//TRUE: 'True';
//FALSE: 'False';
//------string------
fragment STR_CHAR: (~[\\\n\b\t\f\r"] | ESC_SEQUENCE | '\'"');
fragment ESC_SEQUENCE: '\\' [bfrtn'\\];

STRING_LIT: '"'STR_CHAR*'"'
    {
    self.text = self.text[1:-1]
    };

//-------index arr---
arr_exp : literal | literal COMMA arr_exp;
indexarr_lit: LB arr_exp RB;

//------------3.3 ID----------------
ID: (LETTER | UNDERSCORE) (LETTER | DIGIT | UNDERSCORE)*;

//------------------------ fragment --------------------------------
LETTER: [a-zA-Z];
DIGIT: [0-9];
UNDERSCORE: '_';

//------------------------------------------------------------------
fragment ILL_ESCAPE: '\\' ~[btnfr'\\];

UNCLOSE_STRING: '"' STR_CHAR* ([\n\b\t\r\f]|EOF){
    self.text = self.text[1:]
    if self.text[-1] in "\b\t\n\f\r":
	    self.text=self.text[:-1]

    raise UncloseString(self.text)
};

ILLEGAL_ESCAPE:'"' STR_CHAR* ILL_ESCAPE{
    raise IllegalEscape(self.text[1:])
};

ERROR_TOKEN: .{
    raise ErrorToken(self.text)
};