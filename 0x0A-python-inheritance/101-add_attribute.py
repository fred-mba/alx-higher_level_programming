#!/usr/bin/python3
""" Add attribute dynamically to an object if possible."""


def add_attribute(obj, name, value):
    """
    Parameters
    ----------
    obj: Object to which attribute is to be added.
    name: Attribute name to add
    value: Value of the attribute to add

    Raises:
    TypeError: If the object cannot be added to the object
    """
    if hasattr(obj, "__dict__") or \
            (hasattr(obj, "__slots__") and name in obj.__slots__):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
