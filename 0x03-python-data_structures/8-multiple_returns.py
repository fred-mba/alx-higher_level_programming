#!/usr/bin/python3
def multiple_returns(sentence):
    """
    A function that returns a tuple with the length of a string
    and its first character
    """
    sente_len = len(sentence)
    char_1st = sentence[0] if sente_len > 0 else None

    return sente_len, char_1st
