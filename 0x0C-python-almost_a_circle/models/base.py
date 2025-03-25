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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string to file"""
        filename = cls.__name__ + ".json"

        list_dicts = []

        if list_objs:
            for obj in list_objs:
                dictionary = obj.to_dictionary()
                list_dicts.append(dictionary)
            json_string = cls.to_json_string(list_dicts)

            with open(filename, 'w') as file:
                file.write(json_string)
        else:
            return []

    @staticmethod
    def from_json_string(json_string):
        """"JSON string to dictionary"""
        if json_string:
            return json.loads(json_string)
        else:
            return []
