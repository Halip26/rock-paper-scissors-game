import random

# Dictionary that maps input characters to game choices
my_dict = {"R": "Rock", "P": "Paper", "S": "Scissors"}

# Initialize Player and computer scores
user_count = 0
comp_count = 0

# Ask the Player to enter the number of games they want to play
games = int(input("\nEnter the number of games you want to play: "))

# Loop until the total number of games reaches the desired amount
while games > 0:
    games -= 1

    # Ask for Player input and convert it to uppercase
    user_input = input("\nPlayer Input: ")[0].upper()

    # Check if the Player's input is valid (exists in the dictionary)
    if user_input not in my_dict:
        print("INVALID INPUT")
        continue

    # Generate computer input randomly using dictionary keys
    comp_input = random.choice(list(my_dict.keys()))

    # Print computer input
    print("Computer Input: ", my_dict[comp_input])

    # Update scores based on game rules
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

    # Print current score
    print("\nSCORE:")
    print("Player Score:", user_count, "\tComputer Score:", comp_count, "\n")

print("\n\t\tFINAL SCORE:")
print("Player Score:", user_count, "\t\tComputer Score:", comp_count, "\n")

# Check and print the winner or tie result
if user_count > comp_count:
    print("\n\tCONGRATULATIONS! YOU WIN!")
elif user_count < comp_count:
    print("\n\t\tSORRY! YOU LOSE!")
else:
    print("\n\t\tOOPS! IT'S A TIE!")
