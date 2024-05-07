from tkinter import *
from tkinter import messagebox
import pandas as pd
from Ceodashboard import Ceodashboard
from Hrdashboard import HRDashboard
from Manager import ManagerDashboard
from signup import signup


class LoginPage:
    def __init__(self, master):
        self.master = master
        self.master.geometry("927x500+300+200")
        self.master.title("Login")
        self.master.configure(bg="#fff")
        self.master.resizable(False, False)
        self.master.iconbitmap("login.ico")

        self.img = PhotoImage(file="login.png")
        Label(self.master, image=self.img, bg="white").place(x=50, y=50)



        self.frame = Frame(self.master, width=400, height=380, bg="white")
        self.frame.place(x=500, y=70)

        Label(self.frame, text="Sign in", font=("Microsoft YaHei UI Light", "16"), fg="blue").place(x=155, y=10)

        def on_enter(e):
            self.user.delete(0, 'end')

        def on_leave(e):
            if self.user.get() == "":
                self.user.insert(0, "Username")

        self.user = Entry(self.frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", "11"))
        self.user.place(x=100, y=100)
        self.user.insert(0, "username")
        self.user.bind("<FocusIn>", on_enter)
        self.user.bind("<FocusOut>", on_leave)

        Frame(self.frame, width=200, height=2, bg="black").place(x=100, y=122)

        def on_enter(e):
            self.password.delete(0, 'end')

        def on_leave(e):
            if self.password.get() == "":
                self.password.insert(0, "Password")

        self.password = Entry(self.frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", "11"),
                         show="*")
        self.password.place(x=100, y=150)

        Frame(self.frame, width=200, height=2, bg="black").place(x=100, y=172)
        self.password.insert(0, "Password")
        self.password.bind("<FocusIn>", on_enter)
        self.password.bind("<FocusOut>", on_leave)

        self.roles = ["CEO", "HR", "Manager", "Team Leader", "Employee"]
        self.role_var = StringVar(master)
        self.role_var.set("Position")  # Default value
        self.role_dropdown = OptionMenu(self.frame, self.role_var, *self.roles)
        self.role_dropdown.config(width=15, font=("Microsoft YaHei UI Light", "11"))
        self.role_dropdown.place(x=100, y=200)

        self.Login = Button(self.frame, text="Login", fg="Blue", font=("Microsoft YaHei UI Light", "11"), command=self.login)
        self.Login.place(x=100, y=250)

        Label(self.frame, text="I Don't have an account !", bg="white", fg="black", font=("Microsoft YaHei UI Light", "8")).place(x=100, y=295)
        self.signup = Button(self.frame, text="Sign up", bg="white", fg="blue", bd=0, font=("Microsoft YaHei UI Light", "8"), command=lambda:signup())
        self.signup.place(x=235, y=295)

    def login(self):
        username = self.user.get()
        password = self.password.get()
        role = self.role_var.get()

        if any([not username, not password, role == "Position"]):
            messagebox.showerror("Error", "Please fill all fields")
            return
            
        try:
            df = pd.read_excel("users.xlsx")
            
            if (df["Username"] == username).any() and (df["Password"] == password).any() and (df["Designation"] == role).any():
                self.username = username  # Store the username
                if role == "CEO":
                    self.master.destroy()
                    ceo_dash = Ceodashboard(self.username)
                    ceo_dash
                elif role == "HR":
                    self.master.destroy()
                    hr_dash = HRDashboard(self.username)  # Pass username to HRDashboard
                    hr_dash
                elif role == "Manager":
                    self.master.destroy()
                    manager_dash = ManagerDashboard(self.username)
                    manager_dash
                elif role == "Team Leader":
                    self.master.destroy()
                else:
                    messagebox.showerror("Error", "Invalid Username or Password")
            else:
                messagebox.showerror("Error", "No users registered. Please sign up.")
        except FileNotFoundError:
            messagebox.showerror("Error", "No users registered. Please sign up.")
            
def main():
    root = Tk()
    login_page = LoginPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()

