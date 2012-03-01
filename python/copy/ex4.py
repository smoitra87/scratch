""" 
Tries to show how you can use deepcopy to copy stuff in python when 
there are cyclic dependencies between your objects
"""

import copy

class node(object) : 
	""" Graph object """
	def __init__(self,name) : 
		self.name = name
		self.adj = []

	def __repr__(self) : 
		s = 'node=<%s> id=<%d>'%(self.name,id(self))
		return s

	def __deepcopy__(self,memo) : 
		
		# Check if self is already in memo
		nil = []
		exists = memo.get(self,nil)
		if exists is not nil  :
			print "%r already exists as %r"%(self,exists)
			return exists
	
		# Create a duplicate copy if self
		dup = node(copy.deepcopy(self.name,memo))
		memo[self] = dup

		print "Copying %r to %r"%(self,dup)

		for adj_node in self.adj : 
			dup.adj.append(copy.deepcopy(adj_node,memo))

if __name__ == '__main__' : 
	a = node('a')
	b = node('b')
	c = node('c')
	d = node('d')
	a.adj = [a,b,c]
	b.adj = [a]
	c.adj = [a,b]
	a2 = copy.deepcopy(a)

