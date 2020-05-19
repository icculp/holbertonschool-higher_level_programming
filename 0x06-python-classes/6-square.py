#!/usr/bin/python3
"""D"""


class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple)
        or __position[0] < 0 or __position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return (self.__size*self.__size)

    def my_print(self):
        if self.__size == 0:
            for x in range(self.__position[1]):
                print()
            for x in range(self.__position[0]):
                print(" ", end="")
            print()
        else:
            for x in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for column in range(self.__size):
                    print("#", end="")
                print()
