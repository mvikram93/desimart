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
            return 0
        elif not Email.validate_email(user.email):
            self.log.error("Invalid Email ID. Please provide a Valid One")
            Exception.raise_Exception("Invalid Email ID. Please provide a Valid One")
            return 0
        logged_In_User = user_query.get_user(user)
        print(logged_In_User)
        if len(logged_In_User)==0:
            self.log.error("User does not exists. Please provide a Valid One")
            Exception.raise_Exception("User does not exists. Please provide a Valid One")
            return 0
        user.email = logged_In_User[1]
        user.firstname =logged_In_User[2]
        user.lastname = logged_In_User[3]
        user.password = logged_In_User[4]
        self.log.info(logged_In_User)
        return 1
        #messagebox.showinfo("Logged In User Details",
        #                    f"First Name: {user.firstname}\nLast Name: {user.lastname}\nEmail ID: {user.email}\n"
        #                    f"Password: {user.password}")

    def changePassword(self, user):
        user_query = UserQuery()
        if not (user.email and user.password):
            Exception.raise_Exception("Please check all the details. Something is Missing")
            return
        elif not Email.validate_email(user.email):
            Exception.raise_Exception("Invalid Email ID. Please provide a Valid One")
        user_query.update_user(user)

