import random
'''
Guessing game
- get a random between 1 - 10
- prompt the user to guess the number
- loop while the users' guess is not equal to your number
    if the user's guess is less than the number print "too small"
    if the user's guess is greater than the number print "too big"
- print "you are correct" when the user gets the number right
'''
'''
while true
    get random num
    prompt user to guess num
        if their guess is < num then print 'too small'
        if their guess is > num then print 'too big'
        user keeps guessing until their guess = num then print 'you are correct'
        end game on correct guess
'''

num = random.randint(1, 10)
print(str(num))
while True:
    guess = int(input('Guess a number between 1 and 10: '))
    if guess < num:
        print(f'You guessed {guess}. Your guess was too small')
    elif guess > num:
        print(f'You guessed {guess}. Your guess was too big')
    else:
        print(f'You guessed {guess}. Your guess was correct')
        break
