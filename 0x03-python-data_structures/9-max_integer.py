#!/usr/bin/python3
def max_integer(my_list=[]):
    if (my_list[0]):
        n = my_list[0]
        for i in range(len(my_list)):
            if (my_list[i] > n):
                n = my_list[i]
        return (n)
    else:
        return (None)
