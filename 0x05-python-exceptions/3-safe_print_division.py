#!/usr/bin/python3
"""
Write a function that divides 2 integers and prints the result.
- You can assume that a and b are integers
- The result of the division should print on the finally: section
preceded by Inside result:
- Returns the value of the division, otherwise: None
- You have to use try: / except: / finally:
"""


def safe_print_division(a, b):
    try:
        division = a / b
    except (ZeroDivisionError, TypeError):
        division = None
    finally:
        print("Inside Result: {}".format(division))
    return (division)
