#!/usr/bin/python3

class Square:
    """Class Square with area calculation"""

    def __init__(self, size=0):
        # Validates that size is an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        # Validates that size is greater than or equal to 0
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        # Calculates and returns the area of the square
        return self.__size * self.__size
