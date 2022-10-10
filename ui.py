import random



while True:

    league_input = input("Enter 1 for NBA scores or 2 for NFL scores:\n")

    while league_input not in ["1", "2"]:
        print("That is not a correct input, try again.\n")
        break

    if league_input == "1":
        print("NBA it is!\n")
        team_choice = input("Which teams score did you want to check?\n")

    if league_input == "2":
        print("NFL it is!\n")
        team_choice = input("Which teams score did you want to check?\n")



