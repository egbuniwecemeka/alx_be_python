#!/usr/bin/python3

"""Representation of a queue using a list"""

from collections import deque

# A queue is a data structure in which its order f insertion and removal,
# occurs in a FIFO (First-In-First-Out) format

# First inserted element is 'American'
queue = ['American', 'British', 'Chinese', 'Nigerian']

# deque is a double ended queue used for fast insertion and
# removal from both ends, using normal list method
# is slower because it shifts elments in memory
de_queue = deque(queue)
de_queue.popleft()
print(de_queue)
de_queue.appendleft('Igbo')
print(de_queue)
de_queue.pop()
print(de_queue)