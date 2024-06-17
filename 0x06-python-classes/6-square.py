#!/usr/bin/python3
"""
    Defines Square with private attribute size and position

    that are set to 0 by default

"""


class Square:
    """A class representing square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or \
           len(value) != 2 or \
           not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        else:
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(self.__position[1]):
            print("")

        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
