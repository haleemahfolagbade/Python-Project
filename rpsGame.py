# program to give a random hand
# if program shows a rock, user enters scissors = Loses
# if program shows rock, user enters paper = Win
# if program shows paper, user enters scissors = Win
# same hand is a tie = Tie
# once a user wins, break

import random
import sys

p = 'Paper'
r = 'Rock'
s = 'Scissors'
q = 'Quit'

win = 0
losses = 0
ties = 0

guess_remaining = 3
guess_hand = random.choice([p, r, s])
move = ['p', 'r', 's', 'q']

print('ROCK, PAPER, SCISSORS')

while guess_remaining > 0:
    print(str(win) + ' Wins, ' + str(losses) + ' Losses, ' + str(ties) + ' Ties')
    move = input('Enter your move: ' + '(r)ock ' + '(p)aper ' + '(s)cissors ' + '(q)uit\n')
    guess_remaining = guess_remaining - 1

    if move not in ['p', 'r', 's', 'q']:
        print('Invalid input. Please try again')
        continue

    if move == 'q':
        print('Goodbye!')
        sys.exit()

    if guess_hand == r and move == 's':
        print(s + ' versus...\n' + guess_hand + '\n You lose!')
        losses = losses + 1
    elif guess_hand == r and move == 'p':
        print(p + ' versus...\n' + guess_hand + '\n You win!')
        win = win + 1
    elif guess_hand == r and move == 'r':
        print(r + ' versus...\n' + guess_hand + '\n It is a tie!')
        ties = ties + 1
    elif guess_hand == p and move == 's':
        print(s + ' versus...\n' + guess_hand + '\n You win!')
        win = win + 1
    elif guess_hand == p and move == 'p':
        print(p + ' versus...\n' + guess_hand + '\n It is a tie!')
        ties = ties + 1
    elif guess_hand == s and move == 'r':
        print(r + ' versus...\n' + guess_hand + '\n You win!')
        win = win + 1
    elif guess_hand == p and move == 'r':
        print(r + ' versus...\n' + guess_hand + '\n You lose!')
        losses = losses + 1
    elif guess_hand == s and move == 'p':
        print(p + ' versus...\n' + guess_hand + '\n You lose!')
        losses = losses + 1
    elif guess_hand == s and move == 's':
        print(s + ' versus...\n' + guess_hand + '\n It is a tie!')
        ties = ties + 1

if guess_remaining == 0:
    print("You've run out of guesses. You lose")



# write a multi-dimensional array with for loop 2 X 2




















