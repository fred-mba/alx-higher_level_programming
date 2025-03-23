#!/usr/bin/python3
"""Student disk and reload"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a student instance"""
        if attrs is None:
            return self.__dict__
        if isinstance(attrs, list):
            filtered_attr = {}
            for key in self.__dict__.keys():
                if key in attrs:
                    filtered_attr[key] = self.__dict__(key)
            return filtered_attr

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance dynamically"""
        for key, value in json.items():
            setattr(self, key, value)
                
            
