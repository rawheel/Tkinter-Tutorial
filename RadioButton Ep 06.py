from tkinter import *

window = Tk()
window.title("PYTROOPS")
window.configure(background = "yellow")
window.geometry('200x200')


pytroop = StringVar()
pytroop.set("Blue")



def print(ans):
    Label(window , text = ans).pack()

Radiobutton(window , text = "Blue" , variable = pytroop , value = "Blue" ).pack()
Radiobutton(window , text = "Green" , variable = pytroop , value = "Green" ).pack()
Radiobutton(window , text = "Red" , variable = pytroop , value = "Red" ).pack()

a = Button(window , text = "select" , command = lambda : print(pytroop.get())).pack()


window.mainloop()
