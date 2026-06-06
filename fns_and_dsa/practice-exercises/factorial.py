#!/usr/bin/env python3

"""Calculates the factorial of a n"""

def factorial(n: int):
    """Returns the factorial of n"""

    # Base case
    if n == 0:
        return 1

    # Prduct of n and all positive integers below it
    return n * (factorial(n - 1))


print(factorial(int(input('Enter an integar'))))
