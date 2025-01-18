import time
from tkinter import *
from L26_ball import *

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas, 0, 0, 100, 2, 1, 'white')
tennis_ball = Ball(canvas, 0, 0, 30, 4, 3, 'green')
duce_ball = Ball(canvas, 0, 0, 30, 3, 2, 'red')

while True:
    volley_ball.move()
    tennis_ball.move()
    duce_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()
