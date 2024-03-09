#!/usr/bin/python3
""" Function prevents the user from dynamically creating
new instance attributes, except if the new instance attribute
is called first_name
"""


class LockedClass:
    """LockedClass representation"""
    __slots__ = ("first_name",)
