#!/usr/bin/python3
"""Function returns the JSON representation of an object (string)"""

import json


def to_json_string(my_obj):
    """Args:
            my_obj - represents the Python object that
            you want to convert to its JSON representation
    """
    return json.dumps(my_obj)
