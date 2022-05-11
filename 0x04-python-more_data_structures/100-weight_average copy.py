#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list or len(my_list) == 0:
        return (0)
    average, size = 0, 0
    for i in my_list:
        average += (i[0] * i[1])
        size += i[1]
    return (average / size)
