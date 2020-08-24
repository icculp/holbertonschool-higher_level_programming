#!/usr/bin/python3
"""
    Task 3
"""
from urllib import request
from urllib import parse
from urllib import error
import sys


if __name__ == '__main__':
    ur = sys.argv[1]
    try:
        with request.urlopen(ur) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
