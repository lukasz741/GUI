from tkinter import *

root = Tk()

one = Label(root, text="One", bg="red", fg="yellow")
one.pack()

two = Label(root, text="Two", bg="black", fg="green")
two.pack(fill=X)

three = Label(root, text="Three", bg="white", fg="blue")
three.pack(side=LEFT, fill=Y)


root.mainloop()