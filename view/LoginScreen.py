import tkinter as tk
import logging
from tkinter import messagebox

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w',format='%(name)s - %(levelname)s - %(message)s')

class LoginScreen(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Desimart")
        log = logging.getLogger(self.__class__.__name__)
        log.info("Opened Login Screen")
        #self.login_frame = tk.Frame(self)
        # Place the inner frame at the center of the outer frame
        #self.login_frame.pack(fill=tk.BOTH, expand=True)

        self.loginFrame = tk.Frame(self)
        self.loginFrame.pack(fill=tk.BOTH, expand=True)

        # Username Label and Text Entry Box within the frame
        self.usernameLabel = tk.Label(self.loginFrame, text="Username")
        self.usernameLabel.place(relx=0.2, rely=0.3)
        self.usernameEntry = tk.Entry(self.loginFrame)
        self.usernameEntry.place(relx=0.5, rely=0.3)

        # Password Label and Password Entry Box within the frame
        self.passwordLabel = tk.Label(self.loginFrame, text="Password")
        self.passwordLabel.place(relx=0.2, rely=0.5)
        self.passwordEntry = tk.Entry(self.loginFrame, show="*")
        self.passwordEntry.place(relx=0.5, rely=0.5)

        # Login Button within the frame
        self.loginButton = tk.Button(self.loginFrame, text="Login", command=self.login)
        self.loginButton.place(relx=0.5, rely=0.7, anchor='center')

        
    def login(self):
        # Implement the login functionality here
        # For demonstration, we'll just show a message box
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        messagebox.showinfo("Login Info", f"You entered Username: {username} and Password: {password}")

