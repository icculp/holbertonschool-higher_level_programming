#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    new = a_dictionary.copy()
    if len(new) == 0:
        return None
    high = max(new, key=new.get)
    return high
