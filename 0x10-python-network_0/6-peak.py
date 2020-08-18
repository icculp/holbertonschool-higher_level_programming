#!/usr/bin/python3
"""
    Task 6
"""


def find_peak(list_of_integers):
    """ Finds a peak in an array """
    l = len(list_of_integers) - 1
    li = list_of_integers
    i = 1
    if len(li) == 0:
        return None
    if li[0] > li[1]:
        return li[0]
    elif li[l] > li[l - 1]:
        return li[l]
#   l = l - 1
    while i <= l:
        if li[i] > li[i - 1] and li[i] > li[i + 1]:
            return li[i]
        if li[l] > li[l - 1] and li[l] > li[l + 1]:
            return li[l]
        l = l - 1
        i = i + 1
