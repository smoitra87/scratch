"""
This is an example that explored inheritence in python wrt calling 
constructor functions
"""
class GrandParent(object) : 
	def __init__(self,_cigar) :
		self.cigar = _cigar


class Mom(object) : 
	def __init__(self,_perfume='Gucci',_cigar='persian') : 
		self.perfume=_perfume
		#super(Mom,self).__init__(_cigar)

class Dad(GrandParent) : 
	def __init__(self,_golf,_cigar='havana') : 
		self.golf = _golf
		super(Dad,self).__init__(_cigar)


class Child2(Dad,Mom) : 
	def __init__(self,_toy,_golf) :
		self.toy = _toy
		super(Child2, self).__init__(_golf)

if __name__ == '__main__' : 
	c = Child2('gijoe','pga')
	print 'Calling order is '
	print Child2.__mro__
