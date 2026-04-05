#!/usr/bin/env python3

"""A practical explanation of a nested while loop"""

outer_loop = 5

while outer_loop > 0:
    # Iteration of the outer loop controls that of the inner loop
    inner_loop = 1
    while inner_loop <= outer_loop:
        print(f'Inner loop iteraates {inner_loop} time(s)')
        inner_loop += 1
    # Adds a new line after each iteration cycle

    outer_loop -= 1
    print()
