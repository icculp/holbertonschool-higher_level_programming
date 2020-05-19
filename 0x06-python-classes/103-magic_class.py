#!/usr/bin/python3
"""D"""


class MagicClass:
    """Defines a magicb"""

    import math

    def __init__(self, radius=0):
        """Initializing"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self, radius):
        """Doing math and stuff"""
        return (self.__radius ** 2) * math.pi

    def circumference(self, radius):
        """More maths"""
        return 2 * math.pi * self.__radius
