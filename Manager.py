from tkinter import *
from logout import logout
import pandas as pd
from tkinter import messagebox

class ManagerDashboard:
    def __init__(self,username):
        self.username = username
        self.root = Tk()
        self.root.geometry("927x500+300+200")
        self.root.resizable(False, False)
        self.root.title("ceodashboard")
        self.root.configure(bg="white")

        self.pro_label = Label(self.root, text="My Profile", fg="blue", font=("Microsoft YaHei UI Light", "16"))
        self.emp_label = Label(self.root, text="Team Leaders", fg="blue", font=("Microsoft YaHei UI Light", "16"))

        self.frame = Frame(self.root, width=900, height=50, bg="#76EE00", border=5)
        self.frame.place(x=15, y=5)
        Label(self.frame, text="Manager DASHBOARD", fg="red", bg="#76EE00", font=("Microsoft YaHei UI Light", "20")).place(x=350, y=5)

        # Vertical line left
        Frame(self.root, width=3, height=480, bg="#76EE00").place(x=15, y=5)

        # vertical line Right
        Frame(self.root, width=3, height=480, bg="#76EE00").place(x=914, y=5)

        # Horizontal line Bottom
        Frame(self.root, width=900, height=3, bg="#76EE00").place(x=15, y=482)

        self.show_profile_button = Button(self.root, text="Show Profile", width=20, bg="#76EE00", fg="blue", bd=0,
                             font=("Microsoft YaHei UI Light", "16"), command=self.profile)
        self.show_profile_button.place(x=100, y=100)

        self.teams_button = Button(self.root, text="Team", width=20, bg="#76EE00", fg="blue", bd=0,
                                   font=("Microsoft YaHei UI Light", "16"), command=self.teams)
        self.teams_button.place(x=100, y=200)

        self.Logout = Button(self.root, text="Logout", width=6, bg="black", fg="yellow", bd=0, font=("Microsoft YaHei UI Light", "10","bold"),command=lambda:logout(self.root))
        self.Logout.place(x=845,y=60)

    def profile(self):
        # Hide employee label
        self.emp_label.place_forget()

        # Place profile label
        self.pro_label.place(x=550, y=100)

        # Read data from Excel file
        try:
            df = pd.read_excel('users.xlsx')  
            user_data = df[df['Username'] == self.username]  # Filter data for the logged-in user
            if not user_data.empty:
                profile_data = user_data.iloc[0]
                # Display profile data
                # For example, create labels to display each piece of profile information
                Label(self.root, text=f"Name: {profile_data['Name']}").place(x=550, y=150)
                Label(self.root, text=f"Username: {profile_data['Username']}").place(x=550, y=170)
                Label(self.root, text=f"Designation: {profile_data['Designation']}").place(x=550, y=190)
                Label(self.root, text=f"Gender: {profile_data['Gender']}").place(x=550, y=210)
                Label(self.root, text=f"Phone number: {profile_data['Phone']}").place(x=550, y=230)
                Label(self.root, text=f"Address: {profile_data['Address']}").place(x=550, y=250)
                # Add more labels for other profile information as needed
            else:
                messagebox.showinfo("Info", "No profile data found for the logged-in user.")
        except FileNotFoundError:
            messagebox.showerror("Error", "Profile data file not found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


    def teams(self):
        self.emp_label.place(x=550, y=100)
        self.pro_label.place_forget()


