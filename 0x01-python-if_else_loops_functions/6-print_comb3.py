#!/usr/bin/python3
# Authour Adewale_Liadi
# loop first digit from 0 to 9
for num1 in range(0, 10):
    for num2 in range(num1 + 1, 10):
        if num1 == 8 and num2 == 9:
            + 1
            print("{}{}".format(num1, num2))
        else:
            print("{}{}".format(num1, num2), end=", ")
