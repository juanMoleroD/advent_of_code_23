import unittest
from src.partReader import *

class Test_partReader(unittest.TestCase):
    
    def test_findpart(self):
        input: [] = ['..........',
                     '...1111...',
                     '..........']
        expected = { "value": 1111, "partX": 3, "partY": 1, "partLen": 4 }
        self.assertEqual(findPart(input), expected)



    def test_parseInputToMatrix(self):
        pass