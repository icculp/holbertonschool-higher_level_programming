#!/usr/bin/python3
"""
    Task 9 Module
"""


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """ inherits from BaseGeomtry """

    def __init__(self, width, height):
        ''' initialize '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        ''' returns actual area, overriding inheritance '''
        return self.__width * self.__height

    def __str__(self):
        ''' [Rectangle] <width>/<height> '''
        s = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return s
