import tkinter

from tkinter import *
from functools import partial

class user_input():
    def main_screen():
        main_screen = Tk()
        main_screen.geometry("400x150")
        main_screen.title("COVID 19 - TRACER (LOGIN)")
        
        Label(text="Log in or Register")
        Label(text="").pack()
        
        Button(text="Register", height="2", width="30").pack()
        
        main_screen.mainloop()
        
user_input()