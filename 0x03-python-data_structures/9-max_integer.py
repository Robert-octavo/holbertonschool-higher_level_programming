#!/usr/bin/python3
def max_integer(my_list=[]):

    if not my_list:
        return (None)
    max = 0
    for i in range(len(my_list)):
        if my_list[i] > max:
            max = my_list[i]
    return (max)

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))