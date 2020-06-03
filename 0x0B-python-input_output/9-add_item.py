#!/usr/bin/python3
"""
    Task 9 Module
    Write a script that adds all arguments to a Python list,
    and then save them to a file
"""
import json
import sys


load = __import__('8-load_from_json_file').load_from_json_file
save = __import__('7-save_to_json_file').save_to_json_file

try:
    loaded = load('add_item.json')
except FileNotFoundError:
    loaded = []

for s in range(1, len(sys.argv)):
    loaded += sys.argv[s]
save(loaded, "add_item.json")
