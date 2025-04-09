# create teams

# libraries
import pandas as pd
import random
import json



class TeamGeneration:
    def __init__(self, team_amount):
        self.team_amount = team_amount
        
    
    def team_generation(self):
        # pull the file of team names
        with open('C:\\Users\\rocky\\OneDrive\\Desktop\\SimpleHoops\\Code\\NameLists\\team_city.json', 'r') as file:
            file = json.load(file)
        
        # extract lists
        city_names = file['cityNames']
        team_names = file['teamNames']
        
        
        # create DataFrame for teams
        teams = pd.DataFrame(columns=['Team Name'])
        
        # loop through given amount and assign team names
        for i in range(self.team_amount):
            # generate random city and team name and remove them
            city = random.choice(city_names)
            city_names.remove(city)
            
            name = random.choice(team_names)
            team_names.remove(name)
            
            # combine city and team name
            full_name = f"{city} {name}"
            
            # add to teams DataFrame
            new_data = pd.DataFrame([{'Team Name': full_name}])
            teams = pd.concat([teams, new_data], ignore_index=True)
            
        # return teams DataFrame
        return teams