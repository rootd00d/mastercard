#!/usr/bin/env python

values = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "Dupe": "value2"
 }

duplicates = {}

for value in values.values():
    if value in duplicates:
        print("Duplicate value found: " + value)
    else:
        duplicates[value] = 1
