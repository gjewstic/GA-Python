# Functions must be defined before they are called

# Defining a function with no arguments


def first_function():
    print('This is my first function')


# first_function()

# Define a function with a single argument

'''
def message(name):
    print(f'Hello {name}!! How are you?')


# Defining a function, you define it with an argument (name)
# Calling a function, you pass a parameter to it
message('Greg')

'''
# Define a function with two arguments

'''
def send_greeting(name, is_student):
    message = ''
    suffix = ''
    if is_student:
        suffix = 'a student'
    else:
        suffix = 'an instructor'
    message = f'Hello {name}, you are {suffix}'
    print(message)


send_greeting('Greg', True)
# Lookup global vs. local scope in regards to functions
# Cannot print message outside of the functions
# print(message)
'''

# Define a function that returns a value

'''
def sum_my_numbers(nums):
    total = 0
    for num in nums:
        total += num

    return total  # Use return to pass a value to the calling function


result = sum_my_numbers([10, 12, 30, 40, 50])

print(result)

print(sum_my_numbers([1, 2, 3, 4, 5]))
'''
'''
my_list = [1, 2, 3, 4, 4, 5, 5, 6, 6, 6, 7, 4, 2, 1, 3, 4]
my_list = ['apple', 'mango', 'strawberry', 'kiwi', 'kiwi', 'orange']


def item_count(a_list, key):
    count = 0
    for item in a_list:
        if item == key:
            count += 1  # increment your count

    return count


print(item_count(my_list, 'mango'))
'''
# List intersection for homework
# file:///C:/Users/greg_/Downloads/unit-2-homework.pdf

# List intersection
'''

# Python program to illustrate the intersection
# of two lists in most simple way
# Output:
# [9, 11, 26, 28]


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
print(intersection(lst1, lst2))
'''

'''
# Python program to illustrate the intersection
# of two lists using set() method
# Output:
# [9, 10, 4, 5]


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


# Driver Code
lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
print(intersection(lst1, lst2))
'''
'''
Method 3:
In this method we set() the larger list and then use the built-in function called interscetion() 
to compute the intersected list. intersection() is a first-class part of set.

# Python program to illustrate the intersection 
# of two lists using set() and intersection() 
# Output:
# {9, 11}
# Set is another type of list
'''

'''
def Intersection(lst1, lst2):
    return set(lst1).intersection(lst2)


# Driver Code
lst1 = [4, 9, 1, 17, 11, 26, 28, 28, 26, 66, 91]
lst2 = [9, 9, 74, 21, 45, 11, 63]
print(Intersection(lst1, lst2))
'''
# - https://www.geeksforgeeks.org/python-intersection-two-lists/

'''
def list_intersection(list_one, list_two):
    # create a new list with only items in both first and second list
    result = []
    for item_one in list_one:
        for item_two in list_two:
            if item_one == item_two:
                result.append(item_one)
    return result


print(list_intersection([1, 3, 4, 7, 9], [1, 2, 5, 8, 9]))


def list_intersection_2(list_one, list_two):
    result = []
    for item in list_one:
        if item in list_two:
            result.append(item)

    return result


print(list_intersection_2([1, 3, 4, 7, 9], [1, 2, 5, 8, 9]))
'''

r_list = [1, 3, 5, 7, 9]


def reverse_list(my_list):
    new_list = []
    for item in range(len(my_list) - 1, -1, -1):
        new_list.append(my_list[item])
        # new_list.append(item) ** returns the index position as the value (index integer) Result: [4, 3, 2, 1, 0]
        # new_list.append(my_list[item]) ** returns the element (value or content) held within the index Result: [9, 7, 5, 3, 1]
    return new_list


# print(reverse_list(r_list))
def reverse_list_2(my_list):
    return my_list[::-1]


'''
# print(reverse_list_2(r_list))
def is_palindrome(my_string):
#check if my_string is a palindrome
#return true if it is, false otherwise
    reverse_string = ''
    for item in range(len(my_string) - 1, -1, -1):
        reverse_string += my_string[item]

    if reverse_string == my_string:
        return True
    else:
        return False
'''

# print(is_palindrome('racecar'))


def reverse_str(my_string):
    reversed_string = ''
    for idx in range(len(my_string) - 1, -1, -1):
        reversed_string += my_string[idx]
    return reversed_string


def is_palindrome(my_string):
    '''
    check if my_string is a palindrome
    return True if it is, False otherwise
    '''
    backwards = reverse_str(my_string)
    if backwards == my_string:
        return True
    return False


print(is_palindrome('level'))
print(is_palindrome('racecar'))
print(is_palindrome('aaa'))
print(is_palindrome('aaadba'))
print(is_palindrome('amanaplanacanalpanama'))
