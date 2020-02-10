from tkinter import *
# add window by creating object of tkinter class
root = Tk()
# create frame object

newframe = Frame(root)
newframe.pack()

otherframe = Frame(root)
otherframe.pack(side = BOTTOM)

button1 = Button(newframe,text="click here", fg="red")
button2 = Button(newframe,text="click here", fg="blue")

button1.pack()
button2.pack()

root.mainloop()
