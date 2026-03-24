#!/usr/bin/env python3

"""Calculate the factorial of a number(n)"""

def factorial(n):
    """Returns the factorial of a number"""
    # Stores factorial of number (n)
    # 0! = 1
    factorial_n = 1

    # n! = n * (n - 1)
    for i in range(1, n + 1):
        factorial_n *= i
        # print(i, factorial_n)     # degug result
    print(factorial_n)

        
factorial(5)
