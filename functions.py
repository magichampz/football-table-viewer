import pandas as pd
import numpy as np
import csv

# data is obtained from https://www.football-data.co.uk/englandm.php
# code will have to be adjusted for any other csv's obtained of 
# different formats from different websites

file = open("game-stats-2021-2022.csv","r")
data = list(csv.reader(file, delimiter=","))

match_df = pd.read_csv("game-stats-2021-2022.csv") # change to target season
match_df.head()

teams = match_df.HomeTeam.unique() # get league teams
table_stats = ['PTS','GS','GC','STREAK','FORM','GSA','GCA'] # column headers for our table
   

def check_form(streak): 
    '''
    to view the recent form of the team. form is calculated by the 
    percentage of wins from the team's last 5 games
    Args:
        streak (list): teams list of results in a list. Each item 
        in the array is either 0,1,2 corresponding to a Win, Draw or Loss
        
    Returns:
        table (dict): the prem table in a dict, no sorting
        league_table (DataFrame): the prem table as a Pandas DataFrame, sorted by points
    '''
    if len(streak)<5: 
        form = (streak.count(0)/len(streak))*100
    else:
        last_5 = streak[-5:]
        form = (last_5.count(0)/len(last_5))*100
        
    return form



def get_league_table(weeks=38):
    ''' function to view the league table after a certain number of weeks in the season. 
    Args:
        weeks (int) : number of weeks to show the table after. defaults to 38 to show the end of the season
    '''
    
    table = {}
    for team in teams:
        table[team] = [0,0,0,[],0,0,0]    

    for game in data[2:(weeks*10+2)]:
            
        home = game[3]
        away = game[4]
        
        # add points and winstreak, 0 is W, 1 is D, 2 is L
        if game[5]>game[6]:
            table[home][0] += 3
            table[home][3].append(0)
            table[away][3].append(2)
        elif game[5]<game[6]:
            table[away][0]+= 3
            table[home][3].append(2)
            table[away][3].append(0)
        else:
            table[home][0] += 1
            table[away][0] += 1
            table[home][3].append(1)
            table[away][3].append(1)
            
        # add goals scored and conceded
        table[home][1] += int(game[5])
        table[home][2] += int(game[6])
        table[away][1] += int(game[6])
        table[away][2] += int(game[5])
            
        # calculate form
        table[home][4] = check_form(table[home][3])
        table[away][4] = check_form(table[away][3])
        
        # calculate average goals
        table[home][5] = table[home][1]/len(table[home][3])
        table[home][6] = table[home][2]/len(table[home][3])
        table[away][5] = table[away][1]/len(table[away][3])
        table[away][6] = table[away][2]/len(table[away][3])

    
    
    league_table = pd.DataFrame.from_dict(table, orient='index', columns= table_stats)
    league_table = league_table.drop('STREAK',axis =1)
    league_table = league_table.sort_values(by=['PTS'], ascending= False)
    
    return table, league_table

    
def view_next_matches(weeks=0):
    '''
    To view the matches from a certain week onwards, may be used for training a match predictor algorithm
    make a nested list, and each child list represents a match and all the relevant data
    
    
    Args:
        weeks (int): view all matches from the week specified onwards
    
    Returns:
        all_matches (list): nested list containing details of every match in its own list
        data in child list- home team, away team, home points, away points, home GSA, home GCA, away GSA, away GCA, home form, away form, result
    '''
    all_matches = []
    # weeks = 5 

    for week in range(weeks,39):
        for match in data[(2+week*10):(2+(week+1)*10)]:
            l = []
            l.append(match[3])
            l.append(match[4])
            current_table, current_table_df = get_league_table(week)
            l.append(current_table[match[3]][0])
            l.append(current_table[match[4]][0])
            l.append(current_table[match[3]][5])
            l.append(current_table[match[3]][6])
            l.append(current_table[match[4]][5])
            l.append(current_table[match[4]][6])
            l.append(current_table[match[3]][4])
            l.append(current_table[match[4]][4])
            l.append(match[7])
            all_matches.append(l)
            
    return all_matches

    





