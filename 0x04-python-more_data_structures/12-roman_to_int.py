#!/usr/bin/python3
def roman_to_int(roman_string):
    r = roman_string
    if type(r) != str or r is None:
        return 0
    i = 0
    p = 'p'
    for c in range(len(r)):
        if c < len(r) - 1:
            if r[c] == 'I' and r[c + 1] not in 'VXLCDM':
                i += 1
            elif r[c] == 'I' and r[c + 1] == 'V':
                i += 4
            elif r[c] == 'I' and r[c + 1] == 'X':
                i += 9
            elif r[c] == 'V' and p != 'I':
                i += 5
            elif r[c] == 'X' and p != 'I' and r[c + 1] not in 'CL':
                i += 10
            elif r[c] == 'L':
                i += 50
            elif r[c] == 'C' and p != 'X':
                i += 100
            elif r[c] == 'C' and p == 'X':
                i += 90
            elif r[c] == 'D':
                i += 500
        else:
            if r[c] == 'I':
                i += 1
            elif r[c] == 'V' and p != 'I':
                i += 5
            elif r[c] == 'X' and p != 'I':
                i += 10
            elif r[c] == 'L':
                i += 50
            elif r[c] == 'C':
                i += 100
            elif r[c] == 'D':
                i += 500
        p = r[c]
    return i
