#!/usr/bin/python3
"""Exact same object module"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of
       the specified class; otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is a_class
