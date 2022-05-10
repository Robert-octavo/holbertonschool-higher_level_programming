#!/usr/bin/python3
def multiple_returns(sentence):

    l = len(sentence)
    if sentence == "":
        s = None
    else:
        s = sentence[0]
    new_tuple = (l, s)

    return (new_tuple)
