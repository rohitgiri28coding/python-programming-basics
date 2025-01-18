from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)      # window that manages a collection of windows/displays

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text='Tab 2')
notebook.pack(expand=True, fill=BOTH)

Label(tab1, text='this is a label in tab1', width=50, height=25).pack()

Label(tab2, text='this is a label in tab2', width=50, height=25).pack()

window.mainloop()
