from tkinter import *

#creating blank window to work on
root = Tk()

#creating frames
topframe = Frame(root)
topframe.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

#creating buttons in frames
button1 = Button(topframe, text="Button1", fg='red')
button2 = Button(topframe, text="Button2", fg='blue')
button3 = Button(topframe, text="Button3", fg='green')
button4 = Button(bottomframe, text="Button4", fg='purple')

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack()

#keeps window opened
root.mainloop()

