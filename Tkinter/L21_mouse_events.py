from tkinter import *


def do_sth(event):
    print('Mouse coordinates: ', event.x, ', ', event.y)


window = Tk()

window.bind('<Button-1>', do_sth)           # left click
window.bind('<Button-2>', do_sth)           # scroll
window.bind('<Button-3>', do_sth)           # right click
window.bind('<Enter>', do_sth)              # enter the window
window.bind('<Leave>', do_sth)              # leave the window
window.bind('<Motion>', do_sth)

window.mainloop()
