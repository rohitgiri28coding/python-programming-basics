from tkinter import *
from tkinter import ttk
from F2_Mean import mean

def next_page():
    selected_item = dropdown_var.get().lower()
    f = list(f_var.get())
    x = list(x_var.get())
    match selected_item:
        case "mean":
            mean(f, x)



def set_one():
    f_entry.delete(0, END)
    n = ['1,' for _ in range(int(num_entry.get()))]
    f_entry.insert(0, ''.join(n)[0:2*len(n)-1])


def inputCI():
    x_label.config(text="Enter start value of ci and gap")


window = Tk()
# window.geometry('700x500')
window.title('Statistics')
window.config(background='#8cfffb')
dropdown_var = StringVar()
dropdown = ttk.Combobox(window, textvariable=dropdown_var, values=["Mean",
                                                                   "Median",
                                                                   "Mode",
                                                                   'Geometric Mean',
                                                                   'Harmonic Mean',
                                                                   'Standard deviation',
                                                                   'Mean deviation'],
                        font=('Times New Roman', 10)
                        )
choice_label = Label(window,
                     text='Choice',
                     font=('Times New Roman', 12),
                     fg='black',
                     bg='#8cfffb'
                     )

num_label = Label(window,
                  text='Enter number of observation: ',
                  font=('Times New Roman', 12),
                  fg='black',
                  bg='#8cfffb'
                  )

x_label = Label(window,
                text='Enter xi (each separated by comma)',
                font=('Times New Roman', 12),
                fg='black',
                bg='#8cfffb'
                )

f_label = Label(window,
                text='Enter fi (each separated by comma)',
                font=('Times New Roman', 12),
                fg='black',
                bg='#8cfffb'
                )
num_entry = Entry(window,
                  font=('Times New Roman', 12))
num_entry.insert(0, '0')
num_entry.config(fg='black',
                 bg='#8cfffb')
x_var = StringVar()
x_entry = Entry(window,
                font=('Times New Roman', 12))
x_entry.insert(0, '1,2,3,4,5')
x_entry.config(fg='black',
               bg='#8cfffb')
f_var = StringVar()
f_entry = Entry(window,
                font=('Times New Roman', 12))
f_entry.insert(0, '1,2,3,4,5')
f_entry.config(fg='black',
               bg="#8cfffb")

x1 = BooleanVar()
x_checkbutton = Checkbutton(window,
                            text='If data is given in CI',
                            variable=x1,
                            onvalue=True,
                            offvalue=False,
                            command=inputCI,
                            font=('Times New Roman', 10),
                            fg='black',
                            bg='#8cfffb',
                            activebackground='#8cfffb',
                            activeforeground='red',
                            compound='left')

x2 = BooleanVar()
f_checkbutton = Checkbutton(window,
                            text='If all f is 1',
                            variable=x2,
                            onvalue=True,
                            offvalue=False,
                            command=set_one,
                            font=('Times New Roman', 10),
                            fg='black',
                            bg='#8cfffb',
                            activebackground='#8cfffb',
                            activeforeground='red',
                            compound='left')

cal_button = Button(window,
                    text='Calculate',
                    command=next_page,
                    font=('Times New Roman', 20),
                    fg='#00FF00',
                    bg='#8cfffb',
                    activeforeground='black',
                    activebackground='#8cfffb',
                    state=ACTIVE,
                    borderwidth=0,
                    compound='bottom')

choice_label.grid(row=0, column=0, sticky='w', rowspan=2)
dropdown.grid(row=0, column=1, columnspan=2, sticky='w', rowspan=2)

num_label.grid(row=2, column=0, sticky='w')
num_entry.grid(row=2, column=1, columnspan=2)

x_label.grid(row=3, column=0, sticky='w')
x_entry.grid(row=3, column=1, columnspan=2)

x_checkbutton.grid(row=4, column=0, columnspan=2, sticky='w')

f_label.grid(row=5, column=0, sticky='w')
f_entry.grid(row=5, column=1, columnspan=2)

f_checkbutton.grid(row=6, column=0, columnspan=2, sticky='w')

cal_button.grid(row=7, column=2, sticky='se')

window.mainloop()
