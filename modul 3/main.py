
import sys
from pathlib import Path
from tkinter import messagebox

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

# Import Login View
from views.login_view import LoginView

# Import Buku Controller
from controller.buku_controller import BukuController


# Membuat halaman Login
login = LoginView()


# Fungsi proses login
def proses_login():

    username = login.entry_username.get().strip()
    password = login.entry_password.get()

    # Validasi input kosong
    if not username or not password:
        messagebox.showwarning(
            "Peringatan",
            "Username dan Password harus diisi!"
        )
        return

    # Validasi akun Admin
    if username == "admin" and password == "admin123":
        user_role = "admin"

    # Validasi akun Mahasiswa
    elif username == "mahasiswa" and password == "user123":
        user_role = "anggota"

    else:
        messagebox.showerror(
            "Login Gagal",
            "Username atau Password salah!"
        )
        login.entry_password.delete(0, "end")
        return

    # Login berhasil
    messagebox.showinfo(
        "Login Berhasil",
        "Selamat datang, " + username
    )

    # Menutup halaman login
    login.destroy()

    # Membuka halaman sesuai role
    app = BukuController(user_role=user_role)
    app.run()


# Menghubungkan tombol Login
login.btn_login.configure(command=proses_login)

# Menjalankan halaman Login
login.mainloop()



