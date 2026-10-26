from models.buku_model import BukuModel

model = BukuModel()

def tampilkan_buku(judul_tabel):
    print(f"\n--- {judul_tabel} ---")
    for buku in model.get_all_buku():
        # Menggunakan .get() agar kode otomatis mengenali apakah nama kolomnya 'id' atau 'id_buku' di database Anda
        id_buku = buku.get('id', buku.get('id_buku'))
        print(f"[{id_buku}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")

# ==========================================
# 1. CREATE
# ==========================================
print("Menambahkan data buku...")
model.create_buku("Pemrograman Python MVC", "Guido van Rossum", 2023)
print("Data berhasil disimpan ke MySQL!")

# Tampilkan data setelah di-create
tampilkan_buku("Daftar Buku (setelah CREATE)")

# Ambil ID buku terakhir yang baru saja ditambahkan untuk diuji pada Update & Delete
daftar_buku = model.get_all_buku()
id_terakhir = daftar_buku[-1].get('id', daftar_buku[-1].get('id_buku'))

# ==========================================
# 2. UPDATE
# ==========================================
print(f"\nMengupdate buku dengan id {id_terakhir}...")
# Mengubah judul menjadi ada tambahan "(Revisi)" dan tahun menjadi 2024
if model.update_buku(id_terakhir, "Pemrograman Python MVC (Revisi)", "Guido van Rossum", 2024):
    print("Data berhasil diupdate!")
else:
    print("Gagal update: id tidak ditemukan.")

# Tampilkan data setelah di-update
tampilkan_buku("Daftar Buku (setelah UPDATE)")

# ==========================================
# 3. DELETE
# ==========================================
print(f"\nMenghapus buku dengan id {id_terakhir}...")
if model.delete_buku(id_terakhir):
    print("Data berhasil dihapus!")
else:
    print("Gagal hapus: id tidak ditemukan.")

# Tampilkan data setelah di-delete
tampilkan_buku("Daftar Buku (setelah DELETE)")
