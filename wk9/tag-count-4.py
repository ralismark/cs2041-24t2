#!/usr/bin/env python3

"""
Usage: ./tag-count.py [-f | --frequency] <url>
    -f prints tags by frequency (default unsorted)

Fetches the webpage and counts how many of each open tag there are.
"""

import sys
import re
import argparse
import requests
import bs4

parser = argparse.ArgumentParser(
    description="Fetches the webpage and counts how many of each open tag there are."
)
parser.add_argument("--frequency", "-f", help="Prints tags by frequency", action="store_true")
parser.add_argument("url")
args = parser.parse_args()

r = requests.get(args.url)
r.raise_for_status()

count = {}

soup = bs4.BeautifulSoup(r.text, "html5lib")
for tag in soup.find_all():
    if tag.name not in count:
        count[tag.name] = 1
    else:
        count[tag.name] += 1

if args.frequency:
    count_sorted = sorted(count.items(), key=lambda item: item[1])
    for tag, num in count_sorted:
        print(tag, num)
else:
    for tag, num in count.items():
        print(tag, num)
