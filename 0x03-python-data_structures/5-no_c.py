#!/bin/bash/python3


def no_c(my_string):
    modified_string = ''

    for letter in my_string:
        if letter.lower() != 'c':
            modified_string += letter

    return modified_string
