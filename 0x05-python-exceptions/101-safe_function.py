#!/usr/bin/python3
from sys import exc_info
from sys import stderr

"""
Write a function that executes a function safely.
- Prototype: def safe_function(fct, *args):
- You can assume fct will be always a pointer to a function
- Returns the result of the function,
    Otherwise, returns None if something happens during the
    function and prints in stderr the error precede by Exception:
"""


def safe_function(fct, *args):
    try:
        res = fct(*args)
        return (res)
    except:
        print("Exception: {}".format(exc_info()[1]), file=stderr)
        return (None)
