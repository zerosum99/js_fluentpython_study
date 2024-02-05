

import multiprocessing
import time

def producer(queue, exit_signal):
    for i in range(5):
        time.sleep(1)
        print(f"Producing item {i}")
        queue.put(f"Item {i}")
    exit_signal.set()  # 모든 항목을 생성한 후 종료 신호 설정

def consumer(queue, exit_signal):
    while not exit_signal.is_set() or not queue.empty():
        if not queue.empty():
            item = queue.get()
            print(f"Consuming {item}")
        else:
            time.sleep(0.1)  # 큐가 비어있을 때 잠시 대기

if __name__ == "__main__":
    queue = multiprocessing.Queue()
    exit_signal = multiprocessing.Event()

    producer_process = multiprocessing.Process(target=producer, args=(queue, exit_signal))
    consumer_process = multiprocessing.Process(target=consumer, args=(queue, exit_signal))

    producer_process.start()
    consumer_process.start()

    producer_process.join()
    consumer_process.join()
