import tkinter as tk
from PIL import Image, ImageTk
from config.CartManager import CartManager
from view.CheckoutScreen import CheckoutScreen

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
        self.back_button = tk.Button(self, text="Back", fg='black', bg='white', font=("Microsoft YaHei UI Light", 13, "bold"), command=self.back_to_products_screen, border=0)
        self.back_button.place(x=800, y=130)
        self.display_cart()

    def display_cart(self):
        self.cart_frame = tk.Frame(self, bg="white")
        self.cart_frame.place(x=50, y=110, width=450, height=300)

        self.label_product_name = tk.Label(self.cart_frame, text="Product", bg="white", font=("Microsoft YaHei UI Light", 10, "bold"))
        self.label_product_name.place(x=20, y=10)

        self.label_qty = tk.Label(self.cart_frame, text="Qty", bg="white", font=("Microsoft YaHei UI Light", 10, "bold"))
        self.label_qty.place(x=160, y=10)

        label_price = tk.Label(self.cart_frame, text="Price", bg="white", font=("Microsoft YaHei UI Light", 10, "bold"))
        label_price.place(x=260, y=10)

        self.cart_widgets = {} # Dictionary to store widgets associated with each item

        self.total=0

        # Display cart items
        for idx, item in enumerate(self.cart_items):
            y_coordinate = 40 + idx * 30

            self.total+=(item.price)*int(item.qty)

            label_product_name = tk.Label(self.cart_frame, text=item.productname, bg="white")
            label_product_name.place(x=20, y=y_coordinate)

            label_qty = tk.Label(self.cart_frame, text=item.qty, bg="white")
            label_qty.place(x=160, y=y_coordinate)

            label_price = tk.Label(self.cart_frame, text=f"${item.price}", bg="white")
            label_price.place(x=260, y=y_coordinate)

            remove_button = tk.Button(self.cart_frame, text="Remove item", command=lambda idx=idx: self.remove_item(idx,self.total))
            remove_button.place(x=350, y=y_coordinate)
            
            # Store widgets associated with the item
            self.cart_widgets[idx] = (label_product_name, label_qty, label_price, remove_button)

        label_subtotal = tk.Label(self, text=f"Subtotal : {self.total} ", bg="white", font=("Microsoft YaHei UI Light", 10, "bold"))
        label_subtotal.place(x=100, y=420)

        checkout_button = tk.Button(self, text="Continue to checkout", width=45, bg='DodgerBlue4',fg='white',border=0, font=("Microsoft YaHei UI Light", 10,"bold"), command=lambda: self.checkout_cart(self.cart_items))
        checkout_button.place(x=75, y=450)

    def remove_item(self, idx, total):
        if idx < len(self.cart_items):
            removed_item = self.cart_items[idx]  # Get the item to be removed
            total=total-(removed_item.price)*int(removed_item.qty)
            self.cart_manager.remove_from_cart(removed_item)  # Use CartManager to remove the item
            self.cart_items = self.cart_manager.get_cart_items()  # Update cart_items after removal

            # Remove widgets associated with the item
            if idx in self.cart_widgets:
                for widget in self.cart_widgets[idx]:
                    widget.destroy()
                del self.cart_widgets[idx]

                # Redraw the entire display
                for widget in self.cart_frame.winfo_children():
                    widget.destroy()

                # Redraw the header labels
                self.label_product_name = tk.Label(self.cart_frame, text="Product", bg="white", font=("Microsoft YaHei UI Light", 10, "bold"))
                self.label_product_name.place(x=20, y=10)

                self.label_qty = tk.Label(self.cart_frame, text="Qty", bg="white", font=("Microsoft YaHei UI Light", 10, "bold"))
                self.label_qty.place(x=160, y=10)

                label_price = tk.Label(self.cart_frame, text="Price", bg="white", font=("Microsoft YaHei UI Light", 10, "bold"))
                label_price.place(x=260, y=10)

                # Display cart items
                for idx, item in enumerate(self.cart_items):
                    y_coordinate = 40 + idx * 30

                    label_product_name = tk.Label(self.cart_frame, text=item.productname, bg="white")
                    label_product_name.place(x=20, y=y_coordinate)

                    label_qty = tk.Label(self.cart_frame, text=item.qty, bg="white")
                    label_qty.place(x=160, y=y_coordinate)

                    label_price = tk.Label(self.cart_frame, text=f"${item.price}", bg="white")
                    label_price.place(x=260, y=y_coordinate)

                    remove_button = tk.Button(self.cart_frame, text="Remove item", command=lambda idx=idx: self.remove_item(idx,total))
                    remove_button.place(x=350, y=y_coordinate)

                    # Store widgets associated with the item
                    self.cart_widgets[idx] = (label_product_name, label_qty, label_price, remove_button)

                # Check if cart is empty
                if not self.cart_items:
                    empty_cart_label = tk.Label(self.cart_frame, text="Cart is empty!", bg="white", font=("Microsoft YaHei UI Light", 12))
                    empty_cart_label.place(x=350, y=200)


                label_subtotal = tk.Label(self, text=f"Subtotal : {total} ", bg="white", font=("Microsoft YaHei UI Light", 10, "bold"))
                label_subtotal.place(x=100, y=420)

    def back_to_products_screen(self):
        self.withdraw()
        from view.ProductsScreen import ProductsScreen
        ProductsScreen(self.category_id)

    def checkout_cart(self, cart_items):
        self.withdraw()
        # total = sum(item.price * int(item.qty) for item in cart_items)  # Recalculate the total
        CheckoutScreen(cart_items)
