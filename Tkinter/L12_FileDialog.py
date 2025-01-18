from tkinter import *
from tkinter import filedialog


# opening a file


def openfile():
    filepath = filedialog.askopenfilename(initialdir='C:\\Users\\DOS\\OneDrive\\Python_Codes',
                                          title='opening a file',
                                          filetypes=(('text files', '*.txt'),
                                                     ('all files', '*.*')))
    file = open(filepath, 'r')
    print(file.read())
    file.close()


window = Tk()

button = Button(window, text='open', command=openfile)
button.pack()

window.mainloop()


# saving a file


def savefile():
    file = filedialog.asksaveasfile(initialdir='C:\\Users\\DOS\\OneDrive\\Python_Codes',
                                    defaultextension='.txt',
                                    filetypes=[
                                        ('Text file', '.txt'),
                                        ('HTML file', '.html'),
                                        ('Java file', '.java'),
                                        ('All files', '.*')
                                    ])
    if file is None:
        return 
    file_text = str(text.get('1.0', END))
    # file_text = input('enter some txt')       choose a save location and name. then write sth on console to save
    file.write(file_text)
    file.close()


window = Tk()

button = Button(window, text='save file', command=savefile)
button.pack()

text = Text(window)
text.pack()

window.mainloop()
