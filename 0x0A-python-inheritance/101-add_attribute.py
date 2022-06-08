#!/usr/bin/python3
"""
Write a function that adds a new attribute to an object if it is possible:

    - Raise a TypeError exception, with the message can't add new attribute
    if the object cannot have new attribute
    - You are not allowed to use try/except
    - You are not allowed to import any module

"""


def add_attribute(obj, new_attr, attr_val):
    """adds a new attribute to an object if it is possible"""
    err = "can't add new attribute"
    if not hasattr(obj, "__dict__"):
        raise TypeError(err)
    else:
        setattr(obj, new_attr, attr_val)
