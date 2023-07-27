import tkinter as tk  
from functools import partial
from tkinter import *
from tkinter import ttk
from tkinter import filedialog  
from convtostr import *
from window import *
from searchwindow import *

     
#sample call function from another class     
convtostr.return42()

#jaja = convtostr.joinStr("kulafu")
#print (jaja)
 
# submit part       
def call_result(label_results, inputLname, inputFname, inputAge, inputGender, inputAddr, inputContact, inputfever, inputcough, inputbodypain, inputsorethroat, inputfatigue, inputdiarrhea, inputlosssenses, inputdiffbreathing):  
        
        # create list of inputs
        resLname = (inputLname.get())  
        resFname = (inputFname.get())
        resAge   = (inputAge.get())
        resGender   = (inputGender.get())  
        resAddr   = (inputAddr.get())
        resContact   = (inputContact.get())
        resfever = (inputfever.get())  
        rescough = (inputcough.get())
        resbodypain   = (inputbodypain.get())
        ressorethroat   = (inputsorethroat.get())  
        resfatigue   = (inputfatigue.get())
        resdiarrhea   = (inputdiarrhea.get())
        reslosssenses   = (inputlosssenses.get())
        resdiffbreathing = (inputdiffbreathing.get())
        
        
        # combine input and add spaces
        results = (f"{resLname} {resFname} {resAge} {resGender} {resAddr} {resContact} {resfever} {rescough} {resbodypain} {ressorethroat} {resfatigue} {resdiarrhea} {reslosssenses} {resdiffbreathing}")
        
        # this just show result uncomment to show
        # label_result.config(text="Result %s" % results) 
        
        # convert list of input to string using map
        #mystring=''.join(map(str,results)) 
        print (results)
        mystring = convtostr.joinStr(results)
        
        print("show output on main mystring", mystring)
        # just to check the output of map
        # print(mystring)
        
        # open file for reading existing data 
        with open("dBase.txt",'r') as contents:
                save = contents.read()
        # open file for writing to next line
        with open("dBase.txt",'w') as contents:
                contents.write(mystring + "\n")
        # open file for saving append
        with open("dBase.txt",'a') as contents:
                contents.write(save)

        #workOnFile = open("dBase.txt", "a")
        #workOnFile.write(str(results))
        #workOnFile.close()
        
        l1 = tk.Label(root,  text='Database', width=0 ) # added one Label 
        l1.grid(row=20,column=0) 

        t1 = tk.Text(root,  height=10, width=20) # added one text box
        t1.grid(row=20,column=5) 

        with open("dBase.txt", 'r') as f:    
                t1.insert(INSERT, f.read())
        
        
        return  

# Create Window
root = tk.Tk()  
root.geometry('1024x600')  
root.title('Covid 19 Contact')

#setWindow()

lname = tk.StringVar()  
fname = tk.StringVar()  
age = tk.StringVar()
gender = tk.StringVar()
addr = tk.StringVar()
contact = tk.StringVar()
fever = tk.StringVar()  
cough = tk.StringVar()  
bodypain = tk.StringVar()
sorethroat = tk.StringVar()
fatigue = tk.StringVar()
diarrhea = tk.StringVar()
losssenses= tk.StringVar()
diffbreathing = tk.StringVar()

labelNum1 = tk.Label(root, text="Last Name").grid(row=1, column=0)  
labelNum2 = tk.Label(root, text="First Name").grid(row=2, column=0)
labelNum3 = tk.Label(root, text="Age").grid(row=3, column=0)
labelNum4 = tk.Label(root, text="Gender").grid(row=4, column=0)
labelNum5 = tk.Label(root, text="Address").grid(row=5, column=0)
labelNum6 = tk.Label(root, text="Contact No").grid(row=6, column=0)
labelNum7 = tk.Label(root, text="Fever").grid(row=7, column=0)
labelNum8 = tk.Label(root, text="Cough").grid(row=8, column=0)
labelNum9 = tk.Label(root, text="Body Pain").grid(row=9, column=0)
labelNum10 = tk.Label(root, text="Sore Throat").grid(row=10, column=0)
labelNum11= tk.Label(root, text="Fatigue").grid(row=11, column=0)
labelNum12= tk.Label(root, text="Diarrhea").grid(row=12, column=0)
labelNum13= tk.Label(root, text="Loss Sense Smell/Taste").grid(row=13, column=0)
labelNum14= tk.Label(root, text="Difficulty Breathing").grid(row=14, column=0)


entryNum1 = tk.Entry(root, textvariable=lname).grid(row=1, column=2)   
entryNum2 = tk.Entry(root, textvariable=fname).grid(row=2, column=2)
entryNum3 = tk.Entry(root, textvariable=age).grid(row=3, column=2)
entryNum4 = tk.Entry(root, textvariable=gender).grid(row=4, column=2) 
entryNum5 = tk.Entry(root, textvariable=addr).grid(row=5, column=2) 
entryNum6 = tk.Entry(root, textvariable=contact).grid(row=6, column=2)
entryNum7 = tk.Entry(root, textvariable=fever).grid(row=7, column=2)   
entryNum8 = tk.Entry(root, textvariable=cough).grid(row=8, column=2)
entryNum9 = tk.Entry(root, textvariable=bodypain).grid(row=9, column=2)
entryNum10 = tk.Entry(root, textvariable=sorethroat).grid(row=10, column=2) 
entryNum11 = tk.Entry(root, textvariable=fatigue).grid(row=11, column=2) 
entryNum12 = tk.Entry(root, textvariable=diarrhea).grid(row=12, column=2) 
entryNum13 = tk.Entry(root, textvariable=losssenses).grid(row=13, column=2)
entryNum14 = tk.Entry(root, textvariable=diffbreathing).grid(row=14, column=2) 

labelResult = tk.Label(root)   
labelResult.grid(row=20, column=0)       

call_result = partial(call_result, labelResult, lname, fname, age, gender, addr, contact, fever, cough, bodypain, sorethroat, fatigue, diarrhea, losssenses, diffbreathing)  

buttonCal = tk.Button(root, text="Save", command=call_result).grid(row=70, column=0) 

l1 = tk.Label(root,  text='Database', width=0 ) # added one Label 
l1.grid(row=20,column=0) 

t1 = tk.Text(root,  height=10, width=20) # added one text box
t1.grid(row=20,column=5) 

Button(text="Search database", command= hatdog.cheese).grid(row = 80, column = 0)

root.mainloop()  

