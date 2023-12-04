import unittest
from src.partReader import *

class Test_partReader(unittest.TestCase):
    
    def setUp(self):
        self.input1: [] = [ '..........',
                            '...1111...',
                            '..........']

    def test_findPotentialPart(self):
        expected = { "value": 1111, "partX": 3, "partY": 1, "partLen": 4 }
        self.assertEqual(findPotentialPart(self.input1), expected)

    def test_checkIfPart_Sides(self):
        potentialPart = findPotentialPart(self.input1)
        self.assertEqual(checkIfPart(potentialPart, self.input1), False)
        self.input1[1] = "..+1111..."
        self.assertEqual(checkIfPart(potentialPart, self.input1), True)
        self.input1[1] = "...1111-.."
        self.assertEqual(checkIfPart(potentialPart, self.input1), True)

    def test_checkIfPart_Sides_onEdge(self):
        self.input1[1] = "1111......"
        potentialPart = findPotentialPart(self.input1)
        self.assertEqual(checkIfPart(potentialPart, self.input1), False)
        self.input1[1] = "1111.....*" # array[-1] goes to last integer if unchecked
        potentialPart = findPotentialPart(self.input1)
        self.assertEqual(checkIfPart(potentialPart, self.input1), False)
        self.input1[1] = "......1111"
        potentialPart = findPotentialPart(self.input1)
        self.assertEqual(checkIfPart(potentialPart, self.input1), False)

    def test_checkIfPart_top(self):
        PotentialPart = findPotentialPart(self.input1)
        self.assertEqual(checkIfPart(PotentialPart, self.input1), False )
        self.input1[0] = "...%......"
        PotentialPart = findPotentialPart(self.input1)
        self.assertEqual(checkIfPart(PotentialPart, self.input1), True )

    def test_checkIfPart_bottom(self): 
        self.input1[2] = ".....$...."
        potentialPart = findPotentialPart(self.input1)
        self.assertEqual(checkIfPart(potentialPart, self.input1), True )


    def test_parseInputToMatrix(self):
        pass