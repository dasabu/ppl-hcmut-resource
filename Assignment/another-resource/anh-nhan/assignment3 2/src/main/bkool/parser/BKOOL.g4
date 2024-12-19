
grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
    language=Python3;
}

//-----------------------------------------------------------------
//-------------------- 2 PROGRAM STRUCTURE ------------------------
//-----------------------------------------------------------------
program: classDecl+ EOF;

//---------Class declaration----------
type_name: BOOLEAN | INT | FLOAT | STRING | arrType | objType;

classDecl: CLASS className (EXTENDS ID)? LP classMem* RP;
className: ID;
classMem: attributeDecl | methodDecl | constructor | mainMethod | voidMethod;


//---------Attribute declaration-------
attributeDecl: mutableAttribute | immutableAttribute | objAttribute;
mutableAttribute: STATIC? type_name ID muInit (COMMA ID muInit)* SEMI;
muInit: (EQ expr)?;
immutableAttribute: (FINAL | STATIC FINAL | FINAL STATIC) type_name ID immuInit (COMMA ID immuInit)* SEMI;
immuInit: EQ expr;
objAttribute: STATIC? objType ID objInit (COMMA ID objInit)* SEMI;
objInit: (EQ NEW ID LB expList? RB)?;


//---------Method declaration ---------
methodDecl: STATIC? type_name ID LB paramList? RB stmtBlock;
//special method
mainMethod: STATIC? VOID 'main' LB RB stmtBlock_wo_return;
voidMethod: STATIC? VOID ID LB paramList? RB stmtBlock_wo_return;
constructor: className LB paramList? RB stmtBlock_constructor;

paramList: paramInit (SEMI paramInit)*;
paramInit: type_name ID (COMMA ID)*;

//-----------------------------------------------------------------
//-------------------- 6 STATEMENT --------------------------------
//-----------------------------------------------------------------
stmt: asmStmt | ifStmt | forStmt | breakStmt | continueStmt | returnStmt | method_invo_stmt | stmtBlock;
stmt_wo_return: asmStmt | ifStmt | forStmt | breakStmt | continueStmt | method_invo_stmt | stmtBlock_wo_return;
stmtBlock: LP (varDecl | stmt)* RP;
stmtBlock_wo_return: LP (varDecl | stmt_wo_return)* RP;
stmtBlock_constructor: LP (varDecl_constructor | stmt_wo_return)* RP;


//------- 6.1 assignment ------------
asmStmt: lhs ASSIGN expr SEMI;
lhs: ID | (ID|THIS) DOT (ID|ID LSB expr RSB) | ID LSB expr RSB;

//------- 6.2 if  ------------

ifStmt: IF expr THEN stmt (ELSE stmt)?;

//------- 6.3 for ------------

forStmt: FOR ID ASSIGN expr (TO|DOWNTO) expr DO stmt;

//------- 6.4 break continue return ------------
breakStmt: BREAK SEMI;
continueStmt: CONTINUE SEMI;
returnStmt: RETURN expr SEMI;

//method invocation statement
method_invo_stmt:  expr DOT ID (LB expList? RB)? SEMI;
//-----------------------------------------------------------------
//-------------------- 5 EXPRESSION -------------------------------
//-----------------------------------------------------------------


expr: exp2 CONCAT exp2 | exp2;

exp2: exp3 relational exp3 | exp3;

relational: EQQ | NOTEQ | LT | GT | LTEQ | GTEQ;

exp3: exp3 AND exp4 | exp3 OR exp4 | exp4;

exp4: exp4 ADD exp5 | exp4 SUB exp5 | exp5;

exp5: exp5 MUL exp6 | exp5 DIV exp6 | exp5 MOD exp6 | exp5 IDIV exp6 | exp6 ;

exp6: NOT exp6 | exp7;

exp7: (SUB | ADD) exp7 | exp8;

exp8: exp8 LSB expr RSB | exp9;

exp9: exp9 DOT tail_part | exp10;
tail_part: ID | ID LB expList? RB;


exp10: THIS | exp11;

exp11: exp11_access | exp11_call | exp12;
exp11_access: ID DOT ID;
exp11_call: ID DOT ID LB expList? RB;

exp12: NEW ID LB expList? RB | exp13;
exp13: LB expr RB | literal | ID;
expList: expr (COMMA expr)*;
/*-------------------VarDecl-------------------*/

varDecl: mutableVar | immutableVar | objVar;
mutableVar: type_name ID muInit (COMMA ID muInit)* SEMI;
immutableVar: FINAL? type_name ID immuInit (COMMA ID immuInit)* SEMI;
objVar: objType ID objInit (COMMA ID objInit)* SEMI;


/*-------------------VarDecl for constructor-------------------*/

varDecl_constructor: mutableVar_constructor | immutableVar | objVar;
mutableVar_constructor: type_name ID constructorInit (COMMA ID constructorInit)* SEMI;
constructorInit: (EQ expr)?;

//-----------------------------------------------------------------
//-------------------- 4 TYPE AND VALUE ---------------------------
//-----------------------------------------------------------------


//----------4.1 primitive type------
primitive_type: INT | FLOAT | BOOLEAN | STRING | VOID;

//----------4.2 array type----------
arrType: element_type LSB (size)? RSB;
element_type: INT | FLOAT | BOOLEAN | STRING | objType;
size: INTLIT;

//----------4.3 class type----------D
objType: ID;
//-----------------------------------------------------------------
//-------------------- 3 LEXICAL STRUCTURE ------------------------
//-----------------------------------------------------------------

//----------3.1 Char set------------
WS : [ \f\t\r\n]+ -> skip ;

//-----------3.2 comment------------
COMMENT : (('/*' .*? '*/') | ('#' ~ [\r\n]* ('\r'? '\n' | EOF)))-> skip;

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
LB: '(';
RB: ')';
LSB: '[';
RSB: ']';
DOT: '.';
COMMA: ',';
SEMI: ';';
COLON: ':';
LP: '{';
RP: '}';

//------------3.7 literal -----------
literal: INTLIT | FLOATLIT | bool_lit | STRING_LIT | indexarr_lit;

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
bool_lit: TRUE | FALSE;
//TRUE: 'True';
//FALSE: 'False';
//------string------
fragment STR_CHAR: (~[\n\r\\"] | ESC_SEQUENCE);
fragment ESC_SEQUENCE: '\\' [bfrtn"\\];

STRING_LIT: '"'STR_CHAR*'"'
    {
    self.text = self.text[1:-1]
    };

//-------index arr---
arr_exp : literal | literal COMMA arr_exp;
indexarr_lit: LP arr_exp RP;

//------------3.3 ID----------------
ID: (LETTER | UNDERSCORE) (LETTER | DIGIT | UNDERSCORE)*;

//------------------------ fragment --------------------------------
fragment LETTER: [a-zA-Z];
fragment DIGIT: [0-9];
fragment UNDERSCORE: '_';

//------------------------------------------------------------------
fragment ILL_ESCAPE: '\\' ~[btnfr"\\];

UNCLOSE_STRING: '"' STR_CHAR* ([\r\nEOF] | ~'"')
{
	err_char = ['\r','\n',EOFError]
	if self.text[-1] in err_char:
		raise UncloseString(self.text[1:-1])
	else:
		raise UncloseString(self.text[1:])
};

ILLEGAL_ESCAPE:'"' STR_CHAR* ILL_ESCAPE{
    raise IllegalEscape(self.text[1:])
};

ERROR_TOKEN: .{
    raise ErrorToken(self.text)
};
