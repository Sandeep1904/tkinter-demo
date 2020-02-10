from tkinter import *
root = Tk()


label1 = Label(root,text='Fname', bg='red', fg='white')
label2 = Label(root,text='Lname',bg='green',fg = 'white')

# if you want to make self adjusting items
# label1.pack(fill=X)
# label2.pack(side=LEFT,fill=Y)


entry1 = Entry(root)
entry2 = Entry(root)

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
root.mainloop()