#!/usr/bin/python
"""
The module provides a simple Square class with initialize size.
if size is less than 0, raise a ValueError exception with
the message size must be >= 0
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self): that prints in stdout
the square with the character #:
if size is equal to 0, print an empty line
"""


class Square:
    """Class that defines a square by size, which defaults 0.
    Square can also get area, and print square using '#'.
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size is 0:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)
