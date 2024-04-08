import tkinter as tk
from config.CartManager import CartManager
from PIL import Image, ImageTk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkinter import filedialog
from service.EmailService import EmailService

class CheckoutScreen(tk.Toplevel):
    def __init__(self, cart_items, user, orderID):
        super().__init__()
        self.cart_manager = CartManager()
        self.cart_items = cart_items  # Store cart_items passed from the CartScreen
        self.title("Checkout")
        self.geometry("890x500+300+200")
        self.emailObj = EmailService()
        # Center the window on the screen
        self.update_idletasks()  # Update the window
        width = self.winfo_width()  # Get the width of the window
        height = self.winfo_height()  # Get the height of the window
        x = (self.winfo_screenwidth() // 2) - (width // 2)  # Calculate the x position
        y = (self.winfo_screenheight() // 2) - (height // 2)  # Calculate the y position
        self.geometry(f"+{x}+{y}")  # Set the new position
        self.resizable(False, False)
        self.configure(bg='white')
        self.user = user
        self.orderID = orderID
        print(self.user.firstname)
        # Display cart items and total for checkout
        # self.display_cart(cart_items, total)
        self.background_image = Image.open("resources/desi1.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self, image=self.background_photo, bg="white")
        self.background_label.place(x=15, y=5)
        # self.back_button=tk.Button(self, text="Back",fg='black',bg='white',font=("Microsoft YaHei UI Light", 13,"bold"),command=self.back_to_products_screen,border=0)
        # self.back_button.place(x=800,y=130)
        self.shutdown_button = tk.Button(self, text="Logout", bg="darkgoldenrod2", border=0, fg="black", width=8,
                                         command=self.open_loginscreen)
        self.shutdown_button.place(x=820, y=470)
        self.purchase_label = tk.Label(self,
                                       text=f"No minimum purchase requirement  |  Free shipping & handling  |  Default payment mode: COD",
                                       bg="white", fg="black", font=("Microsoft YaHei UI Light", 8))
        self.purchase_label.place(x=240, y=480)
        self.order_items()

    def order_items(self):
        self.total = sum(item.price * int(item.qty) for item in self.cart_items)  # Recalculate the total
        self.confirm_label = tk.Label(self, text=f"Thanks for placing the order! Your order is confirmed.", bg="white",
                                      fg="Black", font=("Microsoft YaHei UI Light", 13, "bold"))
        self.confirm_label.place(x=250, y=110)
        # for back to home
        self.home_img = Image.open("resources/home.png")
        self.home_bg = ImageTk.PhotoImage(self.home_img)
        self.home_button = tk.Button(self, image=self.home_bg, command=self.go_to_home, bg='white', border=0)
        self.home_button.place(x=15, y=90)
        self.print_button = tk.Button(self, text="Print", command=self.print_order, width=10, border=0,
                                      bg='dodgerblue4', fg='white', font=("Microsoft YaHei UI Light", 10, "bold"))
        self.print_button.place(x=350, y=425)
        self.Email_button = tk.Button(self, text="Email",command=lambda: self.emailObj.send_Email(self.user.email, self.orderID), width=10, border=0, bg='dodgerblue4', fg='white',
                                      font=("Microsoft YaHei UI Light", 10, "bold"))
        self.Email_button.place(x=500, y=425)
        self.order_frame = tk.Frame(self, bg="floralwhite")
        self.order_frame.place(x=250, y=150, width=470, height=265)
        self.total_label = tk.Label(self.order_frame, text=f"You pay: {self.total}", bg="floralwhite",
                                    font=("Microsoft YaHei UI Light", 10, "bold"))
        self.total_label.place(x=20, y=10)
        self.delivery_label = tk.Label(self.order_frame, text="Free shipping & handling ", bg="floralwhite",
                                       fg="dodgerblue4", font=("Microsoft YaHei UI Light", 8))
        self.delivery_label.place(x=20, y=35)
        self.delivery_label = tk.Label(self.order_frame, text="Estimated delivery time: 3-4 business days ",
                                       bg="floralwhite", fg="dodgerblue4", font=("Microsoft YaHei UI Light", 8))
        self.delivery_label.place(x=20, y=60)
        self.delivery_label = tk.Label(self.order_frame, text="Default payment mode: COD", bg="floralwhite",
                                       fg="dodgerblue4", font=("Microsoft YaHei UI Light", 8))
        self.delivery_label.place(x=20, y=85)

        self.line_label = tk.Label(self.order_frame, text=f"__________________________________________________________",
                                   bg="floralwhite", fg="black", font=("Microsoft YaHei UI Light", 10, "bold"))
        self.line_label.place(x=20, y=110)

        self.name_label = tk.Label(self.order_frame,
                                   text=f"Delivering to  {self.user.firstname + ' ' + self.user.lastname}",
                                   bg="floralwhite",
                                   font=("Microsoft YaHei UI Light", 10, "bold"))
        self.name_label.place(x=20, y=135)
        self.phoneNo_label = tk.Label(self.order_frame, text=f"Phone: {self.user.phone}", bg="floralwhite",
                                      font=("Microsoft YaHei UI Light", 10))
        self.phoneNo_label.place(x=20, y=160)
        self.email_label = tk.Label(self.order_frame, text=f"Email: {self.user.email}", bg="floralwhite",
                                    font=("Microsoft YaHei UI Light", 10))
        self.email_label.place(x=20, y=185)
        self.address = tk.Label(self.order_frame,
                                text=f"Address: {self.user.address + ',' + self.user.city + ',' + self.user.state + '-' + self.user.zipcode}",
                                bg="floralwhite",
                                font=("Microsoft YaHei UI Light", 10))
        self.address.place(x=20, y=210)
        self.order_id_label = tk.Label(self.order_frame, text=f"Order ID: {self.orderID}", bg="floralwhite",
                                       font=("Microsoft YaHei UI Light", 10))
        self.order_id_label.place(x=20, y=235)

    def go_to_home(self):
        self.withdraw()
        self.cart_items.clear()
        from view.CategoriesScreen import CategoryScreen
        CategoryScreen(self.user)

    def print_order(self):
        # Format the order confirmation details
        order_details = (
            f"\nOrder ID: {self.orderID}\n"
            f"Total: {self.total}\n"
            f"Free shipping & handling\n"
            f"Estimated delivery time: 3-4 business days\n"
            f"___________________________________________\n"
            f"Delivering to: {self.user.firstname} {self.user.lastname}\n"
            f"Phone: {self.user.phone}\n"
            f"Email: {self.user.email}\n"
            f"Address: {self.user.address}, {self.user.city}, {self.user.state} - {self.user.zipcode}\n"

        )

        # Allow the user to select a location to save the PDF
        filename = filedialog.asksaveasfilename(defaultextension=".pdf",
                                                initialfile=f"order_confirmation_{self.orderID}.pdf",
                                                filetypes=[("PDF files", "*.pdf")])
        if filename:
            # Create a PDF file
            c = canvas.Canvas(filename, pagesize=letter)

            c.drawString(100, 750, "Order Confirmation")
            c.drawString(100, 730, "-" * 50)

            # Split order_details into lines
            lines = order_details.split('\n')

            # Set initial y position for drawing text
            y_position = 710

            # Draw each line of text at the specified position
            for line in lines:
                c.drawString(100, y_position, line)
                y_position -= 20  # Adjust y position for the next line

            c.save()

    def open_loginscreen(self):
        self.withdraw()
