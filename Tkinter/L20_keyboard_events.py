from tkinter import *


def do_sth(event):
    # print('you pressed: ', event.keysym)
    label.config(text=event.keysym)


window = Tk()

window.bind('<Key>', do_sth)
# window.bind('<r>', do_sth)

label = Label(window, font=('Helvetica', 100))
label.pack()

window.mainloop()
