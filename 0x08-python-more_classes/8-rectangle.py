#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by:
(based on 1-rectangle.py)

    - Private instance attribute: width:
        - property def width(self): to retrieve it
        - property setter def width(self, value): to set it:
            - width must be an integer, otherwise raise a TypeError
            exception with the message width must be an integer
            - if width is less than 0, raise a ValueError exception
            with the message width must be >= 0
    - Private instance attribute: height:
        - property def height(self): to retrieve it
        - property setter def height(self, value): to set it:
            - height must be an integer, otherwise raise a TypeError
            exception with the message height must be an integer
            - if height is less than 0, raise a ValueError exception
            with the message height must be >= 0
    - Public class attribute number_of_instances:
        - Initialized to 0
        - Incremented during each new instance instantiation
        - Decremented during each instance deletion
    - Public class attribute print_symbol:
        - Initialized to #
        - Used as symbol for string representation
        - Can be any type
    - Instantiation with optional width and height:
    def __init__(self, width=0, height=0):
    - Public instance method: def area(self): that returns the rectangle area
    - Public instance method: def perimeter(self): that returns the rectangle
    perimeter:
        - if width or height is equal to 0, perimeter is equal to 0
    - print() and str() should print the rectangle with the character #:
    (see example below)
    - if width or height is equal to 0, return an empty string
    - repr() should return a string representation of the rectangle to be able
    to recreate a new instance by using eval() (see example below)
    - Print the message Bye rectangle... (... being 3 dots not ellipsis) when
    an instance of Rectangle is deleted
    - Static method def bigger_or_equal(rect_1, rect_2): that returns the
    biggest rectangle based on the area
        - rect_1 must be an instance of Rectangle, otherwise raise a TypeErro
        exception with the message rect_1 must be an instance of Rectangle
        - rect_2 must be an instance of Rectangle, otherwise raise a TypeError
        exception with the message rect_2 must be an instance of Rectangle
        - Returns rect_1 if both have the same area value
You are not allowed to import any module

"""


class Rectangle:
    """Rectangle Class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Print a rectangle"""
        res = ""
        if self.__height == 0 or self.__width == 0:
            return (res)
        for i in range(self.__height):
            for j in range(self.__width):
                res += str(self.print_symbol)
            res += "\n"
        res = res[:-1]
        return (res)

    def __repr__(self):
        """return a string representation of the rectangle
        to be able to recreate"""
        return(f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """deletes a rectangle instance and print a messaje"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Retrives the width of a rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set the width of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrives the height of a rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Set the height of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Biggets rectangle based on the area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if (rect_1.area() >= rect_2.area()) else rect_2
