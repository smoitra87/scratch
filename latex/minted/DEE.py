"""
Program for doing DEE pruning
"""

import numpy as np
from operator import itemgetter
from itertools import product

# Define some constaint
MAXVAL=1e100
MAX_E = 30
MIN_E = 0
N,R = 10,4 # Num aa and nrot/aa

class Protein(object) : 
	""" Describes a protein object"""
	def __init__(self,n,r) : 
		self.n = n
		self.r = r
		# Assign Energies
		self.Es = np.random.uniform(MIN_E,MAX_E,(n,r))
		self.Ep = np.random.uniform(MIN_E,MAX_E,(n,n,r,r))
		self.rotSpace = []
		for i in range(n) : 
			self.rotSpace.append(range(r));

	def calc_Energy(self,conf) :
		""" Calculates Energy for a particular conformation"""
		E_unit = E_pair = 0
		Ep  = self.Ep
		Es = self.Es
		c = conf
		E_unit = np.sum(map(lambda(c):Es[c[0]][c[1]],enumerate(conf)))
		for i in range(len(conf)):
			for j in range(i+1,len(conf)) : 
				E_pair += Ep[i][j][conf[i]][conf[j]] 
		return E_unit + E_pair
				




class SCPSolver(object) : 
	""" Solves the side chain placment problem"""
	def __init__(self,p):	
		self.p = p
		self.sched = self.sched1
		# Define rotameric space
		self.rotSpace = p.rotSpace

	def findmin_brute(self) : 
		""" Find min using brute force search """
		min_energy = MAXVAL
		for c in product(*self.rotSpace) : 
			if min_energy > p.calc_Energy(c) : 
				min_energy = p.calc_Energy(c)
				min_conf = c
		print("Min Energy is: {0}".format(min_energy))
		print("GMEC is {0}".format(min_conf))
		


	def Desmet_DEE(self)  :
		""" Execute the original Desmet DEE criteria"""
		# Complexity $O(n^2r^2)$
		r = self.p.r
		n = self.p.n
		Es = self.p.Es
		Ep = self.p.Ep
		rotSpace = self.p.rotSpace

		elimRots = {}
		for i in range(n) :
			lhs = [0]*len(rotSpace[i])
			rhs = [0]*len(rotSpace[i])
			for r in rotSpace[i] :
				lhs[r] = rhs[r] = Es[i][r]
				for j in range(n) :
					if j == i : continue
					rspj = rotSpace[j]
					lhs[r] = lhs[r] + \
						min([Ep[i][j][r][s] for s in rspj])
					rhs[r] = rhs[r] + \
						max([Ep[i][j][r][s] for s in rspj])
			# Check filtering criteria
			for r in rotSpace[i] :
				for t in rotSpace[i] :
					if(lhs[r]>rhs[t]) :
						try :
							elimRots[i].append((r,t))
						except KeyError : 
							elimRots[i] = [(r,t)]
						break;
	
		# Eliminate the flagged rotamers
		for i in elimRots.keys() : 
			for r,t in elimRots[i] : 
				print("Rot{0} elim by Rot{1} in res{2}".format(r,t,i))
			removed = map(itemgetter(0),elimRots[i])
			rotSpace[i] = filter(lambda(x): x not in removed,\
								rotSpace[i])			

	
	def Desmet_DEE_pair(self)  : 
		""" Execute the pairs DEE criteria """
		# Complexity $O(n)$
		pass

	def Goldstein_DEE(self) : 
		""" Execute the Goldstein singles DEE criteria """
		# Complexity $O(n^2r^3)$
		pass

	def Goldstein_DEE_pairself(self) : 
		""" Execute the pairs Goldstein DEE criteria"""
		# Complexity $O(n^3r^5)$
		pass

	def _pspace(self)  :	
		""" Prints length of param space """
		return reduce(lambda x,y:x*y,map(len,self.rotSpace))

	def print_rotSpace(self) :
		""" Prints the rotamer space """
		print("-"*20+"Rotameric space"+"-"*20);
		print("Param space:{0}".format(self._pspace()))
		for i,rots in enumerate(self.rotSpace) : 
			print("{0}: {1}".format(i,rots))

	def sched1(self) :
		""" Execute the following schedule and print results """
	
		self.print_rotSpace()
		#self.findmin_brute()
		print("-"*20+"Running Desmet DEE"+"-"*20)
		self.Desmet_DEE() 
		self.print_rotSpace()
		#self.findmin_brute()


	def solve(self)  :
		""" Call a schedule to solve the problem """
		self.sched1()



if __name__ == '__main__' : 
	# Initialize stuff
	p = Protein(N,R)
	scp = SCPSolver(p) 
	scp.solve()





