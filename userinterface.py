import csv
from tkinter import *

class User_Input:
    def log_in(self, username, password):
        self.Login_Window = Tk()
        self.Login_Window.geometry("400x150")
        self.Login_Window.title("Log in")
        self.username = username
        self.password = password
        Window = self.Login_Window
        
        username_label =Label(self.Login_Window, text = "Username").grid(row=0, column=1)
        username = StringVar()
        password_entry = Entry(self.Login_Window, textvariable="Username").grid(row=2, column=1)
        
        Window.mainloop()
        return