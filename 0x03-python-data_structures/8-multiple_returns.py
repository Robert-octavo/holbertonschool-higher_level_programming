#!/usr/bin/python3
def multiple_returns(sentence):

    if sentence == "":
        s = None
    else:
        s = sentence[0]
    new_tuple = (len(sentence), s)

    return (new_tuple)
