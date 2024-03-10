import tkinter as tk
import logging
from controller.LoginController import LoginController as Login
from view.ChangePasswordScreen import ChangePasswordScreen

from model.UserModel import User

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')


class LoginScreen(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.deiconify()
        log = logging.getLogger(self.__class__.__name__)
        log.info("Opened Login Screen")
        self.title("Login Screen")
        self.user = User()
        self.login_frame = tk.Frame(self)
        self.login_frame.pack()

        self.email_label = tk.Label(self.login_frame, text="E-Mail:")
        self.email_label.pack()

        self.email_entry = tk.Entry(self.login_frame)
        self.email_entry.pack()

        self.password_label = tk.Label(self.login_frame, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self.login_frame)
        self.password_entry.pack()

        self.submit_button = tk.Button(self.login_frame, text="Submit", command=self.submit_form)
        self.submit_button.pack()

    def submit_form(self):
        login = Login()
        self.user.email = self.email_entry.get()
        self.user.password = self.password_entry.get()
        login.ValidateUser(self.user)
        if self.user.password == "PASSINIT":
            self.withdraw()
            changePassword = ChangePasswordScreen(self.user)
            #changePassword.change_password()