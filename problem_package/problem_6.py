"""Guessing Game"""
import random

number = random.randint(1, 10)
counter = 0

while counter < 10:
    guessed_number = int(input('Enter the guessed number: '))
    if guessed_number == number:
        print('Congratulations', number, 'is correct!')
        break
    else:
        print('Try again')
    counter += 1

if counter == 10:
    print('You have exhausted your number of trials')