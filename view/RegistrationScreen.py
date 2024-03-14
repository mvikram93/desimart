import tkinter as tk
from tkinter import *
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
        self.configure(bg='white')
        #sets the overall size of the main window
        self.geometry("890x500+300+200")
        self.resizable(False,False)
        self.image=PhotoImage(file='resources/desimart.png').subsample(1,1)
        self.bg_image=tk.Label(self,image=self.image,bg="white").place(x=40,y=40)

        self.user = User()
        self.registration_frame = tk.Frame(self, width=500,height=380,bg='white')
        self.registration_frame.place(x=450,y=50)

        self.header_label=tk.Label(self.registration_frame, text="Sign up",bg='white',font=("Microsoft YaHei UI Light", 23, "bold"),fg='DodgerBlue4')
        self.header_label.place(x=150, y=5)

        self.firstname_label = tk.Label(self.registration_frame, text="First Name:",bg='white',font=("Microsoft YaHei UI Light", 9),fg='black')
        self.firstname_label.place(x=30,y=80)

        self.firstname_entry = tk.Entry(self.registration_frame,border='1',width=25,font=("Microsoft YaHei UI Light", 9),bg='ghost white')
        self.firstname_entry.place(x=30,y=105)

        self.lastname_label = tk.Label(self.registration_frame, text="Last Name:",bg='white',font=("Microsoft YaHei UI Light", 9),fg='black')
        self.lastname_label.place(x=30,y=130)

        self.lastname_entry = tk.Entry(self.registration_frame,border='1',width=25,bg='ghost white',font=("Microsoft YaHei UI Light", 9),fg='black')
        self.lastname_entry.place(x=30,y=155)

        self.email_label = tk.Label(self.registration_frame, text="Email ID:",bg='white',font=("Microsoft YaHei UI Light", 9),fg='black')
        self.email_label.place(x=30,y=180)

        self.email_entry = tk.Entry(self.registration_frame,border='1',width=25,bg='ghost white',font=("Microsoft YaHei UI Light", 9),fg='black')
        self.email_entry.place(x=30,y=205)

        self.phone_label = tk.Label(self.registration_frame, text="Phone Number:",bg='white',font=("Microsoft YaHei UI Light", 9),fg='black')
        self.phone_label.place(x=30,y=230)

        self.phone_entry = tk.Entry(self.registration_frame,border='1',width=25,bg='ghost white',font=("Microsoft YaHei UI Light", 9),fg='black')
        self.phone_entry.place(x=30,y=255)

        self.address_label = tk.Label(self.registration_frame, text="Address:",bg='white',font=("Microsoft YaHei UI Light", 9),fg='black')
        self.address_label.place(x=250,y=80)

        self.address_entry = tk.Entry(self.registration_frame,border='1',width=25,bg='ghost white',font=("Microsoft YaHei UI Light", 9),fg='black')
        self.address_entry.place(x=250,y=105)

        self.address_city_label = tk.Label(self.registration_frame, text="City:",bg='white',font=("Microsoft YaHei UI Light", 9),fg='black')
        self.address_city_label.place(x=250,y=130)

        self.address_city_entry = tk.Entry(self.registration_frame,border='1',width=25,bg='ghost white',font=("Microsoft YaHei UI Light", 9),fg='black')
        self.address_city_entry.place(x=250,y=155)

        self.state_label = tk.Label(self.registration_frame, text="State:",bg='white',font=("Microsoft YaHei UI Light", 9),fg='black')
        self.state_label.place(x=250,y=180)

        self.state_entry = tk.Entry(self.registration_frame,border='1',width=25,bg='ghost white',font=("Microsoft YaHei UI Light", 9),fg='black')
        self.state_entry.place(x=250,y=205)

        self.address_zipcode_label = tk.Label(self.registration_frame, text="Zipcode:",bg='white',font=("Microsoft YaHei UI Light", 9),fg='black')
        self.address_zipcode_label.place(x=250,y=230)

        self.address_zipcode_entry = tk.Entry(self.registration_frame,border='1',width=25,bg='ghost white',font=("Microsoft YaHei UI Light", 9),fg='black')
        self.address_zipcode_entry.place(x=250,y=255)

        self.submit_button = tk.Button(self.registration_frame, text="Submit", command=self.submit_form,width=25,pady=5,bg='DodgerBlue4',fg='white',border=0)
        self.submit_button.place(x=125,y=300)

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
