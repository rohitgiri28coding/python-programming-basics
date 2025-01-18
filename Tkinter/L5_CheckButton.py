from tkinter import *


def display():
    if x.get():
        print('you agreed')
    else:
        print('you disagreed')


window = Tk()

# photo = PhotoImage(file='C:\\Users\\DOS\\Desktop\\shell.png')
x = BooleanVar()                # it can be IntVar, StringVar depending on the on-value and off-value
check_button = Checkbutton(window,
                           text='I agree with this image',
                           textvariable=x,
                           onvalue=True,
                           offvalue=False,
                           command=display,
                           font=('Arial', 20),
                           fg='#00FF00',
                           bg='black',
                           activebackground='black',
                           activeforeground='#00FF00',
                           padx=25,
                           pady=25,
                           # image=photo,
                           compound='left')
check_button.pack()
window.mainloop()
