""" 
Experiments with copy and deep copy
shows what happens if your not careful when doing shallow copy 
"""

import copy

class A(object) : 
	def __init__(self) :
		self.x = 1

class B(object) : 
	def __init__(self) : 
		self.a = A()


if __name__ == '__main__' : 
	a1 = A()
	a2 = copy.copy(a1)
	print "a1.x is ", a1.x
	print "a2.x is ", a2.x
	a2.x = 2
	print "a1.x is ", a1.x
	print "a2.x is ", a2.x

	b1 = B()
	b2 = copy.copy(b1)
	print "b1.a.x is", b1.a.x
	print "b2.a.x is", b2.a.x
	b2.a.x = 2
	print "b1.a.x is", b1.a.x
	print "b2.a.x is", b2.a.x

