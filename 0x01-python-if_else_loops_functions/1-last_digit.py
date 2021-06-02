#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number >= 0):
    last = number % 10
else:
    last = (abs(number) % 10) * -1
if (last > 5):
    end = "and is greater than 5"
elif (last == 0):
    end = "and is 0"
else:
    end = "and is less than 6 and not 0"
print("Last digit of", "{:d}".format(number), "is {:d}".format(last), end)
