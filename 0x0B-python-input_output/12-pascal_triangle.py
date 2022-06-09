#!/usr/bin/python3
"""
Technical interview preparation:

    - You are not allowed to google anything
    - Whiteboard first

Create a function def pascal_triangle(n): that returns a list
of lists of integers representing the Pascals triangle of n:

    - Returns an empty list if n <= 0
    - You can assume n will be always an integer

"""
def split(word):
    return [int(char) for char in word]

def pascal_triangle(n):
    """pascal triangle"""
    pascal_list = []
    if n <= 0:
        return []

    for i in range(n):
        """print("[", end="")
        print(','.join(map(str, str(11**i))), end="")
        print("]")"""
        pascal = str(11**i)
        pascal = split(pascal)
        pascal_list.append(pascal)
    return(pascal_list)
