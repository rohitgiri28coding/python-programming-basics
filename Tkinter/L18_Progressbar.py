from tkinter import *
from tkinter.ttk import *
import time


def start():
    tasks = 10
    while tasks != 0:
        time.sleep(1)
        tasks -= 1
        bar['value'] += 10
        progress.set('Progress = ' + str(10 - tasks) + '/10')
        percent.set(str((10 - tasks) * 10) + '% Done')
        window.update_idletasks()         # this will update the progress bar for each iteration


window = Tk()

percent = StringVar()
progress = StringVar()

bar = Progressbar(window, orient=HORIZONTAL)
bar.pack(pady=25)

Button(window, text='download.png', command=start).pack()

percent_label = Label(window, textvariable=percent)
percent_label.pack()
percent.set('0% Done')

progress_label = Label(window, textvariable=progress)
progress_label.pack()
progress.set('Progress = 0/0')

window.mainloop()
