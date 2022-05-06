#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    narg = len(sys.argv) - 1
    sum = 0
    for i in range (narg):
        sum = sum + int(sys.argv[i + 1])
    print(f"{sum}")
