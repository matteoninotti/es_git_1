import time
import os
import shutil


dir_in = "./processing"
dir_out = "./out"


os.makedirs(dir_out, exist_ok=True)
os.makedirs(dir_in, exist_ok=True)  

while True:
        print(f"{time.strftime('%X')}: Controllo della cartella '{dir_in}'...")

        items = os.listdir(dir_in)
        

        files = [i for i in items if os.path.isfile(os.path.join(dir_in, i))]
        
        if files:
            print(f"{time.strftime('%X')}: Trovati {len(files)} file, spostamento in corso...")
            for file_name in files:
                src_path = os.path.join(dir_in, file_name)
                dst_path = os.path.join(dir_out, file_name)
                

                shutil.move(src_path, dst_path)
            print("Spostamento completato.")
        else:
            print("Nessun file trovato.")
            

        time.sleep(30)