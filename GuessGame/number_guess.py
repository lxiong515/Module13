"""
Program: number_guess.py
Author:  Luke Xiong
Date: 07/18/2020

This program will have a set of buttons for users to select a number guess
"""

import tkinter

m=tkinter.Tk() # where m is the name of the main window object

def pick_one():
    label.config(text="Coming right up!")

class NumberGuesser:
    def __init__(self):
        pass
    def add_guess(self):
        guessed_list=0
        return guessed_list

m.title('Guess the Random Number')
label=tkinter.Label(m, text="Pick a number below!")
label.grid(row=1, column=2)
var1=tkinter.IntVar()

#Button generates a random number between 1 and MAX.
start_button=tkinter.Button(m, text='Start Game', width = 15, command=pick_one).grid(row=1, column=1) #highlight #messagebox for correct#)

one_button=tkinter.Button(m, text='1', width = 20, command=pick_one).grid(row=2, column=1)
two_button=tkinter.Button(m, text='2', width = 20, command=pick_one).grid(row=2, column=2)
three_button=tkinter.Button(m, text='3', width = 20, command=pick_one).grid(row=3, column=1)
four_button=tkinter.Button(m, text='4', width = 20, command=pick_one).grid(row=3, column=2)
five_button=tkinter.Button(m, text='5', width = 20, command=pick_one).grid(row=4, column=1)
six_button=tkinter.Button(m, text='6', width = 20, command=pick_one).grid(row=4, column=2)
seven_button=tkinter.Button(m, text='7', width = 20, command=pick_one).grid(row=5, column=1)
eight_button=tkinter.Button(m, text='8', width = 20, command=pick_one).grid(row=5, column=2)

#Create a WINNER window or messagebox to pop up
#Reset game

#Add guessed number to guessed_list in object of type NumberGuesser
guess_label=tkinter.Label(m, text="Numbers guessed: ")
guess_label.grid(row=6, column=1)

#button to reset
reset_button=tkinter.Button(m, text='Play Again!', width=15, command=m.destroy)
reset_button.grid(row=7, column=1)
#button to exit
exit_button=tkinter.Button(m, text='Exit', width=15, command=m.destroy)
exit_button.grid(row=7, column=2)

m.mainloop() #infinite loop that waits for events to happen

