import tkinter as tk
from view.LoginScreen import LoginScreen as Login
import logging 

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w',format='%(name)s - %(levelname)s - %(message)s')
        

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        log = logging.getLogger(self.__class__.__name__)

        self.title("Desimart")
        log.info("Starting the application")
        # Create a Frame for the top part of the GUI
        self.top_frame = tk.Frame(self)
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create a Frame for the bottom part of the GUI
        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # Add buttons to the top frame
        self.greet_button = tk.Button(self.top_frame, text="Greet", command=self.greet)
        self.greet_button.pack(side=tk.LEFT)

        self.new_screen_button = tk.Button(self.top_frame, text="Open New Screen", command=self.open_new_screen)
        self.new_screen_button.pack(side=tk.LEFT)

        self.clear_button = tk.Button(self.top_frame, text="Clear", command=self.clear)
        self.clear_button.pack(side=tk.LEFT)

        # Add a quit button to the bottom frame
        self.quit_button = tk.Button(self.bottom_frame, text="Quit", command=self.destroy)
        self.quit_button.pack(side=tk.RIGHT)

    def greet(self):
        print("Hello, world!")

    def clear(self):
        print("Clearing...")

    def open_new_screen(self):
        # This will create and open a new window
        self.login = Login(self,logging)

# Create the application instance
app = Application()

# Start the application
app.mainloop()
