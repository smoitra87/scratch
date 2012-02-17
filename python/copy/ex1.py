""" 
Experiments with copy and deep copy
"""

import copy

class A(object) : 
	pass

class B(object) : 
	def __init__(self) : 
		self.a = A()


if __name__ == '__main__' : 
	b1 = B()
	b2 = copy.copy(b1)
	b3 = b1
	b4 = copy.deepcopy(b1)
	print 'addr of b1: ', repr(b1)
	print 'addr of b2: ', repr(b2)
	print 'addr of b3: ', repr(b3)
	print 'addr of b1.a', repr(b1.a)
	print 'addr of b2.a', repr(b2.a)
	print 'addr of b4', repr(b4)
	print 'addr of b4.a', repr(b4.a)
