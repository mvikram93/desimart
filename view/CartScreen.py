import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from config.CartManager import CartManager
from view.CheckoutScreen import CheckoutScreen
from model.OrderModel import OrderModel
from query.OrderQuery import OrderQuery
from tkinter import messagebox


class CartScreen(tk.Toplevel):
    def __init__(self, cart_items, user):
        super().__init__()
        self.cart_manager = CartManager()
        self.cart_items = cart_items  # Store cart_items passed from ProductsScreen
        self.title("Cart")
        self.geometry("890x500+300+200")
        # Center the window on the screen
        self.update_idletasks()  # Update the window
        width = self.winfo_width()  # Get the width of the window
        height = self.winfo_height()  # Get the height of the window
        x = (self.winfo_screenwidth() // 2) - (width // 2)  # Calculate the x position
        y = (self.winfo_screenheight() // 2) - (height // 2)  # Calculate the y position
        self.geometry(f"+{x}+{y}")  # Set the new position
        self.resizable(False, False)
        self.configure(bg='white')
        self.category_id = cart_items[0].categoryID
        self.user = user
        # Load and display background image
        self.background_image = Image.open("resources/desi1.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self, image=self.background_photo, bg="white")
        self.background_label.place(x=15, y=5)
        self.back_button = tk.Button(self, text="Back", fg='black', bg='white',
                                     font=("Microsoft YaHei UI Light", 13, "bold"),
                                     command=self.back_to_products_screen, border=0)
        self.back_button.place(x=800, y=100)
        # for back to home
        self.home_img = Image.open("resources/home.png")
        self.home_bg = ImageTk.PhotoImage(self.home_img)
        self.home_button = tk.Button(self, image=self.home_bg, command=self.go_to_home, bg='white', border=0)
        self.home_button.place(x=15, y=90)
        # creating a label for checkout
        self.checkout_image = Image.open("resources/checkout.png")
        self.checkout_photo = ImageTk.PhotoImage(self.checkout_image)
        self.checkout_label = tk.Label(self, image=self.checkout_photo, bg="white")
        self.checkout_label.place(x=470, y=170)

        self.display_cart()

    def display_cart(self):
        self.cart_frame = tk.Frame(self, bg="white")
        self.cart_frame.place(x=65, y=110, width=450, height=300)

        # Creating a canvas to contain the inner frame
        self.canvas = tk.Canvas(self.cart_frame, bg="floralwhite")
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)

        # Bind mouse wheel events to the canvas
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(self.cart_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Linking the canvas to the scrollbar
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # Create another frame to hold your widgets inside the canvas
        self.inner_frame = tk.Frame(self.canvas, bg="floralwhite")
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor=tk.NW)

        self.label_product_name = tk.Label(self.inner_frame, text="Product", bg="floralwhite",
                                           font=("Microsoft YaHei UI Light", 10, "bold"))
        self.label_product_name.grid(row=0, column=0, padx=10, pady=5)

        self.label_qty = tk.Label(self.inner_frame, text="Qty", bg="floralwhite",
                                  font=("Microsoft YaHei UI Light", 10, "bold"))
        self.label_qty.grid(row=0, column=1, padx=10, pady=5)

        label_price = tk.Label(self.inner_frame, text="Price", bg="floralwhite",
                               font=("Microsoft YaHei UI Light", 10, "bold"))
        label_price.grid(row=0, column=2, padx=10, pady=5)

        self.cart_widgets = {}  # Dictionary to store widgets associated with each item

        self.total = 0

        # Display cart items
        for idx, item in enumerate(self.cart_items):
            # y_coordinate = idx * 30
            self.total += (item.price) * int(item.qty)

            label_product_name = tk.Label(self.inner_frame, text=item.productname, bg="floralwhite")
            label_product_name.grid(row=idx + 1, column=0, padx=10, pady=5)

            label_qty = tk.Label(self.inner_frame, text=item.qty, bg="floralwhite")
            label_qty.grid(row=idx + 1, column=1, padx=10, pady=5)

            label_price = tk.Label(self.inner_frame, text=f"${item.price}", bg="floralwhite")
            label_price.grid(row=idx + 1, column=2, padx=10, pady=5)

            remove_button = tk.Button(self.inner_frame, text="Remove item",
                                      command=lambda idx=idx: self.remove_item(idx), border=0, bg='floralwhite',
                                      fg='dodgerblue4', font=("Microsoft YaHei UI Light", 8, "bold"))
            remove_button.grid(row=idx + 1, column=3, padx=10, pady=5)

            # Store widgets associated with the item
            self.cart_widgets[idx] = (label_product_name, label_qty, label_price, remove_button)

        # Update the canvas scroll region
        self.inner_frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        label_subtotal = tk.Label(self, text=f"Subtotal : {self.total} ", bg="white",
                                  font=("Microsoft YaHei UI Light", 10, "bold"))
        label_subtotal.place(x=100, y=420)

        checkout_button = tk.Button(self, text="Continue to checkout", width=45, bg='DodgerBlue4', fg='floralwhite',
                                    border=0, font=("Microsoft YaHei UI Light", 10, "bold"),
                                    command=lambda: self.checkout_cart(self.cart_items))
        checkout_button.place(x=75, y=450)

    def remove_item(self, idx):
        if idx < len(self.cart_items):
            removed_item = self.cart_items.pop(idx)  # Remove the item from the cart list
            self.total -= (removed_item.price) * int(removed_item.qty)  # Update total

            if idx in self.cart_widgets:
                for widget in self.cart_widgets[idx]:
                    widget.destroy()  # Remove associated widgets
                del self.cart_widgets[idx]  # Remove reference from dictionary

            # Update the indices in cart_widgets after the removed item
            for key in range(idx, len(self.cart_items)):
                if key + 1 in self.cart_widgets:
                    # Update the key in cart_widgets to match the new index after removal
                    self.cart_widgets[key] = self.cart_widgets.pop(key + 1)

            # Check if cart is empty
            if not self.cart_items:
                empty_cart_label = tk.Label(self.cart_frame, text="Cart is empty!", bg="floralwhite",
                                            font=("Microsoft YaHei UI Light", 12))
                empty_cart_label.place(x=150, y=120)

            # Redraw the items in the inner frame
            self.redraw_inner_frame()

            # Update the subtotal label
            # self.update_subtotal_label()

    def redraw_inner_frame(self):
        # Clear the existing widgets
        for widget_list in self.cart_widgets.values():
            for widget in widget_list:
                widget.grid_forget()

        # Re-create widgets for each item
        for idx, item in enumerate(self.cart_items):
            label_product_name = tk.Label(self.inner_frame, text=item.productname, bg="floralwhite")
            label_product_name.grid(row=idx + 1, column=0, padx=10, pady=5)

            label_qty = tk.Label(self.inner_frame, text=item.qty, bg="floralwhite")
            label_qty.grid(row=idx + 1, column=1, padx=10, pady=5)

            label_price = tk.Label(self.inner_frame, text=f"${item.price}", bg="floralwhite")
            label_price.grid(row=idx + 1, column=2, padx=10, pady=5)

            remove_button = tk.Button(self.inner_frame, text="Remove item",
                                      command=lambda idx=idx: self.remove_item(idx), border=0, bg='floralwhite',
                                      fg='dodgerblue4', font=("Microsoft YaHei UI Light", 8, "bold"))
            remove_button.grid(row=idx + 1, column=3, padx=10, pady=5)

            # Update or add entry in cart_widgets
            self.cart_widgets[idx] = (label_product_name, label_qty, label_price, remove_button)

        label_subtotal = tk.Label(self, text=f"Subtotal : {self.total} ", bg="white",
                                  font=("Microsoft YaHei UI Light", 10, "bold"))
        label_subtotal.place(x=100, y=420)

        # Update the canvas scroll region
        self.inner_frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def back_to_products_screen(self):
        self.withdraw()
        from view.ProductsScreen import ProductsScreen
        ProductsScreen(self.category_id)

    def go_to_home(self):
        self.withdraw()
        from view.CategoriesScreen import CategoryScreen
        CategoryScreen()

    def checkout_cart(self, cart_items):
        total = sum(item.price * int(item.qty) for item in cart_items)
        order = OrderModel()
        orderQuery = OrderQuery()
        order_id_db_count = orderQuery.getOrderID()
        order.OrderID = order_id_db_count[0] + 1
        order.Tax_Price = 0.0
        order.Total_Price = total
        order.User_ID = self.user.userId
        order_placed = orderQuery.place_Order(order)
        for item in cart_items:
            items_placed = orderQuery.place_Items(item,order.OrderID,order.User_ID)
        if order_placed == 1 and items_placed == 1:
            self.withdraw()
            CheckoutScreen(cart_items, self.user,order.OrderID)
        else:
            messagebox.showerror("Error","Error while processing order. Please try again later")
    def on_mousewheel(self, event):
        if event.num == 5 or event.delta == -120:
            self.canvas.yview_scroll(1, "units")
        elif event.num == 4 or event.delta == 120:
            self.canvas.yview_scroll(-1, "units")

