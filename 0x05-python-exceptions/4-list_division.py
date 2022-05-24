#!/usr/bin/python3
"""
Write a function that divides element by element 2 lists.
- my_list_1 and my_list_2 can contain any type (integer, string, etc.)
- list_length can be bigger than the length of both lists
- Returns  a new list (length = list_length) with all divisions
- If 2 elements can not be divided, the division result should be equal to 0
- If an element is not an integer or float:
    print: wrong type
- If the division can not be done (/0):
    print: division by 0
- If my_list_1 or my_list_2 is too short
    print: out of range
"""


def list_division(my_list_1, my_list_2, list_length):
    my_list_3 = []
    for i in range(0, list_length):
        try:
            division = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("Division by 0")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        except TypeError:
            print("Wrong Type")
            division = 0
        finally:
            my_list_3.append(division)
    return (my_list_3)
