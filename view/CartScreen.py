import tkinter as tk
from PIL import Image, ImageTk

from model.CartModel import cart

class CartScreen(tk.Toplevel):
    def __init__(self, cart_items):
        super().__init__()
        self.title("Cart")
        self.geometry("890x500+300+200")
        self.resizable(False, False)
        self.configure(bg='white')
        # Load and display background image
        self.background_image = Image.open("resources/desi1.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self, image=self.background_photo, bg="white")
        self.background_label.place(x=15, y=5)
        self.back_button=tk.Button(self, text="Back",fg='black',bg='white',font=("Microsoft YaHei UI Light", 13,"bold"),command=self.back_to_products_screen,border=0)
        self.back_button.place(x=800,y=130)

        self.cart_items = cart_items
        # self.category_id=category_id

        self.display_cart()

    def display_cart(self):
        # Display cart items
        for idx, item in enumerate(self.cart_items):
            y_coordinate = 150 + idx * 30

            label_product_name = tk.Label(self, text=f"Product: {item.productname}", bg="white")
            label_product_name.place(x=70, y=y_coordinate)
            
            label_qty = tk.Label(self, text=f"Qty: {item.qty}", bg="white")
            label_qty.place(x=250, y=y_coordinate)

            label_price = tk.Label(self, text=f"Price: ${item.price}", bg="white")
            label_price.place(x=430, y=y_coordinate)
            
            remove_button = tk.Button(self, text="Remove", command=lambda idx=idx: self.remove_item(idx))
            remove_button.place(x=600, y=y_coordinate)

    def remove_item(self, idx):
        del self.cart_items[idx]
        # Clear the previous display and redisplay the cart items
        for widget in self.winfo_children():
            widget.destroy()
        self.display_cart()

    def back_to_products_screen(self):
        self.withdraw()
        from view.ProductsScreen import ProductsScreen
        category_id = self.cart_items[0].categoryID
        print(category_id)
        ProductsScreen(category_id)
