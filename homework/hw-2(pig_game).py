# Every time a player turn is completed, increment a number by 2.  Whomever's number is lesser, that person is the next to roll
# To end the game, use while True: loop that the MAX_SCORE is less than 100.  As it hits 100 or higher, end game
import random

MAX_SCORE = 200

player = input('Who rolls first?  Player 1 or Player 2? ')
player_turn = player


#val = random.randint(1, 6)
total = 0
turn = 0

dice_roll = input(
    f'Hello Player {player_turn}.  Would you like to Roll (y or n)? ')
if dice_roll == ('y'):
    while True:
        val = random.randint(1, 26)
        print(f'{val}')
        if val == 1:
            print(
                f'You rolled a {val} Player {player_turn}, your turn is over - you lose!!')
            total = 0

            break

        else:
            print(f'You got {val} points!!')

            total = total + val
            print(f'{total}')
            if total >= MAX_SCORE:
                print(f'Your final score is {total} ...You win!!')

                break

            else:
                cont = input('Would you like to continue playing? (y or n) ')
                if cont == ('y'):
                    print('Rolling again...')
                else:
                    print(
                        f'Player {player_turn}, your final score was {total}')

                    break
