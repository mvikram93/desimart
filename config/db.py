import mysql.connector
from config.yamlconfig import ConfigLoader

class DatabaseManager:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.config = ConfigLoader("./application.yaml").get_config()
        ##self.config_data = self.config.get_config()
    def connect(self):
        print(self.config)
        try:
            self.conn = mysql.connector.connect(
                host=self.config['database']['host'],
                user=self.config['database']['user'],
                password=self.config['database']['password'],
                database=self.config['database']['database']
            )
            self.cursor = self.conn.cursor()
            print("Connected to MySQL!")
        except mysql.connector.Error as e:
            print("Error connecting to MySQL:", e)

    def execute_query(self, query):
        if not self.conn:
            print("Not connected to MySQL!")
            return
        try:
            self.cursor.execute(query)
            print("Query executed successfully!")
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print("Error executing query:", e)

    def close(self):
        if self.conn:
            self.cursor.close()
            self.conn.close()
            print("Connection to MySQL closed!")


