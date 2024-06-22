#!/usr/bin/python3
"""
A BaseGeometry class module
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle subclass that inherits from BaseGeometry"""
    def __init__(self, width, height):
        # validate the attributes
        self.integer_validator('width', width)
        self.integer_validator('height', height)

        # If valid, set the attributes
        self.__width = width
        self.__height = height
