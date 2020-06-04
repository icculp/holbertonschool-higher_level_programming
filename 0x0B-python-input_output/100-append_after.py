#!/usr/bin/python3
"""
    Task 100 Module
"""


def append_after(filename="", search_string="", new_string=""):
    """ appends after certain string """
    with open(filename, 'r', encoding='UTF-8') as f:
        count = 0
        rl = f.readlines()
        for i in range(len(rl)):
            if search_string in rl[i]:
                rl.insert(i + 1, new_string)
                count += 1
                continue
    with open(filename, 'w', encoding='utf-8') as o:
        o.writelines(rl)
