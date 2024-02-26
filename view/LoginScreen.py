import tkinter as tk
import logging
class LoginScreen(tk.Toplevel):
    def __init__(self, parent,logging):
        super().__init__(parent)
        self.title("Desimart")
        log = logging.getLogger(self.__class__.__name__)
        log.info("Opened Login Screen")
       ## self.geometry("300x200")  # Set the window size
        self.frame_login = tk.Frame(self)
        self.frame_login.pack(padx=10, pady=10, fill='x', expand=True)
        self.label_username = tk.Label(self.frame_login, text="Username")
        self.label_username.pack(fill='x', expand=True)
        self.entry_username = tk.Entry(self.frame_login)
        self.entry_username.pack(fill='x', expand=True)
        self.entry_username.focus()

        # Add widgets to the new screen
        tk.Label(self.frame_login, text="Login!").pack(pady=20)
        tk.Button(self.frame_login, text="Close", command=self.destroy).pack()
        
