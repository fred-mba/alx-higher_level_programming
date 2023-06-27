#!/usr/bin/python3
"""
"Square"  module.

Provides a simple Square class with initialize size.
if size is less than 0, raise aValueError exception with
the message size must be >= 0
"""


class Square:
    """This class defines a square by size and can compute area"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
