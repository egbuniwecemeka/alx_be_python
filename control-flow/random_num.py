#!/usr/bin/python3

"""Number Guessing Emulator"""

import random


while True:
    print("I'm thinking of a number between 1 and 10. Can you guess it?")

    # Random number to be matched by user's guess
    secret_num = random.randint(1, 10)
    print(secret_num)

    # Prompt user for input
    guess = int(input('Guess a number'))

    #counter to keep track for right number of guesses
    counter = 0
    match guess:
        case _ if guess == secret_num:  # guess matched
            print('Congratulations, you guessed it!')
            counter = counter + 1
            print(counter)
        case _ if guess > 10:           # guess above expected range
            print('Oops, your guess is a bit high. Try again!')
        case _ if guess < 1:            # guess below range
            print('Nope, your guess is a bit low. Give it another shot!')
        case _:
            print('Wrong guess, Try again.')
    
    play_again = input('Want to play again? Yes|No?').strip().lower()
    if play_again != 'yes':
        break
