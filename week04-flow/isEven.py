# lab work for week 04
# write a program that asks the user to input a number and the program will tell the user if the number is even or odd.
# author: David Byrne

num = int(input("Enter a number: "))
if (num % 2) == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

