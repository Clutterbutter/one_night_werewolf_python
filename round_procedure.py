#If you want to run go to RUN ME!!!!!!!!!!!!!!!!!!!
######
# This file creates a round on werewolf. The round generator lets you easily add new roles.
# This file should not be modified. Use round generator if you want to modify the roles avaliable.
######

import time
import random
from formatting import cls, prompt_user_continue

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

night_order = []
# Night Routine and Night function
def werewolf_night(roles, player_instances, werewolfs, masons, doppleganger):
    reverse_player_instances = player_instances[::-1]
    for player in player_instances:
        player.assign_end_of_night_role(player.display_role())
    #Doppleganger Functon
    if doppleganger != '':
        cls()
        input ('Player ' + game_sizes[doppleganger.display_number()] + ', aka ' + doppleganger.display_name() + ', please press Enter to recieve your role.')
        print ('Your role is the doppleganger. Choose a player and you will recieve further instruction.')
        success = False
        while success == False:
            for other_player in reversed(player_instances):
                if other_player != doppleganger: 
                    print('Player ' + game_sizes[other_player.display_number()] + ', aka ' + other_player.display_name() + '.')
            number = input('Input the number of a player. (Not word form)')
            if number.isdigit() == False:
                print ('That player does not exist. Please try again.')
                prompt_user_continue()
                continue
            if not len(player_instances) >= int(number) >= 1 or int(number) == doppleganger.display_number():
                print ('That player does not exist or is yourself. Please try again.')
                prompt_user_continue()
            else:
                index_number = int(number) - 1
                other_player_role = reverse_player_instances[index_number].display_end_of_night_role()
                print('Player ' + game_sizes[int(number)] + ', aka ' + reverse_player_instances[index_number].display_name() + "'s role is " + other_player_role + '.')
                if other_player_role == 'villager' or other_player_role == 'tanner' or other_player_role == 'hunter':
                    print('You are now a ' + other_player_role + ' and have gained all abilities and win conditions of that role.')
                    doppleganger.assign_role(other_player_role)
                    prompt_user_continue()
                    success = True
                if other_player_role == 'werewolf':
                    werewolf_print = ''
                    for werewolf in werewolfs:
                        werewolf_print = werewolf_print + werewolf.display_name() + ', '
                    werewolf_print = werewolf_print[:-2]
                    print ('You are now a werewolf. Here is a list of other werewolfs in the game: ' + werewolf_print +'.')
                    doppleganger.assign_role(other_player_role)
                    prompt_user_continue()
                    success = True
                if other_player_role == 'minion':
                    werewolf_print = ''
                    for werewolf in werewolfs:
                        werewolf_print = werewolf_print + werewolf.display_name() + ', '
                    werewolf_print = werewolf_print[:-2]
                    print ('You are now a minion. Here is a list of all werewolfs in the game: ' + werewolf_print +'.')
                    doppleganger.assign_role(other_player_role)
                    prompt_user_continue()
                    success = True
                if other_player_role == 'mason':
                    mason_print = ''
                    for mason in masons:
                        mason_print = mason_print + mason.display_name() + ', '
                    mason_print = mason_print[:-2]
                    doppleganger.assign_role(other_player_role)
                    prompt_user_continue()
                    success = True
                    print ('You are now a mason. Here is a list of all masons in the game: ' + mason_print +'.')
                if other_player_role == 'robber' or other_player_role == 'drunk' or other_player_role == 'troublemaker' or other_player_role == 'seer' or other_player_role == 'insomniac':
                    print ('You are now a ' + other_player_role + '. You will wake up again. You assume their alignment and abilites.')
                    doppleganger.assign_role(other_player_role)
                    prompt_user_continue()
                    success = True
                
    for player in player_instances:
        night_order.append(player)
    random.shuffle(night_order)
    for player in night_order:
        cls()
        if player == doppleganger:
            if player.display_role == 'doppleganger':
                continue
        input ('Player ' + game_sizes[player.display_number()] + ', aka ' + player.display_name() + ', please press Enter to recieve your role.')
        player_role = player.display_role()
        #Minion
        if player_role == 'minion':
            werewolf_print = ''
            for werewolf in werewolfs:
                werewolf_print = werewolf_print + werewolf.display_name() + ', '
            if len(werewolfs) != 0:
                werewolf_print = werewolf_print[:-2]
            else: 
                werewolf_print = 'none'
            print ('Your role is the minion. You win with werewolfs. If there are no werewolfs, you win by getting another player lynched. Here is a list of all werewolfs in the game: ' + werewolf_print +'.')
            prompt_user_continue()
        #Villager
        elif player_role == 'villager':
            print('Your role is the villager. You side with the village. You have no special abilities.')
            prompt_user_continue()
        #Insomniac
        elif player_role == 'insomniac':
            print ('Your role is the insomniac. Your role card currently is ' + player.display_end_of_night_role() + '. If it does not change, you are now that role. Insomniacs side with village.')
            prompt_user_continue()
        #Robber
        elif player_role == 'robber':
            success = False
            while success == False:
                print('You role is the robber. You can choose to assume someone elses role. They will then become the robber. Robber is a village role. If you choose not to rob, you will remain robber and will side with the village. You can not do the action of your new role.')
                number = input('Input the number of an option.\n1) Rob a player\n2) Remain the robber\n')
                if number == '1':
                    cls()
                    for other_player in reversed(player_instances):
                        if other_player != player: 
                            print('Player ' + game_sizes[other_player.display_number()] + ', aka ' + other_player.display_name() + '.')
                    number = input('Input the number of a player. (Not word form)')
                    if number.isdigit() == False:
                        print ('That player does not exist. Please try again.')
                        prompt_user_continue()
                        continue
                    if not len(player_instances) >= int(number) >= 1 or int(number) == player.display_number():
                        print ('That player does not exist or is yourself. Please try again.')
                        prompt_user_continue()
                    else:
                        index_number = int(number) - 1
                        print('Player ' + game_sizes[int(number)] + ', aka ' + reverse_player_instances[index_number].display_name() + "'s role card was " + reverse_player_instances[index_number].display_end_of_night_role() + '. This is now your role.')
                        prompt_user_continue()
                        player.assign_end_of_night_role(reverse_player_instances[index_number].display_end_of_night_role())
                        reverse_player_instances[index_number].assign_end_of_night_role('robber')
                        success = True
                elif number == '2':
                    print ('You have chosen to remain as a robber.')
                    prompt_user_continue()
                    success = True
                else:
                    print ("That input is was invalid. Please enter a valid number.\n")
                    prompt_user_continue()
        #Troublemaker
        elif player_role == 'troublemaker':
            success = False
            while success == False:
                print('You role is the troublemaker. You must switch two player roles. You side with the village.')
                for other_player in reversed(player_instances):
                    if other_player != player: 
                        print('Player ' + game_sizes[other_player.display_number()] + ', aka ' + other_player.display_name() + '.')
                number = input('Input the number of the first player. (Not word form)')
                if number.isdigit() == False:
                    print ('That player does not exist. Please try again.')
                    prompt_user_continue()
                    continue
                if not len(player_instances) >= int(number) >= 1 or int(number) == player.display_number():
                    print ('That player does not exist or is yourself. Please try again.')
                    prompt_user_continue()
                else:
                    number2 = input('Input the number of the second player. (Not word form)')
                    if number2.isdigit() == False:
                        print ('That player does not exist. Please try again.')
                        prompt_user_continue()
                        continue
                    if not len(player_instances) >= int(number2) >= 1 or int(number2) == player.display_number() or number == number2:
                        print ('That player does not exist or is yourself, or has already been chosen. Please try again.')
                        prompt_user_continue()
                    else:
                        index_number = int(number) -1
                        index_number2 = int(number2) - 1
                        reverse_player_instances[index_number].assign_end_of_night_role(reverse_player_instances[index_number2].display_end_of_night_role())
                        reverse_player_instances[index_number2].assign_end_of_night_role(reverse_player_instances[index_number].display_end_of_night_role())
                        print('You have successfully swapped the roles of ' + reverse_player_instances[index_number].display_name() + ' and ' + reverse_player_instances[index_number2].display_name() + '.')
                        prompt_user_continue()
                        success = True
        #Drunk
        elif player_role == 'drunk':
            print ('You are the drunk. A card has randomly been selected from the center. That is now your role. The drunk itself sides with the village.')
            drunk_role = random.choice(roles)
            roles.remove(drunk_role)
            roles.append('drunk')
            player.assign_end_of_night_role(drunk_role)
            prompt_user_continue()
        #Tanner
        elif player_role == 'tanner':
            print ('You are the tanner. You must get lynched during the day to win. The tanner is considered a member of the village. If the tanner is lynched and no werewolfs are lynched, werewolfs do not win.')
            prompt_user_continue()
        #Hunter
        elif player_role == 'hunter':
            print ('You are the hunter. If you are lynched, a player of your choice also dies. You side with the village.')
            prompt_user_continue()
        #Mason
        elif player_role == 'mason':
            mason_print = ''
            for mason in masons:
                mason_print = mason_print + mason.display_name() + ', '
            mason_print = mason_print[:-2]
            print ('Your role is a mason. You win if atleast one werewolf is lynched, or by lynching no one if there is no werewolf. You can see other masons. Here is a list of all masons in the game: ' + mason_print + '.')
            prompt_user_continue()
        #Werewolf
        elif player_role == 'werewolf':
            werewolf_print = ''
            for werewolf in werewolfs:
                werewolf_print = werewolf_print + werewolf.display_name() + ', '
            werewolf_print = werewolf_print[:-2]
            print ('Your role is a werewolf. You win if all werewolves survive the day. Here is a list of all werewolfs in the game: ' + werewolf_print +'.')
            prompt_user_continue()
        #Seer
        elif player_role == 'seer':
            success = False
            while success == False:
                print ("Your role is the seer. You win if atleast one werewolf is lynched, or by lynching no one if there is no werewolf. You can look at another player's role card, or two cards from the center.")
                number = input('Input the number of an option.\n1) Look At Player Card\n2) Look At Two Center Cards\n')
                if number == '1':
                    cls()
                    for other_player in reversed(player_instances):
                        if other_player != player: 
                            print('Player ' + game_sizes[other_player.display_number()] + ', aka ' + other_player.display_name() + '.')
                    number = input('Input the number of a player. (Not word form)')
                    if number.isdigit() == False:
                        print ('That player does not exist. Please try again.')
                        prompt_user_continue()
                        continue
                    if not len(player_instances) >= int(number) >= 1 or int(number) == player.display_number():
                        print ('That player does not exist or is yourself. Please try again.')
                        prompt_user_continue()
                    else:
                        index_number = int(number) - 1
                        print('Player ' + game_sizes[int(number)] + ', aka ' + reverse_player_instances[index_number].display_name() + "'s role is " + reverse_player_instances[index_number].display_end_of_night_role() + '. Note this can change through the night.')
                        prompt_user_continue()
                        success = True
                elif number == '2':
                    first_center = random.choice(roles)
                    roles.remove(first_center)
                    second_center = random.choice(roles)
                    roles.remove(second_center)
                    print('Two center role cards have been selected at random. They are ' + first_center + ' and ' + second_center + '.')
                    roles.append(first_center)
                    roles.append(second_center)
                    prompt_user_continue()
                    success = True
                else:
                    print ("That input is was invalid. Please enter a valid number.\n")
                    prompt_user_continue()
        else:
            print ('Test')
    werewolf_day(roles, player_instances, werewolfs, masons, doppleganger, reverse_player_instances)
    
#Voting and day actions
def werewolf_day(roles, player_instances, werewolfs, masons, doppleganger, reverse_player_instances):
    input('Daytime. It is discussion period. This should last around five minutes. Press Enter when everyone is ready to vote.')
    cls()
    werewolf_vote(roles, player_instances, werewolfs, masons, doppleganger, reverse_player_instances)

def werewolf_vote(roles, player_instances, werewolfs, masons, doppleganger, reverse_player_instances):
    votes = []
    original_dopple_index = doppleganger.display_number() - 1
    dopple_index = original_dopple_index
    original_doppleganger = reverse_player_instances[dopple_index]
    new_doppleganger_original_role = ''
    for player in player_instances:
        if player.display_end_of_night_role() == 'doppleganger':
            new_doppleganger_original_role = player.display_role()
            player.assign_role(doppleganger.display_role())
            doppleganger = player
            
    print('Vote time. In the case of a tie, both people die. If the tied players have 1 vote each, no one dies.')
    prompt_user_continue()
    for player in reversed(player_instances):
        success = False
        while success == False:
            
            print('Player ' + game_sizes[player.display_number()] + ', aka ' + player.display_name() + ', please vote.')
            for other_player in reversed(player_instances):
                if other_player != player: 
                    print('Player ' + game_sizes[other_player.display_number()] + ', aka ' + other_player.display_name() + '.')
            number = input('Input the number of the player you wish to vote for. (Not word form)')
            if number.isdigit() == False:
                print ('That player does not exist. Please try again.')
                prompt_user_continue()
                continue
            if not len(player_instances) >= int(number) >= 1 or int(number) == player.display_number():
                print ('That player does not exist or is yourself. Please try again.')
                prompt_user_continue()
            else:
                index_number = int(number) - 1
                print('You have successfully voted for ' + reverse_player_instances[index_number].display_name() + '.')
                prompt_user_continue()
                success = True
                reverse_player_instances[index_number].add_vote()
    
    print('The results are in. Here are the votes for each player: ')
    
    for player in player_instances:
        print('Votes for ' + player.display_name() + ': ' + str(player.votes) + '.')
        votes.append(player.votes)
        prompt_user_continue()
    
    player_roles = []
    for player in reverse_player_instances:
        player_roles.append(player.display_end_of_night_role())
    
    death_vote = max(votes)
    dopple_index = player_instances.index(doppleganger)
    if death_vote == 1:
        print('No player recieved more than one vote. No one dies.')
        if len(werewolfs) != 0 or player_instances[dopple_index].display_role() == 'werewolf':
            print('No werewolf was lynched. Werewolfs win.')
        else:
            print('There were no werewolfs. Villagers win.')
    else:
        for player in player_instances:
            if player.votes == death_vote:
                if player.display_end_of_night_role() == 'hunter':
                    success = False
                    while success == False:
                        print (player.display_name() + ' was a hunter. They can now choose a player to shoot...')
                        prompt_user_continue()
                        cls()
                        for other_player in reversed(player_instances):
                            if other_player != player and other_player.votes != death_vote: 
                                print('Player ' + game_sizes[other_player.display_number()] + ', aka ' + other_player.display_name() + '.')
                        number = input('Input the number of a player to shoot. (Not word form)')
                        index_number = int(number) - 1
                        if number.isdigit() == False:
                            print ('That player does not exist. Please try again.')
                            prompt_user_continue()
                            continue
                        if not len(player_instances) >= int(number) >= 1 or int(number) == player.display_number() or reverse_player_instances(index_number).votes == death_vote:
                            print ('That player does not exist, is already set to die, or is yourself. Please try again.')
                            prompt_user_continue()
                        else:
                            print('Player ' + game_sizes[int(number)] + ', aka ' + reverse_player_instances[index_number].display_name() + ' was successfully shot.')
                            reverse_player_instances[index_number].votes = death_vote
                            prompt_user_continue()
                            success = True
                            
        for player in player_instances:
            if player.votes == death_vote:
                if player.display_end_of_night_role() == 'werewolf' or player_instances[dopple_index].display_role() == 'werewolf':
                    print (player.display_name() + ' was a werewolf. The villagers win.')
                elif player.display_end_of_night_role() == 'tanner' or player_instances[dopple_index].display_role() == 'tanner':
                    print (player.display_name() + ' was a tanner. Tanner wins.')
        
        for player in player_instances:
            if player.votes == death_vote:
                if player.display_end_of_night_role() == 'minion' or  player_instances[dopple_index].display_role() == 'minion':
                    print(player.display_name() + ' was a minion. If no werewolfs died, minion and werewolfs win.')
                elif player.display_end_of_night_role() != 'werewolf' or player_instances[dopple_index].display_role() == 'werewolf':
                    print (player.display_name() + ' was a ' + player.display_end_of_night_role() + '. If there is a minion and no players are werewolfs, minion wins. One werewolf must be killed for village to win if there are werewolfs.')
    
    prompt_user_continue()
    original_doppleganger.assign_role('doppleganger')
    if new_doppleganger_original_role != '':
        doppleganger.assign_role(new_doppleganger_original_role)
        
    for player in reversed(player_instances):
        print('Player ' + game_sizes[player.display_number()] + ', aka ' + player.display_name() + ' started the night as a ' + player.display_role() + '.')
    print('')
    for player in reversed(player_instances):
        print('Player ' + game_sizes[player.display_number()] + ', aka ' + player.display_name() + ' ended the night as a ' + player.display_end_of_night_role() + '.')
    prompt_user_continue()