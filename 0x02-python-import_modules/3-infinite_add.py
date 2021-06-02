#!/usr/bin/python3
def main():
    import sys
    value = 0
    for i in sys.argv[1:]:
        value += int(i)
    print("{:d}".format(value))
if (__name__ == "__main__"):
    main()
