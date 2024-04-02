from config.DatabaseManager import DatabaseManager


class CategoryQuery:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.db_manager = DatabaseManager()

    def get_Categories(self):
        query = "SELECT Category_ID, Category_Name, CategoryImageUrl FROM tbl_category"
        return self.db_manager.execute_query(query, fetchall=True)
