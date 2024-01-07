#!/usr/bin/python3
"""
This module prints first and last name

Arg:
    first_name(str), last_name(str)
"""


def say_my_name(first_name, last_name=""):
    """Returns (str) of name(s)"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    full_name = ("My name is {} {}".format(first_name, last_name))
    print(full_name)
