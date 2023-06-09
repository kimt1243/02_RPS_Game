# Functions go here


def check_rounds():
    while True:
        response = input("How many rounds: ")

        response_error = ("Please type either <enter> or and integer "
                          "that is more than 0")

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(response_error)
                    continue

            except ValueError:
                print(response_error)
                continue

        return response


# Main routine goes here


rounds_played = 0
choose_instruction = "Please choose between rock / paper " \
                     "/ scissor "

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)

    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)

    print(heading)
    choose = input("{} or 'xxx' to end: ".format(choose_instruction))

    # End game if exit code is typed
    if choose == "xxx":
        break
    # rest of loop / game
    print("You chose{}".format(choose))

    rounds_played += 1

print("Thank you for playing")
