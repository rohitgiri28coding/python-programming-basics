from tkinter import *

window = Tk()

Label(window, text='First Name', width=20).grid(row=0, column=0)
Entry(window).grid(row=0, column=1)
Label(window, text='Last Name').grid(row=1, column=0)
Entry(window).grid(row=1, column=1)
Label(window, text='Email').grid(row=2, column=0)
Entry(window).grid(row=2, column=1)
Button(window, text='Submit').grid(row=3, column=0, columnspan=2)

window.mainloop()
