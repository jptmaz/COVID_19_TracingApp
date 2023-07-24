import tkinter

from tkinter import *
from functools import partial

def user_login(self, username, password):
    print("Username: ", username.get())
    print("Password: ", password.get())
    return

#window
Window = Tk()
Window.geometry('400x150')
Window.title("COVID 19 - Tracer")

#username
username_label = Label(Window, text = "Username").grid(row=0, column = 0)
username = StringVar()
username_entry = Entry(Window, textvariable= username).grid(row=0, column=1)
Window.mainloop()

#password
password_label = Label(Window, text = "Password").grid(row=0, column=1)
password = StringVar()
password_entry = Entry(Window, textvariable="Password").grid(row=0, column=1)