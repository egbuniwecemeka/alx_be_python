#!/usr/bin/env python3

"""Stores information about favorite book"""

book = {'title':'Think big', 'author': 'Ben Carson', 'genre': 'motivational'}

# print a particular key
print(book.get('genre'))

# print the keys
print(book.keys())

# print the values
print(book.values())

# Retrieve keys and values
print(book.items())
