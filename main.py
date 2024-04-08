# import tkinter as tk
# from tkinter import ttk

# # Main window
# root = tk.Tk()
# root.title('Order Screen')

# # Customer details frame
# customer_frame = ttk.LabelFrame(root, text='Customer Details', padding="10")
# customer_frame.grid(row=0, column=0, sticky=(tk.W + tk.E), padx=10, pady=10)

# # Labels and entry widgets for customer details
# ttk.Label(customer_frame, text='Name:').grid(row=0, column=0, sticky=tk.W)
# customer_name_entry = ttk.Entry(customer_frame, width=25)
# customer_name_entry.grid(row=0, column=1)

# ttk.Label(customer_frame, text='Address:').grid(row=1, column=0, sticky=tk.W)
# customer_address_entry = ttk.Entry(customer_frame, width=25)
# customer_address_entry.grid(row=1, column=1)

# ttk.Label(customer_frame, text='Phone:').grid(row=2, column=0, sticky=tk.W)
# customer_phone_entry = ttk.Entry(customer_frame, width=25)
# customer_phone_entry.grid(row=2, column=1)

# # Order details frame
# order_frame = ttk.LabelFrame(root, text='Order Details', padding="10")
# order_frame.grid(row=1, column=0, sticky=(tk.W + tk.E), padx=10, pady=10)

# # Treeview for order items
# columns = ('Product', 'Qty', 'Price')
# order_tree = ttk.Treeview(order_frame, columns=columns, show='headings')
# order_tree.heading('Product', text='Product')
# order_tree.heading('Qty', text='Qty')
# order_tree.heading('Price', text='Price')
# order_tree.grid(row=0, column=0, sticky=(tk.W + tk.E))

# # Insert the example row (as in the image)
# order_tree.insert('', tk.END, values=('Onions', 2, '$5.50'))

# # Button to remove an item
# remove_button = ttk.Button(order_frame, text='Remove item')
# remove_button.grid(row=1, column=0, sticky=tk.E, padx=10, pady=10)

# # Submit button
# submit_button = ttk.Button(root, text='Submit Order')
# submit_button.grid(row=2, column=0, sticky=tk.E, padx=10, pady=10)

# # Run the application
# root.mainloop()
