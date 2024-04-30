from tkinter import *
root = Tk()

root.geometry("927x500+300+200")
root.title("Login")
root.configure(bg="#fff")
root.resizable(False,False)
root.iconbitmap("login.ico")

img = PhotoImage(file="login.png")
Label(root,image=img,bg="white").place(x=50,y=50)

frame = Frame(root,width=380,height=300,bg="white")
frame.place(x=500,y=70)

Label(frame,text="Sign in",font=("Microsoft YaHei UI Light","16"),fg="blue").place(x=155,y=10)

user = Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light", "11"))
user.place(x=100,y=100)
user.insert(0,"username")

Frame(frame,width=200,height=2,bg="black").place(x=100,y=122)

password = Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light", "11"),show="*")
password.place(x=100,y=150)

Frame(frame,width=200,height=2,bg="black").place(x=100,y=172)
password.insert(0,"Password")

Login = Button(frame,text="Login",fg="Blue",font=("Microsoft YaHei UI Light", "11"))
Login.place(x=100,y=200)

root.mainloop()