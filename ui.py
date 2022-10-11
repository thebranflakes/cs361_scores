import random

NFL = ["ARI", "ATL", "BAL", "BUF", "CAR", "CHI", "CIN", "CLE", "DAL", "DEN", "DET",
       "GB", "HOU", "IND", "JAX", "KC", "MIA", "MIN", "NE", "NO", "NYG", "NYJ", "LV",
       "PHI", "PIT", "LAC", "SF", "SEA", "LAR", "TB", "TEN", "WAS"]


while True:
    team_choice = ""
    league_input = input("Enter 1 for NBA scores or 2 for NFL scores:\n")

    while league_input not in ["1", "2"]:
        print("That is not a correct input, try again.\n")
        league_input = input("Enter 1 for NBA scores or 2 for NFL scores:\n")

    if league_input == "1":
        print("NBA it is!\n")
        team_choice = input("Which teams score did you want to check?\n")

    if league_input == "2":
        print("NFL it is!\n")
        team_choice = input("Which teams score did you want to check?\n")

    while team_choice not in NFL:
        team_choice = input("That isn't a team option, try again. Enter 1 for the list of teams or 2 to restart:\n")
        if team_choice == "1":
            print(NFL)
            team_choice = input("Which teams score did you want to check?:\n")
        if team_choice == "2":
            break







