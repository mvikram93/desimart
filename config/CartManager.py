
class CartManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.cart_items = []
        return cls._instance

    def add_to_cart(self, item):
        self.cart_items.append(item)

    def remove_from_cart(self, item):
        self.cart_items.remove(item)

    def clear_cart(self):
        self.cart_items = []

    def get_cart_items(self):
        return self.cart_items
