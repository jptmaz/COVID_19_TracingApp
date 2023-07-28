import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
 
 
class TextboxApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Text Editor")
        self.window.geometry("800x600")
 
        # Create a menu bar
        self.menuBar = tk.Menu(self.window)
 
        # Create the File menu
        self.fileMenu = tk.Menu(self.menuBar, tearoff=0)
        self.fileMenu.add_command(label="New", command=self.newFile)
        self.fileMenu.add_command(label="Open", command=self.openFile)
        self.fileMenu.add_command(label="Save", command=self.saveFile)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.window.quit)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
 
        # Create the Edit menu
        self.editMenu = tk.Menu(self.menuBar, tearoff=0)
        self.editMenu.add_command(label="Cut", command=self.cut)
        self.editMenu.add_command(label="Copy", command=self.copy)
        self.editMenu.add_command(label="Paste", command=self.paste)
        self.menuBar.add_cascade(label="Edit", menu=self.editMenu)
 
        # Add the menu bar to the window
        self.window.config(menu=self.menuBar)
 
        # Create a scrolled text widget
        self.textArea = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, font=("Helvetica", 12))
        self.textArea.pack(fill=tk.BOTH, expand=True)
 
    def newFile(self):
        self.textArea.delete("1.0", tk.END)
 
    def openFile(self):
        filePath = tk.filedialog.askopenfilename()
        with open(filePath, "r") as file:
            fileContents = file.read()
            self.textArea.delete("1.0", tk.END)
            self.textArea.insert(tk.END, fileContents)
 
    def saveFile(self):
        filePath = tk.filedialog.asksaveasfilename(defaultextension=".txt")
        with open(filePath, "w") as file:
            fileContents = self.textArea.get("1.0", tk.END)
            file.write(fileContents)
 
    def cut(self):
        self.textArea.event_generate("<<Cut>>")
 
    def copy(self):
        self.textArea.event_generate("<<Copy>>")
 
    def paste(self):
        self.textArea.event_generate("<<Paste>>")
 
 
if __name__ == '__main__':
    window = tk.Tk()
    TextboxApp(window)
    window.mainloop()