#!/usr/bin/python3
"""
This function reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """Function does not need to manage file permission or file
        doesn't exist exceptions"""
    with open(filename, encoding='utf-8') as file:
        for chars in file:
            print(chars, end="")
