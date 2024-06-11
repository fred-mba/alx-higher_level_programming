#!/usr/bin/python3
"""
Add integer numbers.
"""


def add_integer(a, b=98):
    """
    Add up two integer values.

    This function adds one value integer to a default value 98.

    Parameters
    ----------
    a : int
    b : int, default 98

    Returns
    -------
    int
       Summation of two numbers
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    for key, value in zip([a, b], ['a', 'b']):
        if isinstance(a, (list, tuple, str)) or \
                isinstance(b, (list, tuple, str)):
            raise TypeError("{} must be an integer".format(value))

    return int(a) + int(b)
