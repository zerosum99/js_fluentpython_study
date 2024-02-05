
import multiprocessing
import time

# 이벤트 객체 생성
event = multiprocessing.Event()

# 이벤트를 기다리는 함수
def wait_for_event():
    print("Wait for event...")
    event.wait(timeout=5)  # 5초 동안 이벤트를 기다림
    if event.is_set():
        print("Event occurred!")
    else:
        print("Timeout occurred!")

# 이벤트를 설정하는 함수
def set_event():
    time.sleep(2)
    print("Event set!")
    event.set()  # 이벤트 설정

if __name__ == "__main__":
    # 이벤트를 기다리는 프로세스 생성
    p1 = multiprocessing.Process(target=wait_for_event)
    p1.start()

    # 이벤트를 설정하는 프로세스 생성
    p2 = multiprocessing.Process(target=set_event)
    p2.start()

    # 프로세스 종료 대기
    p1.join()
    p2.join()
