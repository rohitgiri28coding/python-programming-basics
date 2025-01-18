from tkinter import *
from tkinter import colorchooser


def click():
    color = colorchooser.askcolor()
    color_hex = color[1]
    window.config(bg=color_hex)


window = Tk()
window.geometry('420x420')

button = Button(window, text='click me', command=click)
button.pack()

window.mainloop()
