#!/usr/bin/env python3

"""
Usage: ./missing_words.py words1 words2

Print words in words1 but not words2. Files have one word on each line.
"""

import sys

if len(sys.argv) != 3:
    print("Must pass 2 argument")
    exit(1)

with open(sys.argv[2]) as file:
    words2 = {word.rstrip("\n") for word in file}

with open(sys.argv[1]) as file:
    words1 = {word.rstrip("\n") for word in file if word.rstrip("\n") not in words2}

for word in words1:
    print(word)
