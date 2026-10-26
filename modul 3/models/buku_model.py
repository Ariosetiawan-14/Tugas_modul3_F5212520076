
from config.database import Database


class BukuModel:
    def __init__(self):
        self.db = Database()
        self.table_name = "buku"

    def get_all_buku(self):
        conn = self.db.get_connection()
        if conn is None:
            return []

        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(
                f"SELECT * FROM {self.table_name}"
            )
            return cursor.fetchall()

        except Exception as e:
            print(f"Gagal mengambil data buku: {e}")
            return []

        finally:
            cursor.close()
            conn.close()

    def create_buku(self, judul, penulis, tahun_terbit):
        conn = self.db.get_connection()
        if conn is None:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = """
                INSERT INTO buku (judul, penulis, tahun_terbit)
                VALUES (%s, %s, %s)
            """
            cursor.execute(
                query, (judul, penulis, tahun_terbit)
            )
            conn.commit()
            return True

        except Exception as e:
            conn.rollback()
            print(f"Gagal menambah buku: {e}")
            return False

        finally:
            if cursor is not None:
                cursor.close()
            conn.close()
