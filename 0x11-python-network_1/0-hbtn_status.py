#!/usr/bin/python3
"""
    Task 0
"""
from urllib import request


with request.urlopen('https://intranet.hbtn.io/status') as response:
    print("Body response:")
    for thing in response:
        print("\t- type: {}".format(type(thing)))
        print("\t- content: {}".format(thing))
        print("\t- utf8 content: {}".format(thing.decode("utf-8")))
