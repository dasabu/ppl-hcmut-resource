grammar BKOOL;

@lexer::header {
from lexererr import *
}

// @lexer::members {
// def emit(self):
//     tk = self.type
//     result = super().emit()
//     if tk == self.UNCLOSE_STRING:       
//         raise UncloseString(result.text)
//     elif tk == self.ILLEGAL_ESCAPE:
//         raise IllegalEscape(result.text)
//     elif tk == self.ERROR_CHAR:
//         raise ErrorToken(result.text)
//     elif tk == self.UNTERMINATED_COMMENT:
//         raise UnterminatedComment()
//     else:
//         return result;
// }

options{
	language=Python3;
}

program:        vardecls EOF;

vardecls:       vardecl vardecls | vardecl;

vardecl:        VARNAME EQ expr SEMI;

expr:               expr1 DQUES expr1 | expr1;
expr1:              expr2 (ADD | SUB) expr1 | expr2;
expr2:              expr2 (MUL | DIV | MOD) expr3 | expr3;
expr3:              expr3 DOT expr4 | expr4;
expr4:              expr5 DSTAR expr4 | expr5;
expr5:              atom | subexpr;

subexpr:            LP expr RP;

atom:               INTLIT | FLOATLIT | STRINGLIT | arrayLit;

arrayLit:           indexedArray | associativeArray;

indexedArray:       ARRAY LP exprlist RP;
exprlist:           exprprime | ;
exprprime:          expr COMMA exprprime | expr;

associativeArray:   ARRAY LP pairlist RP;
pairlist:           pairprime | ;
pairprime:          pair COMMA pairprime | pair;
pair:               PAIRNAME ARROW expr;
PAIRNAME:           VARNAME;

EQ:         '=';
SEMI:       ';';
LP:         '(';
RP:         ')';
COMMA:      ',';
ARROW:      '=>';
DQUES:      '??';
ADD:        '+';
SUB:        '-';
DIV:        '/';
MUL:        '*';
MOD:        '%';
DOT:        '.';
DSTAR:      '**';
ARRAY:      'array';

INTLIT:     [0-9]+;
FLOATLIT:   [0-9]+ DOT [0-9]+;
STRINGLIT:  '"' .*? '"';

VARNAME:    [a-zA-Z_] [a-zA-Z0-9_]*;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;