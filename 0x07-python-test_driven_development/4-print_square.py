#!/usr/bin/python3
"""
The module uses print_size function with parameter `size` to print out a square
with the '#' character
"""


def print_square(size):
    """
    Print a square with the character #.

    The function prints a 2D square with the # character from the length of the
    square(size).

    Parameter
    ---------
    size : int, float
    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    # size is a float and is less than 0
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(int(size)):
        print("#" * int(size))
