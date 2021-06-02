#!/usr/bin/python3
""" write_file module - function to write to a file """


def write_file(filename="", text=""):
    """ writes to a file """
    with open(filename, 'w', encoding='utf-8') as f:
        num = f.write(text)
    return (num)
