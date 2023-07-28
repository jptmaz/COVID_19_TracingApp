from tkinter import *
 

root = Tk()
fram = Frame(root)
Label(fram,text='Text to find:').pack(side=LEFT)
edit = Entry(fram)
edit.pack(side=LEFT, fill=BOTH, expand=1)
edit.focus_set()
butt = Button(fram, text='Find') 
butt.pack(side=RIGHT)
fram.pack(side=TOP)
 
with open(r'dBase.txt', 'r') as f:
    text = Text(root)
    text.insert(INSERT, f.read())
    text.pack(side=BOTTOM)


def find():
     
    text.tag_remove('found', '1.0', END)
    s = edit.get()
    if s:
        idx = '1.0'
        while 1:
            idx = text.search(s, idx, nocase=1,
                              stopindex=END)
            if not idx: break
            lastidx = '%s+%dc' % (idx, len(s))
            text.tag_add('found', idx, lastidx)
            idx = lastidx
        text.tag_config('found', foreground='red')
    edit.focus_set()
butt.config(command=find)
root.mainloop()