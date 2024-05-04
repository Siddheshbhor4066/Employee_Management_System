from tkinter import *
from logout import logout

class ManagerDashboard:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("927x500+300+200")
        self.root.resizable(False, False)
        self.root.title("ceodashboard")
        self.root.configure(bg="white")

        self.pro_label = Label(self.root, text="My Profile", fg="blue", font=("Microsoft YaHei UI Light", "16"))
        self.emp_label = Label(self.root, text="Employee", fg="blue", font=("Microsoft YaHei UI Light", "16"))

        self.frame = Frame(self.root, width=900, height=50, bg="#76EE00", border=5)
        self.frame.place(x=15, y=5)
        Label(self.frame, text="Manager DASHBOARD", fg="red", bg="#76EE00", font=("Microsoft YaHei UI Light", "20")).place(x=350, y=5)

        # Vertical line left
        Frame(self.root, width=3, height=480, bg="#76EE00").place(x=15, y=5)

        # vertical line Right
        Frame(self.root, width=3, height=480, bg="#76EE00").place(x=914, y=5)

        # Horizontal line Bottom
        Frame(self.root, width=900, height=3, bg="#76EE00").place(x=15, y=482)

        self.show_profile_button = Button(self.root, text="Show Profile", width=20, bg="#76EE00", fg="blue", bd=0,
                             font=("Microsoft YaHei UI Light", "16"), command=self.profile)
        self.show_profile_button.place(x=100, y=100)

        self.teams_button = Button(self.root, text="Team", width=20, bg="#76EE00", fg="blue", bd=0,
                                   font=("Microsoft YaHei UI Light", "16"), command=self.teams)
        self.teams_button.place(x=100, y=200)

        self.Logout = Button(self.root, text="Logout", width=6, bg="black", fg="yellow", bd=0, font=("Microsoft YaHei UI Light", "10","bold"),command=lambda:logout(self.root))
        self.Logout.place(x=845,y=60)

    def profile(self):
        self.pro_label.place(x=550, y=100)
        self.emp_label.place_forget()


    def teams(self):
        self.emp_label.place(x=550, y=100)
        self.pro_label.place_forget()


