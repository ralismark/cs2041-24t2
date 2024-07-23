#!/usr/bin/env python3

"""
Usage: ./tag-count.py [-f | --frequency] <url>
    -f prints tags by frequency (default unsorted)

Fetches the webpage and counts how many of each open tag there are.
"""

import sys
import subprocess
import re

if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--frequency"):
    print_sorted = True
    url = sys.argv[2]
elif len(sys.argv) == 2:
    print_sorted = False
    url = sys.argv[1]
else:
    print("Bad arguments")
    exit(1)

proc = subprocess.run(
    ["curl", url],
    capture_output=True,
    text=True,
)

count = {}

for m in re.finditer(r"<\s*([A-Za-z0-9]+)", proc.stdout):
    tag = m.group(1)
    if tag not in count:
        count[tag] = 1
    else:
        count[tag] += 1

if print_sorted:
    count_sorted = sorted(count.items(), key=lambda item: item[1])
    for tag, num in count_sorted:
        print(tag, num)
else:
    for tag, num in count.items():
        print(tag, num)
