#!/usr#!/usrython3
"""
    Base module
"""
import json
import turtle


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializing Base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' returns a json string representation of dict '''
        if list_dictionaries is None:
            return "[]"
        else:
            s = json.dumps(list_dictionaries)
            return s

    @classmethod
    def save_to_file(cls, list_objs):
        ''' writes json string to file '''
        fn = str(cls.__name__) + '.json'
        if list_objs is None:
            with open(fn, 'w', encoding='utf-8') as f:
                json.dump("[]", f)
        s = []
        for obj in list_objs:
            d = obj.to_dictionary()
            s.append(d)
        t = Base.to_json_string(s)
        u = json.loads(t)
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(t)

    @staticmethod
    def from_json_string(json_string):
        ''' returns list of json string '''
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        ''' returns instance with all attributes already set '''
        dummy = cls(1, 1, 1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        ''' loads instances from a file '''
        fn = str(cls.__name__) + '.json'
        try:
            with open(fn, 'r', encoding='utf-8') as f:
                s = f.read()
                l = cls.from_json_string(s)
            il = []
            for instance in l:
                il.append(cls.create(**instance))
            return il
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        ''' serializes to csv '''
        fn = str(cls.__name__) + ".csv"
        nl = []
        for obj in list_objs:
            d = obj.to_dictionary()
            if cls.__name__ is "Rectangle":
                nl.append("{},{},{},{},{}\n"
                          .format(d['id'], d['width'], d['height'],
                                  d['x'], d['y']))
            if cls.__name__ is "Square":
                nl.append("{},{},{},{}\n"
                          .format(d['id'], d['size'],
                                  d['x'], d['y']))
        with open(fn, 'w', encoding='utf-8') as f:
            f.writelines(nl)

    @classmethod
    def load_from_file_csv(cls):
        ''' deserializes from csv '''
        fn = str(cls.__name__) + ".csv"
        d = dict()
        fl = []
        with open(fn, 'r', encoding='utf-8') as f:
            rl = f.readlines()
            for r in rl:
                l = r.split(',')
                if cls.__name__ is "Rectangle":
                    d['id'] = int(l[0])
                    d['width'] = int(l[1])
                    d['height'] = int(l[2])
                    d['x'] = int(l[3])
                    d['y'] = int(l[4])
                if cls.__name__ is "Square":
                    d['id'] = int(l[0])
                    d['size'] = int(l[1])
                    d['x'] = int(l[2])
                    d['y'] = int(l[3])
                fl.append(cls.create(**d))
        return fl

    @staticmethod
    def draw(list_rectangles, list_squares):
        ''' draws using turtle '''
        d = 90
        i = 0
        for rect in list_rectangles:
            turtle.color('blue', 'orange')
            turtle.begin_fill()
            i += 10
            turtle.forward(rect.width)
            turtle.left(d)
            turtle.forward(rect.height)
            turtle.left(d)
            turtle.forward(rect.width)
            turtle.left(d)
            turtle.forward(rect.height)
            turtle.left(d + i)
            turtle.end_fill()
#           turtle.reset()
#       i = 0
        for sqr in list_squares:
            turtle.color('green', 'yellow')
            turtle.begin_fill()
            i += 10
            turtle.forward(sqr.size)
            turtle.left(d)
            turtle.forward(sqr.size)
            turtle.left(d)
            turtle.forward(sqr.size)
            turtle.left(d)
            turtle.forward(sqr.size)
            turtle.left(d + i)
            turtle.end_fill()
#           turtle.reset()

        turtle.exitonclick()
