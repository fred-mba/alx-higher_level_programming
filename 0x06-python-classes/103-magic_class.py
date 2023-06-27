#!/usr/bin/python3
"""Class MagicClass"""
import dis
import math


class MagicClass:
    """Circle representation"""
    def __init__(self, radius=0):
        """defines the magic class"""
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    @property
    def radius(self):
        """Finds the radius of the circle"""
        return self.__radius

    def area(self):
        """Finds the area of the circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Finds the area of the circle"""
        return 2 * math.pi * self.__radius
