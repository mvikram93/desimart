from config import DatabaseManager
from config.DatabaseManager import DatabaseManager


class OrderQuery:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.db_manager = DatabaseManager()

    def place_Order(self, order):
        query = "Insert into desimart.tbl_order(order_id,Tax_Price,Total_Price,Order_Date_Time,User_ID) values(%s,%s,%s,now(),%s)"
        self.db_manager.execute_query(query, (order.OrderID, order.Tax_Price, order.Total_Price,order.User_ID))
        return 1

    def getOrderID(self):
        query = "Select count(*) from tbl_order"
        return self.db_manager.execute_query(query)

    def place_Items(self, item,orderID,userID):
        query = "Insert into tbl_order_line(Product_ID,Order_ID,Quantity,Price,total_amount) Values(%s,%s,%s,%s,%s)"
        self.db_manager.execute_query(query, (item.productID, orderID, item.qty,item.price,userID))
        return 1
    
    def get_order_lines(self, order_id):
        query = "SELECT Product_ID, Quantity FROM tbl_order_line WHERE Order_ID = %s"
        return self.db_manager.execute_query(query, params=(order_id,), fetchall=True)

    def get_product_details(self, product_id):
        query = "SELECT Product_Name, Price FROM tbl_product WHERE Product_ID = %s"
        params = (product_id,)
        return self.db_manager.execute_query(query, params=params, fetchall=False)
  

