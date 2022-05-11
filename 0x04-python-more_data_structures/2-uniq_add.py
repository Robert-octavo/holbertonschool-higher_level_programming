#!/usr/bin/python3
def uniq_add(my_list=[]):

    new = []
    res = 0
    for i in my_list:
        if i not in new:
            new.append(i)
    for i in range(len(new)):
        res = res + new[i]
    return (res)
