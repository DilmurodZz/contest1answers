import time

def decorator_1(func):
    def wrapper(*white, **black):
        stime = time.time()
        result = func(*white, **black)
        endtime = time.time()
        extime = endtime - stime
        print(f"{func.__name__} call executed in {extime:.4f} sec")
        return result
    return wrapper
