import random


# Functions go here
def check_rounds():
    while True:
        response = input("How many rounds: ")

        response_error = ("Please type either <enter> or and integer "
                          "that is more than 0")

        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to start of loop 
                if response < 1:
                    print(response_error)
                    continue

            except ValueError:
                print(response_error)
                continue

        return response


def choice_checker(question, valid_list, error):

    while True:

        # Ask user for choice
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item),
        # the full item is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item no in list
        print()
        print(error)
        print()


# Main routine goes here

# Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played the game before.
# If 'no', show instructions
# If 'yes', continue game


# ask user for # of rounds then loop...
rounds_played = 0
choose_instruction = "Please choose between rock / paper " \
                     "/ scissor "

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of game play loop

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)

    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)

    print(heading)
    choose_instruction = "Choose between rock / paper / " \
                         "scissors (or xxx to quit):  "

    choose_error = "Please choose from rock / paper / scissors (or xxx to quit)"

    # Ask user for choice and check it's valid
    choose = choice_checker(choose_instruction, rps_list, choose_error)

    # End game if exit code is typed
    if choose == "xxx":
        break
# Ask user if they want to see their game history.
# If 'yes' show game history
