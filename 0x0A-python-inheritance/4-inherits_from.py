#!/usr/bin/python3
"""This function returns True if the object is an instance of a class
   that inherited (directly or indirectly) from the specified class ;
   otherwise False
"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: the object to ccheck
        a_class: the class to compare against
    Returns:
        True: if obj is an instance of a class or its subclass, False otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
