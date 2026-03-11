#!/usr/bin/python3

""" Calculate user's age based on user's input."""

# Retrieve user's age (integer) as input
user_age = int(input('How old are you?'))

# How old will the user be by 2050
# Assumming its the year 2023
year_diff = 2050 - 2023
age_2050 = user_age + year_diff

print(f'In 2050, you will be {age_2050} years old')
