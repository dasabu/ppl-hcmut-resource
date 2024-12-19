// ID 1912190
// Nguyễn Mai Thy

grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: decl EOF;
decl: class_decl decl | class_decl;

//-----------------------------------------------------------------
//-------------------- 2 PROGRAM STRUCTURE ------------------------
//-----------------------------------------------------------------

//---------Class declaration----------
class_decl: CLASS ID superclass LB memberlist RB;
superclass: COLON ID | ;
memberlist: members | ;
members: member members | member;
member: variable_decl| method_decl;

//---------Attribute declaration-------
variable_decl: with_init | without_init;

without_init: (VAR | VAL) attribute_list COLON type_name SEMI;
attribute_list: attribute COMMA attribute_list | attribute;
attribute: ID | DOLLAR_ID;

type_name: INT | FLOAT | BOOLEAN | STRING | array_type | class_type;

with_init: (VAR | VAL) pair_list SEMI;
pair_list: attribute pair expr;
pair: COMMA attribute pair expr COMMA | COLON type_name EQ;

//---------Method declaration ---------
method_decl: normal_method | destruct_method | construct_method;

normal_method: method_name LR paramlist RR block_stmt;
method_name: ID | DOLLAR_ID;
paramlist: params | ;
params: param SEMI params | param;
param: idlist COLON type_name;
idlist: ID COMMA idlist | ID; 

construct_method: CONTSTRUCTOR LR paramlist RR block_stmt;

destruct_method: DESTRUCTOR LR RR block_stmt;

//-----------------------------------------------------------------
//-------------------- 6 STATEMENT --------------------------------
//-----------------------------------------------------------------
block_stmt: LB block_body RB;
block_body: blocks | ;
blocks: stmt blocks | stmt;

stmt: vardecl_stmt | assignment_stmt | if_stmt | for_stmt | break_stmt | continue_stmt | return_stmt | method_invo_stmt | block_stmt;

//------- 6.1 var and const ---------
vardecl_stmt: with_init2 | without_init2;

without_init2: (VAR | VAL) attribute_list2 COLON type_name SEMI;
attribute_list2: ID COMMA attribute_list2 | ID;

with_init2: (VAR | VAL) pair_list2 SEMI;
pair_list2: ID pair2 expr;
pair2: COMMA ID pair2 expr COMMA | COLON type_name EQ;

//------- 6.2 assignment ------------
assignment_stmt: left_exp EQ expr SEMI;

left_exp: scalar_variable | exp9 indexop; 
scalar_variable: ID | DOLLAR_ID | exp9 DOT ID | exp10_access;

//------- 6.3 if else ----------------
if_stmt: if_part elseif_list; 
if_part: IF LR expr RR block_stmt;
elseif_list: elif_stmt elseif_list | else_part;
elif_stmt: ELSEIF LR expr RR block_stmt;
else_part: ELSE block_stmt | ;

//------- 6.4 for in ------------------
for_stmt: FOREACH LR ID IN expr DOTDOT expr (BY expr)? RR block_stmt;

//------- 6.567 break continue return-- ##############
break_stmt: BREAK SEMI;

continue_stmt: CONTINUE SEMI;

return_stmt: RETURN expr? SEMI;

//-------- 6.8 method invocation-------
method_invo_stmt: method_invo SEMI;
method_invo: exp9_method | exp10_method;
exp9_method: exp9 DOT ID LR exp_list RR;
exp10_method: ID SCOPE DOLLAR_ID LR exp_list RR;

//-----------------------------------------------------------------
//-------------------- 5 EXPRESSION -------------------------------
//-----------------------------------------------------------------

expr: exp2 ADDDOT exp2 | exp2 EQQDOT exp2 | exp2;

exp2: 	exp3 relational exp3 | exp3;
relational: EQQ | NOTEQ | LT | GT | LTEQ | GTEQ;

exp3: exp3 AND exp4 | exp3 OR exp4 | exp4;

exp4: exp4 ADD exp5 | exp4 SUB exp5 | exp5;

exp5: exp5 MUL exp6 | exp5 DIV exp6 | exp5 MOD exp6 | exp6;

exp6: NOT exp6 | exp7;

exp7: SUB exp7 | exp8;

//index exp
exp8: exp9 indexop | exp9;
indexop: LS expr RS indexop|LS expr RS;

exp9: exp9 DOT tail_part | exp13;
tail_part: ID | ID LR exp_list RR;

// exp9: exp9_access | exp9_call | exp13;
// exp9_access: exp9 DOT ID;
// exp9_call: exp9 DOT ID LR exp_list RR;

exp13: SELF | exp10;

exp10: exp10_access | exp10_call | exp11;
exp10_access: ID SCOPE DOLLAR_ID;
exp10_call: ID SCOPE DOLLAR_ID LR exp_list RR;

//new exp
exp11: NEW ID LR exp_list RR | exp12;
exp_list: exps | ;
exps: expr COMMA exps | expr;

//operand
exp12: literal | ID | LR expr RR;

//-----------------------------------------------------------------
//-------------------- 4 TYPE AND VALUE ---------------------------
//-----------------------------------------------------------------

//----------4.1 primitive type------
primitive_type: INT | FLOAT | BOOLEAN | STRING;

//----------4.2 array type----------
array_type: ARRAY LS element_type COMMA size RS;
element_type: primitive_type | array_type;
size: INTLIT;

//----------4.3 class type----------D
class_type: ID;

//-----------------------------------------------------------------
//-------------------- 3 LEXICAL STRUCTURE ------------------------
//-----------------------------------------------------------------

//----------3.1 Char set------------
WS : [ \f\t\r\n]+ -> skip ;

//-----------3.2 comment------------
COMMENT : '##'.*?'##'-> skip;

//------------3.4 keyword-----------
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
FOREACH: 'Foreach';
ARRAY: 'Array';
IN: 'In';
INT: 'Int';
FLOAT: 'Float';
BOOLEAN: 'Boolean';
STRING: 'String';
RETURN: 'Return';
NULL: 'Null';
CLASS: 'Class';
VAL: 'Val';
VAR: 'Var';
CONTSTRUCTOR: 'Constructor';
DESTRUCTOR: 'Destructor';
BY: 'By';
SELF: 'Self';

//----------3.5 operator------------
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
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
EQQDOT: '==.';
ADDDOT: '+.';
SCOPE: '::';
NEW: 'New';

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
DOTDOT: '..';

//------------3.7 literal -----------
literal: INTLIT | ZEROLIT | FLOATLIT | boolean_lit | STRING_LIT | indexarr_lit| NULL;

//------int-------
INTLIT: (DEC | HEX | OCT | BI){ self.text = self.text.replace("_","") };
ZEROLIT: '00' | '0x0' | '0b0' | '0B0' | '0X0' | '0';

fragment DEC: [1-9][0-9]*('_'[0-9]+)*;
fragment HEX: '0'[xX][1-9A-F][0-9A-F]*('_'[0-9A-F]+)*;
fragment OCT: '0'[1-7][0-7]*('_'[0-7]+)*;
fragment BI: '0'[bB][1][01]*('_'[01]+)*;

//------float-----
FLOATLIT	: (INT_PART DEC_PART
            | INT_PART EXP_PART
            | DEC_PART EXP_PART
            | INT_PART DEC_PART EXP_PART) { self.text = self.text.replace("_","") };

fragment INT_PART: DEC | '0';
fragment DEC_PART: '.'[0-9]*;
fragment EXP_PART: [eE][+-]?[0-9]+;

//------boolean-----
boolean_lit: TRUE | FALSE;
TRUE: 'True';
FALSE: 'False';
//------string------
fragment STR_CHAR: (~[\\\n\b\t\f\r"] | ESC_SEQUENCE | '\'"');  
fragment ESC_SEQUENCE: '\\' [bfrtn'\\];

STRING_LIT: '"'STR_CHAR*'"' 
    {
    self.text = self.text[1:-1]
    };

//-------index arr---
indexarr_lit: ARRAY LR exp_list RR;

//------------3.3 ID----------------
ID: (LETTER | UNDERSCORE) (LETTER | DIGIT | UNDERSCORE)*;
DOLLAR_ID: '$' (LETTER | DIGIT | UNDERSCORE)+;

//------------------------ fragment --------------------------------
fragment LETTER: [a-zA-Z];
fragment DIGIT: [0-9];
fragment UNDERSCORE: '_';

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
