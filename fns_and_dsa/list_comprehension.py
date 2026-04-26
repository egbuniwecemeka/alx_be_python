#!/usr/bin/env python3

"""A list of squares to n numbers"""

# Using a function
# Explicit and beginner friendly
def squares_n(n):
    """Returns the squares of numbers within a range"""

    # Creates a list
    squares = []

    # Iterates through the list
    for i in range(n):
        # Challenge: Understanding the use of append to add to list
        # Appends elements to list
        squares.append(i**2)
    
    return squares

print(squares_n(10))


# Using functional programming (map + lambda)

s = list(map(lambda x: x**2, range(10)))
print(s)

# Using list comprehension
# Pythonic and preferred
sq = [x**2 for x in range(10)]
print(sq)
