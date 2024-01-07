#!/usr/bin/python3
"""
This is the add integer module

Arg:
    a and b must be first casted to integers if they are float

"""


def add_integer(a, b=98):
    """Returns an addition of two integers

       Othewise raise a TypeError"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    for num, name in zip([a, b], ['a', 'b']):
        if isinstance(a, (list, tuple, str)) or isinstance(b, (list, tuple, str)):
            raise TypeError("{} must be an integer".format(name))

    return int(a) + int(b)
