# Zala Weyker
# 11/15/2023
# This program reads a file from a given name and determines how often each (latin) lettter appears in it. (zero counts are not mentioned.)

import os

try:
    with open(input("Name the input file"), 'r') as fil:
        content = fil.read()
        catalog = {}
        histogramette = []
        for char in content:
            char = char.lower()
            if char.isalpha():
                if char in catalog:
                    catalog[char] += 1
                else:
                    catalog[char] = 1
        for item in catalog:
            histogramette.append(f'{item} -> {str(catalog[item])}')
        histogramette.sort()
        for item in histogramette:
            print(item)

except IOError as e:
    print("Can't open file: ", os.strerror(e.errno))
