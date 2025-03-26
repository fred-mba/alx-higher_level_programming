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

    @staticmethod
    def from_json_string(json_string):
        """"Returns the list of JSON string"""
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"

        try:
            with open(filename, mode='r') as file:
                json_string = file.read()
            list_dict = cls.from_json_string(json_string)

            return [cls.create(**dictionary) for dictionary in list_dict]

        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes JSON string to CSV file"""
        filename = cls.__name__ + ".csv"

        list_dicts = []

        if list_objs:
            for obj in list_objs:
                dictionary = obj.to_dictionary()
                list_dicts.append(dictionary)
        json_string = cls.to_json_string(list_dicts)

        with open(filename, 'w') as file:
            file.write(json_string)

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances from a csv file"""
        filename = cls.__name__ + ".csv"

        try:
            with open(filename, mode='r') as file:
                json_string = file.read()
            list_dict = cls.from_json_string(json_string)

            return [cls.create(**dictionary) for dictionary in list_dict]

        except FileNotFoundError:
            return []
