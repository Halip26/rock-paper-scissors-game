import random

# Dictionary mapping input characters to game options
my_dict = {"R": "Rock", "P": "Paper", "S": "Scissors"}

# Initializing user and computer scores
user_count = 0
comp_count = 0

# Asking user for the number of games they want to play
games = int(input("\nEnter the number of games you want to play: "))

# Looping until the total number of games played reaches the desired number
while games > 0:
    games -= 1

    # Asking for user's input and converting it to uppercase
    user_input = input("\nUser's Input: ")[0].upper()

    # Checking if user's input is valid (exists in the dictionary)
    if user_input not in my_dict:
        print("INVALID INPUT")
        continue

    # Generating computer's input randomly using dictionary keys
    comp_input = random.choice(list(my_dict.keys()))

    # Printing computer's input
    print("Computer's Input: ", my_dict[comp_input])

    # Updating scores based on the rules of the game
    if (
        (user_input == "R" and comp_input == "P")
        or (user_input == "P" and comp_input == "S")
        or (user_input == "S" and comp_input == "R")
    ):
        comp_count += 1
    elif (
        (user_input == "P" and comp_input == "R")
        or (user_input == "S" and comp_input == "P")
        or (user_input == "R" and comp_input == "S")
    ):
        user_count += 1
    else:
        print("TIE")

    # Printing the current scores
    print("\nSCORE:")
    print("User Score:", user_count, "\tComputer Score:", comp_count, "\n")


print("\n\t\tFINAL SCORE:")
print("User Score:", user_count, "\t\t\tComputer Score:", comp_count, "\n")

# Checking and printing the winner or tie result
if user_count > comp_count:
    print("\n\tCONGRATULATIONS! YOU WON!")
elif user_count < comp_count:
    print("\n\t\tSORRY! YOU LOST!")
else:
    print("\n\t\tOOPS! IT'S A TIE!")
