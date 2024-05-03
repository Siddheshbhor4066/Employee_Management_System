from tkinter import *
from Ceodashboard import Ceodashboard
from Hrdashboard import hrdashboard
from Manager import Managerdashboard
from TLeader import TLeader
from employee import Employee

class RegisterPage:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x300+500+200")
        self.master.title("Register")
        self.master.configure(bg="#fff")
        self.master.resizable(False, False)

        self.name_label = Label(self.master, text="Name:")
        self.name_label.pack()
        self.name_entry = Entry(self.master, width=30)
        self.name_entry.pack()

        self.email_label = Label(self.master, text="Email:")
        self.email_label.pack()
        self.email_entry = Entry(self.master, width=30)
        self.email_entry.pack()

        self.gender_label = Label(self.master, text="Gender:")
        self.gender_label.pack()
        self.gender = StringVar()
        Radiobutton(self.master, text="Male", variable=self.gender, value="Male").pack()
        Radiobutton(self.master, text="Female", variable=self.gender, value="Female").pack()

        self.position_label = Label(self.master, text="Position:")
        self.position_label.pack()
        self.position = StringVar()
        Radiobutton(self.master, text="Manager", variable=self.position, value="Manager").pack()
        Radiobutton(self.master, text="Team Leader", variable=self.position, value="Team Leader").pack()
        Radiobutton(self.master, text="Employee", variable=self.position, value="Employee").pack()

        self.register_button = Button(self.master, text="Register", command=self.register)
        self.register_button.pack(pady=20)

    def register(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        gender = self.gender.get()
        position = self.position.get()

        # Here you can add code to save the registration details to a file or database
        # For simplicity, let's just print the details for now
        print("Name:", name)
        print("Email:", email)
        print("Gender:", gender)
        print("Position:", position)

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

        self.frame = Frame(self.master, width=380, height=300, bg="white")
        self.frame.place(x=500, y=70)

        Label(self.frame, text="Sign in", font=("Microsoft YaHei UI Light", "16"), fg="blue").place(x=155, y=10)

        self.user = Entry(self.frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", "11"))
        self.user.place(x=100, y=100)
        self.user.insert(0, "username")

        Frame(self.frame, width=200, height=2, bg="black").place(x=100, y=122)

        self.password = Entry(self.frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", "11"),
                              show="*")
        self.password.place(x=100, y=150)

        Frame(self.frame, width=200, height=2, bg="black").place(x=100, y=172)
        self.password.insert(0, "Password")

        self.Login = Button(self.frame, text="Login", fg="Blue", font=("Microsoft YaHei UI Light", "11"),
                            command=self.login)
        self.Login.place(x=100, y=200)

        self.Register = Button(self.frame, text="Register", fg="Blue", font=("Microsoft YaHei UI Light", "11"),
                               command=self.open_register_page)
        self.Register.place(x=100, y=250)

        self.master.tkraise()

    def login(self):
        username = self.user.get()
        password_value = self.password.get()  # Rename the variable to password_value

        if username == "ceo" and password_value == "ceo123":  # Use password_value instead of password
            self.master.destroy()
            Ceodashboard()

        elif username == "hr" and password_value == "hr123":
            self.master.destroy()
            hrdashboard()

        elif username == "manager" and password_value == "m123":
            self.master.destroy()
            Managerdashboard()

        elif username == "tl" and password_value == "tl123":
            self.master.destroy()
            TLeader()

        elif username == "em" and password_value == "e123":
            self.master.destroy()
            Employee()

    def open_register_page(self):
        register_window = Toplevel(self.master)
        register_page = RegisterPage(register_window)

def main():
    root = Tk()
    login_page = LoginPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
