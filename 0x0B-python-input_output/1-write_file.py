#!/usr/bin/python3
"""This function writes a string to a text file (UTF8) and
    returns the number of characters written"""


def write_file(filename="", text=""):
    """Args:
       filename: name of the file
       text: text to be written to file
       These two are initialized to empty string
    """
    with open(filename, mode='w', encoding="utf-8") as file:
        return file.write(text)
