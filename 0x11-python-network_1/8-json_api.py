#!/usr/bin/python3
"""
    Task 8
"""
import requests
import sys


if __name__ == '__main__':
    p = ""
    if len(sys.argv) == 2:
        p = sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', {'q': p})
    try:
        j = r.json()
        if len(j) != 0:
            print("[{}] {}".format(j.get('id'), j.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
