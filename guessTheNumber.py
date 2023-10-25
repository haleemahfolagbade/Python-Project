# Guessing Game

import random

secret_number = random.randint(1,20)
guess_remaining = 3
print('I am thinking of a number between 1 and 20.')
for number in range(0,3):
    guess_number = int(input('Take a guess: '))
    guess_remaining = guess_remaining - number
    if guess_number < secret_number:
        print('Your guess is too low.')
    elif guess_number > secret_number:
        print('Your guess is too high.')
    else:
        print('Good job! You guessed my number in ' + str(number) + ' ' + 'guesses!')
        break
if guess_remaining == 0:
    print("You've run out of guesses. You lose")