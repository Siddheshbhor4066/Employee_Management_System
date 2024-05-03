from tkinter import *

def logout(root):
    root.destroy()
    # Recreate and show the login page
    from loginpage import LoginPage
    root = Tk()
    login_page = LoginPage(root)
    login_page