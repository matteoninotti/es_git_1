import shutil
import time
from pathlib import Path

INPUT_DIR = Path("./in")
PROCESSING_DIR = Path("./processing")



def move_files_to_processing():
    INPUT_DIR.mkdir(exist_ok=True)
    PROCESSING_DIR.mkdir(exist_ok=True)

    files = [path for path in INPUT_DIR.iterdir() if path.is_file()]

    if not files:
        print(f"Nessun file trovato in {INPUT_DIR}")
        return

    for file_path in files:
        destination = PROCESSING_DIR / file_path.name
        shutil.move(str(file_path), str(destination))
        print(f"Spostato {file_path} in {destination}")



while True:
    move_files_to_processing()
    time.sleep(10)
