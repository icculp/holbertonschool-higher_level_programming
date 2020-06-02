#!/usr/bin/python3
"""
    Task 11 Module
"""


class Square(__import__('9-rectangle').Rectangle):
    """ Square, inherits from Rectangle """

    def __init__(self, size):
        ''' initialize '''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        ''' returns actual area, overriding inheritance '''
        return self.__size ** 2

    def __str__(self):
        ''' [Square] <width>/<height> '''
        s = "[Square] {}/{}".format(self.__size, self.__size)
        return s
