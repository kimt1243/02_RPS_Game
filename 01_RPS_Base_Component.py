import random


# Functions go here


def check_rounds():
    while True:
        response = input("How many rounds do you want to play? (<enter> for infinite rounds): ")

        response_error = ("Please type either <enter> or and integer "
                          "that is more than 0")

        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to start of loop 
                if response < 1:
                    print(response_error)
                    print()
                    continue

            except ValueError:
                print(response_error)
                print()
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

game_summary = []

rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

choose_instruction = "Please choose between rock / paper " \
                     "/ scissor "

# Ask user if they have played the game before.
# If 'no', show instructions
# If 'yes', continue game

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

# Rounds won will be calculated (total - draw - lost)

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
    choose_instruction = "Choose between rock / paper / scissors (or xxx to quit):  "
    choose_error = "Please choose from rock / paper / scissors (or xxx to quit)"

    # Ask user for choice and check it's valid
    user_choice = choice_checker(choose_instruction, rps_list, choose_error)

    # End game if exit code is typed
    if user_choice == "xxx" and rounds_played > 0:
        break
    elif user_choice == "xxx":
        print("You have to play at least one round!")
        continue

    comp_choice = random.choice(rps_list[:-1])

    # compare choices
    if user_choice == comp_choice:
        result = "It's a tie"
        rounds_drawn += 1
    elif user_choice == "rock" and comp_choice == "scissors":
        result = "You win"
    elif user_choice == "paper" and comp_choice == "rock":
        result = "You win"
    elif user_choice == "scissors" and comp_choice == "paper":
        result = "You win"
    else:
        result = "You lose"
        rounds_lost += 1

    print()
    feedback = f'{user_choice} vs {comp_choice} : {result}'
    print(feedback)

    rounds_played += 1
    outcome = f'Round {rounds_played}: {feedback}'
    game_summary.append(outcome)

    if rounds_played == rounds:
        break

# Ask user if they want to see their game history.
# Calculate Game Stats
rounds_won = rounds_played - rounds_lost - rounds_drawn

percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100
percent_draw = rounds_drawn / rounds_played * 100

print()
print("----- Game History -----")
for game in game_summary:
    print(game)

print()

# displays game stats with % values to the nearest whole number
print("===== Game Statistics =====")
print("Win: {}, ({:.0f}%) \nLoss: {}, "
      "({:.0f}%) \nTie: {}, ({:.0f}%)".format(rounds_won, percent_win, rounds_lost, percent_lose,
                                              rounds_drawn, percent_draw))
# Quick Calculations (stats)
rounds_won = rounds_played - rounds_drawn - rounds_lost

# End of Game statements
print()
print("------ End Game Summary ------")
print(f'Won: {rounds_won} \t/\t Lost: {rounds_lost} \t/\t Drawn: {rounds_drawn}')
print()
print("!!!! Thanks for playing !!!!")
