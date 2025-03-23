#!/usr/bin/python3
"""Search and Update"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line
       containing a specific string"""
    with open(filename, mode='r') as file:
        strings = []
        for line in file:
            strings.append(line)
            if search_string in line:
                strings.append(new_string)
    with open(filename, mode='w') as file:
        file.writelines(strings)
