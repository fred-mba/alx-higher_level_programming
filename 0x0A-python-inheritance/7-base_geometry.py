#!/usr/bin/python3
"""
A BaseGeometry class with public instance methods:
    area(): returns an exception
    integer_validator(): validates the value type
"""


class BaseGeometry:

    """A BaseGeometry class """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
