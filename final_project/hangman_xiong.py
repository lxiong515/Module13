"""
Program: hangman_xiong.py
Author:  Luke Xiong
Date: 07/23/2020

This program will have a set of buttons for users to select a number guess
"""
#random word picked
import random
import tkinter as tk

window = tk.Tk()
window.title("Hangman")

label_intro = tk.Label(window, text = "Welcome to Hangman!")
label_instruct = tk.Label(window, text = "Pick a letter below.")
label_guess = tk.Label(window, text="Your Guesses: ")

# create the buttons
buttons = []
for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    button = tk.Button(window, text=letter, #command=lambda index=letter : process(letter),
                        state=tk.DISABLED)
    buttons.append(button)


btnStartGameList = []
for index in range(0, 1):
    btnStartGame = tk.Button(window, text="Start Game", command=lambda : startgame(index))
    btnStartGameList.append(btnStartGame)

# grid
label_intro.grid(row=0, column=0, columnspan=6)
label_instruct.grid(row=2, column=0, columnspan=6)
label_guess.grid(row=4, column=0, columnspan=6)

for row in range(0, 2):
    for col in range(0, 5):
        i = row * 5 + col  # convert 2d index to 1d. 5= total number of columns
        buttons[i].grid(row=row+25, column=col)

btnStartGameList[0].grid(row=13, column=0, columnspan=5)

# Main game logic

guess = 0
totalNumberOfGuesses = 0 #length of random word
#secretNumber = randrange(10)
secret_word = '' #use method to find random word
print(secret_word)
lblLogs = []
guess_row = 4

def select_word():
#import a file with words
#create a method to read a word
    word = (random.choice(open("words.txt").read().split()))
    #print(word) confirmed it's randomly selecting
    #count length of word so # of guesses < length
    len(word)
    #print(len(word)) confirmed its counting word length


def startgame(i):

    #global status
    #for b in buttons:
        #b["state"] = tk.NORMAL

    #if status == "none":
        #status = "started"
        #btnStartGameList[i]["text"] = "Retart Game"
    #else:
        #status = "restarted"
        #init()
    #print("Game started")
    pass
#if __name__=='__main__':
    #pass

window.mainloop()
