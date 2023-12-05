import unittest
from src.cardChecker import *

class TestScratchcardChecker(unittest.TestCase):

    def test_checkWinningNumber(self):
        input: str = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
        self.assertEqual(getCardPoints(input), 8)

    def test_checkMultipleCards(self):
        input = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
                 "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19"]
        self.assertEqual(getAllCardPoints(input), 10)

    def test_checkWinningDetails(self):
        input = "Card 1: 1 2 | 1 0"
        self.assertEqual(getWiningDetails(input), 1)
        input2 = "Card 1: 1 2 | 1 2"
        self.assertEqual(getWiningDetails(input2), 2)

    def test_duplicationOfGames(self):
        input = ["Card 1: 1 2 | 1 0",
                 "Card 2: 1 2 | 3 4"]
        self.assertEqual(getCardCount(input), 3)
        input = [
                    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
                    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
                    'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
                    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
                    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
                    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]
        self.assertEqual(getCardCount(input), 30)