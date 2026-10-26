class AnggotaModel:
    def __init__(self, conn):
        self.conn = conn

    def create_anggota(self, nama, alamat):
        cursor = self.conn.cursor()
        sql = """
            INSERT INTO anggota (nama, alamat)
            VALUES (%s, %s)
        """
        cursor.execute(sql, (nama, alamat))
        self.conn.commit()
        id_anggota = cursor.lastrowid
        cursor.close()
        return id_anggota

    def read_anggota(self):
        cursor = self.conn.cursor(dictionary=True)
        sql = """
            SELECT id_anggota, nama, alamat
            FROM anggota
        """
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        return data