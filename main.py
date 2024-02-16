# Imports
import random


# Variables
actions = ["rock", "paper", "scissors"]


# Defined Functions
def game(computer_choice, user_choice):
    if computer_choice == user_choice:
        print("It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "paper":
            print("You lose!")
        else:
            print("You win!")
    elif user_choice == "paper":
        if computer_choice == "scissors":
            print("You lose!")
        else:
            print("You win!")
    elif user_choice == "scissors":
        if computer_choice == "rock":
            print("You lose!")
        else:
            print("You win!")


# Main
def main():
    action = actions[random.randint(0, 2)]
    # Make sure user inputs a number between 1 and 3
    check = True
    while check:
        user_choice = input(
            "1. Rock\n2. Paper\n3. Scissors\nRock, paper, or scissors?: ")
        if user_choice.isdigit() and 1 <= int(user_choice) <= 3:
            check = False
            user_choice = actions[int(user_choice)-1]
        else:
            print("Please input a number between 1 and 3.\n")
            continue
    print(
        "My answer: "+action
        + "\nYour answer: "+user_choice)
    game(action, user_choice)


if __name__ == "__main__":
    main()
