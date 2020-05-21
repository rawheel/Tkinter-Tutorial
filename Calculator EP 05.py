from tkinter import *

window = Tk()
window.title('CALCULATOR')
window.configure(background = 'black')
window.geometry('400x440')

ent = Entry(window , width = 27 , font = 'Times 20' , borderwidth = 10 , relief = 'ridge')
ent.grid(row = 0 , column = 0 , columnspan = 5 , pady = 10)

def btn_press(num):
    curr = ent.get()
    ent.delete(0 , END)
    ent.insert(0 , str(curr)  + str (num))

def eql():
    ans = ent.get()
    ent.delete(0 , END)
    ent.insert(0 , eval(ans))

def clr():
    ent.delete(0 , END)




#Buttons
btn1 = Button(window , text = "1" , height = 5 , width = 12 , borderwidth = 5 , command = lambda : btn_press(1))
btn2 = Button(window , text = "2" , height = 5 , width = 12 , borderwidth = 5 , command = lambda : btn_press(2))
btn3 = Button(window , text = "3" , height = 5 , width = 12 , borderwidth = 5 , command = lambda : btn_press(3))
btn4 = Button(window , text = "4" , height = 5 , width = 12 , borderwidth = 5 , command = lambda : btn_press(4))
btn5 = Button(window , text = "5" , height = 5 , width = 12 , borderwidth = 5 , command = lambda : btn_press(5))
btn6 = Button(window , text = "6" , height = 5 , width = 12 , borderwidth = 5 , command = lambda : btn_press(6))
btn7 = Button(window , text = "7" , height = 5 , width = 12 , borderwidth = 5 , command = lambda : btn_press(7))
btn8 = Button(window , text = "8" , height = 5 , width = 12 , borderwidth = 5 , command = lambda : btn_press(8))
btn9 = Button(window , text = "9" , height = 5 , width = 12 , borderwidth = 5 , command = lambda : btn_press(9))
btn0 = Button(window , text = "0" , height = 5 , width = 12 , borderwidth = 5 , command = lambda : btn_press(0))
btn_eql = Button(window , text = "=" , height = 5 , width = 12 , borderwidth = 5 , command = eql)
btn_add = Button(window , text = "+" , height = 5 , width = 12 , borderwidth = 5 , command = lambda : btn_press('+'))
btn_sub = Button(window , text = "-" , height = 5 , width = 12 , borderwidth = 5 , command = lambda : btn_press('-'))
btn_mul = Button(window , text = "X" , height = 5 , width = 12 , borderwidth = 5 , command = lambda : btn_press('*'))
btn_div = Button(window , text = "/" , height = 5 , width = 12 , borderwidth = 5 , command = lambda : btn_press('/'))
btn_clr = Button(window , text = "C" , height = 5 , width = 12 , borderwidth = 5 , command = clr)

#griding
btn1.grid(row = 1 , column = 0)
btn2.grid(row = 1 , column = 1)
btn3.grid(row = 1 , column = 2)
btn_add.grid(row = 1 , column = 3)

btn4.grid(row = 2 , column = 0)
btn5.grid(row = 2 , column = 1)
btn6.grid(row = 2 , column = 2)
btn_sub.grid(row = 2 , column = 3)

btn7.grid(row = 3 , column = 0)
btn8.grid(row = 3 , column = 1)
btn9.grid(row = 3 , column = 2)
btn_mul.grid(row = 3 , column = 3)

btn0.grid(row = 4 , column = 0)
btn_div.grid(row = 4 , column = 1)
btn_eql.grid(row = 4 , column = 2)
btn_clr.grid(row = 4 , column = 3)




window.mainloop()