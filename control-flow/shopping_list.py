#!/usr/bin/env python3

""" Saturday's Shopping"""

# List of desired items to shop for
shopping_list = ['oranges', 'pinapple', 'PS5', 'Armani']

# Items condition/availabilty
item_found = False

# Loop iterates until condition is met(true)
while not item_found:
    # User's input or wishlis item
    item = input('Enter an item on my shopping list or (q to quit): ')
    if item.lower() == 'q':
        break

    if item in shopping_list:
        item_found = True
        print(f'{item} is available!')
    else:
        print(f'{item} not found in shopping list')
