import random
import time

# Tipe data collection dictionary
my_dict = {"R": "Rock", "P": "Paper", "S": "Scissors"}

# inisialisasi player score & computer
player_count = 0
computer_count = 0

# ask player to input how many player want to play
games = int(input("\nEnter the number of games you want to play: "))

# Repeats until the total number of games reaches the desired number.
while games > 0:
    games -= 1

    # asking input from player & connverting to Uppercase
    player_input = input("\nPlayer's input (R, P, S): ")[0].upper()

    # Check if the user input is valid (exists in the dictionary)
    if player_input not in my_dict:
        print("Your input is invalid, try again!")
        continue

    # Randomly generate computer input using dictionary keys
    comp_input = random.choice(list(my_dict.keys()))

    print("-" * 25)
    time.sleep(0.5)
    # Print randomly generate computer's choice
    print(f"Computer input: {my_dict[comp_input]}")

    # Updating scores based on game rules
    if (
        (player_input == "R" and comp_input == "P")
        or (player_input == "P" and comp_input == "S")
        or (player_input == "S" and comp_input == "R")
    ):
        computer_count += 1
    elif (
        (player_input == "P" and comp_input == "R")
        or (player_input == "S" and comp_input == "P")
        or (player_input == "R" and comp_input == "S")
    ):
        player_count += 1
    else:
        print("\nTIE!")

    # Print currently score
    print("\n\t\t\tSCORES:")
    print(
        "Player's Score:", player_count, "\t\tComputer's Score:", computer_count, "\n"
    )

# Print FINAL Score
print("\nFINAL SCORE:")
print("Player's Score:", player_count, "\t\tComputer's Score:", computer_count, "\n")

print("-" * 25)
time.sleep(0.5)
# Check & print the winner or tie result
if player_count > computer_count:
    print("\n\tCONGRATULATIONS, YOU WON!")
elif player_count < computer_count:
    print("\n\tSORRY, YOU ARE LOSE!")
else:
    print("\n\tOOPPS, IT'S TIE!")
