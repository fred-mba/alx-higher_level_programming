#!/usr/bin/python3
"""A BaseGeometry class"""


class BaseGeometry:

    """
    A BaseGeometry class with public instance methods:
    area(): returns an exception
    integer_validator(): validates if value passed to name is
                an exact data type or greater than 0
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
