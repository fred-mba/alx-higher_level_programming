#!/usr/bin/python3
def magic_calculation(a, b, c):
    output = None

    if a < b:
        output = c
    elif c > b:
        output = a + b
    else:
        output = a * b - c

    return output
