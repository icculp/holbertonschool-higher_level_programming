#!/usr/bin/python3
"""
    Task 2
"""
from urllib import request
from urllib import parse
import sys


if __name__ == '__main__':
    ur = sys.argv[1]
    em = sys.argv[2]
    d = parse.urlencode({'email': em})
    d = d.encode('utf-8')
    with request.urlopen(ur, d) as response:
        print(response.read().decode('utf-8'))
