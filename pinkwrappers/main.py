import time


def logtime(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f'{func.__name__} took {time.time()-start_time} sec')
        return result
    return wrapper

