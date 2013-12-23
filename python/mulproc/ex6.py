#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
An example of using Queues to get some parallel processing stuff done

"""

from multiprocessing import Process,Queue, current_process, freeze_support
import multiprocessing

import glob
import time,random


def count_lines(fname):
    time.sleep(0.5*random.random())
    with open(fname) as fin:
        return len(fin.readlines())

def worker(input,output):
    for func,args in iter(input.get,'STOP'):
        done_queue.put(calculate(func,args))


def calculate(func,args):
    result = func(*args)
    print("%s says %s%s=%d"%(current_process(),func.__name__,repr(args),result))
    return result

if __name__ == '__main__':
    freeze_support()
    task_queue=Queue()
    done_queue=Queue()

    # get all python files
    pyfiles = glob.glob("*.py")

    # Add tasks to queue
    for f in pyfiles:
        task_queue.put((count_lines,(f,)))

    # Create worker processes
    for i in range(multiprocessing.cpu_count()):
        Process(target=worker,args=(task_queue,done_queue)).start()


    for i in range(multiprocessing.cpu_count()):
        task_queue.put('STOP')


    for i in range(len(pyfiles)):
        print("\t",done_queue.get())



