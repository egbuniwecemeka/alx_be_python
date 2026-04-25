#!/usr/bin/env python3

"""Representation of a stack using lists"""

# A stack operates using LIFO (Last-In-First-Out)
stack = ['English', 'French', 'Igbo']

# According to the above insertion, Igbo is last, therefore it should be the
# first out in a stack

stack_update = stack.append('Hausa')

print(stack)    # Here Hausa becomes the last insserted

# Hausa gets becomes the last updated. Last-In

stack_delete = stack.pop()    # Hausa gets removed
#stack.pop(stack)    # Igbo second last get removed

print(stack)
