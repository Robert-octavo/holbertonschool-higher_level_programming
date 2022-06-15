#!/usr/bin/python3
"""Unittest Square """

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):
    """Test class for Square class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_10_the_square(self):
        """Test Square class: check for attributes."""

        s0 = Square(1)
        self.assertEqual(s0.id, 1)
        s1 = Square(5, 3, 4)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.id, 2)

    def test_10_the_str(self):
        """Test __str__ representation."""

        s1 = Square(9, 4, 5, 6)
        self.assertEqual(str(s1), "[Square] (6) 4/5 - 9")

if __name__ == '__main__':
    unittest.main()