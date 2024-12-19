import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test(self):
        input = """
        class Test{ 
            void testing(int max){
                int x;
                final int y = x;
                for i := 1 to x do {
                    y := x + i;
                    if y > max then max := y;
                    else continue;
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1000))