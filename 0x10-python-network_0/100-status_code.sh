#!/bin/bash
# Task 5
curl -o /dev/null -s -w "%{http_code}" "$1"
