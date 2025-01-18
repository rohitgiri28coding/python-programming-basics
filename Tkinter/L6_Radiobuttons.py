from tkinter import *


def order():
    if x.get() == 0:
        print('you ordered chawal')
    elif x.get() == 1:
        print('you ordered dal')
    elif x.get() == 2:
        print('you ordered chokha')


food = ['chawal', 'dal', 'chokha']
# chawal_photo = PhotoImage('chawal.png')
# dal_photo = PhotoImage('dal.png')
# chokha_photo= PhotoImage('chokha.png')
# images = [chawal_photo, dal_photo, chokha_photo]
window = Tk()

x = IntVar()

for i in range(len(food)):
    radiobutton = Radiobutton(window,               # adds each radiobutton to window
                              text=food[i],         # adds text to each radiobutton
                              variable=x,           # groups radiobutton together if they share the same variable
                              value=i,              # assigns each radiobutton a different value
                              pady=25,
                              padx=25,
                              font=('Impact', 15),
                              # image=images[i],
                              # compound='left',
                              indicatoron=False,         # removes the circle button and makes push button
                              width=50,              # set size of the push button
                              command=order
                              )
    radiobutton.pack(anchor=W)
window.mainloop()
