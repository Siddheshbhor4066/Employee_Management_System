from tkinter import *


def signup(root):
    root.destroy()
    
    root = Tk()
    root.title("Signup")
    root.geometry("600x300")
    root.resizable(False,False)
    root.config(bg="white")


    frame = Frame(root, width=450, height=250, bg="white")
    frame.pack(pady=30)

    user = Label(frame,text="Username",width=15,height=1,bd=0,bg="white",fg="black",font=("Microsoft YaHei UI Light", "14"))
    user.place(x=60,y=10)

    user_entry = Entry(frame, width=20,fg="black", border=3, bg="white", font=("Microsoft YaHei UI Light", "11"))
    user_entry.place(x=250, y=10)

    new_pass = Label(frame,text="New Password",width=15,height=1,bd=0,bg="white",fg="black",font=("Microsoft YaHei UI Light", "14"))
    new_pass.place(x=60,y=60)

    newpass_entry = Entry(frame, width=20,fg="black", border=3, bg="white", font=("Microsoft YaHei UI Light", "11"))
    newpass_entry.place(x=250, y=60)

    conf_pass = Label(frame,text="confirm  Password",width=15,height=1,bd=0,bg="white",fg="black",font=("Microsoft YaHei UI Light", "14"))
    conf_pass.place(x=60,y=110)

    confpass_entry = Entry(frame, width=20,fg="black", border=3, bg="white", font=("Microsoft YaHei UI Light", "11"))
    confpass_entry.place(x=250, y=110)
