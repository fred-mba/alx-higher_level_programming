#!/usr/bin/python3
"""
This is the add integer module

Arg:
    a and b must be first casted to integers if they are float

Returns:
     an addition of thr two integers
"""


def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
