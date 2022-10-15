import random

NFL = ["ARI", "ATL", "BAL", "BUF", "CAR", "CHI", "CIN", "CLE", "DAL", "DEN", "DET",
       "GB", "HOU", "IND", "JAX", "KC", "MIA", "MIN", "NE", "NO", "NYG", "NYJ", "LV",
       "PHI", "PIT", "LAC", "SF", "SEA", "LAR", "TB", "TEN", "WAS"]

NBA = ['ATL', 'BOS', 'BKN', 'CHA', 'CHI', 'CLE', 'DET', 'GS', 'IND', 'LAL', 'MIA', 'NO', 'NY', 'OKC', 'ORL', 'PHX',
       'POR', 'SAC', 'SA', 'TOR', 'UTAH', 'WSH', 'DAL', 'DEN', 'HOU', 'LAC', 'MEM', 'MIL', 'MIN', 'PHI']

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

        if team_choice in NFL:

            quarter = random.randint(1, 5)
            opponent = NFL[random.randint(0, 31)]
            team_score = random.randint(2, 70)
            opp_score = random.randint(2, 70)
            winner = ""

            if team_score > opp_score:
                winner = team_choice
            if opp_score > team_score:
                winner = opponent
            while opponent == team_choice:
                opponent = NFL[random.randint(0, 31)]

            print(team_choice + ": " + str(team_score))
            print(opponent + ": " + str(opp_score))

            if quarter in [1, 2, 3, 4]:
                print("Quarter: " + str(quarter))
                print(winner + " is winning!")
            if quarter > 4:
                print("Final")
                print(winner + " won!")

            what_next = input("\nEnter 1 EXIT or any key to restart:\n")
            if what_next == "1":
                break





