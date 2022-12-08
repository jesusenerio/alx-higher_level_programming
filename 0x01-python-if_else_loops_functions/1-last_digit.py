#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# get the last digit of the number
num = int(str(number)[-1])

# check if the num is less than 6 then print
if num < 6 and num != 0:
    print("Last digit of {} is {} and is less \
            than 6 and not 0".format(number, num))

# check if num is 0 then print
elif num == 0:
    print("Last digit of {} is {} and is 0".format(number, num))

# check if num is greater than 5 then print
else:
    print("Last digit of {} is {} and is greater than 5".format(number, num))
