""" Performs BFS to identify all nodes that are reachable from K296 
Compares if some of these residues are present in the SCA list
"""

import operator as op
from collections import deque
import logging

class GremlinGraph(object) : 
	""" Structure for storing data calculating BFS"""
	def __init__(self,_g=None) : 
		self.g = _g
		self._sca_immed = [293,294,295,299,91,113]
		self._sca_linked = [261,265,268,212]
		self._sca_contig = [121,123,125,219,261,298,299,302]

	def parse(self,fname) : 
		with open(fname,"r") as fin : 
			text = fin.readlines() 
		
		f = lambda x : str.split(str.strip(x))
		self.e = [op.itemgetter(1,3)(f(line)) for line in text]
		self.e = [map(int,e_) for e_ in self.e]
		# Sort the edges with the id of the first node in edge
		self.e = sorted(self.e,key=op.itemgetter(0))
		# create a set of list
		v1 = set(map(op.itemgetter(0),self.e))
		v2 = set(map(op.itemgetter(1),self.e))
		self.v = v1.union(v2)
	
		# build the adjacency list
		self.adj = {}
		for v in self.v : self.adj[v] = []

		for e in self.e	: 
			self.adj[e[0]].append(e[1])
			self.adj[e[1]].append(e[0])
	
		for v in self.v : 
			self.adj[v] = list(set(self.adj[v]))
		
	
	def bfs(self,v) : 
		""" Runs bfs from node v to get the set of connected component"""
		q = deque()
		q.append(v)
		visited = dict([(node,False) for node in self.v ])
		while len(q) > 0 : 
			currv = q.popleft()
			visited[currv] = True
			for adjv in self.adj[currv] :
				if not visited[adjv] : 
					q.append(adjv)
		# Get the connected component
		c = map(op.itemgetter(0),filter(op.itemgetter(1),visited.items()))
		return c	

	def compareSCA(self) : 
		""" Compares the 296th residue against SCA residues """ 
		c = set(self.bfs(296))
		overlap_immed = c.intersection(self._sca_immed)
		overlap_linked = c.intersection(self._sca_linked)
		overlap_contig = c.intersection(self._sca_contig)

		print "Immediate: ", overlap_immed
		print "Linked: ", overlap_linked
		print "Contig: ", overlap_contig

if __name__ == '__main__' : 
	g = GremlinGraph()
	g.parse('data/edgeList_38.dat') 
	g.compareSCA()



