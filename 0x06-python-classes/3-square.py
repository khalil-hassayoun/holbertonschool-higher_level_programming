#!/usr/bin/python3
"""
Square Module - for all your needs, as long as they include printing squares!
"""


class Square:
    """
    Square class: now enabling you to print out the area of the square!
    Revolutionary!
    """
    def __init__(self, size=0):
        """
        Init for Square class. Requires a valid integer size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the area of the square (size ** 2)
        """
        return (self.__size ** 2)
