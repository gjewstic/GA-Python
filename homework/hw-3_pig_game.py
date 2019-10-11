import random

turn = 1
player_one_total = 0
player_two_total = 0

max_score = 50

selection = int(input('Who will be rolling first?  Enter a 1 or 2: '))
turn = selection

while True:
    choice = input(f'Player {turn}, do you choose to roll (r) or pass (p)? ')

    if choice == 'r':
        score = random.randint(1, 15)
        if score is not 1:
            if turn is 1:
                player_one_total += score
                print(
                    f'Player {turn}, you scored {score}.  Your current total is: {player_one_total}')
            else:
                player_two_total += score
                print(
                    f'Player {turn}, you scored {score}.  Your current total is: {player_two_total}')
        else:
            if turn is 1:
                print(
                    f'Player {turn}, your score is {score}.  You lose your turn.')
                player_one_total = 0
                turn = 2
            else:
                print(
                    f'Player {turn}, your score is {score}.  You lose your turn.')
                player_two_total = 0
                turn = 1
    #
    else:
        if turn == 1:
            turn = 2
            print(f'Player {turn}, your score is {score}.')
        else:
            turn = 1
        choice = input(
            f'Player {turn}, do you choose to roll (r) or pass (p)? ')
        score = random.randint(1, 15)
    #
        if score is not 1:
            if turn is 1:
                player_one_total += score
                print(
                    f'Player {turn}, you scored {score}.  Your current total is: {player_one_total}')
            else:
                player_two_total += score
                print(
                    f'Player {turn}, you scored {score}.  Your current total is: {player_two_total}')
        else:
            if turn is 1:
                print(
                    f'Player {turn}, your score is {score}.  You lose your turn.')
                player_one_total = 0
                turn = 2
            else:
                print(
                    f'Player {turn}, your score is {score}.  You lose your turn.')
                player_two_total = 0
                turn = 1

    #
    if player_one_total >= max_score or player_two_total >= max_score:
        if player_one_total > max_score:
            print(f'Player 1 is the winner!!  Score = {player_one_total}')
        else:
            print(f'Player 2 is the winner!!  Score = {player_two_total}')
        break
