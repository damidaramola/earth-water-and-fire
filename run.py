import random

print('Welcome to - Earth, Fire, Water!')
add_username = input('What is your name?: ')
print('Hello ' + add_username + '!')


play_game = input('Would you like to play? ')


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
you_win = 0
computer_wins = 0
draw = 0
select_option = ['Earth', 'Fire', 'Water']


def check_winner(your_choice, computer_choice):
    """
    this function checks if you or computer wins
    """
    if (your_choice == 'Water' and computer_choice == 'Earth'):
        print('You lost - Earth absorbs Water!')
        return 'computer'
    elif (your_choice == 'Water' and computer_choice == 'Fire'):
        print('You won! - Water quenches Fire!')
        return 'player'
    elif (your_choice == 'Fire' and computer_choice == 'Water'):
        print('You lost  - Water quenches Fire!')
        return 'computer'
    elif (your_choice == 'Fire' and computer_choice == 'Earth'):
        print('You won! - Fire Burns Earth!')
        return 'player'
    elif (your_choice == 'Earth' and computer_choice == 'Water'):
        print('You won! - Earth absorbs Water!')
        return 'player'
    elif (your_choice == 'Earth' and computer_choice == 'Fire'):
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
        if( your_choice =='Earth' or your_choice == ' Fire' or your_choice == 'Water' ):
            break
        else:
            print('Wrong input.Pick either Earth, Fire or  Water: ')