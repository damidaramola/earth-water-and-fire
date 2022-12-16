import random

print('Welcome to - Earth, Fire, Water!')

while True:
    add_username = input('What is your name?: ')

    if add_username == '':
        print('invalid output. Please insert a username')
        continue
    elif add_username == ' ':
        print('invalid output. Please insert a username')
        continue
    else:
        print('Hi ' + add_username + ' Let\'s play!')
        break

# play_game = input("Would you like to go play or not? (y/Y or n/N): ")

print('''
Instructions of the game

    You are playing Earth, Fire, Water against the computer
    Type in either Earth, Fire or Water
    The computer will pick one of these 3 options
    Read the rules to see which element wins over the other
    Rules

    1.Earth Absorbs Water
    2.Water Quenches Fire
    3.Fire Burns Earth ''')

# Add variables to track score
computer_wins = 0
you_win = 0
draw = 0
select_option = ['Earth', 'Fire', 'Water']


def check_winner(your_choice, computer_choice):
    """
    this function checks if you or computer wins
    """
    if (your_choice == 'water' and computer_choice == 'Earth'):
        print('You lost - Earth absorbs Water!')
        return 'computer'
    elif (your_choice == 'water' and computer_choice == 'Fire'):
        print('You won! - Water quenches Fire!')
        return 'player'
    elif (your_choice == 'fire' and computer_choice == 'Water'):
        print('You lost  - Water quenches Fire!')
        return 'computer'
    elif (your_choice == 'fire' and computer_choice == 'Earth'):
        print('You won! - Fire Burns Earth!')
        return 'player'
    elif (your_choice == 'earth' and computer_choice == 'Water'):
        print('You won! - Earth absorbs Water!')
        return 'player'
    elif (your_choice == 'earth' and computer_choice == 'Fire'):
        print('You lost - Fire Burns Earth!')
        return 'computer'
    else:
        print('It is a draw!, play again')
        return 'draw'

# Use while loop to commence game


while (you_win != 3 and computer_wins != 3):

    # Validate if player inputs either Earth, Fire or  Water
    while True:
        your_choice = input("\nPick either Earth, Fire or  Water: ")
        your_choice_modified = your_choice.lower()
        if (your_choice_modified == 'earth' or your_choice_modified == 'fire' or your_choice_modified == 'water'):
            break
        else:
            print('Wrong input.Pick either Earth, Fire or  Water: ')

    # Generate the computers choice
    computer_choice = random.choice(select_option)

    # print results
    print('Your Choice: ', your_choice)
    print('Computers Choice: ', computer_choice)
    result = check_winner(your_choice, computer_choice)
    if (result == 'player'):
        you_win += 1
    elif (result == 'computer'):
        computer_wins += 1
    else:
        draw += 1
    # print out final results from game
    print('Your score: ', you_win, 'computer: ', computer_wins, 'Draw: ', draw)

print('Game Over!. Thank you for playing :)')
