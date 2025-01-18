from tkinter import *

# label = an area widget that holds text, and/or an image within a window

window = Tk()

# photo = PhotoImage(file='C:\\Users\\DOS\\Desktop\\shell.png')

label = Label(window,
              text='Rohit created a label',
              font=('Times New Roman', 40, 'italic'),
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              # image=photo,
              compound='bottom')


label.pack()
#  label.place(x=0, y=0)

window.mainloop()
