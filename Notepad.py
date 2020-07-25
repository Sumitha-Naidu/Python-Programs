from tkinter import  *
from tkinter.filedialog import *
import os

font_type=("Arial", "Roboto", "Times New Roman", "Times", "Courier New", "Courier", "Verdand", "Georgia", "Palation", "Garamond", "Bookman", "Comic Sans MS", "Candara", "Arial Black", "Impact")
font_style = ( "","bold", "italic", "underline")
root = Tk()
root.title("Notepad")
root.geometry("450x600")

font = "lucida"
size = "18"
style = ""

Font = "lucida"
Size = "18"
Style = ""

mainfile = None

class Notepad:
    mainfile=None
    def apply(self):
        global font
        global size
        global style
        print(f"{font}, {size}")
        Textarea.update()

    #MainMenu Function
       #File Menu
    def New(self):
        root.title("Untitled Notepad")
        self.mainfile = None
        Textarea.delete("1.0",END)

    def Open(self):
        self.mainfile = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if self.mainfile == "":
            # no file to open
            self.mainfile = None
        else:
            # Try to open the file
            # set the window title
            root.title(os.path.basename(self.mainfile) + " - Notepad")
            Textarea.delete("1.0",END)
            file1 = open(self.mainfile,"r")
            Textarea.insert(1.0,file1.read())
            file1.close()

    def Save(self):
        if self.mainfile == None:
            # Save as new file
            self.mainfile = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
            if self.mainfile == "":
                self.mainfile = None
            else:
                # Try to save the file
                file1 = open(self.mainfile,"w")
                file1.write(Textarea.get("1.0",END))
                file1.close()
                # Change the window title
                root.title(os.path.basename(self.mainfile) + " - Notepad")
        else:
            file1 = open(self.mainfile,"w")
            file1.write(Textarea.get("1.0",END))
            file1.close()

    def Quit(self):
        root.destroy()

        #Edit Menu
    '''def copy():
        Textarea.event_generate(("<<Copy>>"))

    def cut():
        Textarea.event_generate(("<<Cut>>"))

    def paste():
        Textarea.event_generate(("<<Paste>>"))
    '''
    def Config(self):
        A2 = Toplevel(root)
        A2.geometry("450x600")
        A2.configure(bg = "#d0d0d0")
        Label(A2, text="Notepad Config", font="lucida 16 italic", bg="#d0d0d0").grid(row = 0, column = 2)
        Label(A2, text="Font Type :", font="lucida 16 italic", bg="#d0d0d0").grid(row = 1, column = 1)
        Label(A2, text="Font Size :", font="lucida 16 italic", bg="#d0d0d0").grid(row = 2, column = 1)
        Label(A2, text="Font Style :", font="lucida 16 italic", bg="#d0d0d0").grid(row = 3, column = 1)
        Spinbox(A2, values = font_type, textvariable = font).grid(row = 1, column = 2)
        Spinbox(A2, from_=0, to=72, textvariable = size).grid(row = 2, column = 2)
        Spinbox(A2, values = font_style, textvariable = style).grid(row = 3, column = 2)
        Button(A2, text="Apply", command = apply).grid(row = 9, column = 2)

        #Help Menu
    def About_us(self):
        A1 = Toplevel(root)
        A1.geometry("600x250")
        A1.title("About Us")
        Label(A1, text="This Notepad is Created by:- ", font="lucida 16 bold").pack()
        Label(A1, text="unknown", font="lucida 16 bold").pack()
        Label(A1, text="With the help of:-", font="lucida 16 bold").pack()
        Label(A1, text="Python 3 and Tkinter ", font="lucida 16 bold").pack()
#MainMenu Setup
MainMenu = Menu(root)
n = Notepad()
m1 = Menu(MainMenu, tearoff = 0)
m1.add_command(label="New", command = n.New)
m1.add_command(label="Open", command = n.Open)
m1.add_command(label="Save", command = n.Save)
m1.add_separator()
m1.add_command(label="Quit", command = n.Quit)

root.configure(menu = MainMenu)
MainMenu.add_cascade(label = "File", menu = m1)

m1 = Menu(MainMenu, tearoff = 0)
m1.add_command(label="Config", command = Config)
'''m1.add_separator()
m1.add_command(label="Copy", command = copy)
m1.add_command(label="Cut", command = cut)
m1.add_command(label="Paste", command = paste)
'''
root.configure(menu = MainMenu)
MainMenu.add_cascade(label = "Edit", menu = m1)

m1 = Menu(MainMenu, tearoff = 0)
m1.add_command(label="About Us", command = n.About_us)

root.configure(menu = MainMenu)
MainMenu.add_cascade(label = "Help", menu = m1)

#textarea setup
Textarea=Text(root, font=f"{(font) or (Font)} {(size) or (Size)} {(style) or (Style)} ")
Textarea.pack(expand = True, fill = BOTH)

#font setup
font = StringVar()
size = StringVar()
style = StringVar()

root.mainloop()