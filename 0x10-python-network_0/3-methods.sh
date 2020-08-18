#!/bin/bash
# Task 3
curl -sI "$1" | grep Allow: | sed 's|Allow: ||'
