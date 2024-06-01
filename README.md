# 2 Players of the Simple Rock Paper Scissors Game

  Introducing the Rock Paper Scissors Games:

Are you ready for some friendly competition? Look no further than our Rock Paper Scissors Games project! Get ready to go head-to-head against an AI opponent in the ultimate test of strategy and luck.

With our carefully crafted code, this classic game comes to life in a digital format. The rules are simple: choose between rock, paper, or scissors, and see who comes out on top. Will you make the right move to beat your opponent?

Our AI programming assistant ensures that every game is uniquely challenging. Prepare yourself for unexpected twists and turns as you try to outsmart the computer. Will you be the ultimate Rock Paper Scissors champion?

Ramp up the excitement by inviting friends to join in on the fun. Take turns battling against each other or collaborate to beat the AI opponent. With engaging gameplay and a user-friendly interface, everyone can easily join in on the action.

So what are you waiting for? Dive into the world of Rock Paper Scissors Games now and test your skills. Whether you're a seasoned veteran or new to the game, this project guarantees endless entertainment and friendly competition.

Note: The code for the Rock Paper Scissors Games project is provided below:

```python
# Rock Paper Scissors game

import random

print("--- Rock, Paper, Scissors Game ---")
print("Choose your weapon: ")
print("1. Rock")
print("2. Paper")
print("3. Scissors")

player_choice = int(input("Enter your choice (1-3): "))

computer_choice = random.randint(1, 3)

if player_choice == computer_choice:
    print("It's a tie!")
elif (player_choice == 1 and computer_choice == 3) or (player_choice == 2 and computer_choice == 1) or (player_choice == 3 and computer_choice == 2):
    print("Congratulations! You win!")
else:
    print("Oops! Computer wins!")

```

## 1. GUI Rock Paper Scissors Game

  [GUI Rock Paper Scissors](main.py)

## 2. A Simple Rock Paper Scissors Game

  [A Simple Rock Papcer Scissors](simple.py)

### To be Played with a Computer
  
* You can enter the number of games you want to play.
* There is also a score window which is displayed after every turn.

### Example Game

![Game](https://i.postimg.cc/7Y2TJsVJ/Capture.png)
