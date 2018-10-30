#If you want to run the program, go to RUN ME

######
# This file contains the player class.
######

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

class Player:
    
    def __init__(self, player_name, player_number):
        self.player_name = player_name
        self.player_number = player_number
        self.new_role = ''
        self.votes = 0
        
    def assign_role(self, role_name):
        self.role = role_name
        
    def assign_end_of_night_role(self, new_role_name):
        self.new_role = new_role_name
    
    def add_vote(self):
        self.votes = self.votes + 1
        
    def display_end_of_night_role(self):
        return self.new_role
        
    def display_role(self):
        return self.role
        
    def display_name(self):
        return self.player_name
        
    def display_number(self):
        return self.player_number