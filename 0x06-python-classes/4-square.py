#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 3-square.py)

    - Private instance attribute: size:
        - property def size(self): to retrieve it
        - property setter def size(self, value): to set it:
            - size must be an integer, otherwise raise a TypeError
            exception with the message size must be an integer
            - if size is less than 0, raise a ValueError exception with
            the message size must be >= 0
    - Instantiation with optional size: def __init__(self, size=0):
    - Public instance method: def area(self): that returns the current
    square area

    Why?

Why a getter and setter?

    Reminder: size is a private attribute. We did that to make sure we control
    the type and value. Getter and setter methods are not 100% Python, but more
    OOP. With them, you will be able to validate the assignment of a private
    attribute and also define how getting the attribute value will be available
    from outside - by copy? by assignment? etc. Also, adding type/value
    validation in the setter will centralize the logic, since you will do it
    in only one place.
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
