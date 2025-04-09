# main file

# libraries
import pandas as pd

# import files
from GameFiles.league_creation import LeagueGeneration

# generate league (players, teams)
generation = LeagueGeneration(12, 15)


data = generation.create_league()
print(data)