# part of week04 lecture
# write a program that reads a students percentage mark and prints out the corresponding grade
# author: David Byrne :)

percentage = float(input("Enter the percentage: "))
    #print(percentage)

# extra: grades that get 69.5 get rounded to 70
percentage = round(percentage) # rounds to the nearest whole number

if percentage < 0 or percentage > 100:
    # error handling example
    print("Please enter a number between 0 and 100")
elif percentage < 40: # we know it is greater than 0
    print("Fail")
elif percentage < 50: # between 40 and 49
    print("Pass")
elif percentage < 60: # between 50 and 59
    print("Merit 1")
elif percentage < 70:
    print("Merit 2")
else: # only option left is between 70 and 100
    print("Distinction")

