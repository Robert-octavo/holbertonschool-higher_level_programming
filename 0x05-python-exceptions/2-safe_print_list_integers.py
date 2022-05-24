#!/usr/bin/python3
"""
Write a function that prints the first x elements of a
list and only integers.
- my_list can contain any type (integer, string, etc.)
- All integers have to be printed on the same line followed
by a new line - other type of value in the list must be skipped
(in silence).
- x represents the number of elements to access in my_list
- x can be bigger than the length of my_list - if it is the case,
an exception is expected to occur
-Returns the real number of integers printed
"""


def safe_print_list_integers(my_list=[], x=0):

    len = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            len += 1
        except (TypeError, ValueError):
            break
    print("")
    return (len)
