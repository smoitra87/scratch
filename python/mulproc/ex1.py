""" A program that executes parallel system calls """

import multiprocessing
import sys
import os


def worker():
    os.system("~/runJalview")

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()
