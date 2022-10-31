# Author: Kyle Sevier
# Date: 10-10-2022
"""
Description: The Budget Center! Calculates the following
- Calculate house payment based on inputted values (can also tell you if you can afford the payment based on income.
1 - Show documentation for this software
2 - add a house to the list
3 - edit a house from the list
4 - list all saved houses
5 - Exit program (data is not saved)!
Saves the results along the way, with the ability to list later

This package uses the pick library for menu selection
"""

from pick import pick
import re
# for clearing screen
import os
import copy
from math import pi
import random
import time


class House:
    # Contains the data to calculate a house payment
    def __init__(self, home_id, home_price, down_payment, loan_program, interest_rate, pmi,
                 property_taxes, home_insurance, hoa_dues, monthly_payment):
        self._home_id = home_id
        self._home_price = home_price
        self._down_payment = down_payment
        self._loan_program = loan_program
        self._interest_rate = interest_rate
        self._pmi = pmi
        self._property_taxes = property_taxes
        self._home_insurance = home_insurance
        self._hoa_dues = hoa_dues
        self._monthly_payment = monthly_payment

    def __str__(self):
        return f"{self._home_id:<10} {self._home_price:<15} {self._down_payment:<15} {self._loan_program:<15}" \
               f"{self._interest_rate:<15} {self._pmi:<8} {self._property_taxes:<15} {self._home_insurance:<17}" \
               f"{self._hoa_dues:<16} ====>  {self._monthly_payment:<15}"


def delete_house(house_list):
    """deletes a house in the house list by house ID"""
    list_houses(house_list, "delete")

    if house_list:
        print("Home ID to delete:", end=" ")
        home_id = numeric_validation("Home ID")
        if home_id == "quit":
            return "quit"

        for home in house_list:
            if home_id == home._home_id:
                house_copy = copy.deepcopy(house_list)
                mistake = copy.deepcopy(home)  # for undoing the deletion
                house_list.remove(home)
                list_houses(house_list, "delete")
                print("\nThe home with ID", home_id, "was deleted successfully.\n"
                                                     "Press [ENTER] to return to the main menu, or type \"undo\" to undo your deletion.")

                action = input()  # akdfjasl;dk
                if action == "undo":
                    house_list.append(mistake)
                    list_houses(house_list, "delete")
                    print("\nThe home with ID", home_id, "was restored.\n"
                                                         "Press [ENTER] to return to the main menu.")
                    input()
                    return house_list
                else:
                    return house_list

        print("\nItem deletion failed. The Home ID you provided does not exist.\n")
        input("Press [ENTER] to return to the main menu.")

        return house_list  # value isn't found
    else:
        print("The list is empty, so you cannot delete entries.\n"
              "Press [ENTER] to return to the main menu.", end=" ")
        input()


def main_menu_picker():
    title = "--- Main Menu ---\n" \
            "Please select from the following options (use arrow keys and hitting ENTER):"
    options = [
        "1: Show documentation for this software",
        "2: Add a house to the list",
        "3: Delete a house from the list",
        "4: List all saved houses (or filter by home ID)",
        "5: Exit"
    ]
    option, index = pick(options, title)
    return option, index


def exit_confirmation_menu():
    os.system("clear")
    title = "Be advised that exiting will delete all saved house data. Do you still want to exit the program?"
    options = [
        "1: Yes, I want to exit the program.",
        "2: No, I want to return to the main menu.",
    ]
    option, index = pick(options, title)
    return option, index


def confirm_exit():
    os.system("clear")
    choice = exit_confirmation_menu()
    if choice[1] == 0:
        return True
    else:
        return False


def numeric_validation(parameter):
    """ account for float and int"""
    number = input()
    if number == "quit":
        return "quit"

    while not re.match(r'^-?[0-9.]+$', number):
        print("Try again. Enter only a number for", parameter, ":", end=" ")
        number = input()
    if '.' in number:
        # could remove all but one period here via regex to clean input
        return float(number)
    else:
        return int(number)


def show_documentation():
    os.system("clear")
    print("--- Mortgage Database Budget Tool -- (Made in Python)\n")
    print("This software has several features that are broken into bite-sized main menu chunks:\n")

    print("Option 1: Show documentation for this software.\n"
          "\t This is where you are now. Here, you can read what the software is capable of and what to expect when using it.\n\n")

    print("Option 2: Add a house to the master list\n"
          "\t This option allows you to enter the parameters to calculate a house payment. Some of these items include\n"
          ", but are not limited to, home price, insurance rate, and PMI costs. You will be given the option to exit the "
          "option and return to the main menu before a deletion occurs.\n\n")

    print("Option 3: Delete an existing house from the list\n"
          "\t Here, a list will be shown to you, where you'll be give the option to either exit the menu (if you're done)\n"
          " or specify the ID of the house you'd like to delete. You will be walked through this process. You will"
          " be given the option to exit the option and return to the main menu before a deletion occurs.\n\n")

    print("Option 4: List all saved houses (also filter house by Home ID)\n"
          "\t This option automatically shows you a list of all the houses in the database. You will then be given"
          " the option to search for a house based on the Home ID. \nYou will be guided through this process. If the"
          " Home ID is not found, you'll be notified and asked to return to the main menu. You will be given the option"
          " to exit the option and return to the main menu in the middle of the process.\n\n")

    print("Option 5: Exit\n"
          "\tThis option exits the program completely. Your house data will be lost, but pre-processed data will be re-added when"
          " the software is restarted.")

    input("\nPress [ENTER] to exit this list and return to the main menu.")


def add_house(current_home_id):
    """ add a house to the list of houses and calculates payment"""
    os.system("clear")

    print("\nYou've chosen to add a house to the list.\n"
          "Only numbers are valid inputs. If input is non-numeric, you'll be prompted to enter a number.\n"
          "Enter \"quit\" + ENTER at any time to return to the main menu.\n"
          "Keep in mind that this process takes a little longer to complete than the other functions\n")

    home_id = current_home_id

    # the home price logic integrates with my partner's microservice, so it'll need to come from that if selected
    choice = input("Would you like to pull the house price from the microservice? yes/no: ")
    if choice == "yes" or choice == "y":
        home_price = receive_house_price()
    else:
        print("\nInitial Home Price:", end=" ")
        home_price = numeric_validation("Home Price")
        if home_price == "quit":
            return "quit"
        if home_price not in range(100000, 1200000):
            print("The home price you entered is out of the ordinary. Please confirm your input:", end=" ")
            home_price = numeric_validation("Home Price")

    print("\nDown Payment:", end=" ")
    down_payment = numeric_validation("Down Payment")
    if down_payment == "quit":
        return "quit"
    if down_payment not in range(0, 100000):
        print("The down payment you entered is out of the ordinary. Please confirm your input: ", end=" ")
        down_payment = numeric_validation("Down Payment")

    print("\nLoan Program (term length, typically 15 or 30 years):", end=" ")
    loan_program = numeric_validation("Loan Program")
    if loan_program == "quit":
        return "quit"
    if loan_program not in (15, 30):
        print(
            "The term length you entered is out of the ordinary (typically 15 or 30 years). Please confirm your input:",
            end=" ")
        loan_program = numeric_validation("Loan Program")

    print("\nInterest Rate:", end=" ")
    interest_rate = numeric_validation("Interest Rate")
    if interest_rate == "quit":
        return "quit"
    if interest_rate < 3 or interest_rate > 7:
        print("The term length you entered is out of the ordinary. Please confirm your input:", end=" ")
        interest_rate = numeric_validation("Interest Rate")

    print("\nMonthly PMI:", end=" ")
    pmi = numeric_validation("Monthly PMI")
    if pmi == "quit":
        return "quit"
    if pmi not in range(200, 500):
        print("The monthly PMI you entered is out of the ordinary. Please confirm your input:", end=" ")
        pmi = numeric_validation("Monthly PMI")

    print("\nAnnual Property Taxes:", end=" ")
    property_taxes = numeric_validation("Annual Property Taxes")
    if property_taxes == "quit":
        return "quit"
    if property_taxes not in range(2000, 5000):
        print("The annual property tax you entered is out of the ordinary. Please confirm your input:", end=" ")
        property_taxes = numeric_validation("Annual Property Taxes: ")

    print("\nAnnual Home Insurance:", end=" ")
    home_insurance = numeric_validation("Annual Home Insurance")
    if home_insurance == "quit":
        return "quit"
    if home_insurance not in range(300, 2000):
        print("The annual home insurance you entered is out of the ordinary. Please confirm your input:", end=" ")
        home_insurance = numeric_validation("Annual Home Insurance: ")

    print("\nMonthly HOA Dues:", end=" ")
    hoa_dues = numeric_validation("MonthlyHOA Dues")
    if hoa_dues == "quit":
        return "quit"
    if hoa_dues not in range(50, 150):
        print("The Monthly HOA Dues you entered is out of the ordinary. Please confirm your input:", end=" ")
        hoa_dues = numeric_validation("Monthly HOA Dues: ")

    monthly_payment = calculate_monthly_payment(home_price, down_payment, loan_program, interest_rate, pmi,
                                                property_taxes,
                                                home_insurance, hoa_dues)

    new_house = House(home_id, home_price, down_payment, loan_program, interest_rate, pmi, property_taxes,
                      home_insurance, hoa_dues, monthly_payment)

    return new_house


def receive_house_price():
    """this function send a signal to the text file that the microservice is listening for, the text 'go'
	once received, the microservice will generate a random house price that it will then write to the text file.

	This program will wait for that new price and then return it into the add_house function to be used
	when adding a house."""

    # wait for the word "run" in the prng-service.txt file, generate num
    # First write "go" to the text file
    file = open('house_price.txt', 'r+', encoding="utf-8")
    file.write('go\n')
    file.seek(0)

    # wait for partner microservice to write house price, strip newline and check numeric-only line
    while not file.readline().strip().isnumeric():
        file.seek(0)
        time.sleep(1)

    # seek to beginning and store the new house price just written
    file.seek(0)
    key = file.readline()
    print(key)
    file.close()

    # feed add_house function new house value
    return int(key)


def list_houses(house_list, option):
    """list all houses stored in the house list array
	Option: If True, delete home is being called, and we don't want to wait to exit"""

    unused_variable = os.system("clear")

    print(" -- List of Houses --\n ")
    print(f"{'Home ID':<10} {'Home Price':<15} {'Down Payment':<15} {'Loan Program':<15}"
          f"{'Interest Rate':<15} {'PMI':<8} {'Property Taxes':<15} {'Home Insurance':<17}"
          f"{'HOA Dues':<16} {'Monthly Payment':<15}")

    print(u'\u2500' * 150)

    if house_list:
        for house in house_list:
            print(house, '\n')
    else:
        print("\n\n\nHouse list is empty. Add a house from the main menu!\n")
        input("Press [ENTER] to exit this list and return to the main menu.\n")
        return

    if option == "list":
        choice = input(
            "To search for a specific Home ID in this list, type \"search\" + [ENTER]. \nOtherwise, press [ENTER]"
            " to continue: ")

        if choice == 'search':
            print("\nType the home ID you'd like to search for, then press [ENTER]: ", end=' ')
            search = numeric_validation("Home ID")
            if not isinstance(search, int):  # check for float too?
                print("You didn't input a valid home ID. Please re-enter the home ID you want to search: ")
                search = numeric_validation("Home ID")
            # now search for the house
            for house in house_list:
                if house._home_id == search:
                    os.system("clear")
                    print("-- Filtered Search (by Home ID) --\n")
                    print(f"{'Home ID':<10} {'Home Price':<15} {'Down Payment':<15} {'Loan Program':<15}"
                          f"{'Interest Rate':<15} {'PMI':<8} {'Property Taxes':<15} {'Home Insurance':<17}"
                          f"{'HOA Dues':<16} {'Monthly Payment':<15}")
                    print(u'\u2500' * 150)
                    print(house)
                    print("\nHouse ID", search, "found in the database.\n")
                    input("Press [ENTER] to exit this list and return to the main menu.")
                    return

            print("The Home ID you entered does not exist in the database.\n")
            input("Press [ENTER] to exit this list and return to the main menu.\n")
            return
        else:
            print("\nYou did not choose to search the list. If this was a mistake, re-enter this selection\n"
                  "in the main menu and type \"search\" as described above.\n")
            input("Press [ENTER] to exit this list and return to the main menu.")

    else:
        return


def greeting():
    print("Welcome to your home-buying assistant!\n")
    print("I highly recommend reading the short documentation showing the use of this software.\n"
          "You can access this documentation by selecting option one (1) in the main menu.\n")
    input("Press [ENTER] to continue.\n")


def calculate_monthly_payment(home_price, down_payment, loan_program, interest_rate, pmi, property_taxes,
                              home_insurance, hoa_dues):
    # https://mortgage.lovetoknow.com/Calculate_Mortgage_Payments_Formula
    interest_rate /= 100
    interest_rate /= 12
    num_payments = loan_program * 12
    term = (1 + interest_rate) ** num_payments
    monthly_payment = ((home_price - down_payment) * ((interest_rate * term) / (term - 1))) + pmi + (
            property_taxes / 12) + (home_insurance / 12) + hoa_dues
    return monthly_payment


def add_starter_homes(house_list):
    """adds starter homes so the user can tinker with the data"""

    # self, home_id, home_price, down_payment, loan_program, interest_rate, pmi, property_taxes,
    # home_insurance, hoa_dues, monthly payment):
    h1 = House(101, 423100, 10000, 30, 4.5, 123, 235, 120, 2840, 2498.12)
    h2 = House(102, 405000, 7590, 30, 4.5, 123, 235, 101, 2840, 2058.51)
    h3 = House(103, 799999, 0, 23, 15, 5.1, 235, 77, 175, 5890.90)
    h4 = House(104, 225000, 25000, 15, 3.9, 123, 235, 101, 2840, 1765.03)

    house_list.extend((h1, h2, h3, h4))
    return house_list


def main():
    greeting()

    exit_out = False
    current_home_id = 104
    house_list = []

    # add starter homes
    house_list = add_starter_homes(house_list)

    while not exit_out:
        choice = main_menu_picker()

        if choice[1] == 1:
            show_documentation()
        elif choice[1] == 0:
            home_copy = copy.deepcopy(house_list)
            add_house_choice = add_house(current_home_id + 1)
            if add_house_choice == "quit":
                pass
            else:
                house_list.append(add_house_choice)
                current_home_id += 1
        elif choice[1] == 2:
            home_copy = copy.deepcopy(house_list)
            delete_response = delete_house(house_list)  # sdfasdfasd
            if delete_response == "quit":
                house_list = home_copy
        # else:
        # 	house_list = delete_house(house_list)
        elif choice[1] == 3:
            list_houses(house_list, "list")
        elif choice[1] == 4:
            exit_out = confirm_exit()


if __name__ == "__main__":
    main()
