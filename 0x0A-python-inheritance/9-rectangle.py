#!/usr/bin/python3
"""
Base Geometry module! Base for geometry, I guess.
"""


class BaseGeometry:
    """
    Not quite as empty!
    """
    def area(self):
        """
        Not implemented.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates integers.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0.".format(name))


class Rectangle(BaseGeometry):
    """
    Rectangles!
    """
    def __init__(self, width, height):
        """ Init """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Returns the area """
        return (self.__width * self.__height)

    def __str__(self):
        """ String formatting """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
