import tkinter as tk
from tkinter import *
import logging
from controller.LoginController import LoginController as Login
from view.ChangePasswordScreen import ChangePasswordScreen
from view.RegistrationScreen import RegistrationScreen


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
        #changing the icon of the window
        self.iconbitmap("resources/user1.ico")
        self.configure(bg='slate gray')
        #sets the overall size of the main window
        self.geometry("750x500")
       
        self.user = User()
        self.login_frame = tk.Frame(self, bg='slate gray')
        self.login_frame.place(relx=0,rely=0)

        self.header_label=tk.Label(self, text="LOGIN!",bg='slate gray',font=("Segoe Script", 20, "bold"),fg='Black')
        self.header_label.place(relx=0.45, rely=0.1)

        self.email_label = tk.Label(self, text="E-Mail:",bg='slate gray',font=8,fg='Black')
        self.email_label.place(relx=0.2, rely=0.3)

        self.email_entry = tk.Entry(self,font=8,fg='Black')
        self.email_entry.place(relx=0.4, rely=0.3)

        self.password_label = tk.Label(self, text="Password:",bg='slate gray',font=8,fg='Black')
        self.password_label.place(relx=0.15, rely=0.4)

        self.password_entry = tk.Entry(self, font=8,fg='Black',show='*')
        self.password_entry.place(relx=0.4, rely=0.4)

        #using submit image as button
        self.submit_image = PhotoImage(file="resources/submit_button.png")
        self.resized_image=self.submit_image.subsample(5,5)
        self.submit_button = tk.Button(self, image=self.resized_image, command=self.submit_form, bg='slate gray', bd=0)
        self.submit_button.place(relx=0.7, rely=0.5)

        # creating register button
        self.register_image = PhotoImage(file="resources/register_button.png")
        self.re_register_image=self.register_image.subsample(5,5)
        self.greet_button = tk.Button(self, image=self.re_register_image, command=self.open_registration_screen,bg='slate gray',bd=0)
        self.greet_button.place(relx=0.2,rely=0.5)

        # Add a exit button
        self.exit_image = PhotoImage(file="resources/power_button.png")
        self.re_exit_image=self.exit_image.subsample(10,10)
        self.exit_button = tk.Button(self, image=self.re_exit_image, command=self.destroy,bg='slate gray',bd=0)
        self.exit_button.place(relx=0.5,rely=0.5)

    def submit_form(self):
        login = Login()
        self.user.email = self.email_entry.get()
        self.user.password = self.password_entry.get()
        login.ValidateUser(self.user)
        if self.user.password == "PASSINIT":
            self.withdraw()
            changePassword = ChangePasswordScreen(self.user)
            #changePassword.change_password()

    def open_registration_screen(self):
        self.withdraw()
        self.reg = RegistrationScreen()
   


