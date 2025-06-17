# main file

# libraries
import pandas as pd

# import files
from Generation.league_creation import LeagueGeneration

# generate league (players, teams)
generation = LeagueGeneration(12, 15)
generation.create_league()

#data = generation.create_league()
#print(data)