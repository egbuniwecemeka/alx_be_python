#!/usr/bin/env python3

"""Intersection, union and difference of numbers using lists"""

# Using functions
# Explicit and beginner friendly
def intersection(list1, list2):
    """Returns numbers that are """
    intersect = []
    for x in list1:
        for y in list2:
            if x != y:
                # Challenge: understood that appends takes one argument
                intersect.append((x,y))
    return intersect

print(intersection([2,3,4], [3,5,7]))
print()
# Using list comprehension
# Pythonic way, more efficient
intersect = [(x, y) for x in [2, 3, 4] for y in [4, 5, 6]
             if x != y]

print(intersect)
