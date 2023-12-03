from src.game import *
import unittest

class TestGame(unittest.TestCase):

    def setUp(self):
        self.input1: str = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
        self.input2: str = 'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue'

    def test_checkCubes(self):
        self.assertEqual(checkCubes(12, 13, 14, self.input1), 1)
        self.assertEqual(checkCubes(1, 13, 14, self.input1), 0)
        self.assertEqual(checkCubes(12, 13, 1, self.input1), 0)
        self.assertEqual(checkCubes(12, 1, 14, self.input1), 0)

    def test_checkCubes_fromFile(self):
        with open('./tests/test_input_1.txt') as file:
            self.assertEqual(checkGameFileForSumOfIdOnValidGames(file, [12,13,14]), 8)

    def test_getMinimunCubes(self):
        self.assertEqual(getMinimunCubes(self.input1), [4,2,6])
        self.assertEqual(getMinimunCubes(self.input2), [1,3,4])

    def test_getPowers_fromFile(self):
        with open('./tests/test_input_1.txt') as file:
            self.assertEqual(checkGameFileForPower(file), 2286)