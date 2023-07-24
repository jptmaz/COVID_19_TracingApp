from tkinter import *

UI_Window = Tk()
UI_Window.title("Log in/Sign up")
UI_Window.geometry("700x500")

Login_Button = Button(text= "Log in").grid(row = 1, column = 1)
Signup_Button = Button(text= "Sign up").grid(row = 1, column = 2)

UI_Window.mainloop()