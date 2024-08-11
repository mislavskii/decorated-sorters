# done with the help of https://www.youtube.com/watch?v=QH5fw9kxDQA

import logging
from abc import ABC, abstractmethod
from math import sqrt
from time import perf_counter


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for element in range(2, int(sqrt(number)) + 1):
        if number % element == 0:
            return False
    return True


class AbstractComponent(ABC):
    @abstractmethod
    def execute(self, upper_bound: int) -> int:
        pass


class ConcreteComponent(AbstractComponent):
    def execute(self, upper_bound: int) -> int:
        return sum(is_prime(number) for number in range(upper_bound))


class AbstractDecorator(AbstractComponent):
    def __init__(self, decorated: AbstractComponent) -> None:
        self._decorated = decorated


class BenchmarkDecorator(AbstractDecorator):
    def execute(self, upper_bound: int) -> int:
        start_time = perf_counter()
        value = self._decorated.execute(upper_bound)
        end_time = perf_counter()
        run_time = end_time - start_time
        logging.info(
            f'Execution of {self._decorated.__class__.__name__} took {run_time} seconds.'
        )
        return value


class LoggingDecorator(AbstractDecorator):
    def execute(self, upper_bound: int) -> int:
        logging.info(f'Calling {self._decorated.__class__.__name__}.')
        value = self._decorated.execute(upper_bound)
        logging.info(f'Completed execution of {self._decorated.__class__.__name__}.')
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
    logging.basicConfig(level=logging.INFO)
    component = ConcreteComponent()
    benchmarked = BenchmarkDecorator(component)
    logged = LoggingDecorator(benchmarked)
    value = logged.execute(100000)
    logging.info(f'Found {value} prime numbers.')


if __name__ == '__main__':
    main()
