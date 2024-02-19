
class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# 사용 예제
if __name__ == "__main__":
    filename = "example.txt"
    mode = "w"

    with FileHandler(filename, mode) as f:
        f.write("Hello, world!")
