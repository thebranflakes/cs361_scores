import random
import time

NFL = ["ARI", "ATL", "BAL", "BUF", "CAR", "CHI", "CIN", "CLE", "DAL", "DEN", "DET",
       "GB", "HOU", "IND", "JAX", "KC", "MIA", "MIN", "NE", "NO", "NYG", "NYJ", "LV",
       "PHI", "PIT", "LAC", "SF", "SEA", "LAR", "TB", "TEN", "WAS"]

NBA = ['ATL', 'BOS', 'BKN', 'CHA', 'CHI', 'CLE', 'DET', 'GS', 'IND', 'LAL', 'MIA',
       'NO', 'NY', 'OKC', 'ORL', 'PHX', 'POR', 'SAC', 'SA', 'TOR', 'UTAH', 'WSH',
       'DAL', 'DEN', 'HOU', 'LAC', 'MEM', 'MIL', 'MIN', 'PHI']

while True:

    team_choice = ""
    league_input = input("Enter 1 for NBA scores or 2 for NFL scores (You will need to pick a team)\n"
                         "(New Feature) Get a score fast! Random NBA or NFL score, just enter 3!\n")

    while league_input not in ["1", "2", "3"]:
        print("That is not a correct input, try again.\n")
        league_input = input("Enter 1 for NBA scores or 2 for NFL scores:\n"
                             "or 3 for random score.\n")

    if league_input == "1":
        print("NBA it is!\n")
        team_choice = input("Which teams score did you want to check?\n"
                            "OR\n"
                            "Press 1 for List of teams\n"
                            "Press 2 to restart\n")

        while team_choice not in NBA:
            if team_choice == "1":
                print(NBA)
                team_choice = input("Which teams score did you want to check?:\n")
            if team_choice == "2":
                break

        if team_choice in NBA:

            quarter = random.randint(1, 5)
            opponent = NBA[random.randint(0, 29)]
            team_score = random.randint(2, 70)
            opp_score = random.randint(2, 70)
            winner = ""

            if team_score > opp_score:
                winner = team_choice
            if opp_score > team_score:
                winner = opponent
            while opponent == team_choice:
                opponent = NBA[random.randint(0, 29)]

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

    if league_input == "2":
        print("NFL it is!\n")
        team_choice = input("Which teams score did you want to check? (Enter team abbreviation)\n"
                            "OR\n"
                            "Press 1 for List of teams\n"
                            "Press 2 to restart\n")

        while team_choice not in NFL:
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

    if league_input == "3":
        # Open file for writing
        microservice = open("micro.txt", "w")
        time.sleep(1)
        print("Receiving Data from Microservice...\n")

        # Write micro into txt file
        microservice.write("micro")
        time.sleep(3)
        microservice.close()

        # Open file for reading
        microservice = open("micro.txt", "r")
        time.sleep(3)
        micro_num = microservice.read()
        microservice.close()

        print("Data Received, Generating Score...\n")

        # print out the number recieved
        print(micro_num)
        
        what_next = input("\nEnter 1 to EXIT or any other key to restart:\n")
        if what_next == "1":
            break
