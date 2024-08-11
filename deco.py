def print_execution_time(some_func, *args, **kwargs):
    from time import time
    print()
    print(some_func.__name__, ':', sep='')
    start = time()
    res = some_func(*args, **kwargs)
    finish = time()
    print(f'executed in {round(finish - start, 3)} seconds')
    return res
