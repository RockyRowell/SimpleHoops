# This file is called upon to generate a whole league

# libraries
import pandas as pd
import pandas as pd
from pathlib import Path

# import files
from Generation.team_generation import TeamGeneration
from Generation.player_generation import PlayerGeneration
from Generation.physicals_generation import PhysicalsGeneration
from Generation.offense_generation import OffenseGeneration
from Generation.defense_generation import DefenseGeneration


class LeagueGeneration:
    def __init__(self, player_amount, team_amount):
        self.player_amount = player_amount
        self.team_amount = team_amount
        
    # Min function to create league
    def create_league(self):
        # create list of teams
        team_gen = TeamGeneration(self.team_amount)
        team_list = team_gen.team_generation()
        
        # create player list
        player_gen = PlayerGeneration(self.player_amount, self.team_amount)
        player_list = player_gen.player_generation()
        

        # create df for future for loop
        physicals_df = pd.DataFrame(columns=['Player', 'Height', 'Weight'])
        offense_df = pd.DataFrame(columns=['Player', 'Three Point', 'Mid Range', 'Free Throw', 'Post Scoring'])
        defense_df = pd.DataFrame(columns=['Player', 'Perimeter Defense', 'Post Defense', 'Defensive Rebounding', 'Offensive Rebounding', 'Steal', 'Block'])


        # for loop for each player generation
        for index, name in player_list.iterrows():
            # gather player name
            player = name['Full Name']
            
            
            ## physicals generation
            # generate values
            physicals_gen = PhysicalsGeneration(player)
            new_physicals = physicals_gen.physical_generation()
            
            # add to existing df
            physicals_df = pd.concat([physicals_df, new_physicals], ignore_index=True)
            
            # extract physical values for other 
            physicals = physicals_gen.get_attributes()
            
            
            ## offense generation
            # generate values
            offense_gen = OffenseGeneration(player, physicals)
            new_offense = offense_gen.offense_generation()
            
            # add to existing df
            offense_df = pd.concat([offense_df, new_offense], ignore_index=True)
            
            
            ## defense generation
            # generate values
            defense_gen = DefenseGeneration(player, physicals)
            new_defense = defense_gen.defense_generation()
            
            # add to existing df
            defense_df = pd.concat([defense_df, new_defense], ignore_index=True)
        
        
        # Create Main Dataset
        # combine physicals, offense, and defense dataframes while dropping player column from offense and defense
        combined_df = physicals_df.merge(offense_df, on="Player").merge(defense_df, on="Player")
            
            
        # create overall rating
        combined_df['Overall'] = combined_df.iloc[:, 5:19].mean(axis=1)
        
        # round overall rating to 2 decimal places
        combined_df['Overall'] = pd.to_numeric(combined_df['Overall'], errors='coerce')
        combined_df['Overall'] = combined_df['Overall'].round(2)

        # sort by overall rating
        combined_df = combined_df.sort_values(by='Overall', ascending=False)
        
        
        # Draft players to teams in snake order  THIS WILL NEED TO CHANGE LATER!!!
        team_names = team_list['Team Name'].tolist()
        num_teams = len(team_names)
        team_assignments = []
        
        # variable for forward (snake order) and team index
        forward = True
        team_index = 0
        
        # loop through combined_df and assign teams
        for i in range(len(combined_df)):
            team_assignments.append(team_names[team_index])
            
            if forward:
                team_index += 1
                if team_index == num_teams:
                    team_index -= 1
                    forward = False
            else:
                team_index -= 1
                if team_index == -1:
                    team_index += 1
                    forward = True
        
        # add team assignments to main dataset
        combined_df['Team'] = team_assignments
        
        
        # save data to a csv file
        file_path = Path(r'Code\Data\GeneratedData\league_players.csv')
        combined_df.to_csv(file_path, index=False)
        
        
        # save data to a json file
        file_path = Path(r'Code\Data\GeneratedData\rosters.json')
        
        # hierarchy by team
        league_data = {}
        for team in team_names:
            league_data[team] = combined_df[combined_df['Team'] == team].to_dict(orient='records')
        # save to json file
        with open(file_path, 'w') as file:
            import json
            json.dump(league_data, file, indent=4)
        
        
        
        