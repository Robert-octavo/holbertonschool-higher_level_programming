#!/usr/bin/python3
"""
Write a function that divides all elements of a matrix.

    - Prototype: def matrix_divided(matrix, div):
    - matrix must be a list of lists of integers or floats, otherwise
    raise a TypeError exception with the message matrix must be a matrix
    (list of lists) of integers/floats
    - Each row of the matrix must be of the same size, otherwise raise a
    TypeError exception with the message Each row of the matrix must have
    the same size
    - div must be a number (integer or float), otherwise raise a TypeError
    exception with the message div must be a number
    - div cannot be equal to 0, otherwise raise a ZeroDivisionError exception
    with the message division by zero
    - All elements of the matrix should be divided by div, rounded to 2 decimal
    places
    - Returns a new matrix
    - You are not allowed to import any module

"""


def matrix_divided(matrix, div):
    """
    Check for the type of div using isinstance if not int or float raise a
    TypeError
    """
    error = "matrix must be a matrix (list of lists) of integer/floats"
    list_div = []
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be an number")

    """
    Check if div == 0 raise a ZeroDivisionError
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")

    """
    Check for the lenght of the row
    """
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    """
    Check is the matrix is empty and if the matrix is list type
    """
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(error)

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(error)

    for i in matrix:
        for element in i:
            if not (isinstance(element, int) or isinstance(element, float)):
                raise TypeError(error)
        list_div.append([round(element / div, 2) for element in i])

    return (list_div)
