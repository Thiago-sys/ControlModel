import mysql.connector
import os

class DatabaseManager:
    def __init__(self):
        self.connection = mysql.connector.connect(option_files=os.path.expanduser('Control.my.cnf'))
        self.cursor = self.connection.cursor()

    def execute_query(self, query, values=None):
        self.cursor.execute(query, values)
        self.connection.commit()

    def fetch_data(self, query, values=None):
        self.cursor.execute(query, values)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()
