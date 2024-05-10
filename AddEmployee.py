from tkinter import *
from tkinter import messagebox
import os
import pandas as pd
import re


def addemployee():
    root = Tk()
    root.title("Add New Employee")
    root.geometry("400x400")  # Increased height to accommodate the email field
    root.resizable(False, False)

    # Labels
    Label(root, text="Add Employee", font=("Arial", 18)).place(x=130, y=10)
    Label(root, text="Name:").place(x=80, y=50)
    Label(root, text="Email:").place(x=80, y=80)  # Moved email label after name label
    Label(root, text="Username:").place(x=80, y=110)  # Adjusted y-coordinate for other labels
    Label(root, text="Password:").place(x=80, y=140)
    Label(root, text="Confirm Password:").place(x=80, y=170)
    Label(root, text="Designation:").place(x=80, y=200)
    Label(root, text="Gender:").place(x=80, y=230)
    Label(root, text="Phone Number:").place(x=80, y=260)
    Label(root, text="Address:").place(x=80, y=290)

    # Entry fields
    name_entry = Entry(root)
    name_entry.place(x=210, y=50)
    email_entry = Entry(root)  # New entry field for email
    email_entry.place(x=210, y=80)  # Adjusted y-coordinate for email entry
    username_entry = Entry(root)
    username_entry.place(x=210, y=110)
    password_entry = Entry(root, show="*")
    password_entry.place(x=210, y=140)
    confirm_password_entry = Entry(root, show="*")
    confirm_password_entry.place(x=210, y=170)

    # Dropdown menu for designation
    designations = ["CEO", "HR", "Manager", "Team Leader", "Employee"]
    designation_var = StringVar(root)
    designation_var.set("Designation")  # Default value
    designation_dropdown = OptionMenu(root, designation_var, *designations)
    designation_dropdown.place(x=210, y=200)

    # Gender radio buttons
    gender_var = StringVar(root)
    gender_var.set("Male")
    Radiobutton(root, text="Male", variable=gender_var, value="Male").place(x=210, y=230)
    Radiobutton(root, text="Female", variable=gender_var, value="Female").place(x=260, y=230)

    phone_entry = Entry(root)
    phone_entry.place(x=210, y=260)

    address_entry = Entry(root)
    address_entry.place(x=210, y=290)

    def save_to_excel():
        # Get values from input fields
        employee_name = name_entry.get()
        employee_email = email_entry.get()  # Get email value
        employee_username = username_entry.get()
        employee_password = password_entry.get()
        employee_confirm_password = confirm_password_entry.get()
        employee_designation = designation_var.get()  # Get designation value from dropdown
        employee_gender = gender_var.get()
        employee_phone = phone_entry.get()
        employee_address = address_entry.get()

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
            root.destroy()  # to destroy the signup window
            
        else:
            messagebox.showerror("Error", "Password and Confirm Password do not match.")
            return


    Button(root, text="Register", command=save_to_excel).place(x=150, y=330)  # Adjusted y-coordinate

    root.mainloop()


if __name__ == "__main__":
    addemployee()
