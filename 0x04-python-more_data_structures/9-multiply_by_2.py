#!/usr/bin/pythfn3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    i = 0
    for key in new:
        new[key] *= 2
    return new
