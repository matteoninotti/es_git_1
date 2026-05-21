import shutil
import time
from pathlib import Path



INPUT_DIR = Path("./processing")
OUTPUT_DIR = Path("./out")

def move_files_to_output() -> None:
    INPUT_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)

    files = [path for path in INPUT_DIR.iterdir() if path.is_file()]

    if not files:
        print(f"Nessun file trovato in {INPUT_DIR}")
        return

    for file_path in files:
        destination = OUTPUT_DIR / file_path.name
        shutil.move(str(file_path), str(destination))
        print(f"Spostato {file_path} in {destination}")



while True:
    move_files_to_output()
    time.sleep(30)