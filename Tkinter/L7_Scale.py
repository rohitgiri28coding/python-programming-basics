from tkinter import *


def submit():
    print('The temperature is ', scale.get(), 'degree c')


# fire_image = PhotoImage(file='fire.png')
# fireLabel = Label(image=fire_image)
# fireLabel.pack()

window = Tk()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,
              font=('Consolas', 20),
              tickinterval=10,              # add numeric indicators to values
              showvalue=False,              # hide current value
              resolution=5,                 # increment of slider
              troughcolor='#69EAFF',
              fg='#FF1C00',
              bg='black')
scale.set(((scale['from']-scale['to'])/2)+scale['to'])      # set the scale in middle value
scale.pack()

button = Button(window, text='submit', command=submit)
button.pack()

window.mainloop()
