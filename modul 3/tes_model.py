
from models.buku_model import BukuModel

model = BukuModel()

# Menguji penambahan buku
berhasil = model.create_buku(
    "Pemrograman Python",
    "Guido van Rossum",
    2023
)

if berhasil:
    print("Data buku berhasil ditambahkan.")

# Menguji pembacaan data
print("\nDaftar Buku:")
daftar_buku = model.get_all_buku()

for buku in daftar_buku:
    print(buku)
