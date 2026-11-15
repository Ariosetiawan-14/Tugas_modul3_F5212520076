import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from controller.buku_controller import BukuController

print("Controller yang digunakan:", BukuController.__module__)

app = BukuController(user_role="anggota")
app.run()


