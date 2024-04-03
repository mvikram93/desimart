from config.DatabaseManager import DatabaseManager


class ProductQuery:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.db_manager = DatabaseManager()

    def get_Products(self,categoryID):
        query = "SELECT Product_ID, Product_name, Price, Qty FROM tbl_product WHERE Category_ID = %s"
        return self.db_manager.execute_query(query, (categoryID,), fetchall=True)
