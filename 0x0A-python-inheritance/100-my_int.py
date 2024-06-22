#!/usr/bin/python3
"""MyInt class module"""


class MyInt(int):
    """
    MyInt class that inherits from int and returns
    inverted operators from special methods
    """
    def __eq__(self, other):
        if self.__int__ == other.__int__:
            return True
        return False

    def __ne__(self, other):
        if self.__int__ != other.__int__:
            return True
        return False
