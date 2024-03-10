import tkinter as tk
import logging
from controller.RegistrationController import RegistrationController as Register
from model.UserModel import User

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')


class RegistrationScreen(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.deiconify()
        log = logging.getLogger(self.__class__.__name__)
        log.info("Opened Registration Screen")
        self.title("Registration Screen")
        self.user = User()
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

        self.address_city_label = tk.Label(self.registration_frame, text="City:")
        self.address_city_label.pack()

        self.address_city_entry = tk.Entry(self.registration_frame)
        self.address_city_entry.pack()

        self.state_label = tk.Label(self.registration_frame, text="State:")
        self.state_label.pack()

        self.state_entry = tk.Entry(self.registration_frame)
        self.state_entry.pack()

        self.address_zipcode_label = tk.Label(self.registration_frame, text="Zipcode:")
        self.address_zipcode_label.pack()

        self.address_zipcode_entry = tk.Entry(self.registration_frame)
        self.address_zipcode_entry.pack()

        self.submit_button = tk.Button(self.registration_frame, text="Submit", command=self.submit_form)
        self.submit_button.pack()

    def submit_form(self):
        register = Register()
        self.user.firstname = self.firstname_entry.get()
        self.user.lastname = self.lastname_entry.get()
        self.user.email = self.email_entry.get()
        self.user.phone = self.phone_entry.get()
        self.user.city = self.address_city_entry.get()
        self.user.address = self.address_entry.get()
        self.user.state = self.state_entry.get()
        self.user.zipcode = self.address_zipcode_entry.get()
        register.register_user_details(self.user)
