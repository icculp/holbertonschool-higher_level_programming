#!/usr/bin/python3
"""
    Task 7
"""
import requests
import sys


if __name__ == '__main__':
    ur = sys.argv[1]

    r = requests.get(ur)
    if r.status_code > 400:
        print("Error code: {}".format(r.status_code))
    else:
        print("{}".format(r.text))
