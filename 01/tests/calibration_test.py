import unittest
from src.calibration import *

class TestCalibration(unittest.TestCase):
    
    def setUp(self):
        return
    
    def test_return_input(self):
        self.assertEqual(return_input("hello"), "hello")

    def test_gets_first_digit(self):
        input: str = "aaaaa1aa2aaa"
        self.assertEqual(get_first_digit(input), "1")

    def test_gets_first_digit_if_spelled_out(self):
        input: str = "asdfasdfonea2lksdfjl"
        self.assertEqual(get_first_number(input), '1')
        input: str = "aaaaonetwothreefourlaksjdfl"
        self.assertEqual(get_first_number(input), "1")
        input: str = "twoone"
        self.assertEqual(get_first_number(input), "2")
    
    def test_get_first_when_digits_and_numbers(self):
        input: str = "aaatwo34five"
        self.assertEqual(get_first(input), "2")
        input: str = "a7aatwo34five"
        self.assertEqual(get_first(input), "7")

    def test_get_last_when_digits_and_numbers(self):
        input: str = "aaatwo34five"
        self.assertEqual(get_last(input), "5")
        input: str = "a7aatwo34five6kkg"
        self.assertEqual(get_last(input), "6")

    def test_can_handle_repeated_numbers_and_digits(self):
        input: str = "a7aatwo34five7kkg"
        self.assertEqual(get_last(input), "7")

    def test_gets_last_digit(self):
        input: str = "bbb1bb2bbbbb"
        self.assertEqual(get_last_digit(input), "2")
        input: str = "one7three8two"
        self.assertEqual(get_last(input), "2")
    
    def test_gets_last_number_if_spelled_out(self):
        input: str = "onetwothree"
        self.assertEqual(get_last_number(input), "3")

    def test_get_first_and_last(self):
        input: str = "aaaa1bbbbb2cccc"
        self.assertEqual(get_first_and_last(input), "12")


    def test_read_first_line_in_file(self):
        result: str = "12"
        with open('./tests/test_input1.txt', 'r') as file:
            self.assertEqual(read_first_line(file), result)

    def test_get_sum_of_first_last_from_file(self):
        result: int = 64
        with open('./tests/test_input1.txt', 'r') as file:
            self.assertEqual(get_sum(file), result)

    def test_get_sum_of_first_last_from_file_including_numers_and_digits(self):
        result: int = 72
        with open('./tests/test_input2.txt', 'r') as file:
            self.assertEqual(get_sum(file), result)
     