#!/usr/bin/python
import tkinter as tk  
from functools import partial

window = tk.Tk()
window.geometry("400x250")  
greeting = tk.Label(text="Covid 19 Tracing Application")
greeting.pack()
labelResult = tk.Label(window)

def call_result(label_result, lnameEntry, fnameEntry, ageEntry,genderEntry,addressEntry,contactEntry):  
    lNameSub = (lnameEntry.get())   
    fNameSub = (fnameEntry.get())
    ageSub = (ageEntry.get())  
    genderSub = (genderEntry.get())  
    addressSub = (addressEntry.get())  
    contactSub = (contactEntry.get())
    
    result = str(lNameSub)+str(fNameSub)+str(ageSub)+str(genderSub)+str(addressSub)+str(contactSub)
    label_result.config(text="Result = %d" % result)  
    return  

#str1 = tk.StringVar()  
#str2 = tk.StringVar()
#str3 = tk.StringVar()  
#str4 = tk.StringVar()  
#str5 = tk.StringVar()  
#str6 = tk.StringVar()    

#call_result = partial(call_result, labelResult, str1, str2, str3, str4, str5, str6)    
#buttonCal = tk.Button(window, text="Submit", command=call_result).place(x = 10, y = 200)

# labels
lName = tk.Label(window, text = "Last: ").place(x = 10,y = 50)
fName = tk.Label(window, text = "First Name: ").place(x = 10, y = 70) 
age = tk.Label(window, text = "Age: ").place(x = 10, y = 90)
gender = tk.Label(window, text = "Gender: ").place(x = 10, y = 110)   
address = tk.Label(window, text = "Address: ").place(x = 10, y = 130)
contact = tk.Label(window, text = "Contact Number: ").place(x = 10, y = 150)

# entries
lnameEntry = tk.Entry(window).place(x = 160, y = 50)
fnameEntry = tk.Entry(window).place(x = 160, y = 70) 
ageEntry = tk.Entry(window).place(x = 160, y = 90) 
genderEntry = tk.Entry(window).place(x = 160, y = 110) 
addressEntry = tk.Entry(window).place(x = 160, y = 130) 
contactEntry = tk.Entry(window).place(x = 160, y = 150) 

# Check database

#with open('dBase.txt') as f:
#    while True:
#        line = f.readline()
#        if not line:
#            break
#        print(line.strip())
      
      
        
# join all data
#label = tk.Label(text="Hello, Tkinter")
#input_array = [
#    input("Last Name: ")
#    ,input("First Name: ")
#    ,input("Age: ")
#    ,input("Gender: ")
#    ,input("Address: ")
#    ,input("Contact Number: ")
#]

# save result to a variable
#results = (", ".join(input_array))

# open file for reading existing data
#with open("dBase.txt",'r') as contents:
#    save = contents.read()
      
#with open("dBase.txt",'w') as contents:
#    contents.write(results + "\n")
#      
#with open("dBase.txt",'a') as contents:
#    contents.write(save)


#workOnFile = open("dBase.txt", "a")
#workOnFile.write(results)
#workOnFile.close()