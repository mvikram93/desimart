import tkinter as tk
from tkinter import *
import logging
from controller.LoginController import LoginController as Login
from view.ChangePasswordScreen import ChangePasswordScreen
from view.RegistrationScreen import RegistrationScreen
from service.EmailService import EmailService
from messagestemplate.EmailMessagesTemplate import EmailMessagesTemplate
from model.UserModel import User
from view.CategoriesScreen import CategoryScreen
# from service.OTPGeneratorService import OTPGeneratorService

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')

class LoginScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        #self.deiconify()
        log = logging.getLogger(self.__class__.__name__)
        log.info("Opened Login Screen")
        self.title("Login Screen")
        #changing the icon of the window
        self.iconbitmap("resources/user1.ico")
        self.configure(bg='white')
        # self.otpGenerator = OTPGeneratorService()
        
        #sets the overall size of the main window
        self.geometry("890x500+300+200")
        self.resizable(False,False)
        self.img=PhotoImage(file='resources\desi1.png')
        self.bg_img=tk.Label(self,image=self.img,bg="white").place(x=15,y=5)
        self.img1=PhotoImage(file='resources\desimart_logo.png')
        self.bg_img=tk.Label(self,image=self.img1,bg="white").place(x=40,y=90)

    
        self.user = User()
        self.login_frame = tk.Frame(self, width=350,height=350,bg='white')
        self.login_frame.place(x=480,y=100)

        self.header_label=tk.Label(self.login_frame, text="Sign in",bg='white',font=("Microsoft YaHei UI Light", 23, "bold"),fg='DodgerBlue4')
        self.header_label.place(x=100, y=5)

        # self.email_label = tk.Label(self, text="E-Mail:",bg='slate gray',font=8,fg='Black')
        # self.email_label.place(relx=0.2, rely=0.3)


        self.email_entry = tk.Entry(self.login_frame,width=25,fg='black',border=0,bg="white",font=("Microsoft YaHei UI Light", 11))
        self.email_entry.place(x=30, y=80)
        self.email_entry.insert(0,'Email')

        self.email_entry.bind('<FocusIn>', self.on_enter)
        self.email_entry.bind('<FocusOut>', self.on_leave)

        self.frame1=tk.Frame(self.login_frame,width=295,height=2,bg='black')
        self.frame1.place(x=25,y=107)

        self.password_entry = tk.Entry(self.login_frame,width=25,fg='black',border=0,bg="white",font=("Microsoft YaHei UI Light", 11))
        self.password_entry.place(x=30, y=150)
        self.password_entry.insert(0,'Password')

        # Bind events for password entry
        self.password_entry.bind('<FocusIn>', self.on_enter_password)
        self.password_entry.bind('<FocusOut>', self.on_leave_password)


        self.frame2=tk.Frame(self.login_frame,width=295,height=2,bg='black')
        self.frame2.place(x=25,y=177)

        # sign in button
    
        self.signin_button = tk.Button(self.login_frame, text='Sign in', command=self.submit_form, width=39,pady=7,bg='DodgerBlue4',fg='white',border=0)
        self.signin_button.place(x=35, y=204)

        #creating signup button
        self.label=tk.Label(self.login_frame,text="Don't have an account?",fg='black',bg='white',font=("Microsoft YaHei UI Light", 9))
        self.label.place(x=75,y=270)

        self.greet_button = tk.Button(self.login_frame, text='Sign up', command=self.open_registration_screen,border=0,bg='white',cursor='hand2',fg='DodgerBlue4')
        self.greet_button.place(x=215,y=270)

        # # Add a exit button

        # self.exit_button = tk.Button(self, text='Exit', command=self.destroy,bg='slate gray',bd=0)
        # self.exit_button.place(relx=0.5,rely=0.5)

    def submit_form(self):
        login = Login()
        self.user.email = self.email_entry.get()
        self.user.password = self.password_entry.get()
        loggedIn = login.ValidateUser(self.user)
        if loggedIn == 1:
            if self.user.password == "PASSINIT":
                # EmailService.send_Email(self.user.email,"One-Time Email Verification Code",EmailMessagesTemplate.getEmailMessagesTemplateForLogin().format("verification_code",self.otpGenerator.generateOTP()))
                self.withdraw()
                ChangePasswordScreen(self.user,self)
                return
            else:
                self.withdraw()
                category_screen = CategoryScreen()
        else:
            return
   
            
    def open_registration_screen(self):
        self.withdraw()
        self.reg = RegistrationScreen(self)

    def on_enter(self,event):
        self.email_entry.delete(0,'end')

    def on_leave(self,event):
        name = self.email_entry.get()
        if name=='':
            self.email_entry.insert(0,'Email')
    def on_enter_password(self, event):
        self.password_entry.delete(0, 'end')
        self.password_entry.config(show='*')  # Show asterisks for password

    def on_leave_password(self, event):
        password = self.password_entry.get()
        if password == '':
            self.password_entry.insert(0, 'Password')
            self.password_entry.config(show='')  # Show plain text for placeholder

   
