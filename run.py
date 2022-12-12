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

#Add variables to track score 
you_win = 0 
computer_wins = 0
draw = 0 
select_option = ['Earth', 'Fire','Water']
