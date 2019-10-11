
'''
num = 3

if num > 5:
    print('too high')
elif num < 3:
    print('too low')
else:
    print('just right')
'''
# print corresponding letters for grades
# 80 - 100, print letter 'A'
# 79 - 60 , print letter 'B'
# 50 - 59, print letter 'C'
# 0 - 49, print letter 'F'
'''
num = 122

if (num >= 80) and (num <= 100):
    print('A')
elif (num >= 60) and (num <= 79):
    print('B')
elif (num >= 50) and (num <= 59):
    print('C')
elif (num >= 0) and (num <= 49):
    print('F')
else:
    print('default')
'''
# fizzbuzz
# for the first 50 int's
# if it's a multiple of 3, print 'fizz'
# if it's a multiple of 5, print 'buzz'
# if it's a multiple of 15, print 'fizzbuzz'
# otherwise, just print the number

'''
for num in range(1, 51):
    #print(num, end=' ')
    if num % 3 == 0:
        print('fizz')
    if num % 5 == 0:
        print('buzz')
    if num % 15 == 0:
        print('fizzbuzz')
    else:
        print(num)
'''

name = 'Fizzbuzz'

if len(name) > 4:
    print('longer than 4')

if len(name) > 6:
    print('longer than 6')
