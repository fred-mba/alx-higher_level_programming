#!/usr/bin/python3
"""This module prints a square with the character #

   Args:
        size - must be an int otherwise TypeError
             - is > 0, otherwise ValueError
             - if is a float and < 0 Typerror
"""
def print_square(size):
    """Prints a square of #, otherwise exceptions"""
    if not isinstance(size, (int, float)) or isinstance(size, bool):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(int (size)):
        print("#" * int(size))
