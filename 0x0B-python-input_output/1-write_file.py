#!/usr/bin/python3
"""
Write a function that writes a string to a text file (UTF8) and
returns the number of characters written:

    - Prototype: def write_file(filename="", text=""):
    - You must use the with statement
    - You donnot need to manage file permission exceptions.
    - Your function should create the file if doesnot exist.
    - Your function should overwrite the content of the file if
    it already exists.

"""


def write_file(filename="", text=""):
    """function that write a file"""
    with open(filename, "w+", encoding="utf_8") as file:
        return file.write(text)
