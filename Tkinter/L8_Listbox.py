from tkinter import *


def submit():
    print('You have ordered: ', end='')
    print(listbox.get(listbox.curselection()))


def add():
    if entry.get() == '':
        print('enter something to add')
    else:
        listbox.insert(listbox.size(), entry.get())
        listbox.config(height=listbox.size())


def delete():
    for i in reversed(listbox.curselection()):
        print('You have deleted ', listbox.get(i))
        listbox.delete(i)
    # listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())


window = Tk()

listbox = Listbox(window,
                  bg='#f7ffde',
                  font=('Constantia', 25))
listbox.pack()

listbox.insert(1, 'chawal')
listbox.insert(2, 'dal')
listbox.insert(3, 'chokha')
listbox.config(height=listbox.size())

entry = Entry(window)
entry.pack()

addButton = Button(window, text='add', command=add)
addButton.pack()

submitButton = Button(window, text='submit', command=submit)
submitButton.pack()

delButton = Button(window, text='delete', command=delete)
delButton.pack()

window.mainloop()
