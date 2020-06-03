#!/usr/bin/python3
def magic_string():
    magic_string.__dict__['count'] = -1; magic_string.__dict__['count'] += 1
    return "Holberton, " * magic_string.__dict__['count'] + "Holberton"


#def magic_string():
#   magic_string.count = getattr(magic_string, 'count', -1) + 1
#   return "Holberton, " * magic_string.count + "Holberton"
