# average.py
# write a program that keeps reading numbers
# until the user enters a 0. The program should
# append each of them into a list
# the program should then print out each of
# the numbers entered and average them (list)
# author: David Byrne :)

numbers = []

number = int(input("Enter a number (0 to quit): "))

while number != 0:
    numbers.append(number)

    number = int(input("Enter another number (0 to quit): "))

for value in numbers:
    print(value)

# average to be a float
average = float(sum(numbers) / len(numbers))
print(f"The average is {average}.")
