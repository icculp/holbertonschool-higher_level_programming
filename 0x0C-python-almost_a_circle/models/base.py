#!/usr#!/usrython3
"""
    Base module
"""
import json


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
