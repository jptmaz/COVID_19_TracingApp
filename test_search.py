import tkinter as tk
from tkinter import ttk

#in here we have created our tk object
window = tk.Tk()
 
#we have added a title to the window
window.title("Search Text")
window.minsize(600,400)
 
#this is our event for the button
def clickMe():
    x = name.get()
    print(x)
    with open(r'dBase.txt', 'r') as fp:
        # read all lines in a list
            lines = fp.readlines()
            for line in lines:
                if line.find(x) != -1:
                    print(x, 'txt exists in file')
                    print('Line Number:', lines.index(line))
                    print('Line:', line)
            return
    
#This is our label
label = ttk.Label(window, text = "Search Text")
label.grid(column = 0, row = 0)
 
#in here we are getting the text from the text input
name = tk.StringVar()
nameEntered = ttk.Entry(window, width = 15, textvariable = name)
nameEntered.grid(column = 0, row = 1)
 
#this is our button
button = ttk.Button(window, text = "Click Me", command = clickMe)
button.grid(column= 0, row = 2)
 
window.mainloop()