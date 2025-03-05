# guess1.py
# write a program that prompts the user to guess
# a number, the program should keep prompting the
# user until the number is correctly guessed
# author: David Byrne :)

import random

number_to_guess = random.randint(1,100)

guess = int(input("Please guess the number:"))
while guess != number_to_guess:
    if guess < number_to_guess:
        print("Too low")
    else: 
        print("Too high")
    guess = int(input("Wrong! Please guess again:"))