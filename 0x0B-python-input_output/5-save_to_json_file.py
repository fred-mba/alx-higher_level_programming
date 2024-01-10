#!/usr/bin/python3
"""Function that writes an Object to a text file,
   using a JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """Args:
            my_obj - represents object you want to write to a text file
            filename - pointer to filename
    """
    with open(filename, mode='w', encoding-'utf-8') as file:
        file.write(json.dumps(my_obj))
