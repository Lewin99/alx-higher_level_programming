#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 5:
    print("the last digit of the number is {} and is greater than 5\n".format(number))
elif number == 0:
    print("the last digit of the number is {} and is zero\n".format(number))
elif number < 6 and not number == 0:
    print("the last digit of the number is {} and is less than 6 and not 0\n".format(number))
