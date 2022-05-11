#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    copy_a_dictionary = sorted(a_dictionary.items())
    for i in copy_a_dictionary:
        print(f"{i[0]}: {i[1]}")
