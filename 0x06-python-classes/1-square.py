#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 0-square.py)

    - Private instance attribute: size
    - Instantiation with size (no type/value verification)
Why?

Why size is private attribute?

    The size of a square is crucial for a square, many things depend of it
    (area computation, etc.), so you, as class builder, must control the type
    and value of this attribute. One way to have the control is to keep it
    privately. You will see in next tasks how to get, update and validate the
    size value.
"""


class Square:
    """ The __init__ function is called every time an object is created from
    a class - the word self is the first parameter of methods that represents
    the instance of the class.
    """
    def __init__(self, size):
        """__size (Double underscores are used for fully private variables.)"""
        self.__size = size
