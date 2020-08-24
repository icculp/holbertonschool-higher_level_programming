#!/usr/bin/python3
"""
    Task 6
"""
import requests
import sys


if __name__ == '__main__':
    ur = sys.argv[1]
    em = sys.argv[2]
    r = requests.post(ur, {'email': em})
    print(r.text)
