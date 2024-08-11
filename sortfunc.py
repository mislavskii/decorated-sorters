def bubble_sort(listlike):
    ls = listlike.copy()
    for i in range(len(ls) - 1, 0, -1):
        for j in range(i):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
    return ls


def selection_sort(listlike):
    ls = listlike.copy()
    for i in range(len(ls)):
        min_index = i
        for j in range(i, len(ls)):
            if ls[min_index] > ls[j]:
                min_index = j
        if min_index != i:
            ls[min_index], ls[i] = ls[i], ls[min_index]
    return ls


def insertion_sort(listlike):
    ls = listlike.copy()
    for i in range(1, len(ls)):
        current = ls[i]
        j = i - 1
        while ls[j] > current and j >= 0:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = current
    return ls


def print_execution_time(some_func, *args):
    from time import time
    print()
    print(some_func.__name__, ':', sep='')
    start = time()
    res = some_func(*args)
    finish = time()
    print(f'executed in {round(finish - start, 3)} seconds')
    return res
