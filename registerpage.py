from tkinter import *

class RegisterPage:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x300+500+200")
        self.master.title("Register")
        self.master.configure(bg="#fff")
        self.master.resizable(False, False)

        Label(self.master, text="Register", font=("Microsoft YaHei UI Light", "16"), fg="blue").pack(pady=10)

        Label(self.master, text="Name:").pack()
        self.name_entry = Entry(self.master, width=30)
        self.name_entry.pack()

        Label(self.master, text="Email:").pack()
        self.email_entry = Entry(self.master, width=30)
        self.email_entry.pack()

        Label(self.master, text="Gender:").pack()
        self.gender_entry = Entry(self.master, width=30)
        self.gender_entry.pack()

        Label(self.master, text="Position:").pack()
        self.position = StringVar()
        Radiobutton(self.master, text="Manager", variable=self.position, value="Manager").pack()
        Radiobutton(self.master, text="Team Leader", variable=self.position, value="Team Leader").pack()
        Radiobutton(self.master, text="Employee", variable=self.position, value="Employee").pack()

        Button(self.master, text="Register", command=self.register).pack(pady=20)

    def register(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        gender = self.gender_entry.get()
        position = self.position.get()

        # Here you can add code to save the registration details to a file or database
        # For simplicity, let's just print the details for now
        print("Name:", name)
        print("Email:", email)
        print("Gender:", gender)
        print("Position:", position)


    root.mainloop()

RegisterPage()