import random

import sortfunc as sf
import deco

n = 7777
data = [random.randint(1, n * 2) for i in range(n)]
sorters = [sf.bubble_sort, sf.selection_sort, sf.insertion_sort]
random.shuffle(sorters)
print([sorter.__name__ for sorter in sorters])

if __name__ == '__main__':
    print(f'data head(7)={data[:7]}, n={len(data)}')
    [print(deco.print_execution_time(sorter, data)[:7]) for sorter in sorters]
