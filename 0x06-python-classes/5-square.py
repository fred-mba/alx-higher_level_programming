#!/usr/bin/python3
"""Defines a square with private attribute size initialized to 0 by default

   Prints in stdout the square with the character `#`
"""


class Square:
    """A class representing Square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")

        for i in range(self.__size):
            print("#" * self.__size)
