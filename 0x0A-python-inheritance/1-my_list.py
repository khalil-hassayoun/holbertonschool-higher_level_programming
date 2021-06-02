#!/usr/bin/python3
"""
Module for task 1
"""


class MyList(list):
    """
    Prints sorted version of list
    """
    def print_sorted(self):
        print(sorted(self))
