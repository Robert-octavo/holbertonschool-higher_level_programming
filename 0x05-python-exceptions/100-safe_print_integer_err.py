#!/usr/bin/python3
from sys import exc_info
from sys import stderr

"""
Write a function that prints an integer.
- value can be any type (integer, string, etc.)
- The integer should be printed followed by a new line
- Returns True if value has been correctly printed
    (it means the value is an integer)
- Otherwise, returns False and prints in stderr the error
    precede by Exception:
"""


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError):
        print("Exception: {}".format(exc_info()[1]), file=stderr)
        return (False)
