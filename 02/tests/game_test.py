from src.game import *
import unittest

class TestGame(unittest.TestCase):

    def setUp(self):
        self.input1: str = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
        self.input2: str = 'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue'

    def test_parceInputToArray(self):
        game1 = gameFactory(self.input1)
        self.assertEqual(game1.id, 1)
        game2 = gameFactory(self.input2)
        self.assertEqual(game2.id, 2)
    
    # def test_parceOneRound(self):
        # self.assertEqual(parseRound(' 1 red, 2 green, 3 blue'))

    def test_check_reds(self):
        self.assertTrue(checkCubes(12, 13, 14, self.input1))
        self.assertFalse(checkCubes(1, 13, 14, self.input1))
        self.assertFalse(checkCubes(12, 13, 1, self.input1))
        self.assertFalse(checkCubes(12, 1, 14, self.input1))
