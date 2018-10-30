#If you want to run the program, go to RUN ME

######
# This file gives the rules for a round on Werewolf. Here you can easily create your own setups.
######

import random
from player import Player
import time
from formatting import cls, prompt_user_continue
from round_procedure import werewolf_night

game_sizes = {
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : '10'
}

def load_presets():
    roles = []
    player_instances = []
    werewolfs = []
    masons = []
    doppleganger = ''
    input_var = input('How many players do you want? (3-10) (This will determine avaliable presets) ')
    if input_var.isdigit():
        player_number = int(input_var)
        cls()
    else:
        cls()
        print('You did not enter a valid number of players. Please try again.')
        load_presets()
    
    if player_number == 3:
        roles = ['werewolf', 'werewolf', 'seer', 'robber', 'troublemaker', 'villager']
    elif player_number == 4:
        roles = ['werewolf', 'werewolf', 'seer', 'robber', 'troublemaker', 'villager', 'villager']
    elif player_number == 5:
        roles = ['werewolf', 'werewolf', 'seer', 'robber', 'troublemaker', 'villager', 'villager', 'villager']
    elif player_number == 6:
        roles = ['werewolf', 'werewolf', 'minion', 'seer', 'robber', 'troublemaker', 'villager', 'villager', 'tanner']
    elif player_number == 7:
        roles = ['werewolf', 'werewolf', 'villager', 'villager', 'seer', 'robber', 'troublemaker', 'tanner', 'drunk', 'minion']
    elif player_number == 8:
        roles = ['werewolf', 'werewolf', 'villager', 'villager', 'seer', 'robber', 'troublemaker', 'tanner', 'drunk', 'hunter', 'minion']
    elif player_number == 9:
        roles = ['werewolf', 'werewolf', 'minion', 'tanner', 'seer', 'robber', 'troublemaker', 'mason', 'mason', 'villager', 'villager', 'insomniac']
    elif player_number == 10:
        roles = ['werewolf', 'werewolf', 'minion', 'tanner', 'seer', 'robber', 'troublemaker', 'mason', 'mason', 'villager', 'villager', 'insomniac', 'doppleganger']
    else:
        print('You did not enter a valid number of players. Please try again.\n')
        load_presets()

    while (player_number > 0):
        player_name = input('Please give player ' + game_sizes[player_number] + ' a name. Make sure it is unique to avoid confusion. ')
        player_instance = Player(player_name, player_number)
        player_instances.append(player_instance)
        cls()
        for player in reversed(player_instances):
            print('Player ' + game_sizes[player.display_number()] + ' is named ' + player.display_name() + '.')
        player_number = player_number - 1
    
    player_number = len(player_instances)
    
    role_print = ''
    for role in roles:
        role_print = role_print + role + ', '
    role_print = role_print[:-2]
    
    for player in player_instances:
        assigned_role = random.choice(roles)
        if assigned_role == 'werewolf':
            werewolfs.append(player)
        if assigned_role == 'mason':
            masons.append(player)
        if assigned_role == 'doppleganger':
            doppleganger = player
        roles.remove(assigned_role)
        player.assign_role(assigned_role)
    
    print ('Roles in this game: ' + role_print)
    prompt_user_continue()
    
    seconds = 5
    while seconds > 0:
        cls()
        for player in reversed(player_instances):
            print('Player ' + game_sizes[player.display_number()] + ' is named ' + player.display_name() + '.')
        if seconds != 1:
            print('The game will begin in ' + str(seconds) + ' seconds.')
        else:
            print('The game will begin in 1 second.')
        time.sleep(1)
        seconds = seconds - 1
    
    werewolf_night(roles, player_instances, werewolfs, masons, doppleganger)