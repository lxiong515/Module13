"""
Program: number_guess.py
Author:  Luke Xiong
Date: 07/18/2020

This program will have a set of buttons for users to select a number guess
"""
import tkinter as tk
from random import randrange
from tkinter import messagebox

window = tk.Tk()
window.title("Guessing Game")

label_intro = tk.Label(window, text = "Guess a number from 0 to 9")
label_instruct = tk.Label(window, text = "Click a button below!")
label_guess = tk.Label(window, text="Your Guesses: ")

# create the buttons
buttons = []
for index in range(0, 10):
    button = tk.Button(window, text=index, command=lambda index=index : process(index), state=tk.DISABLED)
    buttons.append(button)


btnStartGameList = []
for index in range(0, 1):
    btnStartGame = tk.Button(window, text="Start Game", command=lambda : startgame(index))
    btnStartGameList.append(btnStartGame)

# grid
label_intro.grid(row=0, column=0, columnspan=5)
label_instruct.grid(row=2, column=0, columnspan=3)
label_guess.grid(row=4, column=0, columnspan=5)

for row in range(0, 2):
    for col in range(0, 5):
        i = row * 5 + col  # convert 2d index to 1d. 5= total number of columns
        buttons[i].grid(row=row+10, column=col)

btnStartGameList[0].grid(row=13, column=0, columnspan=5)

guess = 0
secretNumber = randrange(10)
print(secretNumber)
guess_row = 4

# reset all variables
def init():
    global buttons, guess, totalNumberOfGuesses, secretNumber, guess_list, guess_row
    secretNumber = randrange(10)
    print(secretNumber)
    guess_row = 4
    guess_list = []

def process(i):
    global totalNumberOfGuesses, buttons, guess_row, guess_list
    guess = i
    guess_list=[]
    if guess == secretNumber:
        messagebox.showinfo(title="Congratulations!", message="That's the correct number!")

        for b in buttons:
            b["state"] = tk.DISABLED
    else:
        #save the guess to a list
        guess_list.append(i)
        #print the list to verify it is passing the number
        #print(guess_list)
        #need to display the guess_list!!! but how?
    buttons[i]["state"] = tk.DISABLED


status = "none"


def startgame(i):

    global status
    for b in buttons:
        b["state"] = tk.NORMAL

    if status == "none":
        status = "started"
        btnStartGameList[i]["text"] = "Retart Game"
    else:
        status = "restarted"
        init()
    print("Game started")


window.mainloop()
