#!/usr/bin/python3
"""
Write a function that prints a text with 2 new lines after each of these
characters: ., ? and :

    - Prototype: def text_indentation(text):
    - text must be a string, otherwise raise a TypeError exception with
    the message text must be a string
    - There should be no space at the beginning or at the end of each printed
    line
    - You are not allowed to import any module

"""


def text_indentation(text):
    """
    Check for the type of text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])
    print(f"{text}", end="")
