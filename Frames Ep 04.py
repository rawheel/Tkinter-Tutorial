from tkinter import *

window = Tk()
window.title("PYTROOPS")
window.geometry("700x600")
window.configure(background = "yellow")
f1 = Frame(window , bg = 'grey' , borderwidth  = 5 , relief = 'ridge')
f1.pack(side = LEFT , fill = "y")

f2 =  Frame(window , bg = 'grey'  , borderwidth  = 5 , relief = 'ridge')
f2.pack(side = TOP , fill = 'x')

f3 =  Frame(window , bg = 'grey'  , borderwidth  = 5 , relief = 'ridge')
f3.pack(side = LEFT , fill = 'y')


l1 = Label(f1 , text = "HELLO" , bg = 'grey' , fg = 'black' , font = "Times 20 bold")
l1.pack(padx = 60 , pady = 260)

l2= Label(f2 , text = "PYTROOPS" , bg = 'grey' , fg = 'black' , font = "Times 20 bold")
l2.pack()

l3= Label(f3 , text = "WELCOME" , bg = 'grey' , fg = 'black' , font = "Times 20 bold")
l3.pack(padx = 155 , pady = 200)

window.mainloop()