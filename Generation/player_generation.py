# create players

# libraries
import pandas as pd
import random
import json


class PlayerGeneration:
    def __init__(self, player_amount, team_amount):
        self.player_amount = player_amount
        self.team_amount = team_amount
        
    
    def player_generation(self):
        # pull the file of player names
        with open(r'Code\Data\NameLists\player_names.json', 'r') as file:
            file = json.load(file)
        
        # extract lists
        first_names = file['firstNames']
        last_names = file['lastNames']
        
        
        # create DataFrame for teams
        players = pd.DataFrame(columns=['First Name', 'Last Name', 'Full Name'])
        
        # loop through given amount and assign team names
        total_names = self.team_amount * self.player_amount
        
        for i in range(total_names):
            # generate random first and last name and remove them
            first = random.choice(first_names)
            first_names.remove(first)
            
            last = random.choice(last_names)
            last_names.remove(last)
            
            # combine names
            full = str(first) + ' ' + str(last)
            
            # add to teams DataFrame
            new_data = pd.DataFrame([{'First Name': first, 'Last Name': last, 'Full Name': full}])
            players = pd.concat([players, new_data], ignore_index=True)
            
        # return teams DataFrame
        return players
    
    