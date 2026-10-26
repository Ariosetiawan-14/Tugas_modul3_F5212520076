from config.database import Database

class AnggotaModel:
    def __init__(self):
        # Inisialisasi koneksi database
        self.db = Database()
        self.table_name = "anggota"

    def get_all_anggota(self):
        # Operasi READ: Mengambil semua data dari tabel anggota
        conn = self.db.get_connection()
        if conn is None:
            return []

        try:
            # dictionary=True agar hasil yang dikembalikan berformat dictionary
            cursor = conn.cursor(dictionary=True)
            cursor.execute(f"SELECT * FROM {self.table_name}")
            return cursor.fetchall()
            
        except Exception as e:
            print(f"Gagal mengambil data anggota: {e}")
            return []
            
        finally:
            if 'cursor' in locals() and cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()

    def create_anggota(self, nama, alamat):
        # Operasi CREATE: Menambahkan data baru ke tabel anggota
        conn = self.db.get_connection()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
            # id_anggota diasumsikan AUTO_INCREMENT di database, sehingga tidak perlu di-insert manual
            sql = f"INSERT INTO {self.table_name} (nama, alamat) VALUES (%s, %s)"
            cursor.execute(sql, (nama, alamat))
            conn.commit()
            return True
            
        except Exception as e:
            conn.rollback()
            print(f"Gagal menambah anggota: {e}")
            return False
            
        finally:
            if 'cursor' in locals() and cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()