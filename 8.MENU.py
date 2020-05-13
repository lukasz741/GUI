from tkinter import *

def doNothing():
    print("okok")


root = Tk()

menu1 = Menu(root)
root.config(menu=menu1)

#making submenu(dropdown in menu)
subMenu = Menu(menu1)
menu1.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="SAVE+forexample", command=doNothing)
#to seperate in submenu sth(not needed to add it)
subMenu.add_separator()
subMenu.add_command(label="exit", command=doNothing)

# ****************TOOLBAR****************

toolbar = Frame(root, bg="blue")
insertButton = Button(toolbar, text="InsertImage", command=doNothing)
#padx pady -> extra space in X,Y between text
insertButton.pack(side=LEFT, padx=2, pady=2)
printButton = Button(toolbar, text="print", command=doNothing)
printButton.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# ****************STATUSBAR****************
#bd->border
status = Label(root, text="preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


root.mainloop()

