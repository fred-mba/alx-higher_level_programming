#!/usr/bin/python3

output = ""

for i in range(0, 10):
    for j in range(0, 10):
        if i < j:
            if i == 8 and j == 9:
                output += '{}{}'.format(i, j)
            else:
                output += '{}{}, '.format(i, j)

print(output)
