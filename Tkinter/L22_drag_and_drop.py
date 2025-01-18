from tkinter import *


def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y


def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)
    

window = Tk()

label = Label(window, font=('Helvetica', 100), bg='red', width=5, height=3)
label.place(x=0, y=0)

label.bind('<Button-1>', drag_start)
label.bind('<B1-Motion>', drag_motion)

label2 = Label(window, font=('Helvetica', 100), bg='green', width=5, height=3)
label2.place(x=100, y=100)

label2.bind('<Button-1>', drag_start)
label2.bind('<B1-Motion>', drag_motion)

window.mainloop()

# working of functions

# drag_start(event):
#
# In the given code, event.widget is a reference to the widget (in this case, a Label) that triggered the event.
# When an event occurs in a Tkinter application (e.g., a mouse click or a keypress),
# Tkinter generates an event object that contains information about the event.
# The event.widget attribute of the event object is used to identify the widget that triggered the event.
# This function is called when the left mouse button is pressed on the widget ( < Button - 1 > event).
# The event parameter contains information about the event, including the current mouse position.
# We store the initial mouse position (event.x and event.y) in two attributes of the widget:
# widget.startX and widget.startY.
# This is done to keep track of the initial position of the widget when dragging starts.
#
# drag_motion(event):
#
# This function is called when the left mouse button is moved while being held down on the label
# (<B1-Motion> event).
# The event parameter contains information about the event, including the current mouse position.
# We calculate the new position of the widget based on the mouse movement.
# widget.winfo_x() and widget.winfo_y() give the current position of the widget on the window.
# By subtracting widget.startX and widget.startY from the current mouse position (event.x and event.y),
# we obtain the distance the mouse has moved since dragging started.
# We then add this distance to the current position of the widget to get the new position.
# Finally, we update the position of the widget using the place method with the new coordinates x and y,
# making the widget follow the mouse as it moves.
# Overall, these two functions work together to enable the dragging functionality for the widget.
# When you click and hold the left mouse button on the widget,
# the drag_start function is called to record the initial mouse position.
# As you move the mouse while holding down the button,
# the drag_motion function continuously updates the widget's position to follow the mouse cursor,
# resulting in a dragging effect
