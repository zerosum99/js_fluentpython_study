
import concurrent.futures
import os

# 간단한 작업 함수
def task(n):
    pid = os.getpid()
    print(f"Task {n} is running in process {pid}")
    return n * n

if __name__ == "__main__":
    # 최대 3개의 프로세스를 가진 ProcessPoolExecutor 생성
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        # 작업 제출
        future1 = executor.submit(task, 1)
        future2 = executor.submit(task, 2)
        future3 = executor.submit(task, 3)

        # 결과 가져오기
        result1 = future1.result()
        result2 = future2.result()
        result3 = future3.result()

        print(f"Result of task 1: {result1}")
        print(f"Result of task 2: {result2}")
        print(f"Result of task 3: {result3}")
