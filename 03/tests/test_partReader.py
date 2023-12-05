import unittest
from src.partReader import *

class Test_partReader(unittest.TestCase):
    
    def setUp(self):
        self.input1: [] = [ '..........',
                            '...1111...',
                            '..........']
        self.input2: [] = [ '.........222....333..',
                            '...1111.......4......',
                            '55........666666....7']
        self.input3: [] = ['467..114..',
                           '...*......',
                           '..35..633.',
                           '......#...',
                           '617*......',
                           '.....+.58.',
                           '..592.....',
                           '......755.',
                           '...$.*....',
                           '.664.598..']

    def test_findPotentialPart(self):
        expected = [{ "value": 1111, "partX": 3, "partY": 1, "partLen": 4 }]
        self.assertEqual(findPotentialParts(self.input1), expected)

    def test_checkIfPart_Sides(self):
        potentialPart = findPotentialParts(self.input1)[0]
        self.assertEqual(checkIfPart(potentialPart, self.input1), False)
        self.input1[1] = "..+1111..."
        self.assertEqual(checkIfPart(potentialPart, self.input1), True)
        self.input1[1] = "...1111-.."
        self.assertEqual(checkIfPart(potentialPart, self.input1), True)

    def test_checkIfPart_Sides_onEdge(self):
        self.input1[1] = "1111......"
        potentialPart = findPotentialParts(self.input1)[0]
        self.assertEqual(checkIfPart(potentialPart, self.input1), False)
        self.input1[1] = "1111.....*" # array[-1] goes to last integer if unchecked
        potentialPart = findPotentialParts(self.input1)[0]
        self.assertEqual(checkIfPart(potentialPart, self.input1), False)
        self.input1[1] = "......1111"
        potentialPart = findPotentialParts(self.input1)[0]
        self.assertEqual(checkIfPart(potentialPart, self.input1), False)

    def test_checkIfPart_top(self):
        potentialPart = findPotentialParts(self.input1)[0]
        self.assertEqual(checkIfPart(potentialPart, self.input1), False )
        self.input1[0] = "...%......"
        potentialPart = findPotentialParts(self.input1)[0]
        self.assertEqual(checkIfPart(potentialPart, self.input1), True )
     
    def test_checkIfPart_bottom(self): 
        self.input1[2] = ".....$...."
        potentialPart = findPotentialParts(self.input1)[0]
        self.assertEqual(checkIfPart(potentialPart, self.input1), True )

    def test_checkIfPart_top_WhenOnBottomEdge(self):
        self.input1[1] = ".........."
        self.input1[2] = "...1111..."
        potentialPart = findPotentialParts(self.input1)[0]
        self.assertEqual(checkIfPart(potentialPart, self.input1), False)
        self.input1[1] = "......?..."
        self.assertEqual(checkIfPart(potentialPart, self.input1), True)
        
    def test_checkIfPart_top_WhenOnTopEdge(self):
        self.input1[0] = "...1111..."
        self.input1[1] = ".........."
        potentialPart = findPotentialParts(self.input1)[0]
        self.assertEqual(checkIfPart(potentialPart, self.input1), False)
        self.input1[1] = "....!....."
        self.assertEqual(checkIfPart(potentialPart, self.input1), True)
        self.input1[1] = ".........."
        self.input1[2] = "....!....." # again array[-1] needs to be checked
        self.assertEqual(checkIfPart(potentialPart, self.input1), False)

    def test_checkDiagonals(self):
        self.input1[0] = "..^......."
        potentialPart = findPotentialParts(self.input1)[0]
        self.assertEqual(checkIfPart(potentialPart, self.input1), True)
        self.input1[0] = ".......=.."
        self.assertEqual(checkIfPart(potentialPart, self.input1), True)
        self.input1[0] = ".........."
        self.input1[2] = "..(......."
        self.assertEqual(checkIfPart(potentialPart, self.input1), True)
        self.input1[0] = ".......£.."
        self.assertEqual(checkIfPart(potentialPart, self.input1), True)
    
    def test_checkTwoPartsSeparatedBySymbol(self):
        self.input1[1] = "..11*222.."
        potentialParts = findPotentialParts(self.input1)
        self.assertEqual(len(potentialParts), 2)

    def test_findAllPotentialPartsInLine(self):
        potentialParts: [] = findPotentialParts(self.input2)
        self.assertEqual(len(potentialParts), 7)

    def test_checksAndAddsUpAllPieces(self):
        potentialParts: [] = findPotentialParts(self.input1)
        self.assertEqual(checkPartsAndGetSumOfCorrectParts(self.input1), 0)
        self.input1[0] = "...%......"
        self.assertEqual(checkPartsAndGetSumOfCorrectParts(self.input1), 1111)
        potentialParts = findPotentialParts(self.input3)
        self.assertEqual(checkPartsAndGetSumOfCorrectParts(self.input3), 4361)

    def test_findsPotentialGears(self):
        self.assertEqual(len(getPotentialGears(self.input3)), 5)
        self.input1[1] = "..11*222.."
        self.assertEqual(len(getPotentialGears(self.input1)), 2)

    def test_findGearsFromPotential(self):
        self.input1[1] = "..11*222.."
        self.assertEqual(getGears(self.input1), 1)
        self.assertEqual(getGears(self.input3), 2)