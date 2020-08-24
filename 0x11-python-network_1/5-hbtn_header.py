#!/usr/bin/python3
"""
    Task 5
"""
import requests
import sys


if __name__ == '__main__':
    ur = sys.argv[1]
    r = requests.get(ur)
    print(r.headers.get('X-Request-Id'))
