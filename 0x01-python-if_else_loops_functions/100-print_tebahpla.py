#!/usr/bin/python3
i = 25
string = ""
while (i >= 0):
    if (i % 2 != 0):
        string += chr(i + 97)
    else:
        string += chr(i + 65)
    i -= 1
print("{}".format(string), end="")
