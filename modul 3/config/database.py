
import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self):
        self.host = "localhost"
        self.database = "perpustakaan"
        self.user = "root"
        self.password = ""
        
    def get_connection(self):
        try:
            conn = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if conn.is_connected():
                print("Koneksi database berhasil!")
                return conn

        except Error as e:
            print(f"Koneksi database gagal: {e}")

        return None
