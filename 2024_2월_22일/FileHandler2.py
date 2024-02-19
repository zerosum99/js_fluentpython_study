
from contextlib import contextmanager

@contextmanager
def file_handler(filename, mode):
    try:
        file = open(filename, mode)
        yield file
    finally:
        file.close()

# 사용 예제
if __name__ == "__main__":
    filename = "example.txt"
    mode = "w"

    with file_handler(filename, mode) as f:
        f.write("Hello, world! 2222 ")
