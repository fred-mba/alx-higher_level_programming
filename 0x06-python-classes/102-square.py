#!/usr/bin/python3
"""Defines a square by private size attribute

   Size set to 0 by default"""


class Square:
    """A class representing square"""
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

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Square):
            return self.area() != other.area()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Square):
            return self.area() <= other.area()
