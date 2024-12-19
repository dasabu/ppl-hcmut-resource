grammar BKOOL;

program:   (expr NEWLINE)* EOF;
expr:   expr ('*'|'/') expr
    |   expr ('+'|'-') expr
    |   INT
    |   '(' expr ')'
    ;
NEWLINE : [\r\n]+ ;
INT     : [0-9]+ ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
