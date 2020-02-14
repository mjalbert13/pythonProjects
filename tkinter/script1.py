from tkinter import *

window = Tk()

def km2miles():
    miles =float( e1_val.get())*1.6
    t1.insert(END, miles)


bt = Button(window, text="Execute", command=km2miles)
bt.grid(row=0, column= 0)

e1_val=StringVar()
e1= Entry(window, textvariable=e1_val)
e1.grid(row=0, column=1)

t1 =Text(window, height=1, width=20)
t1.grid(row=1,column=2)

window.mainloop()
