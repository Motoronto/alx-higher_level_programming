#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number:d} is positive")
elif number == 0:
    print(f"{number:d} is zero")
else:
    if number >= -4:
        print(f"from {number:d} is positive")
    else:
        print(f"{number:d} is negative")
