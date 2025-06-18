# create league schedule

# libraries
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta



class ScheduleGeneration:
    def __init__(self, teams, games):
        self.teams = teams
        self.games = games

        self.start = datetime.strptime('2025-10-15', "%Y-%m-%d")
        self.end = datetime.strptime('2026-04-15', "%Y-%m-%d")
        
        self.total_games = self.games * len(self.teams) // 2
        self.season_length = (self.end - self.start).days
        
    def generate_schedule(self):
        # Initialize schedule list and tracking dictionaries
        schedule = []
        team_games = {team: 0 for team in self.teams}
        home_games = {team: 0 for team in self.teams}
        away_games = {team: 0 for team in self.teams}
        
        # Calculate target number of home/away games per team
        target_home_away = self.games // 2
        
        # Get available dates
        available_dates = []
        current_date = self.start
        while current_date <= self.end:
            available_dates.append(current_date)
            current_date += timedelta(days=1)
        random.shuffle(available_dates)
        
        # Generate schedule
        for game_date in available_dates:
            teams_used_today = set()
            
            while True:
                # Get available teams that haven't played today
                available_teams = [team for team in self.teams 
                                if team_games[team] < self.games 
                                and team not in teams_used_today]
                
                if len(available_teams) < 2:
                    break
                    
                # Find valid home team (needs home game)
                possible_home = [team for team in available_teams 
                            if home_games[team] < target_home_away]
                if not possible_home:
                    break
                home = random.choice(possible_home)
                available_teams.remove(home)
                
                # Find valid away team (needs away game)
                possible_away = [team for team in available_teams 
                            if away_games[team] < target_home_away]
                if not possible_away:
                    break
                away = random.choice(possible_away)
                
                # Add game to schedule
                schedule.append([game_date.strftime("%Y-%m-%d"), home, away])
                
                # Update tracking
                team_games[home] += 1
                team_games[away] += 1
                home_games[home] += 1
                away_games[away] += 1
                teams_used_today.add(home)
                teams_used_today.add(away)
                
                # Check if schedule is complete
                if all(games >= self.games for games in team_games.values()):
                    break
                    
            if all(games >= self.games for games in team_games.values()):
                break
        
        # Convert to DataFrame and sort by date
        schedule_df = pd.DataFrame(schedule, columns=["Date", "Home Team", "Away Team"])
        schedule_df = schedule_df.sort_values("Date")
        
        # Verify schedule balance
        for team in self.teams:
            home_count = len(schedule_df[schedule_df["Home Team"] == team])
            away_count = len(schedule_df[schedule_df["Away Team"] == team])
            total_games = home_count + away_count
            if total_games != self.games:
                print(f"Warning: {team} has {total_games} total games instead of {self.games}")
            if home_count != away_count:
                print(f"Warning: {team} has {home_count} home games and {away_count} away games")
        
        return schedule_df
    