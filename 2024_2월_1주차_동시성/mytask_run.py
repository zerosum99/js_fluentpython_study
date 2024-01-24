
import time
import multiprocessing

def mytask() :
    print("Starting==>")
    time.sleep(2)
    

if __name__ == '__main__':
    t2 = time.time()

    procs = []

    for i in range(10) :
        process = multiprocessing.Process(target=mytask)
        process.start()
        procs.append(process)
        
    t3 = time.time()
    print(f"Total time for creating 10 processess : {t3-t2}")
    for proc in procs :
        proc.join()
