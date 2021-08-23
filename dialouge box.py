from tkinter import *
import datetime
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter import ttk
root = Tk()


def valid(char):
    if char.isdigit():
        return True
    elif char is str:
        return True
    else:
        return False
valid_num= (root.register(valid),'&P')



root.title("Vaccination Registration App")
root.option_add("*Tcombobox*Listbox*font","None 15 bold")
root.geometry("800x650+260+20")

def submit():
    Name = name.get()
    current_year= datetime.datetime.now().year
    DD=date.get()
    MM= month.get()
    YY=int(year.get())
    course = course.get()
    branch = branch.get()
    gender= gender.get()
    phone = phone.get()
    email = email.get()









def select(event):
    if course.get() == "B.Tech.":
        branch.config(value=Btech)
        branch.set("Select Branch")
    elif course.get() == "B.Sc.":
        branch.config(value=Bsc)
        branch.set("Select Branch")
    elif course.get() == "B.Com.":
        branch.config(value=Bcom)
        branch.set("Select Branch")
    elif course.get() == "B.A.":
        branch.config(value=Ba)
        branch.set("Select Branch")
    elif course.get() == "M.Tech.":
        branch.config(value=Mtech)
        branch.set("Select Branch")
    elif course.get() == "M.Sc.":
        branch.config(value=Msc)
        branch.set("Select Branch")
    elif course.get() == "M.Com.":
        branch.config(value=Mcom)
        branch.set("Select Branch")
    elif course.get() == "M.A.":
        branch.config(value=Ma)
        branch.set("Select Branch")









Label(root, text="Vaccination Registration ", font=("None 28 bold "), bg="tan2").place(x=115, y=50)
Label(root, text="Beneficiary Name:", font=("lucida 25 bold"), bg="tan2").place(x=130, y=130)
Label(root, text="DOB:", font=("lucida 25 bold"), bg="tan2").place(x=130, y=180)
Label(root, text="Vaccine Name:", font=("lucida 25 bold"), bg="tan2").place(x=130, y=230)
Label(root, text="Gender:", font=("lucida 25 bold"), bg="tan2").place(x=130, y=280)
Label(root, text="Phone:", font=("lucida 25 bold"), bg="tan2").place(x=130, y=330)
Label(root, text="Email:", font=("lucida 25 bold"), bg="tan2").place(x=130, y=380)
Label(root, text="Dose Round:", font=("lucida 25 bold"), bg="tan2").place(x=130, y=430)





date = [i for i in range(1, 32)]
date = ttk.Combobox(root, value=date, font=("lucida 20 bold"), state="readonly", width=3)
date.set("1")
date.place(x=320, y=185, width=65, height=40)

month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
         "December"]
month = ttk.Combobox(root, value=month, font=("lucida 20 bold"), state="readonly", width=12)
month.set("January")
month.place(x=390, y=185, width=185, height=40)

year = [i for i in range(1932, 2022)]
year = ttk.Combobox(root, value=year, font=("lucida 20 bold"), state="readonly", width=6)
year.set("2001")
year.place(x=580, y=185, width=100, height=40)

std = ["COVID SHIELS", "COVAXIN"]
course = ttk.Combobox(root, value=std, font=("arial 12 bold"), state="readonly")
course.set("SELECT VACCINE NAME")
course.place(x=380, y=235, width=250, height=40)
course.bind("<<ComboboxSelected>>", select)




gender =["MALE", "FEMALE"]
branch = ttk.Combobox(root, value=gender, font=("lucida 12 bold"), state="readonly")
branch.set("Select Gender")
branch.place(x=320, y=285, width=300)




root.mainloop()