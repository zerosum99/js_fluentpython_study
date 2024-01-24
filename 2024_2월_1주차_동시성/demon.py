
import threading
import time

def daemon_thread():
    while True:
        print("Daemon thread is running")
        time.sleep(1)

def non_daemon_thread():
    for _ in range(5):
        print("Non-daemon thread is working")
        time.sleep(1)
    print("Non-daemon thread completed")

if __name__ == "__main__":
    # 데몬 스레드 생성
    daemon_thread = threading.Thread(target=daemon_thread)
    daemon_thread.daemon = True  # 데몬 스레드로 설정

    # 일반 스레드 생성
    non_daemon_thread = threading.Thread(target=non_daemon_thread)

    # 스레드 시작
    daemon_thread.start()
    non_daemon_thread.start()

    try:
        # 모든 스레드가 완료될 때까지 대기
        non_daemon_thread.join()
        daemon_thread.join()
    except KeyboardInterrupt:
        # Ctrl+C 등의 인터럽트 시그널이 발생하면 프로그램 종료
        pass

    print("Main thread completed")
