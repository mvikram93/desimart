import tkinter as tk
from tkinter import *
import logging
from controller.LoginController import LoginController as Login
from model.UserModel import User
from tkinter import messagebox

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')


class ChangePasswordScreen(tk.Toplevel):
    def __init__(self, user,login_screen_ref):
        super().__init__()
        self.deiconify()
        log = logging.getLogger(self.__class__.__name__)
        log.info("Opened Changed Password Screen")
        self.title("Change Password Screen")
        self.configure(bg='white')
        self.geometry("890x500+300+200")

        # Center the window on the screen
        self.update_idletasks()  # Update the window
        width = self.winfo_width()  # Get the width of the window
        height = self.winfo_height()  # Get the height of the window
        x = (self.winfo_screenwidth() // 2) - (width // 2)  # Calculate the x position
        y = (self.winfo_screenheight() // 2) - (height // 2)  # Calculate the y position
        self.geometry(f"+{x}+{y}")  # Set the new position
        self.resizable(False,False)
        
        self.img=PhotoImage(file='resources\desi1.png')
        self.bg_img=tk.Label(self,image=self.img,bg="white").place(x=15,y=5)
        self.img1=PhotoImage(file='resources\lock.png')
        self.bg_img=tk.Label(self,image=self.img1,bg="white").place(x=400,y=90)

        self.user = User()
        self.change_password = tk.Frame(self,width=350,height=350,bg='white')
        self.change_password.place(x=70,y=130)
        self.user = user
        self.password_reset_label = tk.Label(self.change_password, text="Reset Password",bg='white',font=("Microsoft YaHei UI Light", 20, "bold"),fg='DodgerBlue4')
        self.password_reset_label.place(x=20, y=5)

        self.old_password = tk.Label(self.change_password, text="Old Password:",bg='white',font=("Microsoft YaHei UI Light", 10, "bold"),fg='black')
        self.old_password.place(x=20, y=70)
        self.old_password_value_label = tk.Label(self.change_password)
        self.old_password_value_label.configure(text=user.password)
        self.old_password_entry=tk.Entry(self.change_password,border='1',width=25,font=("Microsoft YaHei UI Light", 10),bg='ghost white')
        self.old_password_entry.place(x=20, y=95)

        self.new_password_label = tk.Label(self.change_password, text="New Password:",bg='white',font=("Microsoft YaHei UI Light", 10,"bold"),fg='black')
        self.new_password_label.place(x=20,y=120)

        self.new_password_entry = tk.Entry(self.change_password,border='1',show='*',width=25,font=("Microsoft YaHei UI Light", 10),bg='ghost white')
        self.new_password_entry.place(x=20,y=145)

        self.confirm_password_label = tk.Label(self.change_password, text="Confirm Password:",bg='white',font=("Microsoft YaHei UI Light", 10,"bold"),fg='black')
        self.confirm_password_label.place(x=20,y=170)

        self.confirm_password_entry = tk.Entry(self.change_password,border='1',show='*',width=25,font=("Microsoft YaHei UI Light", 10),bg='ghost white')
        self.confirm_password_entry.place(x=20,y=195)

        self.submit_button = tk.Button(self.change_password, text="Submit", command=self.submit_form,width=19,bg='DodgerBlue4',fg='white',border=0,font=("Microsoft YaHei UI Light", 10,"bold"))
        self.submit_button.place(x=20,y=230)

        self.label=tk.Label(self.change_password,text="To go back click",fg='black',bg='white',font=("Microsoft YaHei UI Light", 9))
        self.label.place(x=22,y=270)

       # Adding back button
        self.back_button = tk.Button(self.change_password, text="Back", command=self.back_to_login_screen,border=0,bg='white',cursor='hand2',fg='DodgerBlue4')
        self.back_button.place(x=120,y=270)
        self.login_screen_ref = login_screen_ref


    def back_to_login_screen(self):
        self.withdraw()  # Hide the current window
        self.login_screen_ref.deiconify()
  
  
    def submit_form(self):
        login = Login()
        if not (self.old_password_entry.get() == self.new_password_entry.get()) and (
                self.confirm_password_entry.get() == self.new_password_entry.get()):
            self.user.password = self.new_password_entry.get()
            messagebox.showinfo("Success!", "You have successfully reset your password!")
        elif self.old_password_entry.get() == self.new_password_entry.get():
            messagebox.showerror("Error", "Old Password and new Password are the same.")
        else:
            messagebox.showinfo("Error", "Password mismatch!")
        login.changePassword(self.user)
