#!/usr/bin/python3
"""
    Task 1
"""
from urllib import request
from sys import argv


ur = argv[1]
with request.urlopen(ur) as response:
    print(response.getheader('X-Request-Id'))
