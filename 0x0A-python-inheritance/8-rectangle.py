#!/usr/bin/python3
"""
A BaseGeometry class module
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle subclass that inherits from BaseGeometry"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
