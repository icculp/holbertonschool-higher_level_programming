#!/usr/bin/python3.7
#mport hash
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    i = 0
    print(new)
    for key in new:
        v = new.get(key)
        print(i, key, v)
        print(hash(key))
        i += 1
        v *= 2
#       new[key] *= 2
        print(new)
        new.update({key: v})
        print(new)
    return new
