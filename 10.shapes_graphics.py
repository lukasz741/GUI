from tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()

line = canvas.create_line(0,0,200,50)
redline = canvas.create_line(0,100,200,50, fill="red")
greenbox = canvas.create_rectangle(25,25,130,75, fill="green")

#canvas.delete(variable) ->delete element in canvas
root.mainloop()
