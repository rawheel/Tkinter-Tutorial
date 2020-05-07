from tkinter import *

window = Tk()
window.title('PYTROOPS')
window.geometry("600x600")
window.configure(background = "yellow")
ent = Entry(window , width = 70 , bg = "black" , fg = 'white' , borderwidth = 12)
ent.pack()
ent.insert(0 , "Enter your name")

def func():
    a = "WELCOME TO "  + ent.get()
    label1 = Label(window , text = a)
    label1.pack()

btn1 = Button(window , text = "name" , command = func)
btn1.pack()

window.mainloop()