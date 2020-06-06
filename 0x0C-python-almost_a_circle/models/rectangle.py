#!/usr/bin/python3
"""
    Rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializing Rectangle """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        ''' width getter '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' width setter '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        ''' height getter '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' height setter '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        ''' x getter '''
        return self.__x

    @x.setter
    def x(self, value):
        ''' x setter '''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        ''' y getter '''
        return self.__y

    @y.setter
    def y(self, value):
        ''' y setter '''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        ''' returns area of Rectangle '''
        return self.__width * self.__height

    def display(self):
        ''' prints the rectangle using #'s '''
        for l in range(self.__y):
            print()
        for row in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        ''' [Rectangle] (<id>) <x>/<y> - <width>/<height> '''
        s = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return s

    def update(self, *args, **kwargs):
        ''' updates attributes of Rectangle '''
        l = [None] * 5
        for a in range(len(args)):
            l[a] = args[a]
        if l[0] is not None:
            self.id = args[0]
        elif 'id' in kwargs:
            self.id = kwargs['id']
        if l[1] is not None:
            self.__width = args[1]
        elif 'width' in kwargs:
            self.__width = kwargs['width']
        if l[2] is not None:
            self.__height = args[2]
        elif 'height' in kwargs:
            self.__height = kwargs['height']
        if l[3] is not None:
            self.__x = args[3]
        elif 'x' in kwargs:
            self.__x = kwargs['x']
        if l[4] is not None:
            self.__y = args[4]
        elif 'y' in kwargs:
            self.__y = kwargs['y']

    def to_dictionary(self):
        """ returns dictionary representation """
        d = dict()
        d['id'] = self.id
        d['width'] = self.__width
        d['height'] = self.__height
        d['x'] = self.__x
        d['y'] = self.__y
        return d
