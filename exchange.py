# Import random for usage in one of the mini programs
import random

# Function for Currency making change program which breaks down users number into
# smaller bills and coins
def currency_change():
    print("CURRENCY EXCHANGE PROGRAM")
    # Ask user to input a positive number
    money = float(input("Enter a positive number that will be broken down into change (ex. 53.47): "))

    # Has to be int in order to find the remainder
    # Finds the number of twenty dollar bills needed for the total amount inputted
    twenty_d = int(money/ 20)
    twenty_remainder = money - (float(twenty_d) * 20.0)

    # Finds the number of ten dollar bills needed for the total amount inputted
    ten_d = int(twenty_remainder/10)
    ten_remainder = twenty_remainder - (float(ten_d) * 10.0)

    # Finds the number of five dollar bills needed for the total amount inputted
    five_d = int(ten_remainder / 5)
    five_remainder = ten_remainder - (float(five_d) * 5.0)

    # Finds the number of Two dollar coins needed for the total amount inputted
    toonie = int(five_remainder / 2)
    toonie_remainder = five_remainder - (float(toonie) * 2.0)

    # Finds the number of One dollar coins needed for the total amount inputted
    loonie = int(toonie_remainder / 1)
    loonie_remainder = toonie_remainder - (float(loonie) * 1.0)

    # Finds the number of 25 cent coins needed for the total amount inputted
    quarter = int(loonie_remainder / 0.25)
    quarter_r = loonie_remainder - (float(quarter) * 0.25)

    # Finds the number of 10 cent coins needed for the total amount inputted
    dime = int(quarter_r / 0.10)
    dime_r = quarter_r - (float(dime) * 0.10)

    # Finds the number of 5 cent coins needed for the total amount inputted
    nickel = int(dime_r / 0.04)
    nickel_r = dime_r - (float(nickel) * 0.05)

    # finds the remainder of cents left if any
    remainder = int(nickel_r / 0.009)

    # Runs the variables above such that the number the user inputted is broken down
    # into smaller bills and coins
    print("")
    print("The amount given is suggested to be paid as the following")
    print("$" + str(money) + " is broken down to this many:")
    print(twenty_d, " 20 Dollar Bills")
    print(ten_d, " 10 Dollar Bills")
    print(five_d, " 5 Dollar Bills")
    print(toonie, " 2 Dollar Coins")
    print(loonie, " 1 Dollar Coins")
    print(quarter, " 25 Cent Coins")
    print(dime, " 10 Cent Coins")
    print(nickel, " 5 Cent Coins")
    print(remainder, " is the remainder in cents")

    print("------------------------------------------------------------------")

# Ask user if they want to play the game
Ask_user = input("Do you want to start program? Enter (yes or no): ")
# Instructions on how to maneuver through the program
if Ask_user == "yes" or Ask_user == "Yes":
    option_play = True
    print("MENU SYSTEM")
    print("INSTRUCTIONS ")
    print("Type 1 - To Execute/Run a Currency Making Change Generator Program")
    print("Type 2 - To quit/stop Program")
    print("---------------------------------------------------------------------------")

elif Ask_user == "no" or Ask_user == "No":
    option_play = False
    print("User does not want to start, program will not execute......... ")

option_select = 0
# condition such that if user selects option 5 the while statement will stop resulting
# in the end of the program
while option_select != 2:
    # conditions based on user input which will run a function
    if option_play == True:
        option_select = int(input("Select an option: "))
        if option_select == 1:
            currency_change()
        # User enters a integer not between 1 - 5, it will print a statement to that affect
        elif option_select <= 0 or option_select > 2:
            print("Error Invalid Number was Entered")
            print("Please select one of the following options located above")
            print(option_select)

# when while loop stops by entering 5, program will print text below
print("Program has Stopped/Ended")
