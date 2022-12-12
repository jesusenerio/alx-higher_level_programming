#!/usr/bin/python3
def fizzbuzz():
    # use for loop to loop i in 1 to 100
    for i in range(1, 101):
        # when i modulo 3 or 5 is equal 0 print fizzbuzz
        if (i % 3) == 0 and (i % 5) == 0:
            print("FizzBuzz", end=" ")
# when i is 3 print fizz
        elif i == 3 or (i % 3) == 0:
            print("Fizz", end=" ")
# when i is 5 print buzz
        elif i == 5 or (i % 5) == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
