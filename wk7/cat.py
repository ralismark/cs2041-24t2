#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip("\n")
    print(line)

    # or just print(line, end="")
