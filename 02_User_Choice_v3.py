# Version 3 - checks that response is in a given list


# Functions go here
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

# lists for checking responses


rps_list = ["rock", "paper", "scissors", "xxx"]

# Loop for testing purposes
user_choice = ""
while user_choice != "xxx":

    # Ask user for choice and check it's valid
    user_choice = choice_checker("Choose between rock / paper / scissors "
                                 "(or xxx to quit):  ",
                                 rps_list, "Please choose from rock / paper "
                                           "/ scissors (or xxx to quit)"                           "")

    # print out choice for comparison purposes
    print()
    print("You chose {}".format(user_choice))
    print()
