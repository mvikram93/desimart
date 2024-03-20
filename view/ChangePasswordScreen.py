import tkinter as tk
from tkinter import *
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
        self.configure(bg='white')
        self.geometry("890x500+300+200")
        self.resizable(False,False)
        self.img=PhotoImage(file='resources\desi1.png')
        self.bg_img=tk.Label(self,image=self.img,bg="white").place(x=15,y=5)
        self.user = User()
        self.change_password = tk.Frame(self,width=350,height=350,bg='white')
        self.change_password.place(x=480,y=100)
        self.user = user
        self.password_reset_label = tk.Label(self.change_password, text="Reset Password",bg='white',font=("Microsoft YaHei UI Light", 20, "bold"),fg='DodgerBlue4')
        self.password_reset_label.place(x=60, y=5)

        self.old_password = tk.Label(self.change_password, text="Old Password:",bg='white',font=("Microsoft YaHei UI Light", 10, "bold"),fg='black')
        self.old_password.place(x=20, y=70)
        self.old_password_value_label = tk.Label(self.change_password)
        self.old_password_value_label.configure(text=user.password)
        self.old_password_entry=tk.Entry(self.change_password,border='1',width=25,font=("Microsoft YaHei UI Light", 10),bg='ghost white')
        self.old_password_entry.place(x=20, y=95)

        self.new_password_label = tk.Label(self.change_password, text="New Password:",bg='white',font=("Microsoft YaHei UI Light", 10,"bold"),fg='black')
        self.new_password_label.place(x=20,y=120)

        self.new_password_entry = tk.Entry(self.change_password,border='1',width=25,font=("Microsoft YaHei UI Light", 10),bg='ghost white')
        self.new_password_entry.place(x=20,y=145)

        self.confirm_password_label = tk.Label(self.change_password, text="Confirm Password:",bg='white',font=("Microsoft YaHei UI Light", 10,"bold"),fg='black')
        self.confirm_password_label.place(x=20,y=170)

        self.confirm_password_entry = tk.Entry(self.change_password,border='1',width=25,font=("Microsoft YaHei UI Light", 10),bg='ghost white')
        self.confirm_password_entry.place(x=20,y=195)

        self.submit_button = tk.Button(self.change_password, text="Change Password", command=self.submit_form,width=20,pady=5,bg='DodgerBlue4',fg='white',border=0,font=("Microsoft YaHei UI Light", 10,"bold"))
        self.submit_button.place(x=20,y=230)

    def submit_form(self):
        login = Login()
        if not (self.old_password_entry.get() == self.new_password_entry.get()) and (
                self.confirm_password_entry.get() == self.new_password_entry.get()):
            self.user.password = self.new_password_entry.get()
        elif self.old_password_entry.get() == self.new_password_entry.get():
            messagebox.showinfo("Error", "Old Password and new Password are the same.")
        else:
            messagebox.showinfo("Error", "Password mismatch!")
        login.changePassword(self.user)
