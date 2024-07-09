#!/usr/bin/env python3

import re
import sys

with open("dictionary.txt") as file:
    for word in file:
        word = word.strip("\n")
        m = re.search(r"[aeiou]{4}", word)
        if m != None:
            print(word + ":" + m.group(0))
