#!/usr/bin/python3
def uniq_add(my_list=[]):
    new1 = my_list.copy()
    new1.sort()
    sum = 0
    for i in range(len(new1)):
        if new1[i] == new1[i - 1]:
            continue
        else:
            sum += new1[i]
    return sum
