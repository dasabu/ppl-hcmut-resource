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
// attrTyp: primiTyp | classTyp | arrayTyp
// methodTyp: primitTyp | classTyp | VOID
paramDecl:			LB paramList RB;
paramList: 			paramPrime | ;
paramPrime:			param SEMI paramPrime | param;
param:				typ idlist;
idlist:				ID COMMA idlist | ID;



// ~ 2.2: Attribute Declaration  
attrDecl: 			immutDecl | mutDecl;
immutDecl:			immutKeywords typ immutInitList SEMI;
mutDecl:			mutKeyword typ mutMemberList SEMI;

mutKeyword: 		STATIC | ;
mutMemberList: 		mutMember (COMMA mutMember)*;
mutMember:			idlist mutInit;
mutInit:			EQUAL_SIGN expr | ;

immutKeywords:		FINAL | STATIC FINAL | FINAL STATIC;
immutInitList:		immutInit COMMA immutInitList | immutInit;
immutInit:			idlist EQUAL_SIGN expr;


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
immutVardecl:			FINAL typ immutVarBody SEMI;
mutVardecl:				typ mutVarBody SEMI;

immutVarBody:			immutVarMem COMMA immutVarBody | immutVarMem;
immutVarMem:			idlist EQUAL_SIGN expr;

mutVarBody:				mutVarMemList;
mutVarMemList:			mutVarMem (COMMA mutVarMem)*;
mutVarMem:				idlist (EQUAL_SIGN expr)?;

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


// grammar BKOOL;

// // 2111860

// @lexer::header {
// from lexererr import *
// }
// options {
// 	language=Python3;
// }

// // PARSER
// //2.1 Class Declaration
// program: classDeclList EOF;
// classDeclList: classDecl+;
// classDecl: CLASS ID (EXTENDS ID)? LP classMem* RP;
// classMem: attriDecl | methDecl;

// // 2.2 Attribute declaration
// attriDecl: muAttDecl | imAttDecl;
// // attriType: INT | FLOAT | BOOLEAN | STRING | arrayType | classType;
// typ: INT | FLOAT | BOOLEAN | STRING | VOID | classType | arrayType;
// imAttDecl: (STATIC FINAL | FINAL STATIC | FINAL) typ imAttList ';';
// muAttDecl: STATIC? typ muAttList ';';

// imAttList: (imAttName ',') imAttList | imAttName;
// imAttName: idList '=' exp;
// muAttList: (muAttName ',') muAttList | muAttName;
// muAttName: idList ('=' exp)?;
// idList: (ID ',') idList | ID;

// // 2.3 Method declaration
// methDecl: (STATIC? typ)? ID LB paraList RB blockstmt;
// // methType: INT | FLOAT | BOOLEAN | STRING | VOID | classType;
// paraList: paraPrime | ;
// paraPrime: para ';' paraPrime | para;
// para: typ idList;

// //4 TYPE
// classType: ID;
// arrayType: (INT | FLOAT | BOOLEAN | STRING | classType | VOID) LS INTLIT RS;

// // 5 EXPRESSION
// exp:    exp1 (LESS | GREATER | LEQ | GEQ) exp1 | exp1;
// exp1:   exp2 (EQ | NEQ) exp2 | exp2;
// exp2:   exp2 (AND | OR) exp3 | exp3;
// exp3:   exp3 (ADD| SUB) exp4 | exp4;
// exp4:   exp4 (MUL | INTDIV | FLDIV | MOD) exp5 | exp5;
// exp5:   exp5 CONCAT exp6 | exp6;
// exp6:   NOT exp6 | exp7;
// exp7:   (ADD | SUB) exp7 | exp8;
// exp8:   exp9 LS exp RS | exp9;
// exp9:   exp9 DOT ID | exp9 DOT ID LB explist RB | exp10;
// exp10:  NEW ID LB explist RB | exp11;
// exp11: INTLIT | FLOATLIT | STRLIT | boollit | arrayLit | THIS | ID | NIL | subexp;

// subexp: LB exp RB;

// explist: expprime | ;
// expprime: exp CM explist | exp;

// arrayLit: LP arrMemList RP;
// arrMemList: arrMem CM arrMemList | arrMem;
// arrMem: INTLIT | FLOATLIT | STRLIT | boollit;

// // 6 STATEMENT
// stmtlist: stmt stmtlist | ;
// stmt: blockstmt | assignstmt | ifstmt | forstmt | brkstmt | constmt | returnstmt | methstmt | declstmt;

// blockstmt: LP stmtlist RP;

// assignstmt: lhs ASSIGN exp SM;
// lhs: ID | exp9 DOT ID | exp8;

// ifstmt: IF exp THEN stmt (ELSE stmt)?;

// forstmt: FOR ID ASSIGN exp (TO|DOWNTO) exp DO stmt;

// brkstmt: BREAK SM;

// constmt: CONTINUE SM;

// returnstmt: RETURN exp SM;

// methstmt: exp9 DOT ID LB explist RB SM;

// declstmt: mustmtDecl | imstmtDecl;
// imstmtDecl: FINAL typ imAttList ';';
// mustmtDecl: typ muAttList ';';

// // imAttList: (imAttName ',') imAttList | imAttName;
// // imAttName: idList '=' exp;
// // muAttList: (muAttName ',') muAttList | muAttName;
// // muAttName: idList ('=' exp)?;
// // idList: (ID ',') idList | ID;

// // LEXER

// // 3.2 Comments
// CMTLINE: '#' ~[\r\n]* -> skip;
// CMTBLOCK: '/*' .*? '*/' -> skip;

// // 3.4 Keyword
// BOOLEAN: 	'boolean';
// BREAK: 		'break';
// CLASS: 		'class';
// CONTINUE: 	'continue';
// DO: 		'do';
// ELSE: 		'else';
// EXTENDS: 	'extends';
// FLOAT: 		'float';
// IF: 		'if';
// INT: 		'int';
// STRING: 	'string';
// THEN: 		'then';
// FOR: 		'for';
// RETURN: 	'return';
// TRUE: 		'true';
// FALSE: 		'false';
// VOID: 		'void';
// NIL: 		'nil';
// THIS: 		'this';
// FINAL: 		'final';
// STATIC: 	'static';
// TO: 		'to';
// DOWNTO: 	'downto';

// // 3.5 Operator
// ADD:        '+';
// ASSIGN:     ':=';
// SUB:        '-';
// MUL:        '*';
// FLDIV:      '/';
// INTDIV:     '\\';
// MOD:        '%';
// NEQ:        '!=';
// EQ:         '==';
// EQQ:        '=';
// LESS:       '<';
// GREATER:    '>';
// LEQ:        '<=';
// GEQ:        '>=';
// OR:         '||';
// AND:        '&&';
// NOT:        '!';
// CONCAT:     '^';
// NEW:        'new';

// // 3.6 Separator
// SM:         ';';
// CM:         ',';
// LP:         '{';
// RP:         '}';
// LB:         '(';
// RB:         ')';
// LS:         '[';
// RS:         ']';
// CL:         ':';
// DOT:        '.';

// // 3.7. Literal
// // 3.7.1 Integer literal
// INTLIT: [0] | [1-9] [0-9]*;

// // 3.7.2 Float literal
// FLOATLIT: INTLIT (DEC | EXPONENT | DEC EXPONENT);
// fragment DEC: '.' [0-9]*;
// fragment EXPONENT: [eE] [+-]? [0-9]+;

// // 3.7.3 Boolean Literal
// boollit: TRUE | FALSE;

// // 3.7.4 String literal
// STRLIT: '"' CHAR* STRLIT? '"' { self.text = self.text[1:-1] };
// fragment CHAR: ESCAPE | '\\"' | ~([\n\r] | '"' | '\\') ;
// fragment ESCAPE: '\\' ([btnfr"\\]);
// fragment ILLESC: '\\' ~([btnfr"\\]);

// // STRLIT: '"' CHAR* '"' {self.text = self.text[1:-1]};

// // fragment CHAR: ESCAPE | ~[\r\n\\"];
// // fragment ESCAPE: '\\' ( 'b' | 'f' | 'r' | 'n' | 't' | '\\' | '\\"' );
// // fragment ILLESC: '\\' ~( 'b' | 'f' | 'r' | 'n' | 't' | '\\' | '\"' );

// // 3.3 Identifier
// ID: [a-zA-Z_] [a-zA-Z0-9_]*; 
// WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines

// UNCLOSE_STRING: '"' CHAR* ([\n\rEOF] | ~'"') {
// 	if self.text[-1] in ['\n', '\r', 'EOF']:
// 		raise UncloseString(self.text[1:-1])
// 	else:
// 		raise UncloseString(self.text[1:])
// };

// ILLEGAL_ESCAPE: '"' CHAR* ILLESC {
// 	raise IllegalEscape(self.text[1:])
// };

// ERROR_CHAR: . { raise ErrorToken(self.text) };
