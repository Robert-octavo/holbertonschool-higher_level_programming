#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 5-square.py)

    - Private instance attribute: size:
        - property def size(self): to retrieve it
        - property setter def size(self, value): to set it:
            - size must be an integer, otherwise raise a TypeError exception
            with the message size must be an integer
            - if size is less than 0, raise a ValueError exception with the
            message size must be >= 0
    - Private instance attribute: position:
        - property def position(self): to retrieve it
        - property setter def position(self, value): to set it:
            - position must be a tuple of 2 positive integers, otherwise raise
            a TypeError exception with the message position must be a tuple of
            2 positive integers
    - Instantiation with optional size and optional position:
    def __init__(self, size=0, position=(0, 0)):
    - Public instance method: def area(self): that returns the current square
    area
    - Public instance method: def my_print(self): that prints in stdout the
    square
    with the character #:
        - if size is equal to 0, print an empty line
        - position should be use by using space - Don not fill lines by spaces
        when position[1] > 0


"""


class Square:
    """
    The isinstance() function returns True if the specified object
    is of the specified type, otherwise False.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
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

    @property
    def position(self):
        """Return the current position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                not all(isinstance(num, int) for num in value) or
                len(value) != 2 or not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area"""
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
            return

        for a in range(0, self.__position[1]):
            print("")
        for i in range(0, self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(self.__size):
                print("#", end="")
            print("")
