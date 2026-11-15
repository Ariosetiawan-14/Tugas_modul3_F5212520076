
from .buku_model import BukuModel

try:
    from .buku_view import BukuView  # type: ignore[import-not-found]
except ImportError:
    from buku_view import BukuView  # type: ignore[import-not-found]


def __init__(self, user_role):
    print("CONTROLLER BERHASIL DIPANGGIL")
    print("ROLE PENGGUNA:", user_role)
    
    self.model = BukuModel()
    self.view = BukuView()

    self.user_role = user_role.lower()

    if self.user_role == "admin":
        self.view.title(
            "Sistem Manajemen Perpustakaan - Mode ADMIN"
        )

        self.view.btn_simpan.configure(
            text="Simpan Data",
            command=self.simpan_data,
            state="normal"
        )

        self.view.btn_perbarui.configure(
            text="Perbarui Data (Update)",
            command=self.perbarui_data,
            state="normal"
        )

        self.view.btn_hapus.configure(
            text="Hapus Data (Delete)",
            command=self.hapus_data,
            state="normal"
        )

    else:
        self.view.title(
            "Sistem Manajemen Perpustakaan - Mode ANGGOTA"
        )

        self.view.btn_simpan.configure(
            text="Akses Terkunci (Khusus Admin)",
            state="disabled"
        )

        self.view.btn_perbarui.configure(
            state="disabled"
        )

        self.view.btn_hapus.configure(
            state="disabled"
        )

    self.muat_data_tabel()
