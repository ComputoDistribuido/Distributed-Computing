import numpy as np
from time import time
import multiprocessing as mp

np.random.RandomState(100)
arr = np.random.randint(0, 10, size=[200000, 5])
data = arr.tolist()
data[:5]


def howmany_within_range_rowonly(row, minimum=4, maximum=8):
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count


def start():
    pool = mp.Pool(mp.cpu_count())

    results = pool.map(howmany_within_range_rowonly, [row for row in data])

    pool.close()

    print(results[:10])
