import tkinter as tk
import logging
from controller.LoginController import LoginController as Login
from model.UserModel import User
from tkinter import messagebox

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')


class ChangePasswordScreen(tk.Toplevel):
    def __init__(self, user):
        super().__init__()
        self.deiconify()
        log = logging.getLogger(self.__class__.__name__)
        log.info("Opened Changed Password Screen")
        self.title("Change Password Screen")
        self.change_password = tk.Frame(self)
        self.change_password.pack()
        self.user = user
        self.old_password = tk.Label(self.change_password, text="Old Password:")
        self.old_password.pack()

        self.old_password_value_label = tk.Label(self.change_password)
        self.old_password_value_label.configure(text=user.password)
        self.old_password_value_label.pack()

        self.new_password_label = tk.Label(self.change_password, text="New Password:")
        self.new_password_label.pack()

        self.new_password_entry = tk.Entry(self.change_password)
        self.new_password_entry.pack()

        self.confirm_password_label = tk.Label(self.change_password, text="Confirm Password:")
        self.confirm_password_label.pack()

        self.confirm_password_entry = tk.Entry(self.change_password)
        self.confirm_password_entry.pack()

        self.submit_button = tk.Button(self.change_password, text="Change Password", command=self.submit_form)
        self.submit_button.pack()

    def submit_form(self):
        login = Login()
        if not (self.old_password_entry.get() == self.new_password_entry.get()) and (
                self.confirm_password_entry.get() == self.new_password_entry.get()):
            self.user.password = self.new_password_entry.get()
        else:
            messagebox.showinfo("Error", "Password and Confirm Password are the same.")
        login.changePassword(self.user)
