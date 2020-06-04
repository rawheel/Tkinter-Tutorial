from tkinter import *

window = Tk()
window.title("PYTROOPS")
window.configure(background = "yellow")
window.geometry('200x200')


pytroops = IntVar()
pytroops_1 = IntVar()
a = Checkbutton(window , text = 'Pizza' , variable = pytroops , bg = 'yellow').pack()
b = Checkbutton(window , text = 'Burger' , variable = pytroops_1 , bg = 'yellow').pack()

def print():
    lst = [pytroops.get() , pytroops_1.get()]
    l1 = Label(window , text = lst , bg = "yellow").pack()

b1 = Button(window , text = "select" , command = print).pack()

window.mainloop()