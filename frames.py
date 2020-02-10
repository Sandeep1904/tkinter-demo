from tkinter import *
# add window by creating object of tkinter class
root = Tk()
# create frame object

newframe = Frame(root)
newframe.pack()
# creating an element
otherframe = Frame(root)
otherframe.pack(side = BOTTOM)

button1 = Button(newframe,text="click here", fg="red")
button2 = Button(newframe,text="click here", fg="blue")
# adding it to the window
button1.pack()
button2.pack()
# loop to keep the window open
root.mainloop()
