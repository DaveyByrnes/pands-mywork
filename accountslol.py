
# prompt user
acc_num = (input("Please enter your 10 digit account number:"))

# print number
print(acc_num)

# slice the number
anon_num = 'X' * 6 + acc_num[-4:] # negative indexing

# print number
print(anon_num)