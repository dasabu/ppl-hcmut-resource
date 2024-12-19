grammar BKOOL;

//1812665
//Tran Dang Khoa
@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}
//Parser
program:            classDeclList EOF;
classDeclList:      classDecl classDeclList | classDecl ;
classDecl: 			CLASS ID (EXTENDS ID)? classBody;
classBody: 			LP classBodyDeclList? RP;
classBodyDeclList:  classBodyDecl+;
classBodyDecl:      attributeDecl |  methodDecl;

methodDecl:         (STATIC? returnType)? ID LB paramList? RB blockStmt;
paramList:          param SM paramList | param ;
param:              typeType ids;
ids:                ID COMMA ids | ID ;

blockStmt:          LP varDecl* statement* RP;

varDecl:            FINAL? typeType variableDeclList SM ;
attributeDecl:      (STATIC | FINAL | STATIC FINAL | FINAL STATIC)? typeType variableDeclList SM;
variableDeclList:   variableDeclarator COMMA variableDeclList | variableDeclarator ;
variableDeclarator: ID ('=' expression)?;

statement:			blockStmt
					|assignStmt SM
					|ifStmt
					|forStmt               //for statement
					|breakStmt SM
					|continueStmt SM      //continue statement
					|returnStmt SM        //return statement
					|methodInvoStmt SM;   // method invocation statement

breakStmt:          BREAK;
continueStmt:       CONTINUE;
returnStmt:         RETURN expression;
methodInvoStmt:     expression9 DOT ID args;
assignStmt:         lhsAssign ASS expression;
ifStmt:             IF expression THEN statement (ELSE statement)?;
forStmt:            FOR ID ASS expression (TO | DOWNTO) expression DO statement ;
//lhsAssign:          ID | expression DOT ID | expression LSB expression RSB;
lhsAssign:          ID | expression9 DOT ID | expression9 LSB expression RSB;

expression:         expression1 (GT | LT | GTE | LTE) expression1 | expression1;
expression1:        expression2 (EQUAL | NEQUAL) expression2 | expression2;
expression2:        expression2 (AND | OR) expression3 | expression3;
expression3:        expression3 (ADD | SUB) expression4 | expression4;
expression4:        expression4 (MUL | FDIV | IDIV | MOD) expression5 | expression5;
expression5:        expression5 CONCAT expression6 | expression6;
expression6:        NOT expression6 | expression7;
expression7:        (ADD | SUB) expression7 | expression8;
//lhsAssign:          expression8;
expression8:        expression9 LSB expression RSB | expression9;  //
expression9:        expression9 DOT ID args | expression10 | expression9 DOT ID;
expression10:       NEW ID args | expression11;
expression11:       elem | arrayLit | THIS | LB expression RB | ID;


args:               LB expList? RB;
expList:            expression COMMA expList | expression;
typeType:           primitiveType | arrayType | classType ;
returnType: 		typeType;
arrayType:          (primitiveType | ID ) LSB INTLIT RSB;
primitiveType:      INT | FLOAT | BOOLEAN | STRING | VOID ;
classType:			ID;
arrayLit:           LP elemArrays RP;
elemArrays:         elemArray COMMA elemArrays | elemArray ;
elemArray:          INTLIT | FLOATLIT | booleanlit | STRINGLIT | NIL | THIS;
elem:           	INTLIT | FLOATLIT | booleanlit | STRINGLIT | NIL;
booleanlit:         TRUE | FALSE;
//Lexer rules




// 3.4) Keywords
BOOLEAN	: 			'boolean';
BREAK: 				'break';
CLASS: 				'class';
CONTINUE: 			'continue';
DO: 				'do';
ELSE: 				'else';
EXTENDS: 			'extends';
FLOAT: 				'float';
IF: 				'if';
INT: 				'int';
NEW: 				'new';
STRING: 			'string';
THEN: 				'then';
FOR: 				'for';
RETURN: 			'return';
TRUE: 				'true';
FALSE: 				'false';
VOID: 				'void';
NIL: 				'nil';
THIS: 				'this';
FINAL: 				'final';
STATIC: 			'static';
TO: 				'to';
DOWNTO: 			'downto';

// 3.5) Operator
ADD: 				'+';
SUB: 				'-';
MUL: 				'*';
FDIV: 				'/';
IDIV: 				'\\';
MOD:				'%';
NEQUAL: 			'!=';
EQUAL: 				'==';
LT:            		'<';
GT:            		'>';
LTE:            	'<=';
GTE:            	'>=';
OR: 				'||';
AND:            	'&&';
NOT:            	'!';
CONCAT:            	'^';
ASS:                ':=';

// 3.6) Separator
LP:	    			'{';
RP:	    			'}';
LSB:				'[';
RSB:				']';
LB:     			'(';
RB:     			')';
SM:     			';';
COLON:  			':';
COMMA:  			',';
DOT:    			'.';



// 3.7) Literals
WS : 				[ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
LINE_COMMENT: 		'#' ~[\n\r]*  -> skip;
BLOCK_COMMENT: 		'/*' .*? '*/' -> skip;

// 3.7.1) Integer literals
INTLIT  :           [0-9]+;

// 3.7.2) Float literals
FLOATLIT: 		    [0-9]+ (DecimalPart | DecimalPart? ExponentPart);
fragment DecimalPart
					:'.'[0-9]*;
fragment ExponentPart
					: ('e'|'E') ('+'|'-')?[0-9]+;
// 3.7.4) Boolean literals
// TRUE:'true';
// FALSE:'false';
// 3.7.5) Identifier literals
ID: 				[a-zA-Z_][a-zA-Z0-9_]*;

// 3.7.3) String literals
STRINGLIT:          '"' StringCharacter? '"';
fragment StringCharacter
                    :(~["\\\r\n] | EscapeSequence)+;
fragment EscapeSequence
					:'\\' [btnfr"'\\];

UNCLOSE_STRING: '"' StringCharacter*  EOF? {
		y = str(self.text)
		raise UncloseString(y[0:])
	};
ILLEGAL_ESCAPE: '"' StringCharacter* ('\\' ~[bfrnt"\\]) {
		y = str(self.text)
		raise IllegalEscape(y[0:])
	};
ERROR_CHAR: .{
		raise ErrorToken(self.text)
	};