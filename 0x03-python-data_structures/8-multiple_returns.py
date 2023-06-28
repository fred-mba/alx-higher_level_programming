#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Returns a tuple containing the length of the sentence and
    its first character.
    If the sentence is empty, returns None as the first character.
    """
    length = len(sentence)
    first_char = sentence[0] if length > 0 else None
    return length, first_char
