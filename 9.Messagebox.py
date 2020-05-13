from tkinter import *
import tkinter.messagebox


root = Tk()

tkinter.messagebox.showinfo("windowTitle", "blebleble")

answer = tkinter.messagebox.askquestion("Question 1", "do u ble?")

if answer == "yes":
    print('ye, i bleble')


root.mainloop()