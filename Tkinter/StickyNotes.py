from tkinter import *
from tkinter import filedialog


def open_file():
    filepath = filedialog.askopenfilename(initialdir='C:\\Users\\DOS\\OneDrive\\Python_Codes',
                                          title='opening a file',
                                          filetypes=(('text files', '*.txt'),
                                                     ('all files', '*.*')))
    if filepath:
        with open(filepath, 'r') as file:
            text.insert(END, file.read())


def save_file():
    file = filedialog.asksaveasfile(initialdir='C:\\Users\\DOS\\OneDrive\\Python_Codes',
                                    defaultextension='.py',
                                    filetypes=[
                                        ('Text file', '.txt'),
                                        ('HTML file', '.html'),
                                        ('Java file', '.java'),
                                        ('All files', '.*')
                                    ])
    if file is None:
        return
    file_text = str(text.get('1.0', END))
    file.write(file_text)
    file.close()


txt = ['', False]


def update_text_size(event):
    text.config(width=event.width // 10, height=event.height // 30)


def cut():
    global txt
    try:
        txt[0], txt[1] = text.selection_get(), True
        text.delete('sel.first', 'sel.last')
    except TclError:
        print('Selection not done')


def copy():
    global txt
    try:
        txt[0] = text.selection_get()
    except TclError:
        print('Selection not done')


def paste():
    text.insert(text.index(INSERT), txt[0])
    if txt[1]:
        txt[0] = ''


window = Tk()
window.title('Sticky Notes')
window.geometry('450x400')
menubar = Menu(window)
window.config(menu=menubar)

text = Text(window,
            fg='purple',
            bg='light yellow',
            font=('Ink Free', 25),
            padx=15,
            pady=15)

text.pack(expand=True, fill="both")
fileMenu = Menu(menubar, tearoff=0, font=('MV Boli', 10))
menubar.add_cascade(label='File', menu=fileMenu)

fileMenu.add_command(label='Open',
                     command=open_file
                     )
window.bind("<Configure>", update_text_size)
fileMenu.add_command(label='Save', command=save_file)
fileMenu.add_separator()

fileMenu.add_command(label='Exit', command=quit)

editMenu = Menu(menubar, tearoff=0, font=('MV Boli', 10))
menubar.add_cascade(label='Edit', menu=editMenu)

editMenu.add_command(label='Cut', command=cut)
editMenu.add_command(label='Copy', command=copy)
editMenu.add_command(label='Paste', command=paste)


window.mainloop()
