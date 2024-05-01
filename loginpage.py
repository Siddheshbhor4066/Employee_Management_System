from tkinter import *
from Ceodashboard import Ceodashboard
from Hrdashboard import hrdashboard



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

        self.Login = Button(self.frame, text="Login", fg="Blue", font=("Microsoft YaHei UI Light", "11"), command=lambda:self.login.tkraise())
        self.Login.place(x=100, y=200)

    def login(self):
        username = self.user.get()
        password_value = self.password.get()  # Rename the variable to password_value

        if username == "ceo" and password_value == "ceo123":  # Use password_value instead of password
            self.master.destroy()
            Ceodashboard()

        elif username == "hr" and password_value == "hr123":
            self.master.destroy()
            hrdashboard()


def main():
    root = Tk()
    login_page = LoginPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
