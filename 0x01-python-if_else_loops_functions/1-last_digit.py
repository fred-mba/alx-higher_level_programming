#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
put_sign = -1 if number < 0 else 1

Last_digit = abs(number) % 10 * put_sign

if Last_digit > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, Last_digit))
elif Last_digit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, Last_digit))
elif Last_digit < 6 and Last_digit != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, Last_digit))
