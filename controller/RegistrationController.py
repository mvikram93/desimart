from tkinter import messagebox
from exception.Exception import Exception
from service.EmailService import EmailService as Email
import logging

from query.UserQuery import UserQuery

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w',format='%(name)s - %(levelname)s - %(message)s')

class RegistrationController:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.info("Opened Registration Controller")
        
        
        
        
    def register_user_details(self,user):
        user_query = UserQuery()
        self.log.info("Register User Details: {},{},{},{},{},{}",user.firstname,user.lastname,user.email,user.phone,user.address,user.state)
        if not (user.firstname and user.lastname and user.email and user.phone and user.address and user.state):
            self.log.error("Please check all the details. Something is Missing")
            Exception.raise_Exception("Please check all the details. Something is Missing")
            return False
        elif not Email.validate_email(user.email):
            self.log.error("Invalid Email ID. Please provide a Valid One")
            Exception.raise_Exception("Invalid Email ID. Please provide a Valid One")
            return False
        user_query.add_user(user)

        return True

       # messagebox.showinfo("LoggedIn Details", f"First Name: {user.firstname}\nLast Name: {user.lastname}\nEmail ID: {user.email}\nPhone Number: {user.phone}\nAddress: {user.address}\nState: {user.state}")