'''
# integer (Whole Numbers)
age = 44

#float (whole + decimal)
float_number = 3.0

# boolean
has_kids = True
no_kids = False

# check the type of a variable
print('Variable age is', type(age))
print('Variable float_number is', type(float_number))
print('Variable has_kids is', type(has_kids))
print('Variable no_kids is', type(no_kids))
'''
'''
# check if number is even or odd
num = 10
#num = 3
if num % 2 == 0:
    print('It is even')
else:
    print('It is odd')
'''

# Comparison Operators
# > : greater than
# < : less than
# >= : greater than or equal to
# <= : less than or equal to
# == : equal to
# != : not equal to
'''
# Truthiness
x = 10  # A no zero value is truthy (yes)
y = 0   # A zero or negative value is falsey (no)
z = 'Python'  # A string of non-zero length is truthy (yes)
p = ''  # A string of zero length is falsey (no)
q = []  # An empty list (zero length) is falsey (no)

if q:
    print('yes')
else:
    print('no')
'''
'''
# using 'and' / 'or' in conditionals
num = 15

# display number is odd and less than 20
if num % 2 == 1 and num < 20:
    print('Odd number less than 20')
else:
    print('something else')
'''
'''
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5 print Weird

If is even and in the inclusive range of 6 to 20, print Not Weird
If n is even and greater than 20, print Not Weird
'''
'''
n = 26

if (n % 2 == 1) or (n % 2 == 0 and n >= 6 and n <= 20):
    print('Weird')
if (n % 2 == 0 and (n >= 2 and n <= 5)) or (n % 2 == 0 and n > 20):
    print('Not Weird')
'''

# Nested If's
city = 'Toronto'
name = 'Greg'

if city == 'Toronto':
    if name == 'Greg':
        print('Welcome, newcomer')
    elif name == 'Connor':
        print('Hello, Connor')
    else:
        print(f'Hello, {city}')
else:
    print('I don\'t recognize your city')
