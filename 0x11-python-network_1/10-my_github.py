#!/usr/bin/python3
"""
    Task 9
"""
import requests
import sys


if __name__ == '__main__':
    p = ""
    if len(sys.argv) == 2:
        p = sys.argv[1]
    r = requests.get('https://api.github.com/user',
                     auth=(sys.argv[1], sys.argv[2]))
    j = r.json()
    print(j.get('id'))
