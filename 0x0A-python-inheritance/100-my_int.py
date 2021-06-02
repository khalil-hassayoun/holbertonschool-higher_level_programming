#!/usr/bin/python3
""" Module containing an int where == and =! is swapped. """


class MyInt(int):
    """ Int with swapped == and =! returns! """
    def __eq__(self, other):
        """ Returns the opposite. """
        return (int(self) != int(other))

    def __ne__(self, other):
        """ Also returns the opposite. """
        return (int(self) == int(other))
