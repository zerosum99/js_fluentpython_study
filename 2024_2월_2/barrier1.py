
import multiprocessing
import time

# 각 프로세스에서 실행될 함수
def worker(barrier):
    print("Worker {} is waiting at the barrier".format(multiprocessing.current_process().name))
    barrier.wait()
    print("Worker {} passed the barrier".format(multiprocessing.current_process().name))

if __name__ == "__main__":
    # Barrier 객체 생성 (3개의 프로세스가 기다릴 때까지)
    barrier = multiprocessing.Barrier(3)

    # 여러 프로세스 생성하여 Barrier에서 만날 수 있도록 함
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=worker, args=(barrier,))
        processes.append(p)
        p.start()

    # 모든 프로세스 종료 대기
    for p in processes:
        p.join()
