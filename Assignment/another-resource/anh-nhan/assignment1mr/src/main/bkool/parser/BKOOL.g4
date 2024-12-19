grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : mptype 'main' LB RB LP body? RP EOF ;

mptype: INTTYPE | VOIDTYPE ;

body: exp SEMI;

funcall: ID LB exp? RB ;

exp: exp ADD exp1 | exp1;
exp1: funcall | INTLIT;

ADD: '+';
INTTYPE: 'int' ;

VOIDTYPE: 'void'  ;

ID: [a-zA-Z]+ ;

INTLIT: [0-9]+;

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

SEMI: ';' ;


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;