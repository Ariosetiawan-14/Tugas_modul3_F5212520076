
import customtkinter as ctk

class LoginView(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Pengaturan tampilan
        ctk.set_appearance_mode("Light")

        self.title("Login Sistem Perpustakaan")
        self.geometry("680x720")
        self.resizable(False, False)
        self.configure(fg_color="#EEEEEE")

        # Frame utama
        self.frame = ctk.CTkFrame(
            self,
            fg_color="#D9D9D9",
            corner_radius=12
        )
        self.frame.pack(
            pady=38,
            padx=38,
            fill="both",
            expand=True
        )

        # Judul Login
        self.label_judul = ctk.CTkLabel(
            self.frame,
            text="LOGIN SISTEM",
            font=("Arial", 34, "bold"),
            text_color="#222222"
        )
        self.label_judul.pack(pady=(45, 55))

        # Input Username
        self.entry_username = ctk.CTkEntry(
            self.frame,
            placeholder_text="Username",
            height=56,
            font=("Arial", 20),
            corner_radius=10,
            border_width=2,
            border_color="#9AA1A6",
            fg_color="white",
            text_color="#222222"
        )
        self.entry_username.pack(
            padx=38,
            pady=(0, 40),
            fill="x"
        )

        # Input Password
        self.entry_password = ctk.CTkEntry(
            self.frame,
            placeholder_text="Password",
            show="*",
            height=56,
            font=("Arial", 20),
            corner_radius=10,
            border_width=2,
            border_color="#9AA1A6",
            fg_color="white",
            text_color="#222222"
        )
        self.entry_password.pack(
            padx=38,
            pady=(0, 60),
            fill="x"
        )

        # Tombol Masuk
        self.btn_login = ctk.CTkButton(
            self.frame,
            text="Masuk",
            height=58,
            font=("Arial", 22),
            fg_color="blue",
            hover_color="darkblue",
            corner_radius=10
        )
        self.btn_login.pack(
            padx=38,
            fill="x"
        )

        # Fokus ke username
        self.entry_username.focus()
