#!/usr/bin/python3
"""
Write a function that prints a square with the character #.

    - Prototype: def print_square(size):
    - size is the size length of the square
    - size must be an integer, otherwise raise a TypeError exception
    with the message size must be an integer
    - if size is less than 0, raise a ValueError exception with the
    message size must be >= 0
    - You are not allowed to import any module

"""


def print_square(size):
    """
    Check for the type of size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
