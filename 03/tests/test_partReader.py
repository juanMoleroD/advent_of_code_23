import unittest
# from src.partReader import *

class Test_partReader(unittest.TestCase):
    
    def test_findpart(self):
        input: [] = ['..........',
                     '...1111...',
                     '..........']
        self.assertEqual(findPart(input), 1111)


    def test_parseInputToMatrix(self):
        pass