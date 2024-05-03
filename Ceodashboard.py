from tkinter import *
def Ceodashboard():
    root = Tk()
    root.geometry("927x500+300+200")
    root.resizable(False,False)
    root.title("ceodashboard")
    root.configure(bg="white")

    pro = Label(root, text="My Profile", fg="blue", font=("Microsoft YaHei UI Light", "16"))
    emp = Label(root, text="Employee", fg="blue", font=("Microsoft YaHei UI Light", "16"))


    def profile():
        pro.place_forget()
        pro.place(x=550,y=100)
    

    def employeedirectory():
        emp.place_forget()
        emp.place(x=550,y=100)



    frame = Frame(root,width=900,height=50,bg="#76EE00",border=5).place(x=15,y=5)
    Label(frame,text="CEO DASHBOARD",fg="red",bg="#76EE00",font=("Microsoft YaHei UI Light", "20")).place(x=350,y=5)

    #Vertical line left
    l1 = Frame(root,width=3,height=480,bg="#76EE00").place(x=15,y=5)

    #vertical line Right
    l2 = Frame(root,width=3,height=480,bg="#76EE00").place(x=914,y=5)

    #Horizontal line Bottom
    l3 = Frame(root,width=900,height=3,bg="#76EE00").place(x=15,y=482)

    showprofile = Button(root,text="Show Profile",width=20,bg="#76EE00",fg="blue",bd=0,font=("Microsoft YaHei UI Light", "16"),command=profile)
    showprofile.place(x=100,y=100)

    EmployeeDirectory = Button(root,text="Employee Directory",width=20,bg="#76EE00",fg="blue",bd=0,font=("Microsoft YaHei UI Light", "16"),command=employeedirectory)
    EmployeeDirectory.place(x=100,y=200)
    root.mainloop()

