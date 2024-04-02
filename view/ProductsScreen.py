import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from config.DatabaseManager import DatabaseManager
from model.CartModel import cart
from view.CartScreen import CartScreen
from tkinter import messagebox
from config.CartManager import CartManager

class ProductsScreen(tk.Toplevel):
    def __init__(self, category_id):
        super().__init__()
        self.cart_manager = CartManager()
        self.title("Products Screen")
        self.geometry("890x500+300+200")
        self.resizable(False, False)
        self.configure(bg='white')
        self.category_id = category_id
   

        # Load and display background image
        self.background_image = Image.open("resources/desi1.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self, image=self.background_photo, bg="white")
        self.background_label.place(x=15, y=5)
        self.back_button=tk.Button(self, text="Back",fg='black',bg='white',font=("Microsoft YaHei UI Light", 13,"bold"),command=self.back_to_Categories_screen,border=0)
        self.back_button.place(x=800,y=130)
        self.go_to_cart_button = tk.Button(self, text="Go to Cart", command=self.go_to_cart,font=("Microsoft YaHei UI Light", 12),fg='DodgerBlue4',border=0,bg='white')
        self.go_to_cart_button.place(x=780, y=170)

        # Create frame to hold product details and buttons
        self.product_frame = tk.Frame(self,width=450,height=400,bg='white')
        self.product_frame.place(x=70,y=130)


        self.db_manager = DatabaseManager()  # Create an instance of DatabaseManager

        self.display_products()

    def display_products(self):
        self.db_manager.connect()  # Connect to the database
        try:
            query = "SELECT Product_ID, Product_name, Price, Qty FROM tbl_product WHERE Category_ID = %s"
            products = self.db_manager.execute_query(query, (self.category_id,), fetchall=True)
            # print("Products:", products)
            product_label_product = tk.Label(self.product_frame, text="Product", bg="white",font=("Microsoft YaHei UI Light", 10, "bold"))
            product_label_product.place(x=20,y=5)
            product_label_price = tk.Label(self.product_frame, text="Price", bg="white",font=("Microsoft YaHei UI Light", 10, "bold"))
            product_label_price.place(x=140,y=5)
            product_label_qty = tk.Label(self.product_frame, text="Qty", bg="white",font=("Microsoft YaHei UI Light", 10, "bold"))
            product_label_qty.place(x=240,y=5)
            # Display products on the screen
            for idx, product in enumerate(products):
                y_coordinate = 50 + idx * 30  
                product_label = tk.Label(self.product_frame, text=f"{product[1]}", bg="white")
                product_label.place(x=20, y=y_coordinate)
                product_label = tk.Label(self.product_frame, text=f"{product[2]}", bg="white")
                product_label.place(x=140, y=y_coordinate)
                product_label = tk.Label(self.product_frame, text=f"{product[3]}", bg="white")
                product_label.place(x=240, y=y_coordinate)
                spinbox_value = tk.StringVar()  # Create a StringVar to store the Spinbox value
                spinbox = Spinbox(self.product_frame, from_=0, to=10, width=3, textvariable=spinbox_value)  # Pass the StringVar to the Spinbox
                spinbox.place(x=300, y=y_coordinate)
                add_to_cart_button = tk.Button(self.product_frame, text="Add to Cart", command=lambda prod_id=product[0], prod_name=product[1], price=product[2], category_id=self.category_id, spinbox_value=spinbox_value: self.add_to_cart(prod_id, prod_name, price, category_id, spinbox_value.get()))
                add_to_cart_button.place(x=350, y=y_coordinate)


        finally:
            self.db_manager.close()  # Close the database connection

    def add_to_cart(self, product_id, product_name, price, category_id, qty):
        qty = int(qty)
        if int(qty) > 0:
            cart_item = cart(productname=product_name, productID=product_id, price=price, categoryID=category_id, qty=qty)
            self.cart_manager.add_to_cart(cart_item)
            print(f"Added product {product_name} with ID {product_id} to cart with quantity {qty} and price {price}.")
    
    def go_to_cart(self):
        cart_items = self.cart_manager.get_cart_items()
        if cart_items:  # Check if cart is not empty
            self.withdraw()
            cart_window = CartScreen(cart_items=cart_items)

    def back_to_Categories_screen(self):
        self.withdraw()
        from view.CategoriesScreen import CategoryScreen
        CategoryScreen()
