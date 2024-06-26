from tkinter import *
from logout import logout
import pandas as pd
from tkinter import messagebox
from tkinter import ttk

class TeamLeaderDashboard:
    def __init__(self,username):
        self.username = username
        self.root = Tk()
        self.root.geometry("927x500+300+200")
        self.root.resizable(False, False)
        self.root.title("Team Leader Dashboard")
        self.root.configure(bg="white")

        self.pro = Label(self.root, text="My Profile", fg="blue",bg="white", font=("Microsoft YaHei UI Light", "16","bold"))
        self.emp = Label(self.root, text="Employee", fg="blue",bg="white", font=("Microsoft YaHei UI Light", "16","bold"))

        self.frame = Frame(self.root, width=900, height=50, bg="#00FFFF", border=5)
        self.frame.place(x=15, y=5)

        Label(self.frame, text="TEAM LEADER DASHBOARD", fg="black", bg="#00FFFF",
              font=("Microsoft YaHei UI Light", "20")).place(x=350, y=3)

        # Vertical line left
        Frame(self.root, width=3, height=480, bg="#00FFFF").place(x=15, y=5)

        # vertical line Right
        Frame(self.root, width=3, height=480, bg="#00FFFF").place(x=914, y=5)

        # Horizontal line Bottom
        Frame(self.root, width=900, height=3, bg="#00FFFF").place(x=15, y=482)

        self.showprofile = Button(self.root, text="Show Profile", width=20,height=2, bg="#00FFFF", fg="blue", bd=0,
                                  font=("Microsoft YaHei UI Light", "16"), command=self.profile)
        self.showprofile.place(x=100, y=100)

        self.teams_button = Button(self.root, text="Employee", width=20,height=2, bg="#00FFFF", fg="blue", bd=0,
                                   font=("Microsoft YaHei UI Light", "16"), command=self.show_teams)
        self.teams_button.place(x=100, y=200)

        
        self.Logout = Button(self.root, text="Logout", width=6, bg="black", fg="yellow", bd=0, font=("Microsoft YaHei UI Light", "10","bold"), command=lambda:logout(self.root))
        self.Logout.place(x=845,y=60)

        self.tree = None


    def profile(self):
        # Hide employee label
        self.emp.place_forget()

        # Place profile label
        self.pro.place(x=550, y=100)

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
                  
                Label(self.root, text=f"Name: {profile_data['Name']}",bg="white", font=("Microsoft YaHei UI Light", "12","bold")).place(x=550, y=150)
                Label(self.root, text=f"Username: {profile_data['Username']}",bg="white", font=("Microsoft YaHei UI Light", "12","bold")).place(x=550, y=180)
                Label(self.root, text=f"Designation: {profile_data['Designation']}",bg="white", font=("Microsoft YaHei UI Light", "12","bold")).place(x=550, y=210)
                Label(self.root, text=f"Gender: {profile_data['Gender']}",bg="white", font=("Microsoft YaHei UI Light", "12","bold")).place(x=550, y=240)
                Label(self.root, text=f"Phone number: {profile_data['Phone']}",bg="white", font=("Microsoft YaHei UI Light", "12","bold")).place(x=550, y=270)
                Label(self.root, text=f"Address: {profile_data['Address']}",bg="white", font=("Microsoft YaHei UI Light", "12","bold")).place(x=550, y=300)
                # Add more labels for other profile information as needed
            else:
                messagebox.showinfo("Info", "No profile data found for the logged-in user.")
        except FileNotFoundError:
            messagebox.showerror("Error", "Profile data file not found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def show_teams(self):
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

            df = df[df["Designation"] == "Employee"]

            # Display employee directory
            for index, row in df.iterrows():
                self.tree.insert("", "end", values=(row['Name'], row['Designation']))
        except FileNotFoundError:
            messagebox.showerror("Error", "Employee data file not found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        Label(self.root, text="").place(x=400, y=150)
