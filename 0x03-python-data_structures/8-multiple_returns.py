#!/usr/bin/python3
def multiple_returns(sentence):
    """
    A function that returns a tuple with the length of a string
    and its first character
    """
    if sentence is None:
        return None

    sente_len = len(sentence)
    char_1st = sentence[0]

    return sente_len, char_1st
