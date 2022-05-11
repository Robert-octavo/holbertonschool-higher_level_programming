#!/usr/bin/python3
def best_score(a_dictionary):

    if len(a_dictionary) == 0:
        return (None)

    list = a_dictionary.values()
    mvalue = max(list)
    for key, value in a_dictionary.items():
        if value == mvalue:
            return (key)
