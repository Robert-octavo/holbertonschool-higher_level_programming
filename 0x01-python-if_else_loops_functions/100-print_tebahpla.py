#!/usr/bin/python3
i = 2
for alpha in range(ord('z'), ord('a')-1, -1):
    if i % 2 == 0:
        print(chr(alpha), end="")
    else:
        print(chr(alpha - 32), end="")
    i = i + 1
