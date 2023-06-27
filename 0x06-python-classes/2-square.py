#!/usr/bin/python3
"""
This is the "Square"  module.

Provides a simple Square class with initialize size.
if size is less than 0, raise a ValueError exception with
the message size must be >= 0
"""


class Square:
    """A class that defines a square by size"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
