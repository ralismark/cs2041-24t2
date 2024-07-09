#!/usr/bin/env python3

# Support optional -<n> argument:
# print first n lines of stdin (default to 10)
#
# e.g. head -5

import sys

lines_to_print = 10

if len(sys.argv) > 1:
    lines_to_print = -int(sys.argv[1])

for item in zip(range(lines_to_print), sys.stdin):
    print(item[1], end="")

# alternatives:

# for line in sys.stdin:
#     if lines_to_print <= 0:
#         break
#     lines_to_print -= 1
#     print(line, end="")

# for i in range(lines_to_print):
#     line = sys.readline()
#     print(line, end="")
