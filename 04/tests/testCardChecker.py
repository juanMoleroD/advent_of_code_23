import unittest
from src.cardChecker import *

class TestScratchcardChecker(unittest.TestCase):

    def test_checkWinningNumber(self):
        input: str = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
        self.assertEqual(getCardPoints(input), 8)