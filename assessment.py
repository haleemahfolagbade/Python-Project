"""#1
for i in range(1,11):
    print(i)

#2 Write a Python while loop that repeatedly asks the user for a number and prints "Even" if the number is even, and "Odd" if it's odd. Terminate the loop if the user enters -1.


d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s  %d" % (i, d[i]))
"""
# Python program to illustrate
# nested for loops in Python
"""from __future__ import print_function

for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()

name = 'Mary'
password = 'Swordfish'
if name == 'Mary' and password == 'Swordfish':
    print('Hello Mary\n' + 'Access granted' )
else:
    print ('Access denied')

import random

def getAnswers(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My answer is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

print(getAnswers(random.randint(1, 9)))
print('Hello ', end='')
print('World')

def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')
a()

# a starts
# b starts
# c starts
# c returns
# b returns
# d starts
# d returns
# a returns
catNames = []

while True:
    name = input('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop): ')
    if name == '':
        break
    catNames = catNames + [name]

print('The cat names are:')
for name in catNames:
    print(' ' + name)


suppliers = ['pens', 'staplers', 'flamethrowers', 'binders']

for i in range(len(suppliers)):
    print('index ' + str(i) + ' in supplies is: ' + suppliers[i])

# Index 0 in supplies is: pens


myPetnames = ['Zophie', 'Pooka', 'Fat-tail']
name = input('Enter a pet name:')

while True:
    if name in myPetnames:
        print(name + ' is my pet')
        continue
    else:
        print('I do not have a pet named ' + name)
        break


cat = ['fat', 'grey', 'loud']
size, color, disposition = cat

print(disposition)

suppliers = ['pens', 'staplers', 'flamethrowers', 'binders']

for index, item in enumerate(suppliers):
    print('index ' + str(index) + ' in supplies is: ' + item)


import random

pets = ['Dogs', 'Cats', 'Chickens']

random.shuffle(pets)
print(pets)


import random

messages = ['It is certain', 'It is decidedly so', 'Yes',
            'Reply hazy try again', 'Ask again later',
            'Concentrate and ask again', 'My answer is no',
            'Outlook not so good', 'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])
"""

import copy

spam = ['A', 'B', 'C', 'D']
print(id(spam))

cheese = copy.copy(spam)
print(id(cheese))

