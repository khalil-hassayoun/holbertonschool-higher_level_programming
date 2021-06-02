#!/usr/bin/python3
"""
Module to check if an object is the exact given class
"""


def is_same_class(obj, a_class):
    """
    Function to check if an object is an exact class
    """
    if (type(obj) == a_class):
        return True
    return False
