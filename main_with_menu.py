import tkinter as tk
from tkinter import *
from tkinter import scrolledtext

def Close():
    root.destroy()

def newRoot2():
   root=Toplevel(root)
   root.title('Add Entry')
   root = tk.Tk()  
   root.geometry('510x560')  
   root.title('Covid 19 Contact') 
   
def newRoot():
   new=Toplevel(root)
   new.geometry("650x768")
   new.title('Search Window')
   #with open("dBase.txt", "r") as f:
   #Label(new, text=f.read()).pack()
   # Create a scrolled text widget


   with open("dBase.txt", "r") as f:
        
        Label(new, text=f.read()).pack()
   # for searching 
   #txtfld=Entry(new,text="This is Entry Widget", bd=5)
   #txtfld.place(x=10, y=330)
   # Create text widget and specify size.
  
  # btn=Button(new,text="search", fg='blue')
   #btn.place(x=200, y=330)
   #output = Text(new,text="dsdd",height = 5, width = 90,bg = "light cyan")
   #output.place(x=2, y=110)
   # for output
   #T = Text(new, text = "", height = 5, width = 52).place(x=10, y=230)
  # text = Text(new).place(x=10, y=230, height = 100, width = 620)
   #Label(new, text=docSum.read()).pack()
  
   
def readFile(inputFile):
        file = open(inputFile, "r")
        content = file.read()

        print("content type: " + type(content).__name__ + "\n")
        print(content)

        file.close()
        return content

root = Tk()

root.geometry('510x560')  
root.title('Covid 19 Contact')

data = "dBase.txt"


btn=Button(text="search window", command=newRoot, fg='blue')
btn.place(x=10, y=100)

btn=Button(text="Add Entry window", command=newRoot2, fg='blue')
btn.place(x=150, y=100)

btn=Button(text="Exit Program", command=Close, fg='blue')
btn.place(x=310, y=100)

root.mainloop()