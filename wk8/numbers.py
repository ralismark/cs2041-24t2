#!/usr/bin/env python3

"""
Usage: ./numbers.py https://www.unsw.edu.au

Find "phone numbers" in page and print each one once.
"Phone numbers" are sequence of 8-15 digits, possibly with spaces/hyphens.
"""

import sys
import subprocess
import re

proc = subprocess.run(
    ["curl", sys.argv[1]], # individual arguments in a list/tuple
    capture_output=True, # capture stdout & stderr (instead of printing to stdout/stderr) and save to proc.stdout and proc.stderr
    text=True, # output normally in bytes, this converts to text
)

# For running shell commands, pass shell=True. e.g.
#
# proc = subprocess.run(
#         "ls | grep a",
#         shell=True,
# )

for m in re.finditer(r"\d([ -]*\d){7,14}", proc.stdout):
    print(m.group(0))
