#!/usr/bin/python3
"""
    Task 8 Module
"""


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """ inherits from BaseGeomtry """

    def __init__(self, width, height):
        ''' initialize '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
