#import tools for interface
from tkinter import *

#make class
class user_interface():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    #make log in
    def log_in(self, username, password):
        Window = Tk()
        Window.title("Log in")
        Window.geometry("150x150")
        #username
        username_label = Label(Window, text = "Username").grid(row=0, column=0)
        username = StringVar()
        username_entry = Entry(Window, textvariable="Username").grid(row=0, column =1)
        #password
        password_label = Label(Window, text = "Password").grid(row=1, column=0)
        password = StringVar()
        password_entry = Entry(Window, textvariable="Password", show="*").grid(row=1, column =1)


        
    
        
    
    