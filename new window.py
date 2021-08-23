from tkinter import *
from PIL import ImageTk,Image

root = Tk()

root.title("New Window")




def window():
    global my_image
    top = Toplevel()
    top.title("my secod window")
    my_image = ImageTk.PhotoImage(Image.open("instagram.jpg"))
    my_label = Label(top, image= my_image).pack()
    btn_2 = Button(top , text = "Close",command = top.destroy).pack()


btn = Button(root, text="open my second window",command = window).pack()

root.mainloop()


