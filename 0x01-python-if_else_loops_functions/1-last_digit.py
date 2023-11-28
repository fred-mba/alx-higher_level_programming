#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
put_sign = -1 if number < 0 else 1

Last_digit = abs(number) % 10 * put_sign
# Alternative: Last_digit = number % -10 if number < 0 else number % 10

if Last_digit > 5:
    output = 'and is greater than 5'
elif Last_digit == 0:
    output = 'and is 0'
else:
    output = 'and is less than 6 and not 0'

print('Last digit of', '{:d}'.format(number), 'is ', end="")
print('{:d}'.format(Last_digit), output)
