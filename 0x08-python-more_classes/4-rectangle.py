#!/usr/bin/python3
'''Task 2 module'''


class Rectangle:
    '''Defines a rectangle for real this time'''

    def __init__(self, width=0, height=0):
        '''Initializes rectangle class'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''height getter'''
        return self.__height

    @width.setter
    def height(self, value):
        '''height setter'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''returns area of rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''returns perimeter of rectangle'''
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * self.__width + 2 * self.__height

    def __str__(self):
        '''string representation of rectangle'''
        s = ""
        if self.__width is 0 or self.__height is 0:
            return s
        for row in range(self.__height):
            for col in range(self.__width):
                s += "#"
            if row < self.__height - 1:
                s += "\n"
        return s

    def __repr__(self):
        '''string representation of rectangle function'''
        s = "Rectangle({}, {})".format(self.__width, self.__height)
        return s
