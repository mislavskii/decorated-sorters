# done with the help of https://www.youtube.com/watch?v=QH5fw9kxDQA

import logging
from math import sqrt
from time import perf_counter
from typing import Any

logging.basicConfig(level=logging.INFO)

def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for element in range(2, int(sqrt(number)) + 1):
        if number % element == 0:
            return False
    return True


def count_primes(upper_bound: int) -> int:
    return sum(is_prime(number) for number in range(upper_bound))


def benchmark(func, *args) -> Any:
    start_time = perf_counter()
    value = func(*args)
    end_time = perf_counter()
    run_time = end_time - start_time
    logging.info(
        f'Execution of {func.__name__} took {run_time:.3f} seconds.'
    )
    return value


def with_logging(func, *args) -> Any:
    logging.info(f'Calling {func.__name__}.')
    value = func(*args)
    logging.info(f'Completed execution of {func.__name__}.')
    return value


def print_execution_time(some_func, *args, **kwargs):
    from time import time
    print()
    print(some_func.__name__, ':', sep='')
    start = time()
    res = some_func(*args, **kwargs)
    finish = time()
    print(f'executed in {round(finish - start, 3)} seconds')
    return res


def main() -> None:
    value = benchmark(count_primes, 100000)
    logging.info(f'Found {value} prime numbers.')


if __name__ == '__main__':
    main()
