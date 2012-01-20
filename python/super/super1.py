"""
This is an example that explored inheritence in python wrt calling 
constructor functions
"""
class GrandParent(object) : 
	def __init__(self,_cigar) :
		self.cigar = _cigar


class Mom(GrandParent) : 
	def __init__(self) : 
		pass

class Dad(GrandParent) : 
	def __init__(self,_golf) : 
		self.golf = _golf
		GrandParent.__init__(self,'havana')

class Child1(Dad) : 
	def __init__(self,_toy) : 
		self.toy = _toy
		Dad.__init__(self,'pga')
		GrandParent.__init__(self,'persian')

if __name__ == '__main__' : 
	c = Child1('gijoe')

