#!/usr/bin/python3
import hidden_4
def main():
    for i in dir(hidden_4):
        if ("__" not in i):
            print(i)
if (__name__ == "__main__"):
    main()
