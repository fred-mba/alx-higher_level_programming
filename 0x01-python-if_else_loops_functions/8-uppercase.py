#!/usr/bin/python3

def uppercase(str):
    output = ""
    for char in str:
        if 97 <= ord(char) <= 122:
            char = chr(ord(char) - 32)
        output += char
    print(output)
