#Ario Setiawan Dg.Malino F5212520076
import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView

class BukuController:
    def __init__(self):
        # Inisialisasi Model dan View
        self.model = BukuModel()
        self.view = BukuView()

        # Binding (mengikat) tombol di View dengan fungsi di Controller
        self.view.btn_simpan.configure(command=self.simpan_data)

        # --- TAMBAHAN TUGAS 1: Binding tombol Hapus dan Perbarui ---
        # Pastikan nama tombol di file buku_view.py adalah btn_hapus dan btn_perbarui
        if hasattr(self.view, 'btn_hapus'):
            self.view.btn_hapus.configure(command=self.hapus_data)
        if hasattr(self.view, 'btn_perbarui'):
            self.view.btn_perbarui.configure(command=self.update_data)

        # Memuat data ke tabel saat aplikasi pertama kali dibuka
        self.muat_data_tabel()
        
    def update_data(self):
        # Nanti kode logika untuk memperbarui data database (Model) ditaruh di sini
        print("Tombol Perbarui berfungsi!")
        pass
    def delete_data(self):
        # Nanti kode logika untuk menghapus data ditaruh di sini
        print("Tombol Hapus berfungsi!")
        pass
    


    def muat_data_tabel(self):
        # Mengosongkan tabel di View terlebih dahulu
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data dari Model (Database)
        data_buku = self.model.get_all_buku()

        # Memasukkan data baru ke dalam tabel View
        for buku in data_buku:
            self.view.tabel.insert("", "end", values=(buku['id'], buku['judul'], buku['penulis'], buku['tahun_terbit']))
    def run(self):
        self.view.mainloop()

    def simpan_data(self):
        # Mengambil teks dari input di View
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        # Validasi Form Kosong
        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        # Mengirim data ke Model untuk disimpan
        berhasil = self.model.create_buku(judul, penulis, tahun)

        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data.")

    # --- TAMBAHAN TUGAS 1: Fungsi Hapus Data ---
    def hapus_data(self):
        # Mengambil item/baris yang dipilih pengguna di tabel GUI
        selected_item = self.view.tabel.selection()

        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih data di tabel yang ingin dihapus terlebih dahulu!")
            return
