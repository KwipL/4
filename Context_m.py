import time
class CodeTimer:
    def __init__(self):
        self.start = None

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print(exc_tb)
        # print(exc_val)
        # print(exc_type)
        t = time.time() - self.start
        print('Итого время работы' ,t, 'сек')

timer = CodeTimer()

with timer:
    l = [i for i in range(100)]
    l[101]