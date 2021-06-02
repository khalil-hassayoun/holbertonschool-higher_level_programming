#!/usr/bin/python3
i = 0
string = ""
while (i != 26):
    if (chr(i + 97) != 'q' and chr(i + 97) != 'e'):
        print("{}".format(chr(i + 97)), end="")
    i += 1
