# Title: Math Quiz
# Author: Dalila Spencer
# Date: 2025-09-30

# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.

import random
repeat = 'y'

def check_answer(number1, number2, answer):

    returnvalue = False

    if answer == number1 + number2:
        returnvalue = True

    return returnvalue

while repeat == 'y':

    random_number1 = random.randint(1, 300)
    random_number2 = random.randint(1, 300)

    # Give two random numbers to add and get the user's answer
    answer = int(input(f'''{random_number1:>6}
+ {random_number2:>4}
------
> '''))

# check if the answer is right

    if check_answer(random_number1, random_number2, answer):
       print('Correct!')

    # if wrong display that it is incorrect and give the corrct answer
    else:
        print('Incorrect')
        print('The correct answer is', random_number1 + random_number2)

    repeat = input('Would you like to do another one? (y/n): ')
