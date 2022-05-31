#!/usr/bin/python3
"""
Write a function that prints My name is <first name> <last name>

    - Prototype: def say_my_name(first_name, last_name=""):
    - first_name and last_name must be strings otherwise, raise a
    TypeError exception with the message first_name must be a string
    or last_name must be a string
    - You are not allowed to import any module

"""


def say_my_name(first_name, last_name=""):
    """
    Check for the type of first_name and last name (string)
    """
    errorf = "first_name must be a string"
    errorl = "last_name must be a string"
    if not isinstance(first_name, str):
        raise TypeError(errorf)
    if not isinstance(last_name, str):
        raise TypeError(errorl)
    print(f"My name is {first_name} {last_name}")
