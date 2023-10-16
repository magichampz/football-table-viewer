# football-table-viewer

Made some functions to analyse football match and table statistics overtime. The idea was to allow us to reproduce the league table from previous seasons at different points during the season, and use this table to train a match score predictor model and test its accuracy using the actual results. 

There were no other websites or services online that seemed to allow us to view the table at a random point in time in a past season, hence these functions were created.

The jupyter notebook uploaded uses data from the 2021-2022 premier league season, obtained https://www.football-data.co.uk/englandm.php. The functions can easil  be modified to work for other seasons and leagues.



### Function 1: get_league_table(weeks)
returns the league table after a specified number of weeks <br>
output dataframes shown below for weeks 35 to 38, where man city overtook liverpool <br>
<img width="425" alt="Screenshot 2023-10-16 at 11 37 34 PM" src="https://github.com/magichampz/football-table-viewer/assets/91732309/88491737-abe6-4b92-9791-56a3c9869371">
<img width="428" alt="Screenshot 2023-10-16 at 11 37 26 PM" src="https://github.com/magichampz/football-table-viewer/assets/91732309/35c7740c-70b9-45aa-ba4a-6b3023d410ce">

### Function 2: view_next_matches(weeks)
designed to help you create and test your own betting algorithm. For example, you can train a model over the first 20 weeks of the season, and then get it to make a prediction on the 21st week of the season given the statistics procided about each team until the week specified, and validate that against the actual result shown. Example of matches after week 5 shown below

<img width="971" alt="Screenshot 2023-10-16 at 11 52 51 PM" src="https://github.com/magichampz/football-table-viewer/assets/91732309/81ea87b1-bb0c-4ba6-9808-01c662bf07f7">



### Function 3: check_form(streak)
Calculates the form of each team given their overall match results to that point (streak). <br>
Form calculated as the percentage of wins over the last 5 matches
