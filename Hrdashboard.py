from tkinter import *
from tkinter import messagebox, ttk
from logout import logout
import pandas as pd
from AddEmployee import addemployee


class HRDashboard:
    def __init__(self, username):
        self.username = username  # Store the username passed from LoginPage

        self.root = Tk()
        self.root.geometry("927x500+300+200")
        self.root.resizable(False, False)
        self.root.title("HR Dashboard")
        self.root.configure(bg="white")

        self.pro = Label(self.root, text="My Profile",bd =0,bg = "white", fg="blue", font=("Microsoft YaHei UI Light", "16","bold"))
        self.emp = Label(self.root, text="Employee",bd = 0,bg = "white", fg="blue", font=("Microsoft YaHei UI Light", "16","bold"))

        self.frame = Frame(self.root, width=900, height=50, bg="#00FFFF", border=5)
        self.frame.place(x=15, y=5)
        Label(self.frame, text="HR DASHBOARD", fg="black", bg="#00FFFF", font=("Microsoft YaHei UI Light", "20")).place(x=350, y=3)

        # Vertical line left
        l1 = Frame(self.root, width=3, height=480, bg="#00FFFF").place(x=15, y=5)

        # Vertical line Right
        l2 = Frame(self.root, width=3, height=480, bg="#00FFFF").place(x=914, y=5)

        # Horizontal line Bottom
        l3 = Frame(self.root, width=900, height=3, bg="#00FFFF").place(x=15, y=482)

        self.showprofile = Button(self.root, text="Show Profile", width=20,height=2, bg="#00FFFF", fg="blue", bd=0, font=("Microsoft YaHei UI Light", "16"), command=self.profile)
        self.showprofile.place(x=100, y=100)

        self.EmployeeDirectory = Button(self.root, text="Employee Directory", width=20,height=2, bg="#00FFFF", fg="blue", bd=0, font=("Microsoft YaHei UI Light", "16"), command=self.employeedirectory)
        self.EmployeeDirectory.place(x=100, y=200)

        self.AddEmployee = Button(self.root, text=" Add Employee", width=20,height=2, bg="#00FFFF", fg="blue", bd=0, font=("Microsoft YaHei UI Light", "16"),command=lambda:addemployee())
        self.AddEmployee.place(x=100, y=300)

        self.Logout = Button(self.root, text="Logout", width=6, bg="black", fg="yellow", bd=0, font=("Microsoft YaHei UI Light", "10","bold"),command=lambda:logout(self.root))
        self.Logout.place(x=845,y=60)

        self.tree = None  # Placeholder for Treeview widget

    def profile(self):
        # Hide employee label
        self.emp.place_forget()

        # Place profile label
        self.pro.place(x=550, y=100)

        # Remove previous Treeview widget if exists
        if self.tree:
            self.tree.destroy()

        # Read data from Excel file
        try:
            df = pd.read_excel('users.xlsx')  
            user_data = df[df['Username'] == self.username]  # Filter data for the logged-in user
            if not user_data.empty:
                profile_data = user_data.iloc[0]
                # Display profile data
                # For example, create labels to display each piece of profile information
                  
                Label(self.root, text=f"Name: {profile_data['Name']}",bg="white",bd=0, font=("Microsoft YaHei UI Light", "12","bold")).place(x=550, y=150)
                Label(self.root, text=f"Username: {profile_data['Username']}",bg="white", font=("Microsoft YaHei UI Light", "12","bold")).place(x=550, y=180)
                Label(self.root, text=f"Password: {profile_data['Password']}",bg="white", font=("Microsoft YaHei UI Light", "12","bold")).place(x=550, y=210)
                Label(self.root, text=f"Designation: {profile_data['Designation']}",bg="white", font=("Microsoft YaHei UI Light", "12","bold")).place(x=550, y=240)
                Label(self.root, text=f"Gender: {profile_data['Gender']}",bg="white", font=("Microsoft YaHei UI Light", "12","bold")).place(x=550, y=270)
                Label(self.root, text=f"Phone number: {profile_data['Phone']}",bg="white", font=("Microsoft YaHei UI Light", "12","bold")).place(x=550, y=300)
                Label(self.root, text=f"Address: {profile_data['Address']}",bg="white", font=("Microsoft YaHei UI Light", "12","bold")).place(x=550, y=330)
                # Add more labels for other profile information as needed
            else:
                messagebox.showinfo("Info", "No profile data found for the logged-in user.")
        except FileNotFoundError:
            messagebox.showerror("Error", "Profile data file not found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def employeedirectory(self):
        self.pro.place_forget()  # Hide profile label
        self.emp.place(x=550, y=100)  # Place employee label

        # Remove previous Treeview widget if exists
        if self.tree:
            self.tree.destroy()

        # Create and populate the Treeview widget for employee directory
        self.tree = ttk.Treeview(self.root, columns=("Name", "Designation"), show="headings", selectmode="none")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Designation", text="Designation")
        self.tree.place(x=400, y=150)

        try:
            df = pd.read_excel('users.xlsx')

            
            # Display employee directory
            for index, row in df.iterrows():
                self.tree.insert("", "end", values=(row['Name'], row['Designation']))
        except FileNotFoundError:
            messagebox.showerror("Error", "Employee data file not found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def run(self):
        self.root.mainloop()


