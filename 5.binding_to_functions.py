from tkinter import *

root = Tk()

# def printName():
#     print("hello hello")
#
# button_1 = Button(root, text="Print hello", command=printName)
# button_1.pack()

# or
def printName(event):
    print("hello hello")

button_1 = Button(root, text="Print hello")
button_1.bind("<Button-1>", printName)
button_1.pack()

root.mainloop()