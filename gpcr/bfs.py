""" Performs BFS to identify all nodes that are reachable from K296 
Compares if some of these residues are present in the SCA list
"""

import operator as op

class GremlinGraph(object) : 
	""" Structure for storing data calculating BFS"""
	def __init__(self,g=None) : 
		self.g = _g

	def parse(self,fname) : 
		with open(fname,"r") as fin : 
			text = fin.readlines() 
		
		f = lambda x : str.split(str.split(x))
		self.e = [op.itemgetter(1,3)(f(line)) for line in text]
		self.e = [map(int,e_) for e_ in self.e]
		# create a set of list
		self.v = set(map(op.itemgettier(1)(self.e)))
		self.v = sorted(list(self.v))



if __name__ == '__main__' : 
	g = GremlinGraph()
	g.parse('data/edgeList_38.dat') 




