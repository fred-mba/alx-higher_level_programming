#!/usr/bin/python3
"""
    This module defines a square with attribute size by default is 0
"""


class Square:
    """A class representing square"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Computes the area of the square
        Returns:
                the current square area
        """
        return self.__size ** 2
