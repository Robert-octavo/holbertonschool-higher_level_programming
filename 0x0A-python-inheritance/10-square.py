#!/usr/bin/python3
"""
Write a class Square that inherits from Rectangle (9-rectangle.py):

    - Instantiation with size: def __init__(self, size)::
        - size must be private. No getter or setter
        - size must be a positive integer, validated by integer_validator
    - the area() method must be implemented

"""
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """class Rectangle inherits from Basegeometry"""
    def __init__(self, size):
        """Function to Initializes an instance"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return (self.__size * self.__size)
