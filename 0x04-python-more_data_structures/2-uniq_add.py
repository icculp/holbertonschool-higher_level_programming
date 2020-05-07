#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    if (len(my_list) == 0):
        return sum
    new1 = my_list.copy()
    new1.sort()
    sum = new1[0]
    if (len(my_list) == 1):
        return sum
    for i in range(1, len(new1)):
        if new1[i] == new1[i - 1]:
            continue
        else:
            sum += new1[i]
    return sum
