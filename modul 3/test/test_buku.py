# Ario Setiawan F5212520076
from unittest.mock import MagicMock
from models.buku_model import BukuModel

# =========================================================
# 1. Unit Test: Test Tambah Data (Sesuai Prosedur Kerja Poin 5)
# =========================================================
def test_create_buku_berhasil():
    # 1. Menginisialisasi model
    model = BukuModel()

    # 2. Membuat mock koneksi dan cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    # 3. Menghubungkan cursor dengan koneksi
    mock_conn.cursor.return_value = mock_cursor

    # 4. Mengganti database dengan mock
    model.db = MagicMock()
    model.db.get_connection.return_value = mock_conn

    # 5. Menjalankan fungsi tambah buku
    hasil = model.create_buku(
        "Buku Testing", "Penulis QA", 2026
    )

    # 6. Memeriksa hasil pengujian
    assert hasil is True
    mock_cursor.execute.assert_called_once()
    mock_conn.commit.assert_called_once()


# =========================================================
# 2. Unit Test: Test Ambil Semua Data (Sesuai Tugas Poin 3)
# =========================================================
def test_get_all_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()

  # Memanipulasi (Mock) koneksi database agar tidak mengotori data asli
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor
    
    # --- TAMBAHKAN BARIS INI ---
    model.cursor = mock_cursor