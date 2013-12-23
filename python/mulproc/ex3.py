""" Following the example of http://stackoverflow.com/questions/8533318/python-multiprocessing-pool-when-to-use-apply-apply-async-or-ma
trying to write my own prog"""

import os
import sys
from multiprocessing import Pool
from random import randint
import time


def foo(x):
    wt = randint(1, 5)
    time.sleep(wt)
    print("x={};wt={};ct={}".format(x, wt, time.ctime()))
    return x

results_async = []


def log_results(result):
    results_async.append(result)


if __name__ == '__main__':
    pool = Pool(processes=10)
    print("Program started at {}".format(time.ctime()))
    print("Starting Apply processes")
    results = pool.map(foo, range(10))
    print(results)
    print("Starting apply_async processes")
    results = pool.map_async(foo, range(10), callback=log_results)

    print("results_async at time{}:{}".format(time.ctime(), results_async))
    time.sleep(3)
    print("results_async at time{}:{}".format(time.ctime(), results_async))
    pool.close()
    pool.join()
    print("results_async at time{}:{}".format(time.ctime(), results_async))
