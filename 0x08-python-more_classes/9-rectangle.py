#!/usr/bin/python3
'''Task 8 module'''


class Rectangle:
    '''Defines a rectangle for real this time'''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''Initializes rectangle class'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                s += str(self.print_symbol)
            if row < self.__height - 1:
                s += "\n"
        return s

    def __repr__(self):
        '''string representation of rectangle function'''
        s = "Rectangle({}, {})".format(self.__width, self.__height)
        return s

    def __del__(self):
        '''what to do when del called on rectangle'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Compares two rectangles based on area, returns bigger rectangle'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        '''Returns rectangle square where size is side length'''
        return cls(size, size)
