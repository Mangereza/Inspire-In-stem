#!/usr/bin/python

######################
#   gui_examples using tkinker
#   Name    : Stephanie Mangereza
#   Date    : 07 /06 /2022
######################

from tkinter import *

window =  Tk()
window.title("Welcome to my world")
window.geometry("400x400")
window.configure(bg='orange')
f_name = Label(window, text= "First name", font =("Lucida Calligraphy",24))
s_name = Label(window, text= "Second name", font =("Lucida Calligraphy",24))
f_name.grid(column = 60, row =100)
s_name.grid(column = 60, row=120)
btn= Button(window,text ="click me!",bg='purple',fg='white')
btn.grid(column = 150, row = 150 )

txt_box = Entry(window, width =20)
txt_box.grid(column = 100, row = 100)

txt_box = Entry(window, width =20)
txt_box.grid(column = 100, row = 120)

def open_popup():
    top = Toplevel(window)
    top.geometry("300x300")
    top.title("pop up window")
    top.configure(bg='green')
    msg=Label(top,text="Gotcha in my pop up",font=('Mistral 18')).place (x150, y=150)

window.mainloop()



