import random
import time

NFL = ["ARI", "ATL", "BAL", "BUF", "CAR", "CHI", "CIN", "CLE", "DAL", "DEN", "DET",
       "GB", "HOU", "IND", "JAX", "KC", "MIA", "MIN", "NE", "NO", "NYG", "NYJ", "LV",
       "PHI", "PIT", "LAC", "SF", "SEA", "LAR", "TB", "TEN", "WAS"]

NBA = ['ATL', 'BOS', 'BKN', 'CHA', 'CHI', 'CLE', 'DET', 'GS', 'IND', 'LAL', 'MIA',
       'NO', 'NY', 'OKC', 'ORL', 'PHX', 'POR', 'SAC', 'SA', 'TOR', 'UTAH', 'WSH',
       'DAL', 'DEN', 'HOU', 'LAC', 'MEM', 'MIL', 'MIN', 'PHI']


def prog_exit():
    exit()


def league_choice():
    while True:
        league = input("Enter 1 for NBA scores or 2 for NFL scores (You will need to pick a team)\n"
                       "(New Feature) Get a score fast! Random NBA or NFL score, just enter 3!\n")
        if league not in ["1", "2", "3"]:
            print("That is not a correct input, try again.\n")
        if league in ["1", "2", "3"]:
            return league


def team_choice(league):
    while True:
        team = input("Which teams score did you want to check? (City abbreviation)\n"
                     "OR\n"
                     "Enter 1 for List of teams\n"
                     "Enter 2 to restart\n"
                     "Enter 3 to Exit\n")
        if team == "1":
            print(league)
        if team in league or team == "2" or team == "3":
            if team == "3":
                prog_exit()
            return team


def get_score():
    quarter = random.randint(1, 5)
    opponent = league_input[random.randint(0, len(league_input) - 1)]
    team_score = random.randint(2, league_max)
    opp_score = random.randint(2, league_max)
    winner = ""

    if team_score > opp_score:
        winner = team_input
    if opp_score > team_score:
        winner = opponent
    while opponent == team_input:
        opponent = league_input[random.randint(0, len(league_input) - 1)]

    print(team_input + ": " + str(team_score))
    print(opponent + ": " + str(opp_score))

    if quarter in [1, 2, 3, 4]:
        print("Quarter: " + str(quarter))
        print(winner + " is winning!")
    if quarter > 4:
        print("Final")
        print(winner + " won!")

    what_next = input("\nEnter 1 EXIT or any key to restart:\n")
    if what_next == "1":
        prog_exit()


def micro():
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
    time.sleep(5)
    micro_num = microservice.read()
    microservice.close()

    print("Data Received, Generating Score...\n")
    league = True
    lg_max = 0
    if int(micro_num) % 2 == 0:
        league = NFL
        lg_max = 60
    if int(micro_num) % 2 != 0:
        league = NBA
        lg_max = 120

    # print out the number received
    quarter = random.randint(1, 5)
    my_team = league[random.randint(0, len(league) - 1)]
    opponent = league[random.randint(0, len(league) - 1)]
    team_score = random.randint(2, lg_max)
    opp_score = random.randint(2, lg_max)
    winner = ""

    if team_score > opp_score:
        winner = my_team
    if opp_score > team_score:
        winner = opponent

    print(my_team + ": " + str(team_score))
    print(opponent + ": " + str(opp_score))

    if quarter in [1, 2, 3, 4]:
        print("Quarter: " + str(quarter))
        print(winner + " is winning!")
    if quarter > 4:
        print("Final")
        print(winner + " won!")

    what_next = input("\nEnter 1 to EXIT or any other key to restart:\n")
    if what_next == "1":
        prog_exit()


while True:

    league_input = league_choice()

    if league_input == "1":
        league_input = NBA
        league_max = 120

    if league_input == "2":
        league_input = NFL
        league_max = 55

    if league_input == "3":
        micro()
        continue

    team_input = team_choice(league_input)

    if team_input == "2":
        break

    get_score()
