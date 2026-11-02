from models.anggota_model import AnggotaModel

# Menginisialisasi class
model = AnggotaModel()

# 1. Tes CREATE (Menambah data anggota)
print("Menambahkan anggota baru...")
# Silakan ubah nama dan alamat sesuai keinginan
hasil_create = model.create_anggota("Budi Santoso", "Jl. Merdeka No. 45") 
if hasil_create:
    print("Berhasil menambah anggota!\n")
else:
    print("Gagal menambah anggota.\n")

# 2. Tes READ (Mengambil data anggota)
print("Daftar Anggota:")
daftar_anggota = model.get_all_anggota()

if len(daftar_anggota) > 0:
    for anggota in daftar_anggota:
        print(anggota)
else:
    print("Belum ada data anggota.")
    
