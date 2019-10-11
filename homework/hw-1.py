'''
statement = 'Homework is fun!!'
num = 3
for _ in range(num):
    print(statement)

print(statement * num)
'''

num_list = [2, 4, 6, 8, 10]
num = 5

# - go thru each element and multiply it by num
'''
# - this for loop does not change the list
for x in num_list:
    print(x * num)
'''
'''
# - to change the list, must use the index
for idx in range(len(num_list)):
    num_list[idx] *= num

print(num_list)


# Reverse a string
# Create a variable that is an empty string
# add characters of old string 1 by 1, in reverse order

my_string = 'This is a sentence'
reversed_string = ''

# loop from last to first character
for idx in range(len(my_string) - 1, -1, -1):
    reversed_string += my_string[idx]

print(reversed_string)


# Calc u later
# Read an operation (add, multiply, divide, subtract)
# Read two integers
# Execute the operation

op = input('Enter an operation[add, sub, mul, div]: ')

# read in the first and second numbers
# All input from the keyboard is by default a string
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

# Calculate the result
result = None

if op == 'add':
    result = num1 + num2
elif op == 'sub':
    result = num1 - num2
elif op == 'mul':
    result = num1 * num2
elif op == 'div':
    result = num1 / num2
else:
    print('Invalid Operation')

print(result)
'''
