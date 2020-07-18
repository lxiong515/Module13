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

m.title('Guess the Random Number')
label=tkinter.Label(m, text="Pick a number below:")
label.grid(row=1, column=1)
var1=tkinter.IntVar()

one_button=tkinter.Button(m, text='1', width = 20, command=pick_one).grid(row=2, column=1) #highlight #messagebox for correct#)
two_button=tkinter.Button(m, text='2', width = 20, command=pick_one).grid(row=2, column=2) #highlight #messagebox for correct#)
three_button=tkinter.Button(m, text='3', width = 20, command=pick_one).grid(row=3, column=1) #highlight #messagebox for correct#)
four_button=tkinter.Button(m, text='4', width = 20, command=pick_one).grid(row=3, column=2) #highlight #messagebox for correct#)
five_button=tkinter.Button(m, text='5', width = 20, command=pick_one).grid(row=4, column=1) #highlight #messagebox for correct#)
six_button=tkinter.Button(m, text='6', width = 20, command=pick_one).grid(row=4, column=2) #highlight #messagebox for correct#)
seven_button=tkinter.Button(m, text='7', width = 20, command=pick_one).grid(row=5, column=1) #highlight #messagebox for correct#)
eight_button=tkinter.Button(m, text='8', width = 20, command=pick_one).grid(row=5, column=2) #highlight #messagebox for correct#)
exit_button=tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=7, column=2)

m.mainloop() #infinite loop that waits for events to happen

