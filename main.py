# Importing libraries
from tkinter import *

# Creating and setting up the root
window = Tk()
window.geometry("500x400")
window.title("Event Handling")

# Creating event handlers
def key_press(event):
    print(event.char)

def button_click(event):
    print("Left button of mouse was clicked")

# Binding event handlers
window.bind("<Key>", key_press)
window.bind("<Button-1>", button_click)

# Calling the main loop of tkinter
window.mainloop()