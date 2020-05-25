#!/usr/bin/python3
'''Task 11 module'''


import sys

if sys.argc != 2:
    print("Usage: nqueens N")
if type(sys.argv[1]) not int:
    print("N must be a number")
    exit(1)
if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

