#!/usr/bin/python3
""" append_write module - contains a function to append text to a file """


def append_write(filename="", text=""):
    """ appends text to filename """
    with open(filename, 'a', encoding='utf-8') as f:
        total = f.write(text)
    f.closed
    return(total)
