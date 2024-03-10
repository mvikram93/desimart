import mysql.connector
from config.yamlconfig import ConfigLoader


class DatabaseManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._connection = None
        return cls._instance

    def __init__(self):
        self._connection = None
        self.cursor = None
        self.config = ConfigLoader("./application.yaml").get_config()

    def connect(self):
        if not self._connection:
            try:
                self._connection = mysql.connector.connect(
                    host=self.config['database']['host'],
                    user=self.config['database']['user'],
                    password=self.config['database']['password'],
                    database=self.config['database']['database']
                )
                self.cursor = self._connection.cursor()
                print("Connected to MySQL!")
            except mysql.connector.Error as e:
                print("Error connecting to MySQL:", e)

    def execute_query(self, query, params=None, fetchall=False):
        self.connect()
        conn = self._connection
        cursor = conn.cursor(buffered=True)
        try:
            cursor.execute(query, params)
            conn.commit()
            if fetchall:
                return cursor.fetchall()
            else:
                return cursor.fetchone()
        except mysql.connector.Error as e:
            print("Error executing query:", e)
        finally:
            cursor.close()

    def close(self):
        if self._connection:
            self._connection.close()
            self._connection = None

    def get_connection(self):
        return self._connection
