#!/usr/bin/python3
"""
Module to see if object is inherited from a class
"""


def inherits_from(obj, a_class):
    """
    Function to see if obejct is inherited from a class
    """
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
