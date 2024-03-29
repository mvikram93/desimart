import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from model.UserModel import User
from config.DatabaseManager import DatabaseManager
from view.ProductsScreen import ProductsScreen

class CategoryScreen(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Category Screen")
        self.geometry("890x500+300+200")
        self.resizable(False, False)
        self.configure(bg='white')

        # Load and display background image
        self.background_image = Image.open("resources/desi1.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self, image=self.background_photo, bg="white")
        self.background_label.place(x=15, y=5)

        # Create frame to hold category buttons and images
        self.user = User()
        self.category_frame = tk.Frame(self, bg="white")
        self.category_frame.place(relx=0.5, rely=0.7, anchor=S)

        self.db_manager = DatabaseManager()  # Create an instance of DatabaseManager
        self.category_images = []  # List to store PhotoImage objects

        self.fetch_categories()

    def fetch_categories(self):
        self.db_manager.connect()  # Connect to the database
        try:
            query = "SELECT Category_ID, Category_Name, CategoryImageUrl FROM tbl_category"
            categories = self.db_manager.execute_query(query, fetchall=True)
    
            for idx, category in enumerate(categories):
                # Load and display category image
                category_image = Image.open(category[2])  #category[2] contains relative image path
                category_image = category_image.resize((130, 130))  # Resize image 

                category_photo = ImageTk.PhotoImage(category_image)
                self.category_images.append(category_photo)  # Store the PhotoImage object
                
                category_image_label = tk.Label(self.category_frame, image=category_photo, bg="white")
                category_image_label.grid(row=0, column=idx, padx=10, pady=10)

                # Create and display category button
                category_button = tk.Button(self.category_frame, text=category[1], command=lambda cat_id=category[0]: self.category_selected(cat_id), bg='white', border=0)
                category_button.grid(row=1, column=idx, padx=10, pady=10)
        finally:
            self.db_manager.close()  # Close the database connection

    def category_selected(self, category_id):
        # print(f"Category ID selected: {category_id}")
        self.withdraw()
        ProductsScreen(category_id)
        

# Create the CategoryScreen instance and start the main loop
# category_screen = CategoryScreen()
# category_screen.mainloop()


