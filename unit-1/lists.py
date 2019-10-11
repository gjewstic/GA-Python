classmates = ['Connor', 'Efe', 'Alexander', 'Bianca', 'Edwin', 'Greg']
# print(type(classmates))
# print(classmates)
# print(len(classmates))

# Get a specific item in a list
# print(classmates[0])

# Print last element in list
# print(classmates[len(classmates)-1])
# print(classmates[-1])

# 0 = where to start; 3 = number of records to return
# print(classmates[0:3])

# Adding an element to the end of the list
# classmates.append('Greg')
# print(classmates)

# Pop: removes last element in list
# classmates.pop()
# print(classmates)

# Insert: Position, Element
# classmates.insert(0, 'Princeton')

# Removes first occurence of element
# classmates.remove('Princeton')
# print(classmates)

ages = [15, 25, 30, 27, 29, 41, 23, 20, 31, 19]
# print(sum(ages))

# For loop
total_ages = 0
'''
for age in ages:
    total_ages += age
print(total_ages)
'''
# Another for loop - use range and indexes
'''
for idx in range(len(ages)):
    total_ages += ages[idx]
print(total_ages)
'''
'''
# Calculate the sum of all the odd number ages in the list
for age in ages:
    if age % 2 != 0:
        total_ages += age
print(total_ages)
'''
for idx in range(len(ages)):
    if ages[idx] % 2 != 0:
        total_ages += ages[idx]
print(total_ages)
