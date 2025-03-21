#!/usr/bin/python3
"""Defines student based on first & last name, and age"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        if isinstance(attrs, list):
            filtered_dict = {}
            for key in self.__dict__.keys():
                if key in attrs:
                    filtered_dict[key] = self.__dict__[key]
            return filtered_dict
