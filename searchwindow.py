from tkinter import *
from functools import partial

class hatdog():
    
    def searchresult(inputSdbase):
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
        searchroot = Tk()  
        searchroot.geometry('1024x600')  
        searchroot.title('Covid 19 Contact - Search Menu')
        
        sdbase = StringVar()
        
        labelsearch= Label(searchroot, text="Search database for word").grid(row=3, column=0)
        entrysearch = Entry(searchroot, textvariable=sdbase).grid(row=3, column=2)
        
        
        hatdog.searchresult = partial(hatdog.searchresult, sdbase)
        #buttonsubmit
        buttonCal = Button(searchroot, text="Search", command=hatdog.searchresult).grid(row=4, column=0)
        
        
        
        l1 = Label(searchroot,  text='Database', width=0 ) # added one Label 
        l1.grid(row=20,column=0) 
        
        

#Not working
        t1 = Text(searchroot,  height=10, width=20) # added one text box
        t1.grid(row=20,column=5) 

        #with open("dBase.txt", 'r') as f:    
        #    t1.insert(INSERT, f.read())
        
        
        
        searchroot.mainloop()
    

     
