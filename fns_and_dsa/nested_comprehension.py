#!/usr/bin/env python3

"""Transpose a 3*4 dimensional matrix using list comprehension"""

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Transposing a matrix. ie turning rows to columns and vive versa
# Pythonic way. List comprehension
res = [[row[i] for row in matrix] for i in range(4)]

print(res, end='\n\n')

# Transposing using functions or nested loops
# Explicit way
transposed = []

for i in range(4):
    transposed.append([row[i] for row in matrix])
        
print(transposed, end='\n\n')

# Best use: real world built in functions
# zip()
transpose = list(zip(*matrix))
print(transpose)
