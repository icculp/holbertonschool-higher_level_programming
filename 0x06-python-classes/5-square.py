#!/usr/bin/python3
"""D"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return (self.__size*self.__size)

    def my_print(self):
        for row in range(self.__size):
            for column in range(self.__size):
                print("#", end="")
            print()
