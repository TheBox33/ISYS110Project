import numpy as np
import pandas as pd
import string

# ++++++++++++++++++++++++++++++++++++++++++++++++++
# 
# ++++++++++++++++++++++++++++++++++++++++++++++++++
players =pd.read_csv('players.csv')

team_list = pd.read_csv('team_list.csv')


# +++++++++++++++++++++++++++++++++++++++++++++++++
# Display the team list
# +++++++++++++++++++++++++++++++++++++++++++++++++
tl = team_list.sort_values(by ='Team')

# Displays the sport and team name, sorted by team name
print(tl[['Sport','Team'][0:5]])

# +++++++++++++++++++++++++++++++++++++++++++++++++
# Display the players on a specific team
# +++++++++++++++++++++++++++++++++++++++++++++++++

# Uses the previous print function
selection = input("Please type a team to see their All-Time starting 5: ")

I think to display the players on the team I check to see if the index value contains the team name. I think that should work, just have to figure out the syntax.