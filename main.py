import subprocess
import time



def main():
    f1 = "./feature_1.py"
    f2 = "./feature_2.py"
    f3 = "./feature_3.py"
    proc1 = subprocess.Popen(["python", f1])
    proc2 = subprocess.Popen(["python", f2])
    proc3 = subprocess.Popen(["python", f3])

    time.sleep(120)

    proc1.terminate()
    proc2.terminate()
    proc3.terminate()



if __name__ == "__main__":
    main()
