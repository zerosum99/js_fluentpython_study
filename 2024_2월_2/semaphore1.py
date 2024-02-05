
import multiprocessing
import time

# 공유 자원
shared_resource = []
# 세마포어 객체 생성 (최대 2개의 프로세스까지 허용)
semaphore = multiprocessing.Semaphore(2)

# 각 프로세스에서 실행될 함수
def worker():
    # 세마포어를 획득
    semaphore.acquire()
    try:
        # 공유 자원에 접근
        shared_resource.append(multiprocessing.current_process().name)
        print(f"Resource: {shared_resource}")
        time.sleep(1)
    finally:
        # 세마포어를 해제
        semaphore.release()

if __name__ == "__main__":
    # 여러 프로세스 생성하여 공유 자원에 접근
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        processes.append(p)
        p.start()

    # 모든 프로세스 종료 대기
    for p in processes:
        p.join()

