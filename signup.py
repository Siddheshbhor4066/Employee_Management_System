from tkinter import *
from tkinter import messagebox
import os
import pandas as pd


def signup():
    root = Tk()
    root.title("Employee Registration")
    root.geometry("400x450")
    root.resizable(False, False)

    # Labels
    Label(root, text="Employee Registration", font=("Arial", 18)).place(x=20, y=10)
    Label(root, text="Name:").place(x=20, y=50)
    Label(root, text="Username:").place(x=20, y=80)
    Label(root, text="Password:").place(x=20, y=110)
    Label(root, text="Confirm Password:").place(x=20, y=140)
    Label(root, text="Designation:").place(x=20, y=170)
    Label(root, text="Gender:").place(x=20, y=200)
    Label(root, text="Phone Number:").place(x=20, y=230)
    Label(root, text="Address:").place(x=20, y=260)

    # Entry fields
    name_entry = Entry(root)
    name_entry.place(x=150, y=50)
    username_entry = Entry(root)
    username_entry.place(x=150, y=80)
    password_entry = Entry(root, show="*")
    password_entry.place(x=150, y=110)
    confirm_password_entry = Entry(root, show="*")
    confirm_password_entry.place(x=150, y=140)

    # Dropdown menu for designation
    designations = ["CEO", "HR", "Manager", "Team Leader", "Employee"]
    designation_var = StringVar(root)
    designation_var.set("Designation")  # Default value
    designation_dropdown = OptionMenu(root, designation_var, *designations)
    designation_dropdown.place(x=150, y=170)

    # Gender radio buttons
    gender_var = StringVar(root)
    gender_var.set("Male")
    Radiobutton(root, text="Male", variable=gender_var, value="Male").place(x=150, y=200)
    Radiobutton(root, text="Female", variable=gender_var, value="Female").place(x=200, y=200)

    phone_entry = Entry(root)
    phone_entry.place(x=150, y=230)

    address_entry = Entry(root)
    address_entry.place(x=150, y=260)

    def save_to_excel():
        # Get values from input fields
        employee_name = name_entry.get()
        employee_username = username_entry.get()
        employee_password = password_entry.get()
        employee_confirm_password = confirm_password_entry.get()
        employee_designation = designation_var.get()  # Get designation value from dropdown
        employee_gender = gender_var.get()
        employee_phone = phone_entry.get()
        employee_address = address_entry.get()

        if not all(
                [employee_name, employee_username, employee_password, employee_confirm_password, employee_designation,
                 employee_gender, employee_phone, employee_address]):
            messagebox.showerror("Error", "Please Fill The Fields")
            return
        elif employee_password == employee_confirm_password:
            data = {'Name': [employee_name], 'Username': [employee_username], 'Password': [employee_password],
                    'Designation': [employee_designation], "Gender": [employee_gender], "Phone": [employee_phone],
                    "Address": [employee_address]}
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
            # Return to login page
            from loginpage import LoginPage
            master = Tk()
            login_page = LoginPage(master)
            login_page
        else:
            messagebox.showerror("Error", "Password and Confirm Password do not match.")
            return

    Button(root, text="Register", command=save_to_excel).place(x=150, y=300)

    root.mainloop()


if __name__ == "__main__":
    signup()