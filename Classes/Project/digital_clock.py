#!/usr/bin/python

######################
#   Assignment: Designing a digital clock
#   Name    : Stephanie Mangereza
#   Date    : 10 /06 /2022
######################

from tkinter import *
from time import strftime
root = Tk()
root.geometry("500x500")
root.resizable(0,0)
root.title('Python Clock')
Label(root,text = 'Mangereza Xensei', font ='Gadugi 20 bold').pack(side=BOTTOM)
def time():
    string = strftime('%H:%M:%S %p')
    mark.config(text = string)
    mark.after(1000, time)
mark = Label(root, 
            font = ('calibri', 40, 'bold'),
            pady=150,
            foreground = 'black')
mark.pack(anchor = 'center')
time()
 
mainloop()