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

#password
password_label = Label(Window, text = "Password").grid(row=1, column=0)
password = StringVar()
password_entry = Entry(Window, textvariable="Password", show="*").grid(row=1, column=1)

#validate login
validate_login = partial(user_login, username, password)

#login button
login_button = Button(Window, text = "Login", command=validate_login).grid(row=4, column=0)

Window.mainloop()