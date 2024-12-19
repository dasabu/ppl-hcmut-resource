import sys,os
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener,ErrorListener
if not './main/bkool/parser/' in sys.path:
    sys.path.append('./main/bkool/parser/')
if os.path.isdir('../target/main/bkool/parser') and not '../target/main/bkool/parser/' in sys.path:
    sys.path.append('../target/main/bkool/parser/')
from BKOOLLexer import BKOOLLexer
from BKOOLParser import BKOOLParser
from lexererr import *
# from ASTGeneration import ASTGeneration
# from StaticCheck import StaticChecker
# from StaticError import *
# from CodeGenerator import CodeGenerator
# import subprocess

JASMIN_JAR = "./external/jasmin.jar"
TEST_DIR = "./test/testcases/"
SOL_DIR = "./test/solutions/"
Lexer = BKOOLLexer
Parser = BKOOLParser


class TestUtil:
    @staticmethod
    def makeSource(inputStr, num):
        filename = TEST_DIR + str(num) + ".txt"
        file = open(filename, "w")
        file.write(inputStr)
        file.close()
        return FileStream(filename)


class TestLexer:
    @staticmethod
    def test(input, expect, num):
        inputfile = TestUtil.makeSource(input, num)
        print('Testcase {}'.format(num))
        print('Input: ' + input)
        print('Expect: ' + expect)
        TestLexer.check(SOL_DIR, inputfile, num)
        print('\n==================================')
        dest = open(SOL_DIR + str(num) + ".txt", "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir, inputfile, num):
        dest = open(os.path.join(soldir, str(num) + ".txt"), "w")
        lexer = Lexer(inputfile)
        try:

            print('Result: ', end='')
            TestLexer.printLexeme(dest, lexer)
        except (ErrorToken, UncloseString, IllegalEscape) as err:
            print(err.message)
            dest.write(err.message)
        finally:
            dest.close()

    @staticmethod
    def printLexeme(dest, lexer):
        tok = lexer.nextToken()
        if tok.type != Token.EOF:
            print(tok.text + ',', end='')
            dest.write(tok.text + ",")
            TestLexer.printLexeme(dest, lexer)
        else:
            print("<EOF>", end='')
            dest.write("<EOF>")


class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException("Error on line " + str(line) + " col " + str(column) + ": " + offendingSymbol.text)


NewErrorListener.INSTANCE = NewErrorListener()


class SyntaxException(Exception):
    def __init__(self, msg):
        self.message = msg


class TestParser:
    @staticmethod
    def createErrorListener():
        return NewErrorListener.INSTANCE

    @staticmethod
    def test(input, expect, num):
        inputfile = TestUtil.makeSource(input, num)
        print('Input: ' + input)
        print('Expect: ' + expect)
        print('Result: ', end='')
        TestParser.check(SOL_DIR, inputfile, num)
        print('\n========================')
        dest = open(SOL_DIR + str(num) + ".txt", "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir, inputfile, num):
        dest = open(os.path.join(soldir, str(num) + ".txt"), "w")
        lexer = Lexer(inputfile)
        listener = TestParser.createErrorListener()
        tokens = CommonTokenStream(lexer)
        parser = Parser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        try:
            parser.program()
            dest.write("successful")
            print("successful")
        except SyntaxException as f:
            print(f.message)
            dest.write(f.message)
        except Exception as e:
            print(str(e))
            dest.write(str(e))
        finally:
            dest.close()
