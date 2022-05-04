#!/usr/bin/python3
def print_last_digit(number):
    lsdigit = abs(number) % 10
    print(f"{lsdigit}", end="")
    return (abs(number) % 10)
