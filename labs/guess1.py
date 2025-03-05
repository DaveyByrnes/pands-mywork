# guess1.py
# write a program that prompts the user to guess
# a number, the program should keep prompting the
# user until the number is correctly guessed

number_to_guess = 30

guess = int(input("Please guess the number:"))
while guess != number_to_guess:
    guess = int(input("Wrong! Please guess again:"))

print("Well done! Yes the number was", number_to_guess)