#!/bin/bash
# Task 8
curl -s -H "Content-Type: application/json" "$1" -d @"$2"
