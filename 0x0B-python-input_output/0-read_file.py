#!/usr/bin/python3
"""
Write a function that reads a text file (UTF8)
and prints it to stdout:

    - Prototype: def read_file(filename=""):
    - You must use the with statement
    - You donnot need to manage file permission or
    file doesn't exist exceptions.

"""

def read_file(filename=""):
    """function that reads a file"""
    with open(filename, encoding="utf_8") as file:
        print(file.read(), end="")
