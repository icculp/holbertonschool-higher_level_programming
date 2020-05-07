#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for key in new:
        v = new.get(key)
        v *= 2
        new.update({key: v})
    return new
