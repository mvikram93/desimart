import tkinter as tk
import logging
from tkinter import messagebox
from controller.RegistrationController import RegistrationController as Register

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w',format='%(name)s - %(levelname)s - %(message)s')

class RegistrationScreen(tk.Toplevel):
    def __init__(self,parent, logging):
        super().__init__(parent)
        #self.root = root
        log = logging.getLogger(self.__class__.__name__)
        log.info("Opened Registration Screen")
        self.title("Registration Screen")

        self.registration_frame = tk.Frame(self)
        self.registration_frame.pack()

        self.firstname_label = tk.Label(self.registration_frame, text="First Name:")
        self.firstname_label.pack()

        self.firstname_entry = tk.Entry(self.registration_frame)
        self.firstname_entry.pack()

        self.lastname_label = tk.Label(self.registration_frame, text="Last Name:")
        self.lastname_label.pack()

        self.lastname_entry = tk.Entry(self.registration_frame)
        self.lastname_entry.pack()

        self.email_label = tk.Label(self.registration_frame, text="Email ID:")
        self.email_label.pack()

        self.email_entry = tk.Entry(self.registration_frame)
        self.email_entry.pack()

        self.phone_label = tk.Label(self.registration_frame, text="Phone Number:")
        self.phone_label.pack()

        self.phone_entry = tk.Entry(self.registration_frame)
        self.phone_entry.pack()

        self.address_label = tk.Label(self.registration_frame, text="Address:")
        self.address_label.pack()

        self.address_entry = tk.Entry(self.registration_frame)
        self.address_entry.pack()

        self.state_label = tk.Label(self.registration_frame, text="State:")
        self.state_label.pack()

        self.state_entry = tk.Entry(self.registration_frame)
        self.state_entry.pack()

        self.submit_button = tk.Button(self.registration_frame, text="Submit", command=self.submit_form)
        self.submit_button.pack()
        
    def submit_form(self):
        firstname = self.firstname_entry.get()
        lastname = self.lastname_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()
        state = self.state_entry.get()
        Register.register_user_details(firstname,lastname,email,phone,address,state)

