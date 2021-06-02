#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if (number > 0):
    string = "is positive"
elif (number == 0):
    string = "is zero"
else:
    string = "is negative"
print("{:d}".format(number), string)
