#!/usr/bin/python3
"""Function returns an object (Python data structure)
    represented by a JSON string"""

import json


def from_json_string(my_str):
    """Args:
            my_str - represents the JSON-formatted string
            that you want to convert into a Python object.
    """
    return json.loads(my_str)
