from tkinter import *
from PIL import Image, ImageTk


def move_up(event):
    canvas.move(myimage, 0, -10)


def move_down(event):
    canvas.move(myimage, 0, 10)


def move_left(event):
    canvas.move(myimage, -10, 0)


def move_right(event):
    canvas.move(myimage, 10, 0)


window = Tk()

window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)

canvas = Canvas(window, width=800, height=800)
canvas.pack()

image = Image.open('download.png')
photo = ImageTk.PhotoImage(image)
myimage = canvas.create_image(0, 0, image=photo, anchor=NW)

window.mainloop()
