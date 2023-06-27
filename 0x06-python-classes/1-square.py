#!/usr/bin/python3
"""This is the "Square"  module"""


class Square():
"""Class Square, manage validation"""
    def __init__(self, size=0):
        if size != int(size):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
