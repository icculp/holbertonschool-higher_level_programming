#!/usr/bin/python3
"""
    Task 1
"""
from urllib import request
import sys


ur = sys.argv[1]
with request.urlopen(ur) as response:
    print(response.getheader('X-Request-Id'))
