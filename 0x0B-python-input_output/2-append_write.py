#!/usr/bin/python3
"""This function appends a string to a text file (UTF8) and
    returns the number of characters written"""


def append_write(filename="", text=""):
    """Args:
       filename: name of the file
       text: text to be written to file
    """
    with open(filename, mode='a', encoding="utf-8") as file:
        return file.write(text)
