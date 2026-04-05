#!/usr/bin/env python3

"""A simple multiplication table"""

# Iterates over factors of the outer loop
for i in range (1, 9):
    # Iterates over factors of the inner loop
    for j in range(1, 9):
        # Multiple of both factors
        product = i * j
        print(f'{i} * {j} = {product}', end='\t')
    print()
