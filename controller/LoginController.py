from tkinter import messagebox
from exception.Exception import Exception
from service.EmailService import EmailService as Email
import logging

from query.UserQuery import UserQuery

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')


class LoginController:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.info("Opened Login Controller")

    def ValidateUser(self, user):
        user_query = UserQuery()
        if not (user.email and user.password):
            self.log.error("Please check all the details. Something is Missing")
            Exception.raise_Exception("Please check all the details. Something is Missing")
            return
        elif not Email.validate_email(user.email):
            self.log.error("Invalid Email ID. Please provide a Valid One")
            Exception.raise_Exception("Invalid Email ID. Please provide a Valid One")
            return
        logged_In_User = user_query.get_user(user)
        if not logged_In_User:
            self.log.error("Invalid Email ID. Please provide a Valid")
            Exception.raise_Exception("Invalid Email ID. Please")
            return
        user.email = logged_In_User[1]
        user.firstname =  logged_In_User[2]
        user.lastname = logged_In_User[3]
        user.password = logged_In_User[4]
        print(logged_In_User)
        messagebox.showinfo("Logged In User Details",
                            f"First Name: {user.firstname}\nLast Name: {user.lastname}\nEmail ID: {user.email}\nPassword: {user.password}")