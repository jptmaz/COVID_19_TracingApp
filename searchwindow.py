from tkinter import *
import tkinter as tk  
from tkinter import ttk
from tkinter import filedialog 
from functools import partial

class hatdog():
    
    def searchresult(label_result, inputSdbase):
        resDdbase = (inputSdbase.get())
         # create list of inputs
        print(resDdbase)
        print("Sdbasefunc")
        
        with open(r'dBase.txt', 'r') as fp:
            # read all lines in a list
            lines = fp.readlines()
            for line in lines:
                # check if word is present
                    if line.find(resDdbase) != -1:
                        print(resDdbase, 'txt exists in file')
                        print('Line Number:', lines.index(line))
                        print('Line:', line)

    def cheese():
        searchroot = tk.Tk()  
        searchroot.geometry('1024x600')  
        searchroot.title('Covid 19 Contact - Search Menu')
        
        sdbase = tk.StringVar()
        
        labelsearch= tk.Label(searchroot, text="Search database for word").grid(row=3, column=0)
        entrysearch = tk.Entry(searchroot, textvariable=sdbase).grid(row=3, column=2)
     
        print(sdbase)
        print("^^^ After submit sdbase")
        
        labelResult = tk.Label(searchroot)   
        labelResult.grid(row=20, column=0) 
        
        hatdog.searchresult = partial(hatdog.searchresult, labelResult, sdbase)
        #buttonsubmit
        buttonCal = tk.Button(searchroot, text="Search", command=hatdog.searchresult).grid(row=4, column=0)
        
        
        
        l1 = tk.Label(searchroot,  text='Database', width=0 ) # added one Label 
        l1.grid(row=20,column=0) 
        
        

#Not working
        t1 = tk.Text(searchroot,  height=10, width=20) # added one text box
        t1.grid(row=20,column=5) 

        #with open("dBase.txt", 'r') as f:    
        #    t1.insert(INSERT, f.read())
        
        
        
        searchroot.mainloop()
    

     
