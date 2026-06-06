#!/usr/bin/env python3

"""Generates a set of random numbers"""

# Import random module
from random import randrange

# Generates a set of random numbers
# Note sets {} generates on uniqu numbers
rand_range = {randrange(1, 15) for _ in range(10)}

# Print output
print(rand_range)
