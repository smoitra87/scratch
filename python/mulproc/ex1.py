""" A program that executes parallel system calls """

import multiprocessing, sys, os


def worker() : 
	os.system("~/runJalview")

if __name__ == '__main__' :
	jobs = []
	for i in range(5) : 
		p = multiprocessing.Process(target=worker);
		jobs.append(p)
		p.start()


