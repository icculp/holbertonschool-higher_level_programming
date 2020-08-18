#!/usr/bin/env bash
# Task 0

curl -Is "$1" | grep Content-Length | cut -d ' ' -f 2
