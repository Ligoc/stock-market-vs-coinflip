import sqlite3
from sqlite3 import Error

class SQLite3Connectioin:

    
    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(r".\backend\db.sqlite3")
            print(sqlite3.version)
        except Error as e:
            print(e)
        # finally:
        #     if conn:
        #         conn.close()
        return conn