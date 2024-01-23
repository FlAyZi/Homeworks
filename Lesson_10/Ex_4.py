'''Write a Python program that generates a random number between 1 and 100 and asks
the user to guess the number. The program should give hints whether the guessed
number is too high or too low until the correct number is guessed.'''

import random

random_number = random.randint(1, 100)
while True:
    a = int(input())
    if a < random_number:
        print('number too low until')
    elif a > random_number:
        print('number is too high')
    else:
        print('number is guessed.')
        break