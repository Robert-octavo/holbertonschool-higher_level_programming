#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    narg = len(sys.argv) - 1
    if narg == 0:
        print(f"{narg} arguments.")
    else:
        print(f"{narg} arguments:")
    for i in range(narg):
        print(f"{i + 1}: {sys.argv[i + 1]}")
