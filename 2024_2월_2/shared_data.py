
import multiprocessing
import time

# 공유 자원
shared_resource = []

# 공유 자원에 데이터를 추가하는 함수
def add_data(lock, data):
    with lock:
        shared_resource.append(data)

if __name__ == "__main__":
    # Lock 객체 생성
    lock = multiprocessing.Lock()

    # 여러 프로세스를 생성하여 공유 자원에 데이터를 추가
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=add_data, args=(lock, i))
        processes.append(p)
        p.start()

    # 모든 프로세스가 종료될 때까지 대기
    for p in processes:
        p.join()

    # 공유 자원 출력
    print("Shared Resource:", shared_resource)
