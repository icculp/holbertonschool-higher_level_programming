#!/usr/bin/python3
"""
    Square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializing Square """
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        ''' sizeh setter '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value
            self.__height = value
            self.__size = value

    def __str__(self):
        ''' [Square] (<id>) <x>/<y> - <size> '''
        s = "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.__size)
        return s

    def update(self, *args, **kwargs):
        ''' updates attributes of Square '''
        l = [None] * 4
        for a in range(len(args)):
            l[a] = args[a]
        if l[0] is not None:
            self.id = args[0]
        elif 'id' in kwargs:
            self.id = kwargs['id']
        if l[1] is not None:
            self.__size = args[1]
        elif 'size' in kwargs:
            self.__size = kwargs['size']
        if l[2] is not None:
            self.x = args[2]
        elif 'x' in kwargs:
            self.x = kwargs['x']
        if l[3] is not None:
            self.y = args[3]
        elif 'y' in kwargs:
            self.y = kwargs['y']

    def to_dictionary(self):
        ''' dictionary representation of square '''
        d = dict()
        d['id'] = self.id
        d['size'] = self.__size
        d['x'] = self.x
        d['y'] = self.y
        return d
