######
# This file displays the title screen and is the gateway to the other files.
# If you want to play the game, you must run this file.
# If you want to add more roles to the game, you need to make a new role function, and then add it to a setup in "round_procedure.py"
######

from round_generator import load_presets
import random
from formatting import cls, prompt_user_continue
from player import Player

creator_names = ['Alex Clutter', 'Josh Marsh']
first_name = random.choice(creator_names)
creator_names.remove(first_name)

def start_menu():
    print('One Night Werewolf: Python Edition\nCreated by ' + first_name + ' and ' + str(creator_names[0]))
    number = input('Input the number of an option.\n1) Load Game Preset\n2) Make Custom Game\n')
    if number == '1':
        cls()
        load_presets()
    elif number == '2':
        print('Due to time constraints, this option does not exist yet. Please use a preset.')
        prompt_user_continue()
        start_menu()
    else:
        cls()
        print ("That input is invalid. Please enter a valid number.\n")
        start_menu()

#Run the function
start_menu()