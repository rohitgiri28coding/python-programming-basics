from tkinter import *


def create_window():
    new_window = Tk()           # new independent window. needs to be closed separately
    # new_window = Toplevel()       # new window on top of other window linked to a bottom window.
    old_window.destroy()
    new_window.mainloop()          # not necessary


old_window = Tk()

Button(old_window, text='create new window', font=('Consolas', 25), command=create_window).pack()

old_window.mainloop()
