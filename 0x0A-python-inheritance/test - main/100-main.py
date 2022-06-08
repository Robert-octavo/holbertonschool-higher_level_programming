#!/usr/bin/python3
MyInt = __import__('100-my_int').MyInt
"""Check for the atrributes of int"""
print(dir(int))

my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)
