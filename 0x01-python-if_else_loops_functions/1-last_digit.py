#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# get the last digit of the number
num = abs(number) % 10

# check if the num is less than 6 then print
if num == 0:
    print(f"Last digit of {number:d} is {num:d} and is 0")
elif number < 0:
    num = -num
    print(f"Last digit of {number:d} is {num:d} and is less than 6 and not 0")
# check if num is 0 then print
elif num > 5:
    print(f"Last digit of {number:d} is {num:d} and is greater than 5")
else:
    print(f"Last digit of {number:d} is {num:d} and is less than 6 and not 0")
