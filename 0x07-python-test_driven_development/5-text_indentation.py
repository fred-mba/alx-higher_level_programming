#!/usr/bin/python3
"""
This implementation prints each text after `.`, `:`, and `?` on a new lines
"""


def text_indentation(text):
    """
    Print a text with 2 lines after ., ?, and :.

    The function transverses through each character to find the stated 3
    characters. If found, the sentence is printed out one line followed by
    a new line.

    Parameter
    ---------
    text : str
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_char = ['.', '?', ':']
    sentence_line = ""
    is_last_special = False

    for character in text:
        sentence_line += character
        if character in special_char:
            print(sentence_line.strip())
            print()
            sentence_line = ""  # Reset sentence_line after printing
            is_last_special = True
        else:
            is_last_special = False

    if sentence_line.strip():
        if not is_last_special:
            print(sentence_line.strip(), end="")
        else:
            print(sentence_line.strip())
