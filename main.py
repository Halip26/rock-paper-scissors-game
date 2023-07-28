# Import Required Library
from tkinter import *
from tkinter import ttk
from random import *

# Create Object
root = Tk()

# Set geometry
root.geometry("500x500")

root.title("Rock-Paper-Scissors-Game")

# List of players
list = ["rock", "paper", "scissors"]

choose_number = randint(0, 2)
print(choose_number)  # For testing if it works

label = Label(root, text="Computer ", width=20, height=4, font=("algerian", 15))
label.pack()

# Adding dropdown box for Rock,Paper,Scissors
user_select = ttk.Combobox(
    root, font=("arial", 15), width=10, height=4, value=["Rock", "Paper", "Scissors"]
)


# Membuat fungsi spin untuk tombolnya
def spin():
    choose_number = randint(0, 2)
    label.config(text=list[choose_number])
    # Check if user_select is equal to "Rock"
    if user_select.get() == "Rock":
        user_select_value = 0
        print(user_select_value)
    # Check if user_select is equal to "Paper"
    elif user_select.get() == "Paper":
        user_select_value = 1
        print(user_select_value)
    # Check if user_select is equal to "Scissors"
    elif user_select.get() == "Scissors":
        user_select_value = 2
        print(user_select_value)

    # Check if user_select_value is equal to 0,1,2
    if user_select_value == 0:
        # Check if choose_number is equal to 0
        if choose_number == 0:
            wl_label.config(text="Tie! " + "\nComputer : Bad luck")
        # Check if choose_number is equal to 1
        elif choose_number == 1:
            wl_label.config(text="You Loose " + "\nComputer : I am better ")
        # Check if choose_number is equal to 2
        elif choose_number == 2:
            wl_label.config(text="You Won " + "\nComputer : You won by luck")

    # Check if user_select_value is equal to 1
    elif user_select_value == 1:
        # Check if choose_number is equal to 1
        if choose_number == 1:
            wl_label.config(text="Tie! " + "\nComputer : Nice game")
        # Check if choose_number is equal to 0
        elif choose_number == 0:
            wl_label.config(text="You Won " + "\nComputer : Woow! You are better")
        # Check if choose_number is equal to 2
        elif choose_number == 2:
            wl_label.config(text="You Loose " + "\nComputer : Booo LOL")

    # Check if user_select_value is equal to 2
    elif user_select_value == 2:
        # Check if choose_number is equal to 2
        if choose_number == 2:
            wl_label.config(text="Tie!")
        # Check if choose_number is equal to 0
        elif choose_number == 0:
            wl_label.config(
                text="You Loose "
                + " \nComputer : I am playing this \ngame since i was born"
            )
        # Check if choose_number is equal to 1
        elif choose_number == 1:
            wl_label.config(text="You Won")


user_select.current(0)
user_select.pack()

# Add Labels
wl_label = Label(root, text="", font=("arial", 15), width=60, height=4)
wl_label.pack()

# Add Button
button = Button(root, text="Spin!", font=("bell mt", 15), command=spin)
button.pack()

root.mainloop()
