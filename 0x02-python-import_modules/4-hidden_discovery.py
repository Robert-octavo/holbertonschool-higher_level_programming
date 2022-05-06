#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    import sys
#returns all properties and methods of the specified object
    n = dir(hidden_4)
#print(f"{n[0]}")
    for i in n:
        if i[:2] != "__":
            print(f"{i}")
