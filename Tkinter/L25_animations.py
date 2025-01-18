from tkinter import *
import time
from PIL import Image, ImageTk


WIDTH = 500
HEIGHT = 500
X_VELOCITY = 5
Y_VELOCITY = 5

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

# background_image = Image.open('background.png')
# background_photo = ImageTk.PhotoImage(background_image)
# my_background_image = canvas.create_image(0, 0, image=background_photo, anchor=NW)

image = Image.open('download.png')
photo = ImageTk.PhotoImage(image)

image_width = photo.width()
image_height = photo.height()

myimage = canvas.create_image(0, 0, image=photo, anchor=NW)

while True:
    coordinates = canvas.coords(myimage)
    print(coordinates)
    if coordinates[0] > WIDTH - image_width or coordinates[0] < 0:
        X_VELOCITY = - X_VELOCITY
    if coordinates[1] > HEIGHT - image_height or coordinates[1] < 0:
        Y_VELOCITY = - Y_VELOCITY
    canvas.move(myimage, X_VELOCITY, Y_VELOCITY)
    window.update()
    time.sleep(0.1)


# window.mainloop()
