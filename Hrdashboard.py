from tkinter import *


class HRDashboard:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("927x500+300+200")
        self.root.resizable(False, False)
        self.root.title("HR Dashboard")
        self.root.configure(bg="white")

        self.pro = Label(self.root, text="My Profile", fg="blue", font=("Microsoft YaHei UI Light", "16"))
        self.emp = Label(self.root, text="Employee", fg="blue", font=("Microsoft YaHei UI Light", "16"))

        self.frame = Frame(self.root, width=900, height=50, bg="#76EE00", border=5)
        self.frame.place(x=15, y=5)
        Label(self.frame, text="HR DASHBOARD", fg="red", bg="#76EE00", font=("Microsoft YaHei UI Light", "20")).place(x=350, y=5)

        # Vertical line left
        l1 = Frame(self.root, width=3, height=480, bg="#76EE00").place(x=15, y=5)

        # Vertical line Right
        l2 = Frame(self.root, width=3, height=480, bg="#76EE00").place(x=914, y=5)

        # Horizontal line Bottom
        l3 = Frame(self.root, width=900, height=3, bg="#76EE00").place(x=15, y=482)

        self.showprofile = Button(self.root, text="Show Profile", width=20, bg="#76EE00", fg="blue", bd=0, font=("Microsoft YaHei UI Light", "16"), command=self.profile)
        self.showprofile.place(x=100, y=100)

        self.EmployeeDirectory = Button(self.root, text="Employee Directory", width=20, bg="#76EE00", fg="blue", bd=0, font=("Microsoft YaHei UI Light", "16"), command=self.employeedirectory)
        self.EmployeeDirectory.place(x=100, y=200)

        self.AddEmployee = Button(self.root, text=" Add Employee", width=20, bg="#76EE00", fg="blue", bd=0, font=("Microsoft YaHei UI Light", "16"))
        self.AddEmployee.place(x=100, y=300)

        

    def profile(self):
        self.emp.place_forget()  # Hide employee label
        self.pro.place(x=550, y=100)  # Place profile label

    def employeedirectory(self):
        self.pro.place_forget()  # Hide profile label
        self.emp.place(x=550, y=100)  # Place employee label

    

        




