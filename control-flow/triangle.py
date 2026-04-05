#!/usr/bin/env python3

"""A triangle"""

# Outer loop iterates over number of rows
for i in range(1, 10 + 1):
    # Inner loop iterates over the elements of outer loop
    for j in range(1, i + 1):
        print('*', end=' ')
    print()
