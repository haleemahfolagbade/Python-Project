"""
def exponent(baseNumber, powerNumber):
    result = 1
    for index in range(powerNumber):
        result = result * baseNumber
    return result

print (exponent(3,3))

patient_name = 'John Smith'
age = 20
new_patient = True
print (patient_name, age, new_patient)

name = input ('What is your name? ')
color = input ('What is your favorite color? ')
print (name + ' likes ' + color)
"""
"""""
weight = input ('Type in your weight(in pounds): ')
conversion = float(weight)/2.2046
print (conversion)
"""
"""""
course = 'Python for beginners'
print (course.title())

housing_price = 1000000
good_credit = False

if good_credit:
    down_payment = housing_price * 0.1
else:
    down_payment = housing_price * 0.2
print(f"Down Payment: ${down_payment}")

name = 'Ha'

if len(name) < 3:
    print('name must be at least 3 characters')
elif len(name) > 50:
    print('name can be a maximum of 50 characters')
else:
    print('name looks good')


weight = int(input ('Input your weight: '))
unit = input ('(L)lbs or (K)kg: ')

if unit.upper() == "L":
    weight = weight / 2.205
    print(f"Weight = {weight} kilos")
else:
    weight = weight * 2.205
    print(f"Weight = {weight} pounds")


secret_number = 10
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('Sorry, you failed!')

command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "help":
        print(
start - to start the car
stop - to stop the car
quit - to exit operations)
    elif command == "start":
        if started:
            print("Car already started!")
        else:
            started = True
            print("Car Started... time to move")
    elif command == "stop":
        if not started:
            print("Car already stopped!")
        else:
            started = False
            print("Car Stopped... what could be wrong")
    elif command == "quit":
        break
    else:
        print("incorrect input")

price = [10,20,30]

total = 0
for cost in price:
    total = cost + total
print(total)


numbers = [2, 2, 2, 2, 5]
for x_counts in numbers:
    output = ''
    for count in range(x_counts):     #this iterates on each of the list items then add represents each with the variable 'x'
        output += 'x'
        print(output)


list = [3,9,50,8,9]
print (max(list))

lists = [3, 9, 50, 8, 9]
max = lists[0]
for list in lists:
    if list > max:
        max = list
print (max)


numbers = [2, 5, 6, 8, 2,4]
final_numbers = []
for i in numbers:
    if i not in final_numbers:
        final_numbers.append(i)
print (final_numbers)


phone = {"1": "one",
         "2": "two",
         "3": "three",
         "4": "four",
         "5": "five",
         "6": "six",
         "7": "seven",
         "8": "eight",
         "9": "nine"
}

print(input('Input phoneNumber: '))
print (phone)


message = input(">")
words = message.split(" ")
emojis = {
    ":)": "😀",
    ":(": "😞"
}
output = ""
for word in words:
   output += emojis.get(word, word) + " "
print (output)


def greetings(name):
    print(f"Hi, {name}")
    print("Welcome back")

greetings("John")
"""
"""""
def message():
    emojis = {
        ":)": "😀",
        ":(": "😞"
    }
    output = ""
    for word in words:
       output += emojis.get(word, word) + " "

message()

months_conversion = {
    0: "January",
    1: "February",
    2: "March"
}

print(months_conversion.get(0, "Not valid"))


secretWord = "love"
guesses = ""
guessLimit = 3
guessCount = 0
outOfGuesses = False

while guesses != secretWord and not(outOfGuesses):
    if guessCount < guessLimit:
        guesses = input("Enter your guesses: ")
        guessCount += 1
    else:
         outOfGuesses = True

if outOfGuesses:
    print("You are out of guesses. YOU LOSE!")
else:
    print("You win!")


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter your phrase: ")))

# this program is good
from student import student
student1 = student("Haleemah", 3.5, "Health", False)
print(student1.gpa)
"""

#Building a multiple choice question

from zigzag import Question

questionPrompt = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

Questions = [
    Question(questionPrompt[0],"a"),
    Question(questionPrompt[1],"c"),
    Question(questionPrompt[2],"b")
]

#next step is to write a function - to run the test and confirm user enters correct answers

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
        print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(Questions)