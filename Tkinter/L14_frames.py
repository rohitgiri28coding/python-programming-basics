from tkinter import *

window = Tk()

frame = Frame(window, bg='pink', bd=5, relief=SUNKEN)

Button(frame, text='W', font=('Consolas', 25), width=3).pack(side=TOP)
Button(frame, text='A', font=('Consolas', 25), width=3).pack(side=LEFT)
Button(frame, text='S', font=('Consolas', 25), width=3).pack(side=LEFT)
Button(frame, text='D', font=('Consolas', 25), width=3).pack(side=LEFT)

# frame.pack()
frame.place(x=100, y=100)
window.mainloop()
