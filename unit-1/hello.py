
# Python is interpreted language, not compiled
'''
# print('Hello World')
'''
# Variable Definitions:
# Unknown
# Storage
# Change / Changing
# Variety
# Variable names are lowercase (snakecase)
# Uppercase letters in variables represent a constant (doesn't change)
# Can have a number in a variable name; cannot start with a number, can have underscores

first_name = 'Greg'
last_name = 'J'
age = 44
#print(first_name, last_name, sep='-')
#print(first_name, last_name)
#print(first_name + ' ' + last_name)
#print(first_name + ' ' + last_name + ' ' + str(age))
full_name = first_name + ' ' + last_name  # concatenation
# print(full_name)
# format string (PowerShell's -f) -- Python 3.7
#print(f'Hello, my name is {full_name} and I am {age} years old.')
# format string -- Python 3.5
print('Hello, my name is {} and I am {} years old'.format(full_name, age))
