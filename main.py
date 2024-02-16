import tkinter as tk
from config.db import DatabaseManager
root = tk.Tk()
root.title("Hello Tkinter")
db_val = DatabaseManager()
db_val.connect()
db_val.close()
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()
root.mainloop()
