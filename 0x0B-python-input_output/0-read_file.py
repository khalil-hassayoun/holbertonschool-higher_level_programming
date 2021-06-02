#!/usr/bin/python3
"""
read_file module: contains a function that reads a file and prints it to stdout
"""


def read_file(filename=""):
    """
    read_file: takes in a filename. no error checking or handling at all
    prints to stdout
    """
    with open(filename, 'r') as f:
        read_data = f.read()
    print("{:s}".format(read_data), end="")
    f.closed
