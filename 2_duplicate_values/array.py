#!/usr/bin/env python

values = ["one", "two", "three", "two"]
duplicates = {}

for value in values:
    if value in duplicates:
        print("Duplicate value found: " + value)
    else:
        duplicates[value] = 1
