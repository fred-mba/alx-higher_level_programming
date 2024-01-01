#!/usr/bin/python3
def raise_exception():
    try:
        result = 1 + "text"

    except TypeError as error:
        raise error
