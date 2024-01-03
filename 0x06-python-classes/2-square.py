#!/usr/bin/python3
"""This module defines Square with private instance attribute size

   Instantiation with optional size parameter set to 0 by default
"""


class Square:
    """A class representing a square"""
    def __init__(self, size=0):
        """
        Initializes a new square size

        Args:
            size (int): The size of the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size

    @property
    def condition(self):
        """
        Checks the condition of the square

        Returns:
            bool: True if the condition is met, False otherwise
        """
        return self.__size >= 0
