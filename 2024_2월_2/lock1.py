
import multiprocessing
import time

# 공유 자원에 데이터를 갱신하는 함수
def update_shared_resource(lock, shared_resource):
    for _ in range(5):
        # 잠금 획득
        lock.acquire()
        try:
            shared_resource.value += 1
            print("Updated shared resource:", shared_resource.value)
        finally:
            # 잠금 해제
            lock.release()
        time.sleep(0.1)  # 잠시 대기

if __name__ == "__main__":
    # 공유 자원 생성
    shared_resource = multiprocessing.Value('i', 0)
    
    # Lock 객체 생성
    lock = multiprocessing.Lock()

    # 여러 프로세스 생성하여 공유 자원 갱신
    processes = []
    for _ in range(3):
        p = multiprocessing.Process(target=update_shared_resource, args=(lock, shared_resource))
        processes.append(p)
        p.start()

    # 모든 프로세스 종료 대기
    for p in processes:
        p.join()

    print("Final shared resource value:", shared_resource.value)
