import concurrent.futures
import time

def square(number):
    result = number * number
    time.sleep(1)  # 예제를 위해 1초 동안 대기
    print(f"Square of {number}: {result}")
