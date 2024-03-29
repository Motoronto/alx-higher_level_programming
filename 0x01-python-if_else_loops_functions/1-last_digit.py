#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# get the last digit of number
last_digit = abs(number) % 10
# print the output according to the instructions
if number < 0:
    last_digit = -last_digit
if last_digit > 5:
    print(f"Last digit of {number:d} is {last_digit:d} and is "
          f"greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number:d} is {last_digit:d} and is 0")
elif last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number:d} is {last_digit:d} and is "
          f"less than 6 and not 0")
