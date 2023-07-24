from tracer import *
from tkinter import *

C19_Tracer = Tk()
C19_Tracer.title("COVID 19 TRACER")
C19_Tracer.geometry("700x500")

mainscreen_login_signup = Label(C19_Tracer, text = "Sign in:").grid(row = 0, column = 1)
mainscreen_login = Button(C19_Tracer, text = "Log in").grid(row = 0, column = 2)
mainscreen_signup = Button(C19_Tracer, text = "Sign up").grid(row = 0, column = 3)


C19_Tracer.mainloop()

