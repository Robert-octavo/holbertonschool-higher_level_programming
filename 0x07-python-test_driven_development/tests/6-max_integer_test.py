#!/usr/bin/python3
"""
Since the beginning you have been creating “Interactive tests”. For this
exercise, you will add Unittests.

In this task, you will write unittests for the function
def max_integer(list=[]):.

    - Your test file should be inside a folder tests
    - You have to use the unittest module
    - Your test file should be python files (extension: .py)
    - Your test file should be executed by using this command:
    python3 -m unittest tests.6-max_integer_test
    - All tests you make must be passable by the function below
    - We strongly encourage you to work together on test cases,
    so that you donnot miss any edge case

"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for Max Integer"""

    def test_empty(self):
        """test an empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

    def test_regular(self):
        """all ints, Should return the max"""
        list = [1, 2, 3, 4]
        self.assertEqual(max_integer(list), 4)

    def test_negative(self):
        """list with all negative numbers"""
        list = [-6, -40, -1]
        self.assertEqual(max_integer(list), -1)

    def test_floats(self):
        """list with all floats"""
        list = [2.5, 5.5, 8.9]
        self.assertEqual(max_integer(list), 8.9)

    def test_identical(self):
        """Test with a list of identical values"""
        list = [4, 4, 4, 4]
        self.assertEqual(max_integer(list), 4)

    def test_one(self):
        """Test with a list with one element"""
        list = [82]
        self.assertEqual(max_integer(list), 82)

    def test_none(self):
        """Test with a None parameter"""
        self.assertRaises(TypeError, max_integer, None)

    def test_no_list(self):
        """test with somethin that is not a list"""
        self.assertRaises(TypeError, max_integer, 7)

    def test_not_int(self):
        """Test with list letters and int"""
        list = ["a", "d", 2]
        self.assertRaises(TypeError, max_integer, 1)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([10, 9, 8, 2, 1]), 10)

    def test_max_in_meddle(self):
        self.assertEqual(max_integer([8, 4, 10, 6, 1]), 10)

if __name__ == '__main__':
    unittest.main()
