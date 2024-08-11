import logging
import random

import sortfunc as sf

# logging.disable()

n = 7777
data = [random.randint(1, n * 2) for i in range(n)]
sorters = [sf.bubble_sort, sf.selection_sort, sf.insertion_sort]
random.shuffle(sorters)
logging.info(f'{[sorter.__name__ for sorter in sorters]}\n')

if __name__ == '__main__':
    logging.info(f'data head(7)={data[:7]}, n={len(data)}\n')
    # [print(deco.print_execution_time(sorter, data)[:7]) for sorter in sorters]

    print()
    [logging.info(sorter(data)[:7]) for sorter in sorters]

