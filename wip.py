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

print(tl[['Sport','Team'][0]])

