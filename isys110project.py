# The main module I will use to read and manipulate csv data
import pandas as pd
# I am using time to add delay to the display because otherwise there could be too many lines of information all at once.
# I will use time.sleep(1) throughout the project. It is just meant to slow down the display speed for readability.
# This should make it easier for the user (it helps me for sure!)
import time

# +++++++++++++++++++++++++++++++++++++++++++++++++
# Display the team list
# +++++++++++++++++++++++++++++++++++++++++++++++++

def teams():

    # Reading the players file
    players = pd.read_csv('players.csv')

    # Reading the team list file
    team_list = pd.read_csv('team_list.csv')

    # using sort_values from pandas to sort the dataframe. by = 'TEAM' designates that we are sorting alphabetically by the TEAM column values
    tl = team_list.sort_values(by ='TEAM')

    # Displays the sorted dataframe sport and team name columns, there is also data to add championships and city, but those aren't required to be displayed.
    print(tl[['SPORT','TEAM']])

# +++++++++++++++++++++++++++++++++++++++++++++++++
# Display the players on a specific team
# +++++++++++++++++++++++++++++++++++++++++++++++++

# hof is short for Hall of Fame, because this shows the selected team's all time starting 5.
def hof():

    # Reading the players file
    players = pd.read_csv('players.csv')

    # Sorting the players list by team, doing this groups players on like teams together which is important for a future step.
    players = players.sort_values(by = 'TEAM')

    # Reading the list of teams
    team_list = pd.read_csv('team_list.csv')
    
    # Sorting by team again
    tl = team_list.sort_values(by = 'TEAM')

    # This just displays the team names for the user to select from
    print(tl[['TEAM']])

    # Storing user input in a variable
    selection = input("Please type a team to see their All-Time starting 5:\n")

    
    

    # This line is modified a snippet from https://www.slingacademy.com/article/pandas-dataframe-get-indexes-of-rows-where-column-meets-certain-condition/
    # original: index_over_30 = df.index[df['Age'] > 30].tolist()

    # What this line is doing is finding the range of indices that contain the desired team. .tolist() puts those values in a list.
    roster = players.index[players['TEAM'] == selection].tolist()

    # The Pandas documentation describes .loc as something to "Access group of values using labels." 
    # The list of desired indicies are the labels the program uses
    # .loc finds each row in associated with the index values in the list and returns them, showing an array of desired players
    print(players.loc[roster])


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Add a new player to a team
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def add():
    
    # Reading the csv's as described earlier
    players = pd.read_csv('players.csv')
    team_list = pd.read_csv('team_list.csv')

    # I am going to collect information for columns Name and Team as part of the program. This stores the labels of the remaining columns for future use
    player_columns = ['POSITION', 'HEIGHT', 'PPG']
    
    # Making user pick a Team
    # using a while loop so the user can try again if they enter an invalid input
    while True:

        # Displaying the teams for the user to choose from
        print(team_list[['TEAM']])
        
        # Asking for user input and converting it to all caps
        user_team = input("Please select a team to add a player to:\n").upper()
        
        # .values checks the actual data in the column team
        # if the user input isn't in the column the they are prompted to try again
        if user_team not in team_list['TEAM'].values:
            print("Please enter a valid team...\n\n\n~~~~~~~~~~~~~~")
            time.sleep(1)
        # if the input is valid, the program moves on to the next step.
        else:
            print(f"\n{user_team} selected\n")
            time.sleep(1)
            break

    # Making the user enter a player, they can try again if the player already exists
    while True:

        # Collecting the input and capitalizing it
        player_name = input("Please enter player your player's name:\n").upper()

        # If the player the user entered is already in the dataframe, then the user is prompted to try again
        if player_name in players['NAME'].values:
            print("That player already exists, please enter a new player:\n")
            time.sleep(1)
        # If the user enters a valid input, the program goes to the next step.
        else:
            break
    
    # Taking the two previous valid inputs and entering them in a dictionary for the first part of our new row
    player_entry = {"NAME": player_name,
                    'TEAM': user_team
                    }

    # Creating an empty dictionary to fill in the remaining data we need on the player
    player_data = {}

    # This assigns the values from the player_columns list as dictionary keys, and has the user input the corresponding value one-by-one.
    for i in player_columns:

        # i is the key value we took from the player columns list. The user will know what they need to enter for each category
        user_entry = input(f"Please enter {i}: ").upper()

        # Actually adding the user input to the previously empty player_data dictionary
        player_data[i] = user_entry
    
    # This combines our two dictionaries, player_entry and player_data by adding player data to the end of player entry.
    # The data is now ordered in a way that is compatible with our csv, just not formatted
    player_entry.update(player_data)
    
    # Converts our dictionary into a dataframe so it can be used to update the csv.
    player_entry = pd.DataFrame([player_entry])
    
    # This combines the previously extracted full player datafram and the new player dataframe.
    updated = pd.concat([players, player_entry], ignore_index=True)

    # The previous step added the new player to the end, not in order by team. Running a sort again to make the dataframe organized
    updated = updated.sort_values(by = 'TEAM')

    # uploading the new dataframe with player added and sorted to the original CSV. Index = False stops pandas from adding another index column.
    updated.to_csv('players.csv', index=False)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++
# Remove a Player
# +++++++++++++++++++++++++++++++++++++++++++++++++++++


def remove():

    # Reading my csv's
    players = pd.read_csv('players.csv')

    team_list = pd.read_csv('team_list.csv')


    # This displays the team, lets the user select a team, it is nearly identical to what was used in add(), just a change to the text being displayed.
    while True:
        print(team_list[['TEAM']])
        user_team = input("Please select a team to remove a player from:\n").upper()
        if user_team not in team_list['TEAM'].values:
            print("\n\nPlease select a valid team...\n")
            time.sleep(1)
        else:
            print(f"\n{user_team} selected\n")
            time.sleep(1)
            break
    # Sorts the players by their career points per game for their team
    players = players.sort_values(by = 'PPG')

    # This was used earlier to find the index for the desired players and return it as a list
    roster = players.index[players['TEAM'] == user_team].tolist()

    # Asking the user who to cut, while loop for multiple tries if input is invalid
    while True:
        
        # Displays all the players on a given team using the index list, roster.
        print(players.loc[roster])

        # Asking the user who to cut
        delete = input("Please enter the player you would like to move:\n").upper()

        # Checks that the player the user inputed is actually on the list.
        if delete not in players['NAME'].values:
            print("Please eneter a valid player...")
            time.sleep(1)
        else:
            # Player is not removed successfully at this point, that happens on the next step. 
            # This just shows the player is eligible to be deleted, and they will be soon
            print(f"{delete} removed successfully!\n\n\n\n")
            break

    
    # This will delete the specified player, it could delete all instances of the player too, but that isn't relevant here.
    player_location = players.index[players['NAME'] == delete].tolist()

    # .drop removes whatever data the parameters call for
    # index=player_location looks for all index values in the list from out previous operation. There will only be one value in the list.
    # inplace=True means we are changing the players dataframe, not copying it.
    players.drop(index=player_location, inplace=True)

    # updating the players csv with the new dataframe that has a player removed
    players.to_csv('players.csv', index=False)

    # reading the csv directly now that its updated
    updated_csv = pd.read_csv('players.csv')
    
    # Only reading the players from the selected team to show player has been removed from the csv
    roster = updated_csv.index[players['TEAM'] == user_team].tolist()
    print(players.loc[roster])


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Menu Function
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++

def main_menu(): 
    # This lets the user choose one of the designated menu values
    while True:
        # The program will compare user input with this menu list to decide what to do
        menu = ['SHOW TEAMS', 'SHOW ROSTER', 'ADD A PLAYER', 'REMOVE A PLAYER', 'QUIT']

        # Welcome Message giving the user instructions
        print("\nWelcome to the All-Time Team Catalog!\n\n\n~~~ Main Menu ~~~\nSHOW TEAMS\nSHOW ROSTER\nADD A PLAYER\nREMOVE A PLAYER\n~~~~~~~~~~~~~~~~~~")
        
        # Collecting User input
        answer = input("Please enter a menu option, or type 'Quit' to quit the program:\n").upper()

        # Checking if the input is valid
        if answer not in menu:
            print("\n\nPlease type a valid option...")
        else:
            #returns the user input which will be used in the actual program
            return answer

# The decision tree
# Uses while True so the program can be used until the user is done
while True:
    time.sleep(1)

    # Calls the main menu function to get one of the values from the menu list
    selection = main_menu()
    time.sleep(1)
    # Checking what the user selected and executing the appropiate function
    # Quit breaks the menu loop and ends the program
    if selection == 'QUIT':
        break
    
    # If the user enters SHOW TEAMS, they will see the teams() function that outputs all teams
    elif selection == 'SHOW TEAMS':
        teams()
    
    # SHOW ROSTER triggers the hof() function
    elif selection == "SHOW ROSTER":
        hof()

    # ADD A PLAYER triggers the add() function
    elif selection == 'ADD A PLAYER':
        add()

    # REMOVE a player triggers the remove function
    elif selection == 'REMOVE A PLAYER':
        remove()

    # The main_menu() function makes it impossible to get here, but I wanted to finish with an else statement. 
    # If they find a way the program quits
    else:
        print("You're not supposed to be here!?")
        break
# Quitting the program
quit 





