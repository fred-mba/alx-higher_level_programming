#!/usr/bin/python3
"""Base class module"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """"Dictionary to JSON string"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
