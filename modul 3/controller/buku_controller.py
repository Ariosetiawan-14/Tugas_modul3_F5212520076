#Ario Setiawan Dg.Malino F5212520076
import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView

class BukuController:

    def __init__(self, user_role):
        # Inisialisasi Model dan View
        self.model = BukuModel()
        self.view = BukuView()

        # Menyimpan role pengguna
        self.user_role = user_role.lower()

        # =====================================
        # PENGATURAN HAK AKSES ADMIN
        # =====================================
        if self.user_role == "admin":

            self.view.title(
                "Sistem Manajemen Perpustakaan - Mode ADMIN"
            )

            # Tombol Simpan aktif
            self.view.btn_simpan.configure(
                text="Simpan Data",
                command=self.simpan_data,
                state="normal"
            )

            # Tombol Perbarui aktif
            self.view.btn_perbarui.configure(
                text="Perbarui Data (Update)",
                command=self.perbarui_data,
                state="normal"
            )

            # Tombol Hapus aktif
            self.view.btn_hapus.configure(
                text="Hapus Data (Delete)",
                command=self.hapus_data,
                state="normal"
            )

        # =====================================
        # PENGATURAN HAK AKSES MAHASISWA
        # =====================================
        elif self.user_role in ["anggota", "mahasiswa"]:

            self.view.title(
                "Sistem Manajemen Perpustakaan - Mode ANGGOTA"
            )

            # Tombol Simpan dikunci
            self.view.btn_simpan.configure(
                text="Akses Terkunci (Khusus Admin)",
                state="disabled"
            )

            # Tombol Perbarui dikunci
            self.view.btn_perbarui.configure(
                state="disabled"
            )

            # Tombol Hapus dikunci
            self.view.btn_hapus.configure(
                state="disabled"
            )

        else:
            raise ValueError("Role pengguna tidak dikenal!")

        # Memuat data buku ke tabel
        self.muat_data_tabel()

    def perbarui_data(self):
        print("Tombol Perbarui berfungsi!") # Boleh dibiarkan untuk penanda
        
        # 1. Mengecek apakah ada baris tabel yang dipilih
        selected_item = self.view.tabel.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih data di tabel yang ingin diperbarui terlebih dahulu!")
            return
        
        # 2. Mengambil ID Buku dari baris yang dipilih (berada di kolom pertama / indeks 0)
        item_values = self.view.tabel.item(selected_item, 'values')
        id_buku = item_values[0]

        # 3. Mengambil data terbaru yang Anda ketik di Form Input
        judul_baru = self.view.entry_judul.get()
        penulis_baru = self.view.entry_penulis.get()
        tahun_baru = self.view.entry_tahun.get()

        # Validasi form kosong
        if not judul_baru or not penulis_baru or not tahun_baru:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        # 4. Mengirim data ke Model untuk diproses ke database MySQL
        berhasil = self.model.update_buku(id_buku, judul_baru, penulis_baru, tahun_baru)
        
        # 5. Menyegarkan (Refresh) tabel jika database berhasil di-update
        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
            # Bagian ini sangat penting agar tampilan tabel langsung berubah!
            self.muat_data_tabel() 
        else:
            messagebox.showerror("Error", "Tidak ada data yang diubah atau terjadi kesalahan.")
            
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
        # 1. Mengecek apakah ada baris tabel yang dipilih
        selected_item = self.view.tabel.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih data di tabel yang ingin dihapus terlebih dahulu!")
            return
        
        # 2. Mengambil ID Buku dari baris yang dipilih (indeks ke-0)
        item_values = self.view.tabel.item(selected_item, 'values')
        id_buku = item_values[0]

        # 3. Menampilkan pop-up konfirmasi agar tidak terhapus tidak sengaja
        konfirmasi = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus buku ini?")
        
        if konfirmasi:
            # 4. Mengirim perintah ke Model untuk menghapus data di database
            berhasil = self.model.delete_buku(id_buku)
            
            # 5. Menyegarkan (Refresh) tabel jika berhasil dihapus
            if berhasil:
                messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
                self.muat_data_tabel() # Wajib dipanggil agar baris hilang dari layar GUI
            else:
                messagebox.showerror("Error", "Gagal menghapus data dari database.")