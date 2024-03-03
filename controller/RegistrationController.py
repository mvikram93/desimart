from tkinter import messagebox


class RegistrationController:
    def register_user_details(firstname, lastname, email, phone, address, state):
    # You can perform further validation or processing here
        messagebox.showinfo("Registration Details", f"First Name: {firstname}\nLast Name: {lastname}\nEmail ID: {email}\nPhone Number: {phone}\nAddress: {address}\nState: {state}")