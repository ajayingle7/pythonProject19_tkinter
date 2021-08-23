from tkinter import *


root = Tk()
root.title("my app")
r = IntVar()
r.set("2")


MODES = [
    ("HELLO","HELLO"),
    ("HI","HI"),
    ("HEY","HEY"),
    ("HIII","HIII")
]
pizza = StringVar()
pizza.get()
for text,mode in MODES:
    Radiobutton(root,text=text,variable = pizza,value= mode).pack()


def clicked(value):
    mylabel = Label(root, text=value)
    mylabel.pack()


#Radiobutton(root,text = "Option_1",variable = r,value = 1, command = lambda :clicked(r.get())).pack()
#Radiobutton(root,text = "optin_2",variable = r, value = 2,command = lambda :clicked(r.get())).pack()

mylabel= Label(root,text = r.get())
mylabel.pack()

mybutton = Button(root,text = "clic me",command = lambda :clicked(pizza.get()))
mybutton.pack()







root.mainloop()