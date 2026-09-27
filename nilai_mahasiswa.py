# Program Menghitung Nilai Mahasiswa

print("=== PROGRAM NILAI MAHASISWA ===")

# Input data mahasiswa
nama = input("Masukkan nama mahasiswa: ")
nim = input("Masukkan NIM: ")

# Input nilai
tugas = float(input("Masukkan nilai Tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

# Menghitung nilai akhir
nilai_akhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)

# Menentukan grade
if nilai_akhir >= 85:
    grade = "A"
elif nilai_akhir >= 75:
    grade = "B"
elif nilai_akhir >= 65:
    grade = "C"
elif nilai_akhir >= 50:
    grade = "D"
else:
    grade = "E"

# Menentukan keterangan
if nilai_akhir >= 65:
    keterangan = "LULUS"
else:
    keterangan = "TIDAK LULUS"
90
# Menampilkan hasil
print("\n=== HASIL NILAI MAHASISWA ===")
print("Nama        :", nama)
print("NIM         :", nim)
print("Nilai Tugas :", tugas)
print("Nilai UTS   :", uts)
print("Nilai UAS   :", uas)
print("Nilai Akhir :", nilai_akhir)
print("Grade       :", grade)
print("Keterangan  :", keterangan)
