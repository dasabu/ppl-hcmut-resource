grammar BKOOL;

// 2112762
// Le Duy Anh

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

// ! ------------------ PARSER ---------------------

// ~ 2.1: Class Declaration 
program: 			classDeclList EOF;
classDeclList: 		classDecl classDeclList | classDecl;
classDecl: 			CLASS ID classExtends classBody;
classExtends: 		EXTENDS ID | ;
classBody:			LP classMemberList RP;
classMemberList:	classMember classMemberList | ;
classMember:		attrDecl | methodDecl;


// ~ 2.3: Method Declaration 
methodDecl:			constructor | normalMethod; 

constructor:		ID paramDecl blockstmt; 
normalMethod: 		(STATIC | ) typ ID paramDecl blockstmt;	// blockStmt below

typ:				primiTyp | classTyp | arrayTyp | VOID;
paramDecl:			LB paramList RB;
paramList: 			paramPrime | ;
paramPrime:			param SEMI paramPrime | param;
param:				typ idlist;
idlist:				ID COMMA idlist | ID;


// ~ 2.2: Attribute Declaration  
attrDecl: 			immutDecl | mutDecl;
immutDecl:			immutKeywords typ attrList SEMI;
mutDecl:			mutKeyword typ attrList SEMI;

mutKeyword: 		STATIC | ;
immutKeywords:		FINAL | STATIC FINAL | FINAL STATIC;
attrList:			attrMember COMMA attrList | attrMember;
attrMember:			idlist attrInit;
attrInit:			EQUAL_SIGN expr | ; 


// ~ 3.7.4,5: Boolean + Array Literal 
arrayLit:			LP arrMemberList RP;
arrMemberList:		arrMember COMMA arrMemberList | arrMember;
arrMember:			INTLIT | FLOATLIT | STRINGLIT | booleanLit;
booleanLit:			TRUE | FALSE; 


// ~ 5: Expression 
expr:		expr1 (GT_OP | LT_OP | GTE_OP | LTE_OP) expr1 | expr1;
expr1:		expr2 (EQUAL_OP | NEQUAL_OP) expr2 | expr2;
expr2:		expr2 (AND_OP | OR_OP) expr3 | expr3;
expr3: 		expr3 (ADD_OP | SUB_OP) expr4 | expr4;
expr4: 		expr4 (MUL_OP | INTDIV_OP | FLODIV_OP | MOD_OP) expr5 | expr5;
expr5:		expr5 (CONCAT_OP) expr6 | expr6;
expr6: 		(NOT_OP) expr6 | expr7;
expr7: 		(ADD_OP | SUB_OP) expr7 | expr8;
expr8: 		expr9 LSB expr RSB | expr9;
expr9:		expr9 DOT ID 					// attribute access
	| 		expr9 DOT ID LB arglist RB		// method access
	| 		expr10;
expr10:		NEW ID LB arglist RB| expr11;
expr11: 	THIS | ID | NIL | primiLit | arrayLit | subexpr;


arglist:	argprime | ;
argprime: 	expr COMMA argprime | expr;
primiLit: 	INTLIT | FLOATLIT | STRINGLIT | booleanLit;

subexpr:	LB expr RB;

// ~ 6: Statement 
stmtlist:			stmt stmtlist | ;
stmt:				vardecllist
	|				blockstmt
	|				asmstmt
	|				ifstmt
	|				forstmt
	|				breakstmt
	|				contstmt
	|				retstmt
	|				methodivkstmt;

// & 6.1: Block Statement 
blockstmt: 				LP stmtlist RP;

vardecllist:			vardecl vardecllist | vardecl;
vardecl:				immutVardecl | mutVardecl;
immutVardecl:			FINAL typ attrList SEMI;
mutVardecl:				typ attrList SEMI;

// immutVarBody:			immutVarMem COMMA immutVarBody | immutVarMem;
// immutVarMem:			idlist EQUAL_SIGN expr;

// mutVarBody:				mutVarMemList;
// mutVarMemList:			mutVarMem (COMMA mutVarMem)*;
// mutVarMem:				idlist (EQUAL_SIGN expr)?;

// & 6.2: Assignment Statement 
asmstmt:				asmlhs ASSIGN_OP expr SEMI;
asmlhs:					ID | expr9 DOT ID | expr8;

// & 6.3: If Statement 
ifstmt:					IF expr THEN stmt | IF expr THEN stmt ELSE stmt;

// & 6.4: For Statement 
forstmt: 				FOR ID ASSIGN_OP expr (TO | DOWNTO) expr DO stmt;

// & 6.5: Break Statement 
breakstmt:				BREAK SEMI;

// & 6.6: Continue Statement 
contstmt:				CONTINUE SEMI;

// & 6.7: Return Statement 
retstmt:				RETURN expr SEMI;

// & 6.8: Method Invocation Statement 
methodivkstmt:			expr9 DOT ID LB arglist RB SEMI;

// ~ 4: TYPE 
primiTyp:			INT | FLOAT | STRING | BOOLEAN;
classTyp:			ID;
arrayTyp: 			(primiTyp | classTyp) LSB INTLIT RSB;

//! ------------------- LEXICAL STRUCTURE ----------------------


// ~ 3.4: Keyword
BOOLEAN: 	'boolean';
BREAK: 		'break';
CLASS: 		'class';
CONTINUE: 	'continue';
DO: 		'do';
ELSE: 		'else';
EXTENDS: 	'extends';
FLOAT: 		'float';
IF: 		'if';
INT: 		'int';
NEW: 		'new';
STRING: 	'string';
THEN: 		'then';
FOR: 		'for';
RETURN: 	'return';
TRUE: 		'true';
FALSE: 		'false';
VOID: 		'void';
NIL: 		'nil';
THIS: 		'this';
FINAL: 		'final';
STATIC: 	'static';
TO: 		'to';
DOWNTO: 	'downto';


// ~ 3.5: Operator
ADD_OP: 	'+';
SUB_OP: 	'-';
MUL_OP: 	'*';
FLODIV_OP: 	'/';
INTDIV_OP: 	'\\';
MOD_OP: 	'%';
EQUAL_OP: 	'==';
NEQUAL_OP: 	'!=';
LT_OP: 		'<';
GT_OP: 		'>';
LTE_OP: 	'<=';
GTE_OP: 	'>=';
OR_OP: 		'||';
AND_OP: 	'&&';
NOT_OP: 	'!';
CONCAT_OP: 	'^';
ASSIGN_OP: 	':=';

EQUAL_SIGN: '=';


// ~ 3.6: Seperator 
LSB: 	'[';
RSB:	']';
LP: 	'{';
RP: 	'}';
LB: 	'(';
RB: 	')';
SEMI: 	';';
COLON: 	':';
DOT: 	'.';
COMMA: 	',';


// ~ 3.3: Identifier 
ID: [_a-zA-Z] [_a-zA-Z0-9]*;


// ~ 3.2: Comment 
WS : 			[ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines
LINE_COMMENT: 	'#' ~[\n\r]* -> skip;
BLOCK_COMMENT: 	'/*' .*? '*/' -> skip;


// ~ 3.7: Literal 
	// & 3.7.1: Integer Literal 
INTLIT: [1-9][0-9]* | [0];
	// & 3.7.2: Float Literal 
FLOATLIT: (INTPART DECPART) | (INTPART DECPART? EXPPART);
fragment INTPART: [0-9]+;
fragment DECPART: '.' [0-9]*;
fragment EXPPART: [eE] [+-]? [0-9]+;
	// & 3.7.4: String Literal (im not sure) 
STRINGLIT: '"' CHARLIT* STRINGLIT? '"' { self.text = self.text[1:-1] } ;
fragment CHARLIT: ESCSEQ | '\\"' | ~([\n\r] | '"' | '\\');
fragment ESCSEQ: '\\' ([btnfr"\\]);
fragment ILLESC: '\\' ~([btnfr"\\]);
// * DA
// fragment ESCSEQ: '\\' ('b' | 'f' | 'r' | 'n' | 't' | '"' | '\\');

// fragment ILLESC: '\\' ~('b' | 'f' | 'r' | 'n' | 't' | '"' | '\\');
// * Ngoc
// STRLIT: '"' CHAR* STRLIT? '"' { self.text = self.text[1:-1] };
// fragment CHAR: ESCAPE | '\\"' | ~([\n\r] | '"' | '\\') ;
// fragment ESCSEQ: '\\' ([btnfr"\\]);
// fragment ILLESC: '\\' ~([btnfr"\\]);

// STRING : '"' (ESC_SEQ | ~["\\])* '"';
// fragment ESC_SEQ : '\\' ('b' | 'f' | 'r' | 'n' | 't' | '"' | '\\');

UNCLOSE_STRING: '"' CHARLIT* ([\n\rEOF] | ~'"') {
	if self.text[-1] in ['\n', '\r', 'EOF']:
		raise UncloseString(self.text[1:-1])
	else:
		raise UncloseString(self.text[1:])
};

ILLEGAL_ESCAPE: '"' CHARLIT* ILLESC {
	raise IllegalEscape(self.text[1:])
};

ERROR_CHAR: . { raise ErrorToken(self.text) };