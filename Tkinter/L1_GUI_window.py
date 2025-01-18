from tkinter import *

# widgets = GUI elements: buttons, text boxes, labels, images
# window = serves as a container to hold or contain these widgets

window = Tk()     # instantiating a window
window.geometry("420x420")
window.title('Rohit\'s GUI')
icon = PhotoImage(file='C:\\Users\\DOS\\Desktop\\shell.png')
window.iconphoto(True, icon)
window.config(background='black')

window.mainloop()  # places window on screen, listens to event
