#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    for i in reversed(range(0, len(my_list))):
        print(my_list[i])
