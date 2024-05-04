from tkinter import *


def signup(root):
    root.destroy()

    root = Tk()
    root.title("Signup")
    root.geometry("600x500")
    root.resizable(False,False)
    root.config(bg="#BF3EFF")


    frame = Frame(root, width=450, height=300, bg="white")
    frame.pack(pady=30)

    Email = Label(frame,text="Email",width=15,height=1,bd=0,bg="white",fg="black",font=("Microsoft YaHei UI Light", "14"))
    Email.place(x=60,y=10)

    Email_entry = Entry(frame, width=20,fg="black", border=3, bg="white", font=("Microsoft YaHei UI Light", "11"))
    Email_entry.place(x=250, y=10)
#####--------------------------------------------------------------------------------------------------------------------------------
    User = Label(frame,text="Username",width=15,height=1,bd=0,bg="white",fg="black",font=("Microsoft YaHei UI Light", "14"))
    User.place(x=60,y=60)

    User_entry = Entry(frame, width=20,fg="black", border=3, bg="white", font=("Microsoft YaHei UI Light", "11"))
    User_entry.place(x=250, y=60)
#####--------------------------------------------------------------------------------------------------------------------------------
    password = Label(frame,text="Password",width=15,height=1,bd=0,bg="white",fg="black",font=("Microsoft YaHei UI Light", "14"))
    password.place(x=60,y=110)

    password_entry = Entry(frame, width=20,fg="black", border=3, bg="white", font=("Microsoft YaHei UI Light", "11"))
    password_entry.place(x=250, y=110)

    conf_password = Label(frame,text="Confirm Password",width=15,height=1,bd=0,bg="white",fg="black",font=("Microsoft YaHei UI Light", "14"))
    conf_password.place(x=60,y=160)

    confpassword_entry = Entry(frame, width=20,fg="black", border=3, bg="white", font=("Microsoft YaHei UI Light", "11"))
    confpassword_entry.place(x=250, y=160)

    signup_bt = Button(frame,text="Sign Up",fg="Blue",bg="black",font=("Microsoft YaHei UI Light", "8"))
    signup_bt.place(x=300,y=230)
    
