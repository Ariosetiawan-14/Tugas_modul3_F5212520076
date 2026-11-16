
import sys
from pathlib import Path

# Mengambil lokasi folder utama project
ROOT = Path(__file__).resolve().parent.parent

# Menambahkan folder utama ke Python Path
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
