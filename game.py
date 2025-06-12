#solving the game
import random

user_input = int(input("enter the number 0 for ROCK, 1 for SCISSORS, 2 for PAPER"))
print("User input is:")
print(user_input)
if user_input > 2:
    print("invalid input, you lose")
else:
    comp_choice = random.randint(0, 2)
    print("computer choice: ")
    print(comp_choice)
    if comp_choice == user_input:
        print("you draw")
    elif comp_choice > user_input:
        print("you win")
    elif comp_choice < user_input:
        print("you lose")
    elif comp_choice == 0 and user_input == 2:
        print("you lose")
    elif comp_choice == 2 and user_input == 0:
        print("you win")

