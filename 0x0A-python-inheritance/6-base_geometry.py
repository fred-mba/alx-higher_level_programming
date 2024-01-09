#!/usr/bin/python3
"""A Geometry module with public instance area"""


class BaseGeometry:
    """
    Exception:
        raises area() is not implemented
    """
    def area(self):
        raise Exception("area() is not implemented")
