#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    c = new_list.count(search)
    for i in range(c):
        idx = new_list.index(search)
        new_list.insert(idx, replace)
        new_list.remove(search)
    return new_list
