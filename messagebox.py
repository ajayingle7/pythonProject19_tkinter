from tkinter import *
from PIL import ImageTk,Image
from tkinter import  messagebox

root = Tk()
root.title("Message Box")

def popup():
    message=messagebox.askquestion("this is  my popup","helo world")
    Label(root,text=message).pack()
    if message=="yes":
        Label(root,text = "You clicked Yes").pack()
    else:
        Label(root,text = "You clicked no ").pack()

def show():
    messagebox.showinfo("hello","hi guys")



Button(root,text = "popup", command = popup).pack()
Button(root,text = "click", command = show).pack()

root.mainloop()