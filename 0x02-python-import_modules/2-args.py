#!/usr/bin/python3


def main():
    import sys
    if (len(sys.argv) == 1):
        print("0 argument.")
        exit()
    elif (len(sys.argv) == 2):
        print("1 argument:")
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
    d = 1
    for i in sys.argv[1:]:
        print("{:d}: {}".format(d, i))
        d = d + 1

if (__name__ == "__main__"):
	main()
