import mysql.connector
from yamlconfig import config

class DatabaseManager:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=config['database']['host'],
                user=config['database']['user'],
                password=config['database']['password'],
                database=config['database']['database']
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


