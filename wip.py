import numpy as np
import pandas as pd
import string

# ++++++++++++++++++++++++++++++++++++++++++++++++++
# 
# ++++++++++++++++++++++++++++++++++++++++++++++++++
players = pd.read_csv('players.csv')

team_list = pd.read_csv('team_list.csv')


# +++++++++++++++++++++++++++++++++++++++++++++++++
# Display the team list
# +++++++++++++++++++++++++++++++++++++++++++++++++

def teams():
    tl = team_list.sort_values(by ='Team')

    # Displays the sport and team name, sorted by team name
    print(tl[['Sport','Team'][0:5]])

# +++++++++++++++++++++++++++++++++++++++++++++++++
# Display the players on a specific team
# +++++++++++++++++++++++++++++++++++++++++++++++++

# Display the team list file.
# The user chooses a team. 
# Read the players file.
# Display only the list of players for that team, sorted by the player name, position or other property.

# Prints the selected team's all time starting 5. Their Hall of Fame (hof).

def hof():
    players = pd.read_csv('players.csv')
    team_list = pd.read_csv('team_list.csv')

    print(team_list)
    selection = input("Please type a team to see their All-Time starting 5: ")

    # This line was taken from https://www.slingacademy.com/article/pandas-dataframe-get-indexes-of-rows-where-column-meets-certain-condition/
        
    players = players.sort_values(by = 'PPG')
    roster = players.index[players['Team'] == selection].tolist()

    print(players.loc[roster])


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Add a new player to a team
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def add():
    write_players = pd.read_csv('players.csv')
    player_columns = ['NAME', 'TEAM', 'POSITION', 'HEIGHT', 'PPG']
    # User inputs a string

    print("Please Enter player data in the following format:\n" \
    "Name (First Last), Team, Position (PG,SG,SF,PF,C), Height (foot-inches), Points Per Game (XX.X):\n")
    player_entry = {}
    for i in player_columns:
        user_entry = input(f"Please enter {i}: ").upper()
        player_entry[i] = user_entry
    
    player_entry = pd.DataFrame([player_entry])
    
    updated = pd.concat([write_players, player_entry], ignore_index =True)

    updated.to_csv('players_test.csv', index=False)

add()





