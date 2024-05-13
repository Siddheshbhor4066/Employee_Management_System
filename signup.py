from tkinter import *
from tkinter import messagebox
import os
import pandas as pd
import re


class SignupPage:
    def __init__(self):
    
        self.root = Tk()
        self.root.title("Employee Registration")
        self.root.geometry("400x400")  # Increased height to accommodate the email field
        self.root.resizable(False, False)

        # Labels
        Label(self.root, text="Employee Registration", font=("Arial", 18)).place(x=100, y=10)
        Label(self.root, text="Name:").place(x=80, y=50)
        Label(self.root, text="Email:").place(x=80, y=80)  # Moved email label after name label
        Label(self.root, text="Username:").place(x=80, y=110)  # Adjusted y-coordinate for other labels
        Label(self.root, text="Password:").place(x=80, y=140)
        Label(self.root, text="Confirm Password:").place(x=80, y=170)
        Label(self.root, text="Designation:").place(x=80, y=200)
        Label(self.root, text="Gender:").place(x=80, y=230)
        Label(self.root, text="Phone Number:").place(x=80, y=260)
        Label(self.root, text="Address:").place(x=80, y=290)

        # Entry fields
        self.name_entry = Entry(self.root)
        self.name_entry.place(x=210, y=50)
        self.email_entry = Entry(self.root)  # New entry field for email
        self.email_entry.place(x=210, y=80)  # Adjusted y-coordinate for email entry
        self.username_entry = Entry(self.root)
        self.username_entry.place(x=210, y=110)
        self.password_entry = Entry(self.root, show="*")
        self.password_entry.place(x=210, y=140)
        self.confirm_password_entry = Entry(self.root, show="*")
        self.confirm_password_entry.place(x=210, y=170)

        # Dropdown menu for designation
        designations = ["CEO", "HR", "Manager", "Team Leader", "Employee"]
        self.designation_var = StringVar(self.root)
        self.designation_var.set("Designation")  # Default value
        self.designation_dropdown = OptionMenu(self.root, self.designation_var, *designations)
        self.designation_dropdown.place(x=210, y=200)

        # Gender radio buttons
        self.gender_var = StringVar(self.root)
        self.gender_var.set("Male")
        Radiobutton(self.root, text="Male", variable=self.gender_var, value="Male").place(x=210, y=230)
        Radiobutton(self.root, text="Female", variable=self.gender_var, value="Female").place(x=260, y=230)

        self.phone_entry = Entry(self.root)
        self.phone_entry.place(x=210, y=260)

        self.address_entry = Entry(self.root)
        self.address_entry.place(x=210, y=290)

        Button(self.root, text="Register", command=self.save_to_excel).place(x=150, y=330)  # Adjusted y-coordinate

        self.root.mainloop()

    def save_to_excel(self):
        # Get values from input fields
        employee_name = self.name_entry.get()
        employee_email = self.email_entry.get()  # Get email value
        employee_username = self.username_entry.get()
        employee_password = self.password_entry.get()
        employee_confirm_password = self.confirm_password_entry.get()
        employee_designation = self.designation_var.get()  # Get designation value from dropdown
        employee_gender = self.gender_var.get()
        employee_phone = self.phone_entry.get()
        employee_address = self.address_entry.get()

        try:
            # Check if the username or email already exists in the Excel file
            df = pd.read_excel('users.xlsx')
            if (df['Username'] == employee_username).any():
                messagebox.showerror("Error", "Username already exists. Please choose a different username.")
                return
            elif (df['Email'] == employee_email).any():
                messagebox.showerror("Error", "Email already exists. Please use a different email address.")
                return
        except FileNotFoundError:
            pass  # If the file doesn't exist, no need for checks, just proceed

        if not re.match(r'^[a-zA-Z\s]{2,}$', employee_name):
            messagebox.showerror("Error", "Please enter a valid name.")
        elif not re.match(r'^[a-z0-9_.+-]+@[a-z0-9-]+\.com$', employee_email):
            messagebox.showerror("Error", "Please enter a valid email address.")
        elif not re.match(r'^[a-zA-Z0-9]{4,}$', employee_username):
            messagebox.showerror("Error", "Please enter a valid username (at least 4 characters, alphanumeric).")
        elif not re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@$!%*?&])[A-Za-z0-9@$!%*?&]{8,}$',employee_password):
            messagebox.showerror("Error",
                                "Please enter a valid password (at least 8 characters, including uppercase, lowercase, digit, and special character).")
        elif not re.match(r'^[0-9]{10}$', employee_phone):
            messagebox.showerror("Error", "Please enter a valid phone number (10 digits).")
        elif not re.match(r'^[a-zA-Z0-9\s,.-]+$', employee_address):
            messagebox.showerror("Error", "Please enter a valid address.")
        elif employee_password != employee_confirm_password:
            messagebox.showerror("Error", "Password and Confirm Password do not match.")
        elif not employee_designation:
            messagebox.showerror("Error", "Please select a designation.")
        elif not employee_gender:
            messagebox.showerror("Error", "Please select a gender.")

        elif not all(
                [employee_name, employee_email, employee_username, employee_password, employee_confirm_password, employee_designation,
                employee_gender, employee_phone, employee_address]):  # Check if any field is empty
            messagebox.showerror("Error", "Please Fill The Fields")
            return
        elif employee_password == employee_confirm_password:
            data = {'Name': [employee_name], 'Email': [employee_email], 'Username': [employee_username], 'Password': [employee_password],
                    'Designation': [employee_designation], "Gender": [employee_gender], "Phone": [employee_phone],
                    "Address": [employee_address]}  # Include email in data
            df = pd.DataFrame(data)
            # Check if file exists
            if os.path.exists('users.xlsx'):
                # Load existing data
                existing_df = pd.read_excel('users.xlsx')
                # Append new data
                updated_df = pd.concat([existing_df, df], ignore_index=True)
                updated_df.to_excel('users.xlsx', index=False)
            else:
                # If file doesn't exist, save new data
                df.to_excel('users.xlsx', index=False, header=True)
            messagebox.showinfo("Successful", "User Sign Up Successful")
            self.root.destroy()  # to destroy the signup window
            
        else:
            messagebox.showerror("Error", "Password and Confirm Password do not match.")
            return
<<<<<<< HEAD


    Button(root, text="Register", command=save_to_excel).place(x=150, y=330)  # Adjusted y-coordinate

    root.mainloop()


if __name__ == "__main__":
    signup()


=======
        
>>>>>>> e85b7cfeae18f669ad22ea7ec945f966e1faa3d8
