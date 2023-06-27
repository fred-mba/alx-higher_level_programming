#!/usr/bin/python3
"""
"Square" module definition.

This module provides a simple Square class with initialize size.
Public instance method: def area(self): that returns the 
current square area.
Public instance method: def my_print(self): that prints in
stdout the square with the character "#".
"""


class Square():
    """Class Square, print #"""
    def __init__(self, size=0):
        """initializes the square"""
        self.__size = size

    def area(self):
        """finds the area of the square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Returns size of square"""
        return self.__size

    @size.setter
    def size(self, x):
        """setter of --size"""
        if not str(x).isdigit():
            raise TypeError("size must be an integer")
        if x < 0:
            raise ValueError("size must be >= 0")

        self.__size = x

    def my_print(self):
        """prints the square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
