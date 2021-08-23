from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import datetime

root = Tk()
root.title("STUDENT REGISTRATION FORM")
root.option_add("*Tcombobox*Listbox*font","None 15 bold")
root.geometry("800x650+260+20")
root.resizable(0,0)

def valid(char):
    if char.isdigit():
        return True
    elif char is str:
        return True
    else:
        return False
valid_num= (root.register(valid),'&P')

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


    file1 = open(f"C:/Users/KCK/PycharmProjects/pythonProject19_tkinter/{Name}.txt","w")
    file1.write("\n\n")


    if (Name==""):
        msg.showerror("Missing Data","Please enter you name.")
    else:
        file1.write("\t\tName :"+ Name +"\n\n")

    if (YY==current_year or YY==current_year-1 or YY==current_year-2 or DD== current_year-3 or DD==current_year-4):
        msg.showerror("Invalid Data","Please enter correct birth year")
    else:
        file1.write("\t\tDOB :" +DD + "-"+ MM + "-"+ str(YY) + "\n\n" )

    if (course == "Select Course" or branch == "Select Branch"):
        msg.showerror("Missing Data", "Please select a Course or Branch.")
    else:
        file1.write("\t\tCourse  :  " + course + "\n\n")
        file1.write("\t\tBranch  :  " + branch + "\n\n")

    if (gender == 1):
        file1.write("\t\tGender  :  " + "Male" + "\n\n")
    elif (gender == 2):
        file1.write("\t\tGender  :  " + "Female" + "\n\n")
    else:
        msg.showerror("Missing Data", "Please select your Gender.")

        # Write Phone in Text File
    if (phone == ""):
        msg.showerror("Missing Data", "Please Enter Your Phone Number.")
    else:
        file1.write("\t\tPhone   :  " + "+91" + " " + phone + "\n\n")

        # Write Email in Text File
    if (email == ""):
        msg.showerror("Missing Data", "Please Enter Your Name.")
    else:
        file1.write("\t\tEmail   :  " + email + "\n\n")

        # Close Text File
    file1.close()

    # Check if Password is Not Empty So it will Display Congrats Message
    if (password.get() != "" and Name != "" and (YY < current_year - 4) and (
            course != "Select Course" or branch != "Select Branch") and
            ((gender == 1) or (gender == 2)) and phone != "" and email != ""):
        msg.showinfo("Congratulation", "You Registered Successfully!")


# Create a Function to Reset All the Entry
def reset():
    Entry(root, validate="key", validatecommand=valid_num,
          font=("lucida 22 bold"), bd=2).place(x=380, y=385, width=300)
    name.set("")
    date.set("1")
    month.set("January")
    year.set("2021")
    gender.set(Boy.deselect())
    gender.set(Girl.deselect())
    course.set("Select Course")
    branch.set("Select Branch")
    phone.set("")
    email.set("")
    password.set("")


# Create a Function to make dependent Course and Branch section to  Each Other
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


# Crete a PanedWindow for all the Entries
PanedWindow(root, width=620, height=600, bg="tan2", relief=GROOVE, bd=10).place(x=100, y=30)

# Make Labels for Every Entry
Label(root, text="STUDENT REGISTRATION FORM", font=("None 28 bold "), bg="tan2").place(x=115, y=50)
Label(root, text="Name:", font=("lucida 25 bold"), bg="tan2").place(x=130, y=130)
Label(root, text="DOB:", font=("lucida 25 bold"), bg="tan2").place(x=130, y=180)
Label(root, text="Course:", font=("lucida 25 bold"), bg="tan2").place(x=130, y=230)
Label(root, text="Branch:", font=("lucida 25 bold"), bg="tan2").place(x=130, y=280)
Label(root, text="Gender:", font=("lucida 25 bold"), bg="tan2").place(x=130, y=330)
Label(root, text="Phone:", font=("lucida 25 bold"), bg="tan2").place(x=130, y=380)
Label(root, text="Email:", font=("lucida 25 bold"), bg="tan2").place(x=130, y=430)
Label(root, text="Password:", font=("lucida 25 bold"), bg="tan2").place(x=130, y=480)

# Entry for Name
name = StringVar()
Entry(root, textvariable=name, font=("lucida 22 bold"), bd=2).place(x=320, y=135, width=360)

#  It gives the Options to Select Dates from 1 to 31 in the Date Entry
date = [i for i in range(1, 32)]
date = ttk.Combobox(root, value=date, font=("lucida 20 bold"), state="readonly", width=3)
date.set("1")
date.place(x=320, y=185, width=65, height=40)

#  It gives the Options to Select Month in the Month Entry
month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
         "December"]
month = ttk.Combobox(root, value=month, font=("lucida 20 bold"), state="readonly", width=12)
month.set("January")
month.place(x=390, y=185, width=185, height=40)

# It gives the Options to Select Year in the Year Entry
year = [i for i in range(1981, 2022)]
year = ttk.Combobox(root, value=year, font=("lucida 20 bold"), state="readonly", width=6)
year.set("2021")
year.place(x=580, y=185, width=100, height=40)

# It gives the Options to Select Course in the Course Entry
std = ["B.Tech.", "B.Sc.", "B.Com.", "B.A.", "M.Tech.", "M.Sc.", "M.Com.", "M.A."]
course = ttk.Combobox(root, value=std, font=("lucida 22 bold"), state="readonly")
course.set("Select Course")
course.place(x=320, y=235, width=250, height=40)
course.bind("<<ComboboxSelected>>", select)

# It gives the Options to Select Branch in the Branch Entry
Btech = Mtech = ["Computer Science", "Information Technology", "Electronic & Communications", "Biotechnology",
                 "Electrical", "Mechanical"]
Bsc = Msc = ["Computer Science", "Mathematics", "Biology", "Statics"]
Bcom = Mcom = ["Accounts & Finance", "Banking & Insurance", "Marketing", "Economics"]
Ba = Ma = ["Political Science", "English", "History", "Psychology", "Philosophy", "Economics", "Sociology", "Geography"]

# Creata a ComboxBox for Branch Entry
branch = ttk.Combobox(root, value=[" "], font=("lucida 22 bold"), state="readonly")
branch.set("Select Branch")
branch.place(x=320, y=285, width=300)

# Create Gender Entry to Specify the Student Gender
gender = IntVar()
Boy = Radiobutton(root, text="Male", variable=gender, value=1, font=("lucida 22 bold"), bg="tan2",
                  activebackground="tan2")
Boy.place(x=350, y=335)
Girl = Radiobutton(root, text="Female", variable=gender, value=2, font=("lucida 22 bold"), bg="tan2",
                   activebackground="tan2")
Girl.place(x=500, y=335)

# Create a Country Code Entry
code = IntVar()
Entry(root, text=code, font=("lucida 22 bold"), state="readonly", bd=2).place(x=320, y=385, width=55)
code.set("+91")

# Create a Phone No. Entry
phone = StringVar()
Entry(root, textvariable=phone, validate="key", validatecommand=valid_num, font=("lucida 22 bold"),
      bd=2).place(x=380, y=385, width=300)

# Create a Email Entry
email = StringVar()
Entry(root, textvariable=email, font=("lucida 22 bold"), bd=2).place(x=320, y=435, width=360)

# Create a Password Entry
password = StringVar()
Entry(root, textvariable=password, font=("lucida 22 bold"), bd=2, show="*").place(x=320, y=485, width=360)

# Button for Reset Entry Data
Button(root, text="Reset", font=("lucida 22 bold"), command=reset, bg="yellow3",
       activebackground="darksalmon", bd=5).place(x=170, y=545)

# Button for Cancel Entry Data
Button(root, text="Cancel", font=("lucida 22 bold"), command=quit, bg="indianred1",
       activebackground="darksalmon", bd=5).place(x=340, y=545)

# Button for Submit Entry Data
Button(root, text="Submit", font=("lucida 22 bold"), command=submit, bg="lawngreen",
       activebackground="chartreuse3", bd=5).place(x=520, y=545)

# Close the Root Window
root.mainloop()






