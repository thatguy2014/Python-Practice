#Simple Random Number Generator using inspiration and tools from GeeksforGeeks tutorials

#import tkinter (the GUI module)
from tkinter import *

#import random for the randomizer
import random

#creates the GUI window
rng = Tk() 

# set the background colour of GUI window 
rng.configure(background="dark green") 

#set the title of GUI window 
rng.title("Random Number Generator") 

#set the size of GUI window 
rng.geometry("400x300")

#removes the ability to resize the window because resizing messes up the spacing
rng.resizable(False, False)

#function that should randomize 3 numbers from 0-9 and set them to the 3 labels
def SpinPress():
    Label1.config(text = str(int(10*random.random())))
    Label2.config(text = str(int(10*random.random())))
    Label3.config(text = str(int(10*random.random())))

#creates the labels for outputting the 3 numbers
Label1 = Label(rng, text=str(int(10*random.random())), relief=RAISED, height=10, width=4,)
Label1.place(relx=.3, rely=.4,anchor= CENTER)
Label2 = Label(rng, text=str(int(10*random.random())), relief=RAISED, height=10, width=4)
Label2.place(relx=.5, rely=.4,anchor= CENTER)
Label3 = Label(rng, text=str(int(10*random.random())), relief=RAISED, height=10, width=4)
Label3.place(relx=.7, rely=.4,anchor= CENTER)

#creates a button and places it
Spinbutton = Button(rng, text=' Spin! ', fg='black', bg='red', height=1, width=7, padx=10, pady=10, command=lambda:SpinPress())
Spinbutton.place(relx=.5, rely=.8,anchor= CENTER)

#start the gui window
rng.mainloop()