#!/usr/bin/python3
i = 0
j = 0
while (i < 8):
    j = i
    while (j <= 9):
        if (j != i):
            print("{}{}".format(i, j), end=", ")
        j += 1
    i += 1
print("{}{}".format(i, j - 1), sep="")
