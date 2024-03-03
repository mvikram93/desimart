import mysql.connector
from config import db

class UserQuery:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def get_user_by_id(self, user_id):
        db.DatabaseManager.connect()
        if not self.conn:
            print("Not connected to MySQL!")
            return None
        try:
            query = "SELECT * FROM users WHERE id = %s"
            self.cursor.execute(query, (user_id,))
            return self.cursor.fetchone()
        except mysql.connector.Error as e:
            print("Error executing query:", e)
        finally:
            db.DatabaseManager.close()

    def get_all_users(self):
        if not self.conn:
            print("Not connected to MySQL!")
            return None
        try:
            query = "SELECT * FROM users"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print("Error executing query:", e)

    def add_user(self, username, email):
        if not self.conn:
            print("Not connected to MySQL!")
            return None
        try:
            query = "INSERT INTO users (username, email) VALUES (%s, %s)"
            self.cursor.execute(query, (username, email))
            self.conn.commit()
            print("User added successfully!")
        except mysql.connector.Error as e:
            print("Error executing query:", e)

    def close(self):
        if self.conn:
            self.conn = None
      
