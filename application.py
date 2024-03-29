import tkinter as tk
from view.LoginScreen import LoginScreen
import logging

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')




# Create the application instance
app = LoginScreen()

# Start the application
app.mainloop()
