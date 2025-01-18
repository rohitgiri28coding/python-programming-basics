# text widget
from tkinter import *


def click():
    entered_input = text.get('1.0', END)
    print(entered_input)


window = Tk()

text = Text(window,
            fg='purple',
            bg='light yellow',
            font=('Ink Free', 25),
            height=8,
            width=20,
            padx=20,
            pady=20)
text.pack()

button = Button(window, text='click me', command=click)
button.pack()

window.mainloop()
