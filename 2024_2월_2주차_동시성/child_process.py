import multiprocessing
import time
import os

def child_process():
    print("Child process is running")
    print(" child process " ,multiprocessing.current_process())
    print(" parant process ", multiprocessing.parent_process())
    print(f"Child process (PID: {os.getpid()}) is running")
    time.sleep(2)
    print("Child process completed")
