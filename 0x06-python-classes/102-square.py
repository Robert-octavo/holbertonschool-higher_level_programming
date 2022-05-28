#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 4-square.py)

    - Private instance attribute: size:
        - property def size(self): to retrieve it
        - property setter def size(self, value): to set it:
            - size must be a number (float or integer), otherwise raise
            a TypeError exception with the message size must be a number
            - if size is less than 0, raise a ValueError exception with
            the message size must be >= 0
    - Instantiation with size: def __init__(self, size=0):
    - Public instance method: def area(self): that returns the current
    square area
    - Square instance can answer to comparators: ==, !=, >, >=, < and <=
    based on the square area

"""


class Square:
    """
    The isinstance() function returns True if the specified object
    is of the specified type, otherwise False.
    """
    def __init__(self, size=0):
        self.__size = size
    """In Python property()is a built-in function that creates and
        returns a property object. A property object has three methods,
        getter(), setter(), and delete()
        https://www.geeksforgeeks.org/getter-and-setter-in-python/
    """
    @property
    def size(self):
        """Return the current size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Return the current area"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Equal"""
        return (self.area() == other.area())

    def __ne__(self, other):
        """Different"""
        return (self.area() != other.area())

    def __ge__(self, other):
        """greater or equal to"""
        return (self.area() >= other.area())

    def __lt__(self, other):
        """Less than"""
        return (self.area() < other.area())

    def __gt__(self, other):
        """Greater than"""
        return (self.area() > other.area())

    def __le__(self, other):
        """Less than or Equal"""
        return (self.area() <= other.area())
