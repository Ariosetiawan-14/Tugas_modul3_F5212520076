import customtkinter as ctk
from tkinter import ttk

class AnggotaView(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Konfigurasi Jendela Utama ---
        self.title("Sistem Manajemen Perpustakaan - Data Anggota")
        self.geometry("900x500")
        
        # Mengatur tema tampilan menjadi terang agar sesuai dengan gambar
        ctk.set_appearance_mode("light") 

        # ==========================================
        # FRAME KIRI (Form Data Anggota)
        # ==========================================
        self.frame_kiri = ctk.CTkFrame(self, corner_radius=10)
        self.frame_kiri.pack(side="left", fill="y", padx=20, pady=20)

        # Judul Form
        self.lbl_judul_form = ctk.CTkLabel(self.frame_kiri, text="Form Data Anggota", font=ctk.CTkFont(size=16, weight="bold"))
        self.lbl_judul_form.pack(pady=(20, 20), padx=20)

        # Input Nama Anggota
        self.entry_nama = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Nama Anggota", width=250)
        self.entry_nama.pack(pady=10, padx=20)

        # Input Alamat
        self.entry_alamat = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Alamat", width=250)
        self.entry_alamat.pack(pady=(10, 30), padx=20) # Padding bawah lebih besar untuk jarak ke tombol

        # Tombol Simpan Data (Hijau)
        self.btn_simpan = ctk.CTkButton(self.frame_kiri, text="Simpan Data", fg_color="green", hover_color="darkgreen")
        self.btn_simpan.pack(pady=10, padx=20, fill="x")

        # Tombol Perbarui Data (Biru)
        self.btn_update = ctk.CTkButton(self.frame_kiri, text="Perbarui Data (Update)", fg_color="blue", hover_color="darkblue")
        self.btn_update.pack(pady=10, padx=20, fill="x")

        # Tombol Hapus Data (Merah)
        self.btn_delete = ctk.CTkButton(self.frame_kiri, text="Hapus Data (Delete)", fg_color="red", hover_color="darkred")
        self.btn_delete.pack(pady=10, padx=20, fill="x")

        # ==========================================
        # FRAME KANAN (Daftar Anggota Perpustakaan)
        # ==========================================
        self.frame_kanan = ctk.CTkFrame(self, corner_radius=10)
        self.frame_kanan.pack(side="right", fill="both", expand=True, padx=(0, 20), pady=20)

        # Judul Tabel
        self.lbl_judul_tabel = ctk.CTkLabel(self.frame_kanan, text="Daftar Anggota Perpustakaan", font=ctk.CTkFont(size=16, weight="bold"))
        self.lbl_judul_tabel.pack(pady=(20, 20))

        # --- Konfigurasi Tabel (Treeview) ---
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview.Heading", font=('Arial', 10, 'bold'))
        style.configure("Treeview", font=('Arial', 10), rowheight=25)

        # Mendefinisikan Kolom Tabel
        kolom_tabel = ("ID", "Nama Anggota", "Alamat")
        self.tabel_anggota = ttk.Treeview(self.frame_kanan, columns=kolom_tabel, show="headings", height=15)
        
        # Mengatur Nama dan Lebar Kolom
        self.tabel_anggota.heading("ID", text="ID")
        self.tabel_anggota.column("ID", width=50, anchor="center")

        self.tabel_anggota.heading("Nama Anggota", text="Nama Anggota")
        self.tabel_anggota.column("Nama Anggota", width=250, anchor="w")

        self.tabel_anggota.heading("Alamat", text="Alamat")
        self.tabel_anggota.column("Alamat", width=300, anchor="w")

        self.tabel_anggota.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        # --- Memasukkan Data Dummy (Sesuai Contoh Gambar) ---
        data_dummy = [
            ("1", "Ario Setiawan Dg.Malino  F5212520076", "Jl. Soekarno Hatta No. 14"),
            ("2", "Aulia Pratiwi Ayuningtias", "Jl. Marantale No. 7")
        ]
        
        for data in data_dummy:
            self.tabel_anggota.insert("", "end", values=data)

if __name__ == "__main__":
    app = AnggotaView()
    app.mainloop()