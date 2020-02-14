from tkinter import *

window = Tk()

def converter():
    grams = float(e1_val.get()) * 1000
    pounds = float(e1_val.get()) * 2.20462
    ounces = float(e1_val.get()) * 35.274
    t1.insert(END, grams)
    t2.insert(END, pounds)
    t3.insert(END, ounces)


l1 = Label(window, text="Kg")
l1.grid(row=0, column=0)

e1_val =StringVar()
e1 = Entry(window, textvariable=e1_val)
e1.grid(row=0, column=1)

bt = Button(window, text="Convert", command=converter)
bt.grid(row=0, column=2)

t1= Text(window, height=1, width=20)
t1.grid(row=1,column=0)

t2= Text(window, height=1, width=20)
t2.grid(row=1,column=1)

t3= Text(window, height=1, width=20)
t3.grid(row=1,column=2)

window.mainloop()