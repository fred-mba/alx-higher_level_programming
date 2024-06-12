#!/usr/bin/python3
"""
This module prints out 1st and last name using say_my_name function
"""


def say_my_name(first_name, last_name=""):
    """
    Print 1st and last name.

    This function takes the two parameters which should print out concantenated
    string name.

    Parameters
    ----------
    first_name : str
    last_name : str, default whitespace ""
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    full_name = ("My name is {} {}".format(first_name, last_name))
    print(full_name)
