#!/usr/bin/python3

for i in range(122, 96, -1):
    char = chr(i)
    if i % 2 != 0:
        char = char.upper()
    print(char, end='')
