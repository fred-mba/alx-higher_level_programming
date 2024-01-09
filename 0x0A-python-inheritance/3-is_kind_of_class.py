#!/usr/bin/python3
"""This  function returns True if the object is an instance of,
   or if the object is an instance of a class that inherited from, 
   the specified class ; otherwise False"""
def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: the object to ccheck
        a_class: the class to compare against
    Returns:
        True: if obj is an instance of a class or its subclass, False otherwise
    """
    return isinstance(obj, a_class)
