#!/usr/bin/python3
"""
    Task 1
"""
from urllib import request
from sys import argv


ur = argv[1]
with request.urlopen(ur) as response:
    print(response.getheader('X-Request-Id'))
'''
    for thing in response:
        print("\t- type: {}".format(type(thing)))
        print("\t- content: {}".format(thing))
        print("\t- utf8 content: {}".format(thing.decode("utf-8")))
'''
