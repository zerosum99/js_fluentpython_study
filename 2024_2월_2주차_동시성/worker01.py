
def square_numbers(numbers, result, index):
    for idx, num in enumerate(numbers):
        result[idx] = num * num
        index.value = idx  # 공유 메모리 업데이트
        

def square_number(number):
    return number * number
