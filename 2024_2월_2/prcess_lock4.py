
import concurrent.futures
import threading
import multiprocessing

# 공유 변수
shared_var = 0

# 스레드 락
thread_lock = threading.Lock()

# 프로세스 락
process_lock = multiprocessing.Lock()

# 공유 변수를 증가시키는 함수
def increment_shared_var_thread():
    global shared_var
    for _ in range(100000):
        with thread_lock:
            shared_var += 1

def increment_shared_var_process():
    global shared_var
    for _ in range(100000):
        with process_lock:
            shared_var += 1
            
if __name__ == "__main__" : 

    # 스레드 풀 생성
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # 스레드를 풀에 추가
        futures = [executor.submit(increment_shared_var_thread) for _ in range(10)]

    # 모든 스레드의 작업이 완료될 때까지 대기
    concurrent.futures.wait(futures)

    # 공유 변수 값 출력
    print("Shared variable value (threading):", shared_var)

    # 프로세스 풀 생성
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # 프로세스를 풀에 추가
        futures = [executor.submit(increment_shared_var_process) for _ in range(10)]

    # 모든 프로세스의 작업이 완료될 때까지 대기
    concurrent.futures.wait(futures)

    # 공유 변수 값 출력
    print("Shared variable value (multiprocessing):", shared_var)
