#!/usr/bin/python3
"""
Square Module - for all your needs, as long as they include printing squares!
"""

class Square:
    """
    Square class, now with size that can be set
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
