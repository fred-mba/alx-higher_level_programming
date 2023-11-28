#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
put_sign = -1 if number < 0 else 1

Last_digit = abs(number) % 10 * put_sign
#Alternatively: Last_digit = number % -10 if number < 0 else number % 10

if Last_digit > 5:
    print("Last digit of {:d} is {:d} and is greater than 5\n".format(number, Last_digit))
elif Last_digit == 0:
    print("Last digit of {:d} is {:d} and is 0\n".format(number, Last_digit))
elif Last_digit < 6 and Last_digit != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0\n".format(number, Last_digit))
