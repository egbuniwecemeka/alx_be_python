#!/usr/bin/env python3

"""Stores information about favorite book"""

book = {'title':'Think big', 'author': 'Ben Carson', 'genre': 'motivational'}

# Retrieve a particular key
print(book.get('genre'))

# Retrieve the keys
print(book.keys())

# Retrieve the values
print(book.values())

# Retrieve keys and values
print(book.items())
