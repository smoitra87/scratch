""" 
Testing asynchronous function call
"""

import time
from multiprocessing import Pool

def f1() : 
	for i in range(5) : 
		time.sleep(1)
		print "Return after 1 sec"
		print time.time()

def f2() : 
	for i in range(5) : 
		time.sleep(2)
		print "Return after 2 sec"
		print time.time()

if __name__ == '__main__' :
	pool = Pool(2)

	t1 = time.time() 
	print("Initial Time {0}".format(time.time()))
	pool.apply_async(f1)
	pool.apply_async(f2)
	
	while time.time() - t1 < 3 : 
		time.sleep(1)
	pool.terminate()

