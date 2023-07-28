import tkinter as tk
from tkinter import ttk
 
 
#in here we have created our tk object
window = tk.Tk()
 
#we have added a title to the window
window.title("Python Tkinter Text Box")
window.minsize(600,400)
 
#this is our event for the button
def clickMe():
    label.configure(text= 'Hello ' + name.get())
 
#This is our label
label = ttk.Label(window, text = "Enter Your Name")
label.grid(column = 0, row = 0)
 
#in here we are getting the text from the text input
name = tk.StringVar()
nameEntered = ttk.Entry(window, width = 15, textvariable = name)
nameEntered.grid(column = 0, row = 1)
 
 
#this is our button
button = ttk.Button(window, text = "Click Me", command = clickMe)
button.grid(column= 0, row = 2)
 
window.mainloop()