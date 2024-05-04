from tkinter import *
from tkinter import messagebox
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

        self.frame = Frame(self.master, width=380, height=300, bg="white")
        self.frame.place(x=500, y=70)

        Label(self.frame, text="Sign in", font=("Microsoft YaHei UI Light", "16"), fg="blue").place(x=155, y=10)

######------------------------------------------------------------------------------------------------------------
        def on_enter(e):
            self.user.delete(0,'end')

        def on_leave(e):
            if self.user.get() == "":
                self.user.insert(0,"Username")

        self.user = Entry(self.frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", "11"))
        self.user.place(x=100, y=100)
        self.user.insert(0, "username")
        self.user.bind("<FocusIn>",on_enter)
        self.user.bind("<FocusOut>",on_leave)

        Frame(self.frame, width=200, height=2, bg="black").place(x=100, y=122)

#####------------------------------------------------------------------------------------------------------------------


        def on_enter(e):
            self.password.delete(0,'end')

        def on_leave(e):
            if self.password.get() == "":
                self.password.insert(0,"Password")

        self.password = Entry(self.frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", "11"),
                         show="*")
        self.password.place(x=100, y=150)

        Frame(self.frame, width=200, height=2, bg="black").place(x=100, y=172)
        self.password.insert(0, "Password")
        self.password.bind("<FocusIn>",on_enter)
        self.password.bind("<FocusOut>",on_leave)

#####----------------------------------------------------------------------------------------------------------------------

        self.Login = Button(self.frame, text="Login", fg="Blue", font=("Microsoft YaHei UI Light", "11"), command=self.login)
        self.Login.place(x=100, y=200)

#####----------------------------------------------------------------------------------------------------------------------

        Label(self.frame,text="I Don't have an account !",bg="white",fg="black",font=("Microsoft YaHei UI Light", "8")).place(x=100,y=245)

#####-----------------------------------------------------------------------------------------------------------------------
        self.signup = Button(self.frame,text="Sign up",bg="white",fg="blue",bd=0,font=("Microsoft YaHei UI Light", "8"),command=lambda:signup(self.master))
        self.signup.place(x=235,y=245)

#####--------------------------------------------------------------------------------------------------------------------------

    def login(self):
        username = self.user.get()
        password_value = self.password.get()  

        if username == "ceo" and password_value == "ceo123":  
            self.master.destroy()
            ceo_dashboard = Ceodashboard()
            ceo_dashboard

        elif username == "hr" and password_value == "hr123":
            self.master.destroy()
            hr_dashboard = HRDashboard()
            hr_dashboard

        elif username == "manager" and password_value =="manager123":
            self.master.destroy()
            manager_db = ManagerDashboard()
            manager_db
            
        else:
            messagebox.showerror("Error","Please fill correct Username and Password")
            return
        
    


def main():
    root = Tk()
    login_page = LoginPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
