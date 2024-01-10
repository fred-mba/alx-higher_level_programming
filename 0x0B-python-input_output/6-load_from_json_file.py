#!/usr/bin/python3
"""Function that creates an Object from a “JSON file" """

import json


def load_from_json_file(filename):
    """Args:
            filename - represents the name of the JSON file
            you want to load and convert into a Python object
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
