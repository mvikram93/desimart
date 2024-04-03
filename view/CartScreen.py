# CartScreen.py

import tkinter as tk
from PIL import Image, ImageTk
from config.CartManager import CartManager

class CartScreen(tk.Toplevel):
    def __init__(self, cart_items):
        super().__init__()
        self.cart_manager = CartManager()
        self.cart_items = cart_items  # Store cart_items passed from ProductsScreen
        self.title("Cart")
        self.geometry("890x500+300+200")
        self.resizable(False, False)
        self.configure(bg='white')
        self.category_id = cart_items[0].categoryID
        # Load and display background image
        self.background_image = Image.open("resources/desi1.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self, image=self.background_photo, bg="white")
        self.background_label.place(x=15, y=5)
        self.back_button=tk.Button(self, text="Back",fg='black',bg='white',font=("Microsoft YaHei UI Light", 13,"bold"),command=self.back_to_products_screen,border=0)
        self.back_button.place(x=800,y=130)

        self.display_cart()

    def display_cart(self):

        self.label_product_name = tk.Label(self, text="Product", bg="white",font=("Microsoft YaHei UI Light", 10, "bold"))
        self.label_product_name.place(x=70, y=150)
        
        self.label_qty = tk.Label(self, text="Qty", bg="white",font=("Microsoft YaHei UI Light", 10, "bold"))
        self.label_qty.place(x=190, y=150)

        label_price = tk.Label(self, text="Price", bg="white",font=("Microsoft YaHei UI Light", 10, "bold"))
        label_price.place(x=290, y=150)
        
        # Display cart items
        for idx, item in enumerate(self.cart_items):
            y_coordinate = 180 + idx * 30

            label_product_name = tk.Label(self, text=item.productname, bg="white")
            label_product_name.place(x=70, y=y_coordinate)
            
            label_qty = tk.Label(self, text=item.qty, bg="white")
            label_qty.place(x=190, y=y_coordinate)

            label_price = tk.Label(self, text=f"${item.price}", bg="white")
            label_price.place(x=290, y=y_coordinate)
            
            remove_button = tk.Button(self, text="Remove item", command=lambda idx=idx: self.remove_item(idx))
            remove_button.place(x=400, y=y_coordinate)

    def remove_item(self, idx):
        if idx < len(self.cart_items):  # Ensure idx is within the range of cart_items
            removed_item = self.cart_items[idx]  # Get the item to be removed
            self.cart_manager.remove_from_cart(removed_item)  # Use CartManager to remove the item
            self.cart_items = self.cart_manager.get_cart_items()  # Update cart_items after removal

            # Store widgets to be removed
            widgets_to_remove = []

            # Find and mark widgets to be removed
            for widget in self.winfo_children():
                if widget.winfo_y() == 180 + idx * 30:
                    widgets_to_remove.append(widget)

            # Destroy marked widgets
            for widget in widgets_to_remove:
                widget.destroy()

            # Shift down the widgets below the removed item
            for widget in self.winfo_children():
                if widget.winfo_y() > 180 + idx * 30:
                    widget.place_configure(y=widget.winfo_y() - 30)

            # Check if cart is empty
            if not self.cart_items:
                empty_cart_label = tk.Label(self, text="Cart is empty!", bg="white", font=("Microsoft YaHei UI Light", 12))
                empty_cart_label.place(x=350, y=200)


    def back_to_products_screen(self):
        self.withdraw()
        from view.ProductsScreen import ProductsScreen
        ProductsScreen(self.category_id)
