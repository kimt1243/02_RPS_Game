# Functions go here
def choice_checker(question):

    error = "Please choose between rock / paper / scissor (or xxx to quit)"

    while True:

        # Ask user for choice
        response = input(question).lower()

        if response == "r" or response == "rock":
            return "rock"
        if response == "s" or response == "scissors":
            return "scissors"
        if response == "p" or response == "paper":
            return "paper"

        # exit code
        elif response == "xxx":
            return response

        else:
            print()
            print(error)
            print()
# Main routine goes here


# Loop for testing purposes
user_choice = ""
while user_choice != "xxx":

    # Ask user for choice and check it's valid
    user_choice = choice_checker("Choose between (rock / paper / scissors) ")

    # print out choice for comparison purposes
    print("You chose {}".format(user_choice))
