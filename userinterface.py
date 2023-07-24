import csv
from tkinter import *

class User_Input:
    def log_in(self, username, password):
        self.Login_Window = Tk()
        self.Login_Window.geometry("400x150")
        self.Login_Window.title("Log in")
        self.username = username
        self.password = password
        
        #username
        username_label =Label(self.Login_Window, text = "Username").grid(row=0, column=1)
        username = StringVar()
        username_entry = Entry(self.Login_Window, textvariable="Username").grid(row=0, column=2)
        #password
        password_label = Label(self.Login_Window, text = "Password",).grid(row=1, column=1)
        password = StringVar()
        password_entry = Entry(self.Login_Window, textvariable="Password", show="*").grid(row=1, column=2)
        
        self.Login_Window.mainloop()
    