#!/usr/bin/python3
def new_in_list(my_list, idx, new_element):
    if idx < 0:
        return (my_list)
    if idx > (len(my_list) - 1):
        return (my_list)

    my_new_list = []
    my_new_list.extend(my_list)
    #print(my_new_list)
    my_new_list[idx] = new_element

    return (my_new_list)
