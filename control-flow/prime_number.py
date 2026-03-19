#!/usr/bin/python

"""Prints composite numbers and prime numbers"""

# iterate over a range of numbers
for i in range(2, 20):      # Outer loop iterating over range to determine
    for j in range(2, i):   # Inner loop iterating over divisible factors
        if i % j == 0:      # Condition determining composite numbers
            print(f'{i} is a composite number')
            break
    else:               # else executes if loop runs normally, i.e.  no break
        print(f'{i} is  prime number')
