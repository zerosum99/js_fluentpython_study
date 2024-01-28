
import multiprocessing, time



# 첫 번째 프로세스
def process1(resource1, resource2):
    with resource1:
        print("Process 1 has Resource 1")
        time.sleep(1)  # 시간 지연을 추가하여 교착상태를 발생시키기 쉽게 함
        # 어떤 작업 수행
        with resource2:
            print("Process 1 has Resource 2")
            # 어떤 작업 수행

# 두 번째 프로세스
def process2(resource1, resource2):
    with resource2:
        print("Process 2 has Resource 2")
        time.sleep(1)  # 시간 지연을 추가하여 교착상태를 발생시키기 쉽게 함
        # 어떤 작업 수행
        with resource1:
            print("Process 2 has Resource 1")
            # 어떤 작업 수행
