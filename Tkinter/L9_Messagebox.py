from tkinter import *
from tkinter import messagebox


def click():
    # messagebox.showinfo(title='this is an info message box', message='you are a human')
    # while True:
    #     messagebox.showwarning(title='WARNING!', message='you are a human')
    # messagebox.showerror(title='ERROR', message='sth went wrong')
    # if messagebox.askokcancel(title='ok cancel', message='do you want to do it'):
    #     print('you did it')
    # else:
    #     print("you cancelled it")
    # if messagebox.askretrycancel(title='retry cancel', message='do you want to do it'):
    #     print('you retried it')
    # else:
    #     print("you cancelled it")
    # if messagebox.askyesno(title='yes or no', message='do you want to do it'):
    #     print('you said yes')
    # else:
    #     print("you said no")
    # if messagebox.askquestion(title='retry cancel', message='do you want to do it') == 'yes':
    #     print('you said yes')
    # else:
    #     print("you said no")
    answer = messagebox.askyesnocancel(title='coding', message='do you want to code now?', icon='info')
    if answer:
        print('ok,.....which language')
    elif answer is False:
        print('stop playing and start coding that is an order')
    elif answer is None:
        print('stop dodging the question')


window = Tk()

button = Button(window, command=click, text='click me')
button.pack()

window.mainloop()
