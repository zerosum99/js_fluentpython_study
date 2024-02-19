
from contextlib import ContextDecorator

class FileHandler(ContextDecorator):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

# 수정된 사용 예제
if __name__ == "__main__":
    filename = "example.txt"
    mode = "w"

    @FileHandler(filename, mode)
    def write_to_file(file):  # 파일 객체를 인자로 받도록 수정
        file.write("Hello, world!")
