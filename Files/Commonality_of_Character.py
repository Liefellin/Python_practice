# Zala Weyker
# 11/15/2023
# This program reads a file from a given name and determines how often each (latin) lettter appears in it. (zero counts are not mentioned. Histogram is sorted in descending order of frequency)

import os

try:
    i = input("Name the input file")
    with open(i, 'r') as infile:
        content = infile.read()
        catalog = {}
        histogram = []
        for char in content:
            char = char.lower()
            if char.isalpha():
                catalog[char] = catalog.get(char, 0)+1

        for item in catalog:
            histogram.append((lambda x: [x, catalog[x]])(item))

        histogram = sorted(histogram, key=lambda character: character[1], reverse=True)
        with open(i+'.hist', 'w') as outfile:
            for letter, frequency in histogram:
                outfile.write(f"{letter} -> {frequency}\n")

except IOError as e:
    print("Can't open file: ", os.strerror(e.errno))
