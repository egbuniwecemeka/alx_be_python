#!/usr/bin/python3

"""Number Guess Quiz"""

import random

# Random number to be matched by user input
rand_num = random.randint(0, 20)
print(rand_num)

# Variable taking user guess input
guess = 0

# Variable tracking number of guesses
guess_no = 0


while guess != rand_num:
    # Keeps trcks of number of guesses
    guess_no += 1
    print(f'No of guesses {guess_no}')
    # User's input or guess
    guess = int(input('Guess a random number between 0 - 20: '))

print(f'You got it right in {guess_no} tries!')
