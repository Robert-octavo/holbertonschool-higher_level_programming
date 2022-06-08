#!/usr/bin/python3
"""
Write a class Rectangle that inherits from BaseGeometry
(7-base_geometry.py). (task based on 8-rectangle.py)

    - Instantiation with width and height: def __init__(self, width, height):
        - width and height must be private. No getter or setter
        - width and height must be positive integers validated by
        integer_validator
    - the area() method must be implemented
    - print() should print, and str() should return, the following rectangle
    description: [Rectangle] <width>/<height>

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle inherits from Basegeometry"""
    def __init__(self, width, height):
        """Function to Initializes an instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """formated string"""
        return ()

    def area(self):
        """ Rectangle area"""
        return()

