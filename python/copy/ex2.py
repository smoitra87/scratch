""" 
Experiments with copy and deep copy
What happens if you change the address of a pointer to an object
Do all the pointers to that object get changed as well ? 
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
	b2.a = None
	print 'Init addr of b1.a', repr(b1.a)
	print 'Addr of b2.a', repr(b2.a)
	print 'addr of b1.a', repr(b1.a)
