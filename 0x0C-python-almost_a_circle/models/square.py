#!/usr/bin/python3
"""
    Square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializing Square """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        ''' sizeh setter '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def __str__(self):
        ''' [Square] (<id>) <x>/<y> - <size> '''
        s = "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
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
            self.width = args[1]
            self.height = args[1]
        elif 'size' in kwargs:
            self.width = kwargs['size']
            self.height = kwargs['size']
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
        d['size'] = self.width
        d['x'] = self.x
        d['y'] = self.y
        return d
